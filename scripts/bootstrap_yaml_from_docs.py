"""(1회용) 기존 액티비티 문서 11개를 역파싱해 data/activities.yaml 을 만든다.

원본 저장소에서 삭제된 옛 생성기의 설명 데이터(website/data/activities.yaml)는 복구할 수 없으므로,
현재 docs/user/activities/*.md 가 유일한 한국어 설명 기록이다. 이 스크립트는 그 설명을 yaml 로 옮긴다.

  python scripts/bootstrap_yaml_from_docs.py [--force]

이미 data/activities.yaml 이 있으면 --force 없이는 덮어쓰지 않는다.
"""

from __future__ import annotations

import argparse
import collections
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import neorpa_docs as nd  # noqa: E402

# 문서 파일 키 → 툴박스 CategoryName / 동명 클래스 해소용 네임스페이스 힌트
CATEGORIES = [
    ("chrome", "Chrome", ["MeetupWfIntro.MeetupActivityLibrary.Activities.Meetup", "DX.TEST.Activities"]),
    ("chrome-native", "Chrome (일반)", ["MeetupWfIntro.MeetupActivityLibrary.Activities.Meetup", "DX.TEST.Activities"]),
    ("control", "Control", ["DX.TEST.Activities", "MeetupWfIntro.MeetupActivityLibrary.Activities.Meetup"]),
    ("statements", "Statements", ["MeetupWfIntro.MeetupActivityLibrary.Activities.Meetup.Statements",
                                  "DX.TEST.Activities", "SwitchActivityLibrary.Activities"]),
    ("excel-workbook", "Excel WorkBook", ["MeetupWfIntro.MeetupActivityLibrary.Activities.Meetup", "DX.TEST.Activities"]),
    ("excel-scope", "Excel Scope", ["ExcelScopeLibrary.Activities.ExcelScope"]),
    ("datatable", "DataTable", ["DataTableLibrary.Activities", "DX.TEST.Activities"]),
    ("mail", "Mail", ["DX.TEST.Activities"]),
    ("system", "System", ["DX.TEST.Activities", "MeetupWfIntro.MeetupActivityLibrary.Activities.Meetup"]),
    ("db", "DB", ["DX.TEST.Activities", "MeetupWfIntro.MeetupActivityLibrary.Activities.Meetup"]),
    ("outlook", "OutLook", ["DX.TEST.Activities", "MeetupWfIntro.MeetupActivityLibrary.Activities.Meetup"]),
]

_H2 = re.compile(r"^## (.*?)\s+<small>`([\w<>_]+)`</small>\s*$")
_ROW = re.compile(r"^\| (.*?) \| (입력|출력|입출력|설정) \| `(.*?)` \| (.*) \|\s*$")


def parse_page(path: Path) -> tuple[str, str, dict[str, dict]]:
    lines = nd.normalize(path.read_text(encoding="utf-8")).split("\n")
    title = next(l[2:].strip() for l in lines if l.startswith("# "))
    intro = ""
    seen_title = False
    for l in lines:
        if l.startswith("# "):
            seen_title = True
            continue
        if seen_title and l.strip() and not l.startswith(">") and not l.startswith("##"):
            intro = l.strip()
            break
    acts: dict[str, dict] = {}
    cur: dict | None = None
    i = 0
    while i < len(lines):
        m = _H2.match(lines[i])
        if m:
            type_id = m.group(2).replace("<T>", "")
            cur = {"desc": "", "props": collections.OrderedDict()}
            acts[type_id] = cur
            # 설명: 헤딩 다음 첫 비어있지 않은 문단
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and not lines[j].startswith("**"):
                cur["desc"] = lines[j].strip()
            i = j
            continue
        rm = _ROW.match(lines[i]) if cur is not None else None
        if rm:
            head = rm.group(1)
            pm = re.search(r"<small>`(\w+)`</small>", head)
            pname = pm.group(1) if pm else head.strip("`")
            cur["props"][pname] = rm.group(4).strip().replace("\\|", "|")
        i += 1
    return title, intro, acts


def parse_index(path: Path) -> tuple[dict[str, str], str | None]:
    text = nd.normalize(path.read_text(encoding="utf-8"))
    summaries: dict[str, str] = {}
    for m in re.finditer(r"^\| ([^|]+?) \| ([^|]+?) \|$", text, flags=re.M):
        if m.group(1).strip() in ("카테고리", "---"):
            continue
        summaries[m.group(1).strip()] = m.group(2).strip()
    tip = re.search(r'(!!! tip "Excel WorkBook vs Excel Scope"\n(?:    .*\n?)+)', text)
    return summaries, (tip.group(1).rstrip() if tip else None)


def hidden_props_from_source(source: Path) -> dict[str, set[str]]:
    """클래스 단순명 → [Browsable(false)] 속성 집합(상속 포함). 문서에 있었던 숨김 속성에 show: true 를 주기 위함."""
    if not (source / nd.TOOLBOX_FILE).exists():
        return {}
    index = nd.build_class_index(source)
    out: dict[str, set[str]] = {}
    for cls in index.values():
        hidden = {p.name for p in nd.collect_props(index, cls, []) if p.browsable_false}
        if hidden:
            out.setdefault(cls.name, set()).update(hidden)
    return out


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--source", type=Path, default=nd.DEFAULT_SOURCE)
    args = ap.parse_args()
    if nd.DATA_FILE.exists() and not args.force:
        print(f"이미 존재합니다: {nd.DATA_FILE} (--force 로 덮어쓰기)")
        return 1
    hidden = hidden_props_from_source(args.source)

    summaries, index_tip = parse_index(nd.ACTIVITY_DOCS_DIR / "index.md")
    categories = []
    prop_texts: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)
    parsed: dict[str, tuple[str, str, dict]] = {}
    for key, name, hints in CATEGORIES:
        title, intro, acts = parse_page(nd.ACTIVITY_DOCS_DIR / f"{key}.md")
        parsed[key] = (title, intro, acts)
        for a in acts.values():
            for pname, desc in a["props"].items():
                prop_texts[pname][desc] += 1

    # 같은 속성명으로 3회 이상 반복되는 설명은 common_props 로 승격
    common: dict[str, str] = {}
    for pname, counter in prop_texts.items():
        desc, n = counter.most_common(1)[0]
        if n >= 3 and pname not in nd.INTERNAL_PROPS:
            common[pname] = desc

    for key, name, hints in CATEGORIES:
        title, intro, acts = parsed[key]
        ydefs = {}
        for type_id, a in acts.items():
            entry: dict = {"desc": a["desc"]}
            props = {}
            for pname, desc in a["props"].items():
                if pname in nd.INTERNAL_PROPS:
                    continue  # 셀렉터 편집기 내부 값 — 문서에서 제외
                entry_p: dict = {}
                if pname in hidden.get(type_id, set()):
                    entry_p["show"] = True  # 옛 문서에 있던 숨김 속성은 계속 노출
                if common.get(pname) != desc:
                    entry_p["desc"] = desc
                if entry_p:
                    props[pname] = entry_p
            if props:
                entry["props"] = props
            ydefs[type_id] = entry
        categories.append({
            "key": key, "name": name, "title": title,
            "summary": summaries.get(name, summaries.get(title, "")),
            "intro": intro, "namespace_hint": hints, "activities": ydefs,
        })

    data = {
        "meta": {
            "description": "NeoRPA 액티비티 문서의 한국어 설명 데이터. 표시명·속성 목록은 소스에서 자동 추출되므로 여기에는 설명만 둔다.",
            "type_id_overrides": {"System.Activities.Statements.ForEach<>": "ForEach_WF"},
            "hidden_categories": ["Misc"],
            "index_notes": index_tip or "",
        },
        "common_props": dict(sorted(common.items())),
        "categories": categories,
    }
    nd.DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    nd.dump_yaml(data, nd.DATA_FILE)
    n_act = sum(len(c["activities"]) for c in categories)
    print(f"WRITE {nd.DATA_FILE.relative_to(nd.DOCS_ROOT)}: 카테고리 {len(categories)} · 액티비티 {n_act} · 공통 속성 {len(common)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
