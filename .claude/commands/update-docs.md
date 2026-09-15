---
description: NeoRPA 원본(rpa-designer) 변경을 사용자 문서에 반영하는 반복 절차. 삼각측량 → 액티비티 페이지 재생성 → 수기 페이지 점검 → 변경 이력 → strict 빌드 → 커밋.
---

# /update-docs — NeoRPA 문서 동기화

원본 저장소: `$ARGUMENTS` 가 비어 있으면 `C:\RPA_Code\rpa-designer`(또는 환경변수 `NEORPA_SOURCE`). 먼저 `CLAUDE.md` 의 진실의 원천 표와 규약을 따른다. 아래 단계를 **순서대로** 수행하고, 각 단계의 결과를 짧게 보고한다.

## 0. 준비

- `pwsh -File scripts/build.ps1 -NoBuild` 로 `.venv` 를 준비한다. 이후 파이썬은 `.venv\Scripts\python` 을 쓰고 `$env:PYTHONUTF8=1` 을 켠다.
- 원본의 브랜치·HEAD·미커밋 변경을 확인한다: `git -C <원본> status --short`, `git -C <원본> log -1 --oneline`. 미커밋 변경은 문서에 반영하지 않는다(사용자에게 알린다).
- `data/source-state.json` 의 `source_commit` 이 기준점이다. 없으면 사용자에게 기준 커밋을 묻는다.

## 1. 삼각측량

`python scripts/source_diff.py --full-log` 를 실행해 다음을 정리한다.

- 커밋 목록과 본문에서 **사용자에게 보이는 변경**(새/개명/삭제 액티비티, 속성 추가, UI 화면·메뉴, 명령줄, 원격 러타임, 설치)을 뽑는다. 내부 리팩터링·테스트는 제외.
- 영역별 변경 파일과 매핑된 문서 페이지를 확인한다. "매핑되지 않은 파일" 중 사용자 영향이 있는 것은 `data/source-map.yaml` 에 규칙을 추가한다.
- 표시명 리소스 diff 와 툴박스 항목 diff 를 메모한다(헤딩·라벨 변화, 신규 항목).

## 2. 액티비티 페이지

1. `python scripts/gen_activities.py --check` 를 실행한다.
2. **ERROR** 를 하나씩 없앤다.
   - `yaml 에 없는 액티비티`: 원본 액티비티 `.cs`(Execute 본문·주석·기본값), 디자이너 `.xaml`, 관련 커밋 메시지를 읽고 `data/activities.yaml` 의 해당 카테고리 `activities` 에 `desc`(한 문단, 사용자 관점, 무엇을 하고 언제 쓰는지)와 필요한 `props.<이름>.desc` 를 쓴다. 기본값이 있으면 "(기본 …)" 으로 적는다.
   - `속성 desc 없음`: 여러 액티비티에 같은 의미면 `common_props`, 아니면 그 액티비티의 `props` 에 쓴다.
   - `동명 클래스가 여럿`: 카테고리의 `namespace_hint` 를 조정한다.
   - `같은 카테고리에 동일한 타입 ID`: `meta.type_id_overrides` 에 별도 ID 를 준다.
   - `[Browsable(false)] 숨김 속성`: 디자이너 화면에서 편집하는 속성(예: 인자 목록)이면 `show: true`, 내부 값이면 yaml 에서 제거.
   - `생성 결과와 현재 문서가 다릅니다`: 3단계에서 해결된다.
3. **WARN** 은 문서 문제가 아니라 대개 원본 리소스 누락이다. 최종 보고의 "원본 수정 제안"에 모아 둔다(예: `X_DisplayName` 없음, 제네릭 액티비티 폴백 표시명 없음, ko/en resx 불일치).
4. `python scripts/gen_activities.py --write` 후 `git diff --stat docs/user/activities` 와 주요 diff 를 훑어 의도한 변경(새 항목, 표시명 변경, 속성 추가/삭제)만 있는지 확인한다. 뜻밖의 대량 변화(속성 순서 뒤집힘, 라벨 사라짐)는 생성기 회귀이므로 `scripts/neorpa_docs.py` 를 먼저 고친다.
5. `--check` 가 ERROR 0 으로 끝나야 한다.

## 3. 수기 페이지

1단계 매핑에 따라 해당 페이지만 열어 점검한다. 원칙:

- UI 문자열(버튼·메뉴·창 제목·트레이 메뉴)은 원본 XAML(`Views/**`)·`Resources.ko.resx`·`.bat`/`README` 에서 **그대로 인용**한다. 스크린샷 없이 글로 위치를 설명한다.
- 동작을 서술할 때는 해당 `.cs` 를 읽고 확인한 뒤 쓴다. 확인하지 못한 내용은 쓰지 않는다.
- 제약·지원 범위 문구는 커밋 메시지나 코드로 뒷받침될 때만 완화/강화한다.
- 자주 갱신되는 절: `getting-started.md`(설치 파일명·버전, 시작 화면, 리본, 명령줄), `concepts.md`(프로젝트, 디버깅 패널 표, 로그 수준), `remote-desktop.md`(설치·로그·제약), `troubleshooting.md`, `glossary.md`.

## 4. 변경 이력

`docs/changelog.md` 맨 위(제목 바로 아래)에 새 절을 추가한다.

```
## YYYY-MM-DD · NeoRPA <버전> { #v<버전-대시> }

원본 `<이전 7자>` → `<현재 7자>` (<날짜 범위>)

### 새 액티비티 / ### 변경된 액티비티 / ### 디자이너 / ### 원격 데스크톱 자동화 / ### 문서
```

항목은 사용자 관점 한 줄씩. 해당 없는 소절은 생략한다. 버전은 `data/source-state.json` 의 `product_version`.

## 5. 검증

- `pwsh -File scripts/build.ps1` → `mkdocs build --strict` 경고 0. 새 페이지가 있으면 `mkdocs.yml` `nav` 에 한 줄 추가(파일을 텍스트로 편집).
- `python scripts/gen_activities.py --check` exit 0, 그리고 `--write` 를 다시 실행해도 변경 없음(결정성).
- `grep -rn "gen_activity_stubs\|website/" docs README.md` 결과 없음.
- 수기 페이지에서 인용한 UI 라벨을 원본 문자열과 한 번 더 대조한다.

## 6. 마무리

- `git status` 로 변경 파일을 확인하고 하나의 커밋으로 만든다: `docs: sync with rpa-designer <7자 해시> (v<버전>)`. 의미 단위가 다르면(하네스 수정 등) 커밋을 나눈다.
- **push 는 하지 않는다.** 사용자가 명시적으로 요청했을 때만 push 한다(`main` push = 공개 사이트 즉시 배포).
- 최종 보고: 반영한 원본 커밋 범위와 버전, 새/변경 액티비티 수, 수정한 수기 페이지 목록, 남은 TODO(설명 미작성, 확인 못한 동작), **원본 수정 제안**(WARN 목록: resx 누락·제네릭 폴백 표시명·csproj 미포함 소스 등).
