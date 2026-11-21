<!-- 이 파일은 scripts/gen_activities.py 로 자동 생성됩니다.
     직접 편집하지 말고 data/activities.yaml 을 고친 뒤 `python scripts/gen_activities.py --write` 를 다시 실행하세요. -->


# PowerPoint (텍스트 읽기 · 바꾸기)

PowerPoint 문서(.pptx)의 글을 슬라이드별로 읽고, 글을 찾아 바꿉니다. 서식 발표 자료의 `{{월}}` 같은 자리를 채워 보고 자료를 찍어 내는 데 씁니다. 파일을 직접 다루므로 **PowerPoint 가 설치되어 있지 않아도** 됩니다.

> 이 카테고리에는 2개의 액티비티가 있습니다. 각 액티비티의 **속성** 표는 소스에서 자동 추출되며(상속 포함), 표시명·설명은 리소스/설명 데이터에서 해석됩니다.

!!! note "제공 버전"
    PowerPoint 카테고리는 NeoRPA 2.2.4 다음 버전부터 제공됩니다. 툴박스에 **PowerPoint** 가 보이지 않으면 도움말 탭 → **버전 관리** 에서 새 버전을 확인하세요.

!!! warning "다루는 파일과 글"
    - **.pptx**(.pptm·.potx 포함)만 다룹니다. 예전 형식(**.ppt**)과 **암호가 걸린 문서**는 PowerPoint 에서 암호 없이 .pptx 로 저장한 뒤 쓰세요.
    - 슬라이드의 도형·표 안의 글을 다룹니다. **차트·SmartArt 안의 글과 슬라이드 마스터의 글**(모든 슬라이드에 깔리는 바닥글 등)은 읽거나 바꾸지 않습니다.
    - 문서를 PDF 로 저장하는 기능은 아직 없습니다.

## PowerPoint 텍스트 읽기  <small>`ReadPowerPointText`</small>

PowerPoint 문서(.pptx)의 글을 슬라이드별로 읽습니다. 도형의 문단마다 한 줄, 표는 행마다 한 줄(칸은 탭으로 구분)입니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 파일 경로 <small>`FilePath`</small> | 입력 | `string` | 읽을 PowerPoint 문서(.pptx). 상대 경로는 프로젝트 폴더 기준입니다. 카드의 `…` 버튼으로 고를 수 있습니다. |
| 슬라이드 노트 포함 <small>`IncludeNotes`</small> | 설정 | `bool` | 슬라이드 노트의 글도 함께 읽을지 여부(기본 false). 그 슬라이드의 글 뒤에 붙습니다. |
| 결과 <small>`Result`</small> | 출력 | `string` | 모든 슬라이드의 글(출력). 슬라이드 사이에는 빈 줄이 하나 들어갑니다. |
| 슬라이드별 텍스트 <small>`SlideTexts`</small> | 출력 | `string[]` | 슬라이드별 글(출력, 문자열 배열 — 발표 순서). `SlideTexts(0)` 이 첫 슬라이드입니다. 글이 없는 슬라이드는 빈 텍스트입니다. |
| 슬라이드 수 <small>`SlideCount`</small> | 출력 | `int` | 슬라이드 수(출력). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## PowerPoint 텍스트 바꾸기  <small>`ReplacePowerPointText`</small>

PowerPoint 문서(.pptx)의 모든 슬라이드에서 텍스트를 찾아 **모두** 바꿉니다. 도형과 표 안의 글에서 찾습니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 파일 경로 <small>`FilePath`</small> | 입력 | `string` | 고칠 PowerPoint 문서(.pptx) — 서식 발표 자료. 상대 경로는 프로젝트 폴더 기준입니다. |
| 찾을 텍스트 <small>`SearchText`</small> | 입력 | `string` | 찾을 텍스트(글자 그대로). 화면에 이어져 보이는 글이면, 파일 안에서 서식이 여러 조각으로 나뉘어 있어도 찾습니다. 탭·줄바꿈·다른 문단에 걸친 글은 찾지 않습니다. |
| 바꿀 텍스트 <small>`Replacement`</small> | 입력 | `string` | 바꿀 텍스트. 비우면 찾은 곳을 지웁니다. 줄바꿈(`vbLf`)을 넣으면 문서에도 줄바꿈으로 들어갑니다. 찾은 곳이 **시작하는 자리의 서식**(굵게·글자 크기)을 따릅니다. |
| 저장할 파일 <small>`OutputPath`</small> | 입력 | `string` | 결과를 저장할 파일. **비우면 원본을 고칩니다.** 적으면 원본은 그대로 두고 이 파일로 씁니다(있으면 덮어씀, 폴더가 없으면 만듦) — 서식 파일에서 문서를 찍어 낼 때 씁니다. 카드의 `…` 버튼으로 이름을 정할 수 있습니다. |
| 대소문자 무시 <small>`IgnoreCase`</small> | 설정 | `bool` | 대소문자를 가리지 않고 찾을지 여부(기본 false). |
| 슬라이드 노트 포함 <small>`IncludeNotes`</small> | 설정 | `bool` | 슬라이드 노트의 글도 바꿀지 여부(기본 false). |
| 개수 <small>`Count`</small> | 출력 | `int` | 바꾼 곳의 수(출력). 못 찾으면 0 이고 오류는 아닙니다 — 경고 로그가 남습니다. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

- 쓰는 법은 [Word 의 서식 문서로 문서 찍어 내기](word.md#word-template)와 같습니다.
- 슬라이드 번호·날짜처럼 PowerPoint 가 채우는 자리(필드)의 글은 바꾸지 않습니다.
- 문서가 PowerPoint 에서 **열려 있으면 저장하지 못합니다**. 닫고 실행하세요.
