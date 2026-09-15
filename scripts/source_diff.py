"""원본(rpa-designer) 변경을 문서 페이지별로 분류해 보여주는 삼각측량 리포트.

  python scripts/source_diff.py                 # data/source-state.json 의 커밋 이후 변경
  python scripts/source_diff.py --since dd34a1d # 특정 커밋 이후
  python scripts/source_diff.py --full-log      # 커밋 본문까지 출력(변경 이력 초안 작성용)

출력: 커밋 목록 → data/source-map.yaml 규칙별 변경 파일과 점검할 문서 → 매핑되지 않은 파일 → resx 키 diff.
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import re
import subprocess
import sys
from collections import OrderedDict
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import neorpa_docs as nd  # noqa: E402

MAP_FILE = nd.DOCS_ROOT / "data" / "source-map.yaml"


def git(source: Path, *args: str) -> str:
    return subprocess.check_output(["git", "-C", str(source), *args], text=True, encoding="utf-8",
                                   errors="replace").rstrip("\n")


def match(path: str, pattern: str) -> bool:
    # fnmatch 는 '*' 가 '/' 도 넘기므로 '**' 와 '*' 를 구분해 정규식으로 바꾼다.
    rx = re.escape(pattern).replace(r"\*\*/", "(?:.*/)?").replace(r"\*\*", ".*").replace(r"\*", "[^/]*")
    return re.fullmatch(rx, path) is not None


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source", type=Path, default=nd.DEFAULT_SOURCE)
    ap.add_argument("--since", help="기준 커밋(기본: data/source-state.json 의 source_commit)")
    ap.add_argument("--full-log", action="store_true")
    args = ap.parse_args()

    since = args.since
    if not since:
        if not nd.STATE_FILE.exists():
            print("ERROR data/source-state.json 이 없습니다. --since 로 기준 커밋을 지정하세요.")
            return 2
        since = json.loads(nd.STATE_FILE.read_text(encoding="utf-8"))["source_commit"]
    head = git(args.source, "rev-parse", "HEAD")
    print(f"# 원본 변경 삼각측량: {since[:7]} → {head[:7]}  ({args.source}, {git(args.source, 'rev-parse', '--abbrev-ref', 'HEAD')})")
    dirty = git(args.source, "status", "--short")
    if dirty:
        print(f"! 원본 작업 트리에 커밋되지 않은 변경 {len(dirty.splitlines())}건 (문서는 커밋된 상태만 반영)")

    print("\n## 커밋")
    fmt = "%h %cs %s%n%b" if args.full_log else "%h %cs %s"
    log = git(args.source, "log", f"--format={fmt}", f"{since}..{head}")
    print(log or "(변경 없음)")

    names = git(args.source, "diff", "--name-status", "-M", since, head).splitlines()
    smap = yaml.safe_load(MAP_FILE.read_text(encoding="utf-8"))
    ignore = smap.get("ignore", [])
    groups: "OrderedDict[str, list[str]]" = OrderedDict((r["name"], []) for r in smap["rules"])
    unmapped: list[str] = []
    for line in names:
        parts = line.split("\t")
        status, path = parts[0], parts[-1]
        if any(match(path, g) for g in ignore):
            continue
        entry = f"{status[0]} {path}" + (f"  (← {parts[1]})" if status.startswith("R") else "")
        for rule in smap["rules"]:
            if any(match(path, g) for g in rule["globs"]):
                groups[rule["name"]].append(entry)
                break
        else:
            unmapped.append(entry)

    print("\n## 영역별 변경 파일 → 점검할 문서")
    for rule in smap["rules"]:
        files = groups[rule["name"]]
        if not files:
            continue
        print(f"\n### {rule['name']}  ({len(files)}개)")
        for d in rule["docs"]:
            print(f"  → {d}")
        if rule.get("note"):
            print(f"  ※ {rule['note']}")
        for f in files[:60]:
            print(f"  {f}")
        if len(files) > 60:
            print(f"  ... 외 {len(files) - 60}개")
    if unmapped:
        print(f"\n### 매핑되지 않은 파일 ({len(unmapped)}개) — 필요하면 data/source-map.yaml 에 규칙 추가")
        for f in unmapped[:80]:
            print(f"  {f}")

    # resx 키 diff (표시명 변경은 문서 헤딩/라벨에 직접 반영됨)
    print("\n## 표시명 리소스 변경(Resources.ko.resx)")
    for rel in nd.RESX_KO:
        try:
            diff = git(args.source, "diff", since, head, "--", str(rel).replace("\\", "/"))
        except subprocess.CalledProcessError:
            continue
        keys = re.findall(r'^([-+])\s*<data name="([^"]+)"', diff, flags=re.M)
        vals = re.findall(r'^([-+])\s*<value>(.*)</value>', diff, flags=re.M)
        if keys or vals:
            print(f"- {rel}: 키 추가/삭제 {len(keys)}건, 값 변경 {len(vals)}건")
            for sign, k in keys:
                print(f"    {sign} {k}")
            for sign, v in vals[:40]:
                print(f"    {sign} value: {v}")
    # 툴박스 항목 diff
    tb = git(args.source, "diff", since, head, "--", str(nd.TOOLBOX_FILE).replace("\\", "/"))
    items = re.findall(r"^([-+]).*CreateToolboxItem\(typeof\(([^)]+)\)", tb, flags=re.M)
    if items:
        print("\n## 툴박스 항목 변경")
        for sign, t in items:
            print(f"  {sign} {t}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
