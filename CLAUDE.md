# CLAUDE.md — neorpa-docs

NeoRPA(주식회사 디엑스솔루션즈의 Windows RPA 저작 도구) **공개 사용자 문서** 저장소. MkDocs Material, 한국어.
`main`에 push 하면 GitHub Actions(`.github/workflows/deploy.yml`)가 `mkdocs build --strict`로 빌드해 GitHub Pages에 배포한다.
개발자 문서는 별도 저장소(`DxSolutions1/license-admin-dashboard`, RPA 관리자 전용 포털)에서 관리하며 여기서 다루지 않는다.

## 진실의 원천

| 내용 | 원천 | 비고 |
|---|---|---|
| 액티비티 **목록·순서·카테고리** | 원본 `RehostedDesigner/Helpers/ToolboxManager.cs` `AddCategories()` | 사용자가 보는 유일한 목록. 소스에 있어도 여기 없으면 문서화하지 않음 |
| 액티비티 **속성**(이름·방향·타입) | 원본 액티비티 `.cs`(csproj `<Compile Include>` 에 있는 파일만, 상속 포함) | 트리에 낡은 미컴파일 `.cs`가 남아 있으므로 csproj 기준이 필수 |
| **표시명·속성 라벨** | 원본 `Resources.ko.resx`(디자이너 → 액티비티 순) | 키 `{Type}_DisplayName`, `{Prop}_Property_DisplayName` |
| 액티비티·속성 **한국어 설명** | 이 저장소 `data/activities.yaml` | 사람이 유지. 옛 생성기 데이터는 원본에서 삭제되어 이 파일이 유일본 |
| 마지막 동기화 원본 커밋·버전 | `data/source-state.json` | `--write` 가 갱신 |
| 원본 변경 영역 → 점검 문서 매핑 | `data/source-map.yaml` | `scripts/source_diff.py` 가 사용 |
| 제품 버전 | 원본 `RehostedDesigner/Properties/AssemblyInfo.cs`, `RehostedDesignerInstaller/*.wixproj` | 설치 파일명 `NeoRPA-v{버전}.msi` |

원본 저장소 기본 경로는 `C:\RPA_Code\rpa-designer`(환경변수 `NEORPA_SOURCE` 또는 `--source` 로 변경). 원본에는 CHANGELOG 가 없으므로 **git log 가 유일한 변경 기록**이다.

## 생성물과 수기 문서

- `docs/user/activities/*.md`(12개)는 **생성물**이다. 직접 고치지 말고 `data/activities.yaml` 을 고친 뒤 `python scripts/gen_activities.py --write` 를 실행한다. 헤더 주석이 그 사실을 알린다.
- 그 외 `docs/**` 는 수기 문서. UI 라벨·메뉴 이름·파일 이름은 반드시 원본 XAML/`.cs`/resx 에서 확인한 문자열을 그대로 쓴다(추측 금지). 내부 구현은 "개발자 문서(RPA 관리자 전용 포털)"로 넘긴다.

## 명령

```powershell
pwsh -File scripts/build.ps1            # .venv 준비 + mkdocs build --strict (CI 와 동일)
pwsh -File scripts/build.ps1 -Serve     # 로컬 미리보기
.venv\Scripts\python scripts\source_diff.py            # 마지막 동기화 이후 원본 변경 삼각측량
.venv\Scripts\python scripts\gen_activities.py --check # 누락 설명·resx·불일치 보고 (exit 1 = 조치 필요)
.venv\Scripts\python scripts\gen_activities.py --write # 액티비티 페이지 재생성 + source-state 갱신
```

Windows 콘솔에서 한글이 깨지면 `$env:PYTHONUTF8=1`.

## 문서 갱신 절차 (요약 — 전체는 `/update-docs`)

1. `source_diff.py` 로 원본 변경을 영역별로 파악한다(커밋 메시지 본문은 `--full-log`).
2. `gen_activities.py --check` 의 ERROR 를 없앤다: 새 액티비티/속성은 **원본 .cs·디자이너 xaml·커밋 메시지를 읽고** yaml 에 설명을 쓴다.
3. `--write` 후 `git diff docs/user/activities` 로 의도한 변경만 있는지 본다.
4. `data/source-map.yaml` 매핑대로 수기 페이지를 점검·수정한다.
5. `docs/changelog.md` 맨 위에 항목을 추가한다(날짜 · 버전 · 원본 커밋 범위 · 새/변경 액티비티 · 디자이너 · 원격 · 문서).
6. `scripts/build.ps1` 이 경고 없이 통과해야 한다. 새 페이지는 `mkdocs.yml` `nav` 에 직접 추가(`!!python/name:` 태그 때문에 YAML 라이브러리로 재직렬화하지 말 것).
7. 커밋 메시지: `docs: sync with rpa-designer <7자 해시> (v<버전>)`. **push 는 사용자 확인 후**(공개 사이트 즉시 배포).

## 원본 변경 영역 ↔ 점검 문서 (요약; 전체는 `data/source-map.yaml`)

| 원본 | 문서 |
|---|---|
| `ToolboxManager.cs`, `ActivityLibraries/*/Activities/**`, `Resources*.resx` | `data/activities.yaml` → 재생성 |
| `Views/Start/*`, `NewProjectWindow`, `ProjectSettingsWindow`, `Views/Project/*`, `Helpers/Project*.cs` | `getting-started.md`, `concepts.md#project` |
| `Helpers/CommandLine.cs`, `App.xaml.cs` | `getting-started.md#cli` |
| `Views/DebugView*`, `Helpers/DebugManager*`, `WorkflowExecutor.cs`, `LogService/*` | `concepts.md#run-debug`, `troubleshooting.md#logs` |
| `NeoRPA.RemoteRuntime/**`, `NeoRPA.RdpPlugin/**`, `Rdp*.cs` | `remote-desktop.md`, `troubleshooting.md#remote-desktop`, `glossary.md` |
| `Activities/UI/**`(요소 편집기), `Selector*.cs`, `ElementFinder*.cs` | `concepts.md#selector`, `troubleshooting.md#selector-not-found` |
| `RehostedDesignerInstaller/**`, `AssemblyInfo.cs`, `Resources/LocalFiles/**` | `getting-started.md`(설치), `changelog.md` |

## 생성기 규칙 (scripts/neorpa_docs.py)

- 속성 포함: `InArgument/OutArgument/InOutArgument/Activity<T>` 공개 속성, 그리고 `[Category]`/`[CustomDisplayName]`/`[DisplayName]` 이 붙은 일반 속성(방향 "설정").
- 제외: `[Browsable(false)]`(yaml `show: true` 로 예외), `meta.hidden_categories`(기본 `Misc`), `DisplayName`, yaml `hide: true`.
- 순서: 파생 클래스 선언 순 → 기반 클래스 순, 이름 중복은 첫 등장 유지. 액티비티 순서는 툴박스 순서.
- 표시명: yaml `display` → (제네릭) 툴박스 폴백 라벨 → ko resx `{Type}_DisplayName` → 폴백 → 타입명. 제네릭 타입은 런타임에서 resx 를 못 찾으므로 문서도 폴백을 쓴다.
- 속성 라벨: ko resx `{Prop}_Property_DisplayName` → `[DisplayName]` → 없으면 코드명만. 라벨이 코드명과 같으면 생략.
- 같은 카테고리에 같은 단순명이 둘이면 `meta.type_id_overrides` 로 별도 ID(예: 표준 `ForEach<>` → `ForEach_WF`).
- 한계: 정규식 파서(`#if` 무시, 식 본문 속성 미지원). 기반 클래스가 3개 라이브러리 밖이면 그 위는 수집하지 않고 WARN.

## 문체·형식 규약

- 존댓말("~합니다"), 제품명 **NeoRPA**, 실행 파일은 `Rehosted WF Designer.exe`, 설치 파일은 `NeoRPA-v{버전}.msi`.
- 헤딩은 `#`/`##`/`###` 까지. 다른 페이지에서 링크할 헤딩은 `{ #kebab-slug }` 를 붙인다(한국어 헤딩의 자동 slug 는 쓰지 않는다).
- admonition: `!!! note` / `!!! tip "제목"` / `!!! warning "제목"` / `!!! info`. 문제 해결은 **증상 → 확인 → 조치**.
- 액티비티는 한국어 표시명으로 부르고 필요하면 코드명을 괄호나 백틱으로 덧붙인다(`클릭 V2`, `ClickV2`).
- 이미지는 아직 없다. 추가하면 `docs/assets/` 아래에 두고 이 절을 갱신한다.
- 커밋: Conventional Commits `docs:` 접두어.
