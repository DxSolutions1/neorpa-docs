"""NeoRPA 액티비티 문서 생성 라이브러리.

원본 저장소(rpa-designer)에서 다음을 읽어 액티비티 페이지를 만든다.

* ``RehostedDesigner/Helpers/ToolboxManager.cs`` ``AddCategories()`` — 카테고리·항목·순서(사용자가 보는 유일한 목록)
* 액티비티 ``.cs``(csproj 의 ``<Compile Include>`` 에 있는 파일만) — 속성(상속 포함),
  ``[Category]`` / ``[Browsable]`` / ``[CustomDisplayName]`` / ``[DisplayName]`` 특성
* ``Resources.ko.resx`` / ``Resources.resx`` — 표시명(``{Type}_DisplayName``, ``{Prop}_Property_DisplayName``)

한국어 설명은 이 저장소의 ``data/activities.yaml`` 이 유일한 원천이다.

표준 라이브러리 + PyYAML 만 사용한다.

알려진 한계
* 정규식 기반 C# 파서: ``#if`` 전처리 무시, 특성 인자 안의 ``]``/``)``, 식 본문(``=>``) 속성은 다루지 않는다.
* 기반 클래스가 인덱스 범위(3개 라이브러리) 밖이면 그 이상은 수집하지 않는다(WARN 으로 알림).
"""

from __future__ import annotations

import dataclasses
import html
import os
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Iterable

import yaml

# --------------------------------------------------------------------------------------
# 경로·상수
# --------------------------------------------------------------------------------------

DOCS_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = DOCS_ROOT / "data" / "activities.yaml"
STATE_FILE = DOCS_ROOT / "data" / "source-state.json"
ACTIVITY_DOCS_DIR = DOCS_ROOT / "docs" / "user" / "activities"

DEFAULT_SOURCE = Path(os.environ.get("NEORPA_SOURCE", r"C:\RPA_Code\rpa-designer"))

TOOLBOX_FILE = Path("RehostedDesigner") / "Helpers" / "ToolboxManager.cs"
# (프로젝트 폴더, 액티비티 소스 하위 폴더) — csproj 가 있으면 그 Compile 목록을, 없으면 rglob 을 쓴다.
ACTIVITY_PROJECTS = (
    Path("ActivityLibraries") / "MeetupActivityLibrary",
    Path("ActivityLibraries") / "DataTableLibrary",
    Path("ActivityLibraries") / "ExcelScopeLibrary",
)
RESX_KO = (
    Path("RehostedDesigner") / "Properties" / "Resources.ko.resx",
    Path("ActivityLibraries") / "MeetupActivityLibrary" / "Properties" / "Resources.ko.resx",
)
RESX_EN = (
    Path("RehostedDesigner") / "Properties" / "Resources.resx",
    Path("ActivityLibraries") / "MeetupActivityLibrary" / "Properties" / "Resources.resx",
)
VERSION_FILE = Path("RehostedDesigner") / "Properties" / "AssemblyInfo.cs"

# 속성 수집을 멈추는(프레임워크) 기반 클래스
STOP_BASES = {"CodeActivity", "NativeActivity", "AsyncCodeActivity", "Activity", "object"}
# 소스가 없어도 정상인 표준 WF 액티비티(System.Activities.*)
STANDARD_WF = {
    "Assign", "If", "Parallel", "Sequence", "TryCatch", "Throw", "Rethrow", "WriteLine", "ForEach",
    "AddToCollection", "Flowchart", "FlowSwitch", "FlowDecision", "InvokeMethod", "State", "FinalState",
    "StateMachine", "Delay", "Switch", "While", "DoWhile", "Pick", "PickBranch",
}
# 셀렉터 편집기가 내부적으로 채우는 속성 — yaml 에 설명이 남아 있어도 조용히 무시
INTERNAL_PROPS = {"PicInfo", "Xpath", "VisionTarget"}

HEADER_COMMENT = (
    "<!-- 이 파일은 scripts/gen_activities.py 로 자동 생성됩니다.\n"
    "     직접 편집하지 말고 data/activities.yaml 을 고친 뒤 "
    "`python scripts/gen_activities.py --write` 를 다시 실행하세요. -->"
)
NO_ARGS_NOTE = "!!! note\n    표준 WF 액티비티이거나 별도 인자가 없습니다."
DIRECTION = {"In": "입력", "Out": "출력", "InOut": "입출력", "Activity": "설정", "Plain": "설정"}


# --------------------------------------------------------------------------------------
# 데이터 모델
# --------------------------------------------------------------------------------------

@dataclasses.dataclass
class ToolboxItem:
    category: str
    typeof_text: str          # typeof(...) 안의 원문 (예: System.Activities.Statements.ForEach<>)
    fallback_label: str | None
    order: int

    @property
    def is_generic(self) -> bool:
        return self.typeof_text.endswith("<>")

    @property
    def simple_name(self) -> str:
        head = self.typeof_text[:-2] if self.is_generic else self.typeof_text
        return head.split(".")[-1]

    @property
    def namespace(self) -> str | None:
        head = self.typeof_text[:-2] if self.is_generic else self.typeof_text
        return head.rsplit(".", 1)[0] if "." in head else None


@dataclasses.dataclass
class PropInfo:
    name: str
    type_text: str            # 선언된 타입 원문 (InArgument<string> 등)
    kind: str                 # In / Out / InOut / Activity / Plain
    inner_type: str           # 표에 쓸 타입 (string, DataTable, Activity<bool>, bool ...)
    browsable_false: bool
    category: str | None
    custom_display_name: bool
    display_name_attr: str | None   # [DisplayName("...")] 문자열
    declared_in: str


@dataclasses.dataclass
class ClassInfo:
    name: str
    namespace: str
    arity: int
    bases: list[str]
    file: Path
    usings: list[str]
    props: list[PropInfo]

    @property
    def key(self) -> tuple[str, str, int]:
        return (self.namespace, self.name, self.arity)


@dataclasses.dataclass
class Activity:
    item: ToolboxItem
    type_id: str                       # yaml 키
    code: str                          # 문서 <small> 에 표시할 타입 코드 (ReadCell<T> 등)
    display: str
    cls: ClassInfo | None              # 표준 WF 등 소스 없음이면 None
    props: list[PropInfo]
    desc: str
    notes: str | None
    prop_desc: dict[str, str]
    prop_label: dict[str, str | None]  # 속성명 → 한국어 라벨(없으면 None)


@dataclasses.dataclass
class Finding:
    level: str      # ERROR / WARN
    category: str
    subject: str
    message: str


@dataclasses.dataclass
class Model:
    categories: list[tuple[dict, list[Activity]]]
    ko: dict[str, str]
    en: dict[str, str]
    toolbox_count: int


# --------------------------------------------------------------------------------------
# C# 텍스트 유틸
# --------------------------------------------------------------------------------------

def strip_comments_and_strings(src: str) -> str:
    """주석과 문자열 리터럴 내용을 공백으로 치환한다(오프셋 유지)."""
    out = []
    i, n = 0, len(src)
    while i < n:
        c = src[i]
        two = src[i:i + 2]
        if two == "//":
            j = src.find("\n", i)
            j = n if j == -1 else j
            out.append(" " * (j - i))
            i = j
        elif two == "/*":
            j = src.find("*/", i + 2)
            j = n if j == -1 else j + 2
            out.append(re.sub(r"[^\n]", " ", src[i:j]))
            i = j
        elif two == '@"':
            j = i + 2
            while j < n:
                if src[j] == '"':
                    if src[j:j + 2] == '""':
                        j += 2
                        continue
                    break
                j += 1
            j = min(j + 1, n)
            out.append('""' + " " * max(0, j - i - 2))
            i = j
        elif c in ('"', "'"):
            q = c
            j = i + 1
            while j < n and src[j] != q:
                j += 2 if src[j] == "\\" else 1
            j = min(j + 1, n)
            out.append(q + " " * max(0, j - i - 2) + q)
            i = j
        else:
            out.append(c)
            i += 1
    return "".join(out)


def match_brace(text: str, open_idx: int) -> int:
    depth = 0
    for k in range(open_idx, len(text)):
        if text[k] == "{":
            depth += 1
        elif text[k] == "}":
            depth -= 1
            if depth == 0:
                return k
    raise ValueError("unbalanced braces")


def split_generic_args(s: str) -> list[str]:
    parts, depth, cur = [], 0, []
    for ch in s:
        if ch == "<":
            depth += 1
        elif ch == ">":
            depth -= 1
        if ch == "," and depth == 0:
            parts.append("".join(cur).strip())
            cur = []
        else:
            cur.append(ch)
    if cur:
        parts.append("".join(cur).strip())
    return parts


def short_type(t: str) -> str:
    """네임스페이스 접두어 제거: System.Data.DataTable → DataTable, List<System.String> → List<String>."""
    return re.sub(r"\b(?:[A-Za-z_]\w*\.)+(?=[A-Za-z_]\w*)", "", t)


# --------------------------------------------------------------------------------------
# 툴박스 파싱
# --------------------------------------------------------------------------------------

_ITEM_RE = re.compile(r'CreateToolboxItem\(\s*typeof\(([^()]+?)\)\s*(?:,\s*"([^"]*)")?\s*\)')


def parse_toolbox(source: Path) -> list[ToolboxItem]:
    text = (source / TOOLBOX_FILE).read_text(encoding="utf-8-sig")
    clean = strip_comments_and_strings(text)
    start = clean.find("void AddCategories(")
    if start == -1:
        raise RuntimeError("AddCategories() 를 찾을 수 없습니다: " + str(source / TOOLBOX_FILE))
    body_open = clean.index("{", start)
    body_close = match_brace(clean, body_open)
    body_clean = clean[body_open:body_close]
    body_raw = text[body_open:body_close]

    items: list[ToolboxItem] = []
    order = 0
    for m in re.finditer(r'CategoryName\s*=\s*"', body_clean):
        name_end = body_raw.index('"', m.end())
        cat_name = body_raw[m.end():name_end]
        tools_open = body_clean.index("{", body_clean.index("Tools", m.end()))
        tools_close = match_brace(body_clean, tools_open)
        for im in _ITEM_RE.finditer(body_raw[tools_open:tools_close]):
            items.append(ToolboxItem(cat_name, im.group(1).strip(), im.group(2), order))
            order += 1
    return items


# --------------------------------------------------------------------------------------
# 클래스 인덱스
# --------------------------------------------------------------------------------------

_CLASS_RE = re.compile(
    r"(?:(?:public|internal|private|protected)\s+)?(?:(?:static|abstract|sealed|partial)\s+)*"
    r"class\s+(\w+)\s*(<[^>{]*>)?\s*(?::\s*([^{]+?))?\s*(?:where\s[^{]*)?\{"
)
_NS_RE = re.compile(r"\bnamespace\s+([\w\.]+)\s*\{")
_PROP_RE = re.compile(
    r"((?:\[[^\]]*\]\s*)*)public\s+(?:(?:override|virtual|new|static|sealed|abstract|readonly)\s+)*"
    r"(?P<type>[^;{}=]*?)\s+(?P<name>\w+)\s*\{\s*(?:get|set)\b"
)
_ARG_RE = re.compile(r"^(In|Out|InOut)Argument<(.+)>$")
_ACT_RE = re.compile(r"^Activity<(.+)>$")


def _compiled_files(source: Path, project_dir: Path) -> list[Path] | None:
    """csproj 의 <Compile Include> 목록. csproj 가 없으면 None."""
    csprojs = list((source / project_dir).glob("*.csproj"))
    if not csprojs:
        return None
    files: list[Path] = []
    for cp in csprojs:
        text = cp.read_text(encoding="utf-8-sig", errors="replace")
        for inc in re.findall(r'<Compile\s+Include="([^"]+)"', text):
            if "*" in inc:
                files.extend((source / project_dir).glob(inc.replace("\\", "/")))
            else:
                files.append(source / project_dir / inc.replace("\\", "/"))
    return files


def iter_cs_files(source: Path) -> Iterable[Path]:
    for proj in ACTIVITY_PROJECTS:
        compiled = _compiled_files(source, proj)
        candidates = compiled if compiled is not None else list((source / proj).rglob("*.cs"))
        for p in candidates:
            s = str(p).replace("\\", "/")
            if "/bin/" in s or "/obj/" in s or "/Activities/" not in s:
                continue
            if p.name.endswith(".xaml.cs") or p.name.endswith(".Designer.cs") or not p.exists():
                continue
            yield p


def _parse_props(body_raw: str, body_clean: str, class_name: str) -> list[PropInfo]:
    # 중첩 타입 본문을 공백으로 지워 깊이 1 멤버만 남긴다.
    blanked = body_clean
    for m in re.finditer(r"\b(class|struct|enum|interface)\s+\w+\s*(?:<[^>]*>)?\s*(?::[^{]*)?\{", body_clean):
        o = m.end() - 1
        try:
            c = match_brace(blanked, o)
        except ValueError:
            continue
        blanked = blanked[:o] + " " * (c - o + 1) + blanked[c + 1:]
    props: list[PropInfo] = []
    for m in _PROP_RE.finditer(blanked):
        attrs_clean = m.group(1)
        attrs_raw = body_raw[m.start(1):m.end(1)]   # 문자열 인자 복원용
        type_text = re.sub(r"\s+", " ", m.group("type").strip())
        name = m.group("name")
        if not type_text or " " in type_text.split("<")[0]:
            continue
        kind, inner = "Plain", type_text
        am = _ARG_RE.match(type_text)
        if am:
            kind, inner = am.group(1), am.group(2)
        elif _ACT_RE.match(type_text):
            kind, inner = "Activity", type_text
        cat = re.search(r'\[Category\("([^"]*)"\)\]', attrs_raw)
        dn = re.search(r'\[DisplayName\("([^"]*)"\)\]', attrs_raw)
        props.append(PropInfo(
            name=name, type_text=type_text, kind=kind, inner_type=short_type(inner),
            browsable_false=bool(re.search(r"\[Browsable\(\s*false\s*\)\]", attrs_raw)),
            category=cat.group(1) if cat else None,
            custom_display_name="CustomDisplayName" in attrs_clean,
            display_name_attr=dn.group(1) if dn else None,
            declared_in=class_name,
        ))
    return props


def build_class_index(source: Path) -> dict[tuple[str, str, int], ClassInfo]:
    index: dict[tuple[str, str, int], ClassInfo] = {}
    for path in iter_cs_files(source):
        raw = path.read_text(encoding="utf-8-sig", errors="replace")
        clean = strip_comments_and_strings(raw)
        usings = re.findall(r"^\s*using\s+([\w\.]+)\s*;", clean, flags=re.M)
        ns_spans: list[tuple[str, int, int]] = []
        for nm in _NS_RE.finditer(clean):
            o = clean.index("{", nm.end() - 1)
            ns_spans.append((nm.group(1), o, match_brace(clean, o)))
        class_spans: list[tuple[int, int]] = []
        for cm in _CLASS_RE.finditer(clean):
            o = cm.end() - 1
            try:
                c = match_brace(clean, o)
            except ValueError:
                continue
            if any(a < cm.start() < b for a, b in class_spans):
                continue  # 중첩 클래스는 인덱스에 넣지 않는다
            class_spans.append((o, c))
            ns = next((n for n, a, b in ns_spans if a < cm.start() < b), "")
            arity = len(split_generic_args(cm.group(2)[1:-1])) if cm.group(2) else 0
            bases = [b.strip() for b in split_generic_args(cm.group(3))] if cm.group(3) else []
            info = ClassInfo(
                name=cm.group(1), namespace=ns, arity=arity, bases=bases, file=path,
                usings=usings, props=_parse_props(raw[o:c + 1], clean[o:c + 1], cm.group(1)),
            )
            if info.key in index:            # partial class → 속성 병합
                index[info.key].props.extend(info.props)
                index[info.key].bases = index[info.key].bases or info.bases
            else:
                index[info.key] = info
    return index


def resolve_class(index: dict[tuple[str, str, int], ClassInfo], name: str, arity: int,
                  namespace: str | None, hints: list[str]) -> tuple[ClassInfo | None, list[str]]:
    """이름(+네임스페이스/힌트)으로 클래스를 찾는다. (결과, 모호한 후보 목록)"""
    cands = [c for c in index.values() if c.name == name and c.arity == arity]
    if namespace:
        exact = [c for c in cands if c.namespace == namespace]
        return (exact[0] if exact else None), []
    if len(cands) <= 1:
        return (cands[0] if cands else None), []
    for h in hints:
        hit = [c for c in cands if c.namespace == h]
        if len(hit) == 1:
            return hit[0], []
    return None, [f"{c.namespace}.{c.name}" for c in cands]


def collect_props(index: dict[tuple[str, str, int], ClassInfo], cls: ClassInfo,
                  warnings: list[str]) -> list[PropInfo]:
    """파생 클래스 선언 순 → 기반 클래스 순으로 속성을 모으고 이름 중복은 첫 등장을 유지한다."""
    seen: set[str] = set()
    out: list[PropInfo] = []
    cur: ClassInfo | None = cls
    visited: set[tuple[str, str, int]] = set()
    while cur and cur.key not in visited:
        visited.add(cur.key)
        for p in cur.props:
            if p.name not in seen:
                seen.add(p.name)
                out.append(p)
        if not cur.bases:
            break
        base = cur.bases[0]
        base_head = base.split("<")[0]
        base_simple = base_head.split(".")[-1]
        base_arity = len(split_generic_args(base[base.index("<") + 1:-1])) if "<" in base else 0
        if base_simple in STOP_BASES:
            break
        base_ns = base_head.rsplit(".", 1)[0] if "." in base_head else None
        nxt, amb = resolve_class(index, base_simple, base_arity, base_ns, [cur.namespace] + cur.usings)
        if nxt is None:
            if amb:
                warnings.append(f"기반 클래스 {base} 후보가 여럿입니다: {amb}")
            else:
                warnings.append(f"기반 클래스 {base} 를 인덱스에서 찾지 못해 그 위쪽 속성은 수집하지 않습니다")
            break
        cur = nxt
    return out


# --------------------------------------------------------------------------------------
# resx / 버전
# --------------------------------------------------------------------------------------

def load_resx(paths: Iterable[Path]) -> dict[str, str]:
    """앞선 파일이 우선(디자이너 resx → 액티비티 resx). 런타임 GlobalResourceManager 와 같은 순서."""
    out: dict[str, str] = {}
    for p in paths:
        if not p.exists():
            continue
        for data in ET.parse(p).getroot().iter("data"):
            name = data.get("name")
            val = data.find("value")
            if name and val is not None and name not in out:
                out[name] = (val.text or "").strip()
    return out


def read_product_version(source: Path) -> str | None:
    p = source / VERSION_FILE
    if not p.exists():
        return None
    m = re.search(r'^\[assembly: AssemblyVersion\("([\d\.]+)"\)', p.read_text(encoding="utf-8-sig"), flags=re.M)
    return m.group(1) if m else None


# --------------------------------------------------------------------------------------
# yaml 데이터
# --------------------------------------------------------------------------------------

def load_data(path: Path = DATA_FILE) -> dict:
    with path.open(encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    data.setdefault("meta", {})
    data.setdefault("categories", [])
    data.setdefault("common_props", {})
    data["meta"].setdefault("hidden_categories", ["Misc"])
    data["meta"].setdefault("type_id_overrides", {})
    for cat in data["categories"]:
        cat.setdefault("activities", {})
        cat.setdefault("namespace_hint", [])
    return data


def dump_yaml(data: dict, path: Path) -> None:
    text = yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=10_000, default_flow_style=False)
    path.write_text(text, encoding="utf-8", newline="\n")


# --------------------------------------------------------------------------------------
# 병합
# --------------------------------------------------------------------------------------

def _prop_def(prop_defs: dict, name: str) -> dict:
    d = prop_defs.get(name)
    if d is None:
        return {}
    return d if isinstance(d, dict) else {"desc": d}


def build_model(source: Path, data: dict, findings: list[Finding]) -> Model:
    items = parse_toolbox(source)
    index = build_class_index(source)
    ko = load_resx(source / p for p in RESX_KO)
    en = load_resx(source / p for p in RESX_EN)
    overrides: dict[str, str] = data["meta"].get("type_id_overrides") or {}
    hidden_cats: set[str] = set(data["meta"].get("hidden_categories") or [])
    cats_by_name = {c["name"]: c for c in data["categories"]}
    result: list[tuple[dict, list[Activity]]] = []

    toolbox_cats: list[str] = []
    for it in items:
        if it.category not in toolbox_cats:
            toolbox_cats.append(it.category)
    for name in toolbox_cats:
        if name not in cats_by_name:
            findings.append(Finding("ERROR", name, "(category)",
                                    "툴박스 카테고리가 data/activities.yaml 에 없습니다 (key/name/title/summary/intro 추가 필요)"))
    for name in cats_by_name:
        if name not in toolbox_cats:
            findings.append(Finding("WARN", name, "(category)", "yaml 카테고리가 툴박스에 없습니다(삭제 후보)"))

    for cat_name in toolbox_cats:
        cat = cats_by_name.get(cat_name)
        if cat is None:
            continue
        acts: list[Activity] = []
        seen_ids: set[str] = set()
        for it in (i for i in items if i.category == cat_name):
            type_id = overrides.get(it.typeof_text, it.simple_name)
            if type_id in seen_ids:
                findings.append(Finding("ERROR", cat_name, type_id,
                                        f"같은 카테고리에 동일한 타입 ID가 두 번 등장합니다 ({it.typeof_text}) → "
                                        "meta.type_id_overrides 로 별도 ID를 지정하세요"))
                continue
            seen_ids.add(type_id)
            ydef = cat["activities"].get(type_id) or {}
            if type_id not in cat["activities"]:
                findings.append(Finding("ERROR", cat_name, type_id, "yaml 에 없는 액티비티 → desc 작성 필요"))
            elif not (ydef.get("desc") or "").strip():
                findings.append(Finding("ERROR", cat_name, type_id, "desc 가 비어 있습니다"))

            cls, amb = resolve_class(index, it.simple_name, 1 if it.is_generic else 0,
                                     it.namespace, cat.get("namespace_hint", []))
            is_standard = (it.namespace or "").startswith("System.") or ydef.get("standard") or (
                cls is None and it.simple_name in STANDARD_WF)
            if cls is None:
                if amb:
                    findings.append(Finding("ERROR", cat_name, type_id, f"동명 클래스가 여럿입니다: {amb} → namespace_hint 조정"))
                elif not is_standard:
                    findings.append(Finding("ERROR", cat_name, type_id,
                                            "소스에서 클래스를 찾지 못했습니다(csproj Compile 목록 확인). 표준 WF 라면 yaml 에 standard: true"))
            warns: list[str] = []
            raw_props = collect_props(index, cls, warns) if cls else []
            for w in warns:
                findings.append(Finding("WARN", cat_name, type_id, w))

            prop_defs: dict = ydef.get("props") or {}
            props: list[PropInfo] = []
            raw_names = {p.name for p in raw_props}
            for p in raw_props:
                d = _prop_def(prop_defs, p.name)
                if p.name == "DisplayName" or d.get("hide"):
                    continue
                if p.browsable_false and not d.get("show"):
                    if d.get("desc") and p.name not in INTERNAL_PROPS:
                        findings.append(Finding("WARN", cat_name, type_id,
                                                f"속성 `{p.name}` 은 [Browsable(false)] 로 숨김 상태입니다 → yaml 에 show: true 또는 설명 제거"))
                    continue
                if p.category in hidden_cats and not d.get("show"):
                    continue
                if p.kind == "Plain" and not (p.category or p.custom_display_name or p.display_name_attr):
                    continue
                props.append(p)

            prop_desc: dict[str, str] = {}
            prop_label: dict[str, str | None] = {}
            for p in props:
                text = _prop_def(prop_defs, p.name).get("desc") or data["common_props"].get(p.name)
                if not text:
                    findings.append(Finding("ERROR", cat_name, type_id, f"속성 `{p.name}` 설명(desc) 없음"))
                    text = ""
                prop_desc[p.name] = str(text).strip()
                # 라벨: 캔버스 디자이너(TranslateExtension)와 속성 그리드([CustomDisplayName]) 모두 같은 키를 쓴다.
                label = ko.get(f"{p.name}_Property_DisplayName") or p.display_name_attr
                if label and label.replace(" ", "").lower() == p.name.lower():
                    label = None  # 라벨이 속성명과 같으면 중복 표기하지 않음
                prop_label[p.name] = label
                if p.custom_display_name and f"{p.name}_Property_DisplayName" not in ko:
                    findings.append(Finding("WARN", cat_name, type_id,
                                            f"속성 `{p.name}` 의 한국어 리소스 키 {p.name}_Property_DisplayName 없음(원본 resx 보완 필요)"))
            for n in prop_defs:
                if n not in raw_names and n not in INTERNAL_PROPS:
                    findings.append(Finding("WARN", cat_name, type_id, f"yaml 속성 `{n}` 이 소스에 없습니다(삭제 후보)"))

            # 표시명: 런타임(GlobalResourceManager → 폴백 → Type.Name) 과 같은 순서.
            # 제네릭은 Type.Name 이 `Name`1` 이라 resx 를 절대 찾지 못한다 → 폴백/yaml display 사용.
            display = ydef.get("display")
            if not display:
                if it.is_generic:
                    display = it.fallback_label or it.simple_name
                    if not it.fallback_label:
                        findings.append(Finding("WARN", cat_name, type_id,
                                                f"제네릭 액티비티는 툴박스에 `{it.simple_name}`1` 로 표시됩니다(원본에서 폴백 표시명 지정 권장). "
                                                "문서에는 yaml display 를 지정하세요"))
                else:
                    display = ko.get(f"{it.simple_name}_DisplayName") or it.fallback_label
                    if not display:
                        display = it.simple_name
                        if not is_standard:
                            findings.append(Finding("WARN", cat_name, type_id,
                                                    f"한국어 표시명 리소스 {it.simple_name}_DisplayName 없음(툴박스에 타입명이 그대로 보임)"))
                    elif not is_standard and f"{it.simple_name}_DisplayName" not in en:
                        findings.append(Finding("WARN", cat_name, type_id, "영어 리소스 키 없음(ko/en resx 불일치)"))

            acts.append(Activity(
                item=it, type_id=type_id, code=it.simple_name + ("<T>" if it.is_generic else ""),
                display=display, cls=cls, props=props,
                desc=str(ydef.get("desc") or "").strip(), notes=ydef.get("notes"),
                prop_desc=prop_desc, prop_label=prop_label,
            ))
        for yid in cat["activities"]:
            if yid not in seen_ids:
                findings.append(Finding("WARN", cat_name, yid, "yaml 에만 있고 툴박스에 없는 액티비티(삭제 후보)"))
        result.append((cat, acts))
    return Model(categories=result, ko=ko, en=en, toolbox_count=len(items))


# --------------------------------------------------------------------------------------
# 렌더링
# --------------------------------------------------------------------------------------

def _cell(text: str) -> str:
    return " ".join(str(text).split()).replace("|", "\\|")


def render_category(cat: dict, acts: list[Activity]) -> str:
    lines: list[str] = [HEADER_COMMENT, "", "", f"# {cat['title']}", "", cat["intro"].strip(), ""]
    lines.append(
        f"> 이 카테고리에는 {len(acts)}개의 액티비티가 있습니다. 각 액티비티의 **속성** 표는 소스에서 "
        "자동 추출되며(상속 포함), 표시명·설명은 리소스/설명 데이터에서 해석됩니다."
    )
    lines.append("")
    if cat.get("notes"):
        lines += [str(cat["notes"]).rstrip(), ""]
    for a in acts:
        lines.append(f"## {html.escape(a.display, quote=False)}  <small>`{a.code}`</small>")
        lines.append("")
        lines.append(a.desc or "_(설명 준비 중)_")
        lines.append("")
        lines.append("**속성**")
        lines.append("")
        if not a.props:
            lines.append(NO_ARGS_NOTE)
        else:
            lines.append("| 속성 | 방향 | 타입 | 설명 |")
            lines.append("|------|------|------|------|")
            for p in a.props:
                label = a.prop_label.get(p.name)
                col = f"{label} <small>`{p.name}`</small>" if label else f"`{p.name}`"
                lines.append(f"| {col} | {DIRECTION[p.kind]} | `{p.inner_type}` | {_cell(a.prop_desc.get(p.name, ''))} |")
        lines.append("")
        if a.notes:
            lines += [str(a.notes).rstrip(), ""]
    return "\n".join(lines).rstrip("\n") + "\n"


def render_index(data: dict, model: Model, missing_desc: int) -> str:
    total = sum(len(a) for _, a in model.categories)
    lines = [
        HEADER_COMMENT, "", "",
        "# 액티비티 사용법", "",
        f"{len(model.categories)}개 카테고리 · {total}개 액티비티를 툴박스 순서대로 정리합니다. "
        "표시명·속성 표는 NeoRPA 소스에서 자동 추출되고, 설명은 `data/activities.yaml`에서 관리됩니다.",
        "",
    ]
    if missing_desc:
        lines += ["!!! note \"설명 채우는 중\"",
                  f"    표시명·목록은 완비되어 있고, 설명이 비어 있는 항목이 {missing_desc}개 남아 있습니다.", ""]
    lines += ["## 카테고리 (툴박스 기준)", "", "| 카테고리 | 액티비티 수 | 내용 |", "|---|---:|---|"]
    for cat, acts in model.categories:
        lines.append(f"| [{cat['title']}]({cat['key']}.md) | {len(acts)} | {_cell(cat.get('summary', ''))} |")
    lines.append("")
    if data["meta"].get("index_notes"):
        lines += [str(data["meta"]["index_notes"]).rstrip(), ""]
    return "\n".join(lines).rstrip("\n") + "\n"


def render_all(data: dict, model: Model) -> dict[Path, str]:
    out: dict[Path, str] = {}
    missing = 0
    for cat, acts in model.categories:
        missing += sum(1 for a in acts if not a.desc)
        out[ACTIVITY_DOCS_DIR / f"{cat['key']}.md"] = render_category(cat, acts)
    out[ACTIVITY_DOCS_DIR / "index.md"] = render_index(data, model, missing)
    return out


def normalize(text: str) -> str:
    return text.replace("\r\n", "\n").rstrip("\n") + "\n"
