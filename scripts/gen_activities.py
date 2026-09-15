r"""액티비티 문서 생성기 CLI.

사용법:
  python scripts/gen_activities.py --check            # 원본과 문서를 대조하고 누락/불일치를 보고(exit 1 = 조치 필요)
  python scripts/gen_activities.py --write            # docs/user/activities/*.md 재생성 + data/source-state.json 갱신
  python scripts/gen_activities.py --write --category control
옵션:
  --source PATH   원본 저장소 경로 (기본: 환경변수 NEORPA_SOURCE 또는 C:\RPA_Code\rpa-designer)
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import neorpa_docs as nd  # noqa: E402


def git(source: Path, *args: str) -> str:
    try:
        return subprocess.check_output(["git", "-C", str(source), *args], text=True, encoding="utf-8",
                                       stderr=subprocess.DEVNULL).strip()
    except Exception:  # noqa: BLE001
        return ""


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source", type=Path, default=nd.DEFAULT_SOURCE)
    ap.add_argument("--category", help="yaml key (예: control) 하나만 처리")
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    args = ap.parse_args()

    source: Path = args.source
    if not (source / nd.TOOLBOX_FILE).exists():
        print(f"ERROR 원본 저장소를 찾을 수 없습니다: {source} (--source 또는 NEORPA_SOURCE 지정)")
        return 2

    findings: list[nd.Finding] = []
    data = nd.load_data()
    model = nd.build_model(source, data, findings)
    rendered = nd.render_all(data, model)
    if args.category:
        rendered = {p: t for p, t in rendered.items() if p.stem == args.category}
        findings = [f for f in findings if f.category in {c["name"] for c, _ in model.categories if c["key"] == args.category}]

    stale: list[Path] = []
    for path, text in rendered.items():
        cur = nd.normalize(path.read_text(encoding="utf-8")) if path.exists() else ""
        if cur != nd.normalize(text):
            stale.append(path)

    if args.write:
        for path in stale:
            path.write_text(rendered[path], encoding="utf-8", newline="\n")
            print(f"WRITE {path.relative_to(nd.DOCS_ROOT)}")
        if not stale:
            print("문서가 이미 최신입니다.")
        if not args.category:
            state = {
                "source_repo": str(source),
                "source_branch": git(source, "rev-parse", "--abbrev-ref", "HEAD"),
                "source_commit": git(source, "rev-parse", "HEAD"),
                "source_commit_date": git(source, "log", "-1", "--format=%cs"),
                "product_version": nd.read_product_version(source),
                "synced_at": dt.date.today().isoformat(),
                "toolbox_items": model.toolbox_count,
                "documented_activities": sum(len(a) for _, a in model.categories),
            }
            nd.STATE_FILE.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n",
                                     encoding="utf-8", newline="\n")
            print(f"WRITE {nd.STATE_FILE.relative_to(nd.DOCS_ROOT)}  "
                  f"({state['source_commit'][:7]}, v{state['product_version']})")
    else:
        for path in stale:
            findings.append(nd.Finding("ERROR", "(docs)", str(path.relative_to(nd.DOCS_ROOT)),
                                       "생성 결과와 현재 문서가 다릅니다 → --write 실행"))

    errors = [f for f in findings if f.level == "ERROR"]
    warns = [f for f in findings if f.level == "WARN"]
    for f in errors + warns:
        print(f"{f.level:5} [{f.category}] {f.subject}: {f.message}")
    total = sum(len(a) for _, a in model.categories)
    print(f"\n카테고리 {len(model.categories)}개 · 툴박스 항목 {model.toolbox_count}개 · 문서화 {total}개 · "
          f"ERROR {len(errors)} · WARN {len(warns)}")
    return 1 if (errors and args.check) else 0


if __name__ == "__main__":
    sys.exit(main())
