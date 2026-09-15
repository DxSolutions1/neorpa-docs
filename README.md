# NeoRPA 문서 (공개 사이트)

NeoRPA **사용자 문서**의 원본 저장소입니다. MkDocs Material 기반, GitHub Pages 배포.

- 배포 URL: https://dxsolutions1.github.io/neorpa-docs/
- 배포: `main` 에 push 하면 GitHub Actions(`.github/workflows/deploy.yml`)가 `mkdocs build --strict` 로 빌드·배포합니다.
  - 최초 1회: **Settings → Pages → Source = "GitHub Actions"**.
- 개발자 문서(RPA 관리자 전용)는 별도 저장소에서 관리되며 이 사이트에 포함되지 않습니다.

## 콘텐츠 구조

| 경로 | 성격 |
|---|---|
| `docs/**` (activities 제외) | 수기 문서 — 시작하기, 기본 개념, 원격 데스크톱, 문제 해결, 용어집, 변경 이력 |
| `docs/user/activities/*.md` | **생성물** — 직접 편집하지 마세요. 표시명·속성 표는 NeoRPA 소스에서 자동 추출됩니다 |
| `data/activities.yaml` | 액티비티·속성의 **한국어 설명**(사람이 유지하는 유일한 원천) |
| `data/source-state.json` | 마지막으로 반영한 NeoRPA 소스 커밋·버전 |
| `data/source-map.yaml` | 소스 변경 영역 → 점검할 문서 페이지 매핑 |
| `scripts/` | 생성기(`gen_activities.py`), 원본 변경 삼각측량(`source_diff.py`), 빌드(`build.ps1`) |
| `CLAUDE.md`, `.claude/commands/update-docs.md` | 문서 갱신 절차(Claude Code `/update-docs`) |

## 로컬 미리보기 / 빌드

```powershell
pwsh -File scripts/build.ps1          # .venv 생성 + 의존성 설치 + mkdocs build --strict
pwsh -File scripts/build.ps1 -Serve   # http://127.0.0.1:8000 미리보기
```

## 액티비티 문서 갱신

원본 소스 저장소(`rpa-designer`)가 로컬에 있어야 합니다(기본 `C:\RPA_Code\rpa-designer`, 환경변수 `NEORPA_SOURCE` 로 변경).

```powershell
$env:PYTHONUTF8 = 1
.venv\Scripts\python scripts\source_diff.py             # 마지막 동기화 이후 원본 변경 → 점검할 문서
.venv\Scripts\python scripts\gen_activities.py --check  # 새 액티비티/속성 설명 누락, resx 누락 보고
#   → data/activities.yaml 에 설명 작성
.venv\Scripts\python scripts\gen_activities.py --write  # 페이지 재생성 + source-state 갱신
```

전체 절차는 `CLAUDE.md` 와 `.claude/commands/update-docs.md` 를 참고하세요.
