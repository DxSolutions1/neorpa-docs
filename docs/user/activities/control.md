<!-- 이 파일은 scripts/gen_activities.py 로 자동 생성됩니다.
     직접 편집하지 말고 data/activities.yaml 을 고친 뒤 `python scripts/gen_activities.py --write` 를 다시 실행하세요. -->


# Control (데스크톱 UI · 파일 · 프로세스)

데스크톱 애플리케이션 UI 자동화(셀렉터·이미지·OCR)와 파일·클립보드·프로세스·코드 실행 유틸.

> 이 카테고리에는 34개의 액티비티가 있습니다. 각 액티비티의 **속성** 표는 소스에서 자동 추출되며(상속 포함), 표시명·설명은 리소스/설명 데이터에서 해석됩니다.

## 창 연결 (스코프)  <small>`AttachWindowScope`</small>

이미 열려 있는 데스크톱 창에 연결하는 스코프입니다. 본문에 놓인 자식 액티비티가 그 창을 대상으로 동작합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 셀렉터 <small>`Selector`</small> | 입력 | `string` | 동작 대상 UI 요소를 식별하는 셀렉터. |
| 타임아웃 <small>`Timeout`</small> | 입력 | `int` | 대상을 찾기까지 대기할 최대 시간(밀리초). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
| 애플리케이션 창 <small>`ApplicationWindow`</small> | 출력 | `Process` | 연결하거나 새로 연 애플리케이션 창(프로세스)을 담는 변수. |

## 연결 (윈도우)  <small>`AttachWindow`</small>

이미 실행 중인 데스크톱 애플리케이션 창에 연결해 이후 UI 액티비티의 대상으로 삼습니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
| 타임아웃 <small>`Timeout`</small> | 입력 | `int` | 대상을 찾기까지 대기할 최대 시간(밀리초). |
| 애플리케이션 창 <small>`ApplicationWindow`</small> | 출력 | `Process` | 연결하거나 새로 연 애플리케이션 창(프로세스)을 담는 변수. |
| 셀렉터 <small>`Selector`</small> | 입력 | `string` | 동작 대상 UI 요소를 식별하는 셀렉터. |

## 텍스트 입력  <small>`TypeInto`</small>

셀렉터로 지정한 입력 요소에 텍스트를 입력합니다. 특수키 토큰(`[k(enter)]` 등)·입력 방식(하드웨어/시뮬레이트)·기존 값 비우기를 지원합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
| 타이핑 전 클릭 <small>`ClickBeforeTyping`</small> | 입력 | `bool` | 텍스트를 입력하기 전에 대상 요소를 먼저 클릭할지 여부. |
| 작업 전 타임아웃 <small>`BeforeTimeout`</small> | 입력 | `int` | 동작을 시작하기 전에 대기할 시간(밀리초). |
| 작업 후 타임아웃 <small>`AfterTimeout`</small> | 입력 | `int` | 동작을 마친 뒤 추가로 대기할 시간(밀리초). |
| 요소 찾기 대기 시간 <small>`WaitTimeout`</small> | 입력 | `int` | 대상 요소를 찾기까지 대기할 최대 시간(밀리초). |
| 필드 비우기 <small>`EmptyField`</small> | 입력 | `bool` | 입력하기 전에 대상 필드를 비울지 여부. |
| SendKey 사용 <small>`UseSendKey`</small> | 입력 | `bool` | SendKeys 방식으로 키를 전송할지 여부. |
| 입력 방식 <small>`InputMethod`</small> | 입력 | `string` | 텍스트 입력 방식(하드웨어 이벤트, 윈도우 메시지 등). |
| 키 간 지연 <small>`DelayBetweenKeys`</small> | 입력 | `int` | 키 입력 사이에 둘 지연 시간(밀리초). |
| 비우기 방식 <small>`ClearMethod`</small> | 입력 | `string` | 입력 전에 기존 필드 내용을 지우는 방식. |
| 값 <small>`Value`</small> | 입력 | `string` | 대상 요소에 입력할 텍스트. |
| 셀렉터 <small>`Selector`</small> | 입력 | `string` | 동작 대상 UI 요소를 식별하는 셀렉터. |

## 클릭  <small>`Click`</small>

셀렉터로 지정한 요소를 클릭합니다. 좌/우/더블 클릭, 시뮬레이터(백그라운드) 클릭과 물리 클릭을 지원합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
| 작업 전 타임아웃 <small>`BeforeTimeout`</small> | 입력 | `int` | 동작을 시작하기 전에 대기할 시간(밀리초). |
| 작업 후 타임아웃 <small>`AfterTimeout`</small> | 입력 | `int` | 동작을 마친 뒤 추가로 대기할 시간(밀리초). |
| 요소 찾기 대기 시간 <small>`WaitTimeout`</small> | 입력 | `int` | 대상 요소를 찾기까지 대기할 최대 시간(밀리초). |
| 시뮬레이터 사용 <small>`UseSimulator`</small> | 입력 | `bool` | 시뮬레이터(백그라운드 입력) 방식으로 동작할지 여부. |
| 로딩 상태 <small>`ReadyState`</small> | 입력 | `string` | 동작을 실행하기 전에 기다릴 페이지 로딩 상태(예: INTERACTIVE, COMPLETE). |
| 사각 영역 <small>`RectArea`</small> | 입력 | `string` | 대상 요소의 화면상 사각 영역(경계 좌표). |
| 위치 <small>`ClickPosition`</small> | 입력 | `string` | 요소 영역 안에서 클릭 기준으로 삼을 지점(가운데, 좌상단 등). |
| 오프셋 X <small>`OffsetX`</small> | 입력 | `int` | 클릭 기준점에서 가로로 이동할 오프셋(픽셀). |
| 오프셋 Y <small>`OffsetY`</small> | 입력 | `int` | 클릭 기준점에서 세로로 이동할 오프셋(픽셀). |
| 마우스 버튼 종류 <small>`MouseButton`</small> | 입력 | `string` | 클릭에 사용할 마우스 버튼(왼쪽/오른쪽/가운데). |
| 클릭 동작 <small>`ClickAction`</small> | 입력 | `string` | 클릭 동작의 종류(단일 클릭, 더블 클릭 등). |
| 셀렉터 <small>`Selector`</small> | 입력 | `string` | 동작 대상 UI 요소를 식별하는 셀렉터. |

## 클릭 V2  <small>`ClickV2`</small>

셀렉터로 지정한 요소를 클릭하는 개선판 클릭 액티비티입니다. 요소 탐색 범위를 제한해 응답이 느린 창에서도 빠르게 대상을 찾고, 셀렉터 속성이 정확히 일치하지 않아도 **유사 일치**로 요소를 찾을 수 있습니다. 속성 구성은 `클릭`과 같고 유사 일치 옵션 세 가지가 추가되었습니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
| 작업 전 타임아웃 <small>`BeforeTimeout`</small> | 입력 | `int` | 동작을 시작하기 전에 대기할 시간(밀리초). |
| 작업 후 타임아웃 <small>`AfterTimeout`</small> | 입력 | `int` | 동작을 마친 뒤 추가로 대기할 시간(밀리초). |
| 요소 찾기 대기 시간 <small>`WaitTimeout`</small> | 입력 | `int` | 대상 요소를 찾기까지 대기할 최대 시간(밀리초). |
| 시뮬레이터 사용 <small>`UseSimulator`</small> | 입력 | `bool` | 시뮬레이터(백그라운드 입력) 방식으로 동작할지 여부. |
| 로딩 상태 <small>`ReadyState`</small> | 입력 | `string` | 동작을 실행하기 전에 기다릴 페이지 로딩 상태(예: INTERACTIVE, COMPLETE). |
| 유사 일치 사용 <small>`EnableFuzzyMatching`</small> | 입력 | `bool` | 셀렉터와 정확히 일치하는 요소가 없을 때 유사 일치로 대상을 찾을지 여부(기본 true). |
| 유사 일치 임계값 <small>`FuzzyThreshold`</small> | 입력 | `int` | 유사 일치로 인정할 최소 유사도(0~100, 기본 82). 값이 낮을수록 느슨하게 찾습니다. |
| 고유 대상 필요 <small>`RequireUniqueTarget`</small> | 입력 | `bool` | 유사 일치 후보가 여럿일 때 가장 높은 점수의 요소가 확실히 구분되는 경우에만 클릭할지 여부(기본 true). 구분되지 않으면 실패로 처리합니다. |
| 사각 영역 <small>`RectArea`</small> | 입력 | `string` | 대상 요소의 화면상 사각 영역(경계 좌표). |
| 위치 <small>`ClickPosition`</small> | 입력 | `string` | 요소 영역 안에서 클릭 기준으로 삼을 지점(가운데, 좌상단 등). |
| 오프셋 X <small>`OffsetX`</small> | 입력 | `int` | 클릭 기준점에서 가로로 이동할 오프셋(픽셀). |
| 오프셋 Y <small>`OffsetY`</small> | 입력 | `int` | 클릭 기준점에서 세로로 이동할 오프셋(픽셀). |
| 마우스 버튼 종류 <small>`MouseButton`</small> | 입력 | `string` | 클릭에 사용할 마우스 버튼(왼쪽/오른쪽/가운데). |
| 클릭 동작 <small>`ClickAction`</small> | 입력 | `string` | 클릭 동작의 종류(단일 클릭, 더블 클릭 등). |
| 셀렉터 <small>`Selector`</small> | 입력 | `string` | 동작 대상 UI 요소를 식별하는 셀렉터. |

## 클릭 (Vision)  <small>`ClickVision`</small>

OCR/비전 하이브리드로 화면의 텍스트·요소를 찾아 클릭합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
| 작업 전 타임아웃 <small>`BeforeTimeout`</small> | 입력 | `int` | 동작을 시작하기 전에 대기할 시간(밀리초). |
| 작업 후 타임아웃 <small>`AfterTimeout`</small> | 입력 | `int` | 동작을 마친 뒤 추가로 대기할 시간(밀리초). |
| 요소 찾기 대기 시간 <small>`WaitTimeout`</small> | 입력 | `int` | 대상 요소를 찾기까지 대기할 최대 시간(밀리초). |
| 대상 텍스트 <small>`TargetText`</small> | 입력 | `string` | 화면 비전으로 찾을 대상의 텍스트. |
| 앵커 텍스트 <small>`AnchorText`</small> | 입력 | `string` | 대상 요소를 찾을 때 기준점으로 삼는 주변 텍스트. |
| 앵커 위치 <small>`AnchorPosition`</small> | 입력 | `string` | 앵커 텍스트를 기준으로 대상이 위치한 방향(위/아래/좌/우 등). |
| 이미지 경로 <small>`ImageCropPath`</small> | 입력 | `string` | 비전 매칭에 사용할 크롭 이미지 파일 경로. |
| OCR 신뢰도 <small>`OcrConfidence`</small> | 입력 | `double` | OCR 텍스트 인식의 최소 신뢰도(0~1). |
| 이미지 임계값 <small>`ImageThreshold`</small> | 입력 | `double` | 이미지 매칭 임계값(0~1, 높을수록 엄격하게 일치). |
| 오프셋 X <small>`OffsetX`</small> | 입력 | `int` | 클릭 기준점에서 가로로 이동할 오프셋(픽셀). |
| 오프셋 Y <small>`OffsetY`</small> | 입력 | `int` | 클릭 기준점에서 세로로 이동할 오프셋(픽셀). |
| 마우스 버튼 종류 <small>`MouseButton`</small> | 입력 | `string` | 클릭에 사용할 마우스 버튼(왼쪽/오른쪽/가운데). |
| 클릭 동작 <small>`ClickAction`</small> | 입력 | `string` | 클릭 동작의 종류(단일 클릭, 더블 클릭 등). |
| 셀렉터 <small>`Selector`</small> | 입력 | `string` | 동작 대상 UI 요소를 식별하는 셀렉터. |

## 클릭 (이미지)  <small>`ImageClick`</small>

화면에서 지정한 이미지와 일치하는 위치를 찾아 클릭합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
| 작업 전 타임아웃 <small>`BeforeTimeout`</small> | 입력 | `int` | 동작을 시작하기 전에 대기할 시간(밀리초). |
| 작업 후 타임아웃 <small>`AfterTimeout`</small> | 입력 | `int` | 동작을 마친 뒤 추가로 대기할 시간(밀리초). |
| 파일 이름 <small>`FileName`</small> | 입력 | `string` | 대상 파일의 이름 또는 경로. |
| 마우스 버튼 종류 <small>`MouseButton`</small> | 입력 | `string` | 클릭에 사용할 마우스 버튼(왼쪽/오른쪽/가운데). |
| 클릭 동작 <small>`ClickAction`</small> | 입력 | `string` | 클릭 동작의 종류(단일 클릭, 더블 클릭 등). |
| 탐색 시간 <small>`SearchTimeout`</small> | 입력 | `int` | 대상 이미지를 찾기까지 대기할 최대 시간(밀리초). |
| 유사도 <small>`Similarity`</small> | 입력 | `int` | 이미지 매칭 유사도(백분율, 높을수록 엄격하게 일치). |
| 오프셋 X <small>`OffsetX`</small> | 입력 | `int` | 클릭 기준점에서 가로로 이동할 오프셋(픽셀). |
| 오프셋 Y <small>`OffsetY`</small> | 입력 | `int` | 클릭 기준점에서 세로로 이동할 오프셋(픽셀). |

## ImageExists  <small>`ImageExists`</small>

화면에 지정한 이미지가 존재하는지 확인해 참/거짓을 반환합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
| 작업 전 타임아웃 <small>`BeforeTimeout`</small> | 입력 | `int` | 동작을 시작하기 전에 대기할 시간(밀리초). |
| 작업 후 타임아웃 <small>`AfterTimeout`</small> | 입력 | `int` | 동작을 마친 뒤 추가로 대기할 시간(밀리초). |
| 파일 이름 <small>`FileName`</small> | 입력 | `string` | 대상 파일의 이름 또는 경로. |
| 탐색 시간 <small>`SearchTimeout`</small> | 입력 | `int` | 대상 이미지를 찾기까지 대기할 최대 시간(밀리초). |
| 유사도 <small>`Similarity`</small> | 입력 | `int` | 이미지 매칭 유사도(백분율, 높을수록 엄격하게 일치). |
| 결과 <small>`Result`</small> | 출력 | `bool` | 액티비티 실행 결과(출력). |

## 마우스 오버  <small>`Hover`</small>

셀렉터로 지정한 요소 위로 마우스를 올립니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
| 사각 영역 <small>`RectArea`</small> | 입력 | `string` | 대상 요소의 화면상 사각 영역(경계 좌표). |
| 작업 전 타임아웃 <small>`BeforeTimeout`</small> | 입력 | `int` | 동작을 시작하기 전에 대기할 시간(밀리초). |
| 작업 후 타임아웃 <small>`AfterTimeout`</small> | 입력 | `int` | 동작을 마친 뒤 추가로 대기할 시간(밀리초). |
| 요소 찾기 대기 시간 <small>`WaitTimeout`</small> | 입력 | `int` | 대상 요소를 찾기까지 대기할 최대 시간(밀리초). |
| 셀렉터 <small>`Selector`</small> | 입력 | `string` | 동작 대상 UI 요소를 식별하는 셀렉터. |

## 텍스트 가져오기  <small>`GetText`</small>

셀렉터로 지정한 요소의 텍스트를 읽어 반환합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
| 작업 전 타임아웃 <small>`BeforeTimeout`</small> | 입력 | `int` | 동작을 시작하기 전에 대기할 시간(밀리초). |
| 작업 후 타임아웃 <small>`AfterTimeout`</small> | 입력 | `int` | 동작을 마친 뒤 추가로 대기할 시간(밀리초). |
| 요소 찾기 대기 시간 <small>`WaitTimeout`</small> | 입력 | `int` | 대상 요소를 찾기까지 대기할 최대 시간(밀리초). |
| 로딩 상태 <small>`ReadyState`</small> | 입력 | `string` | 동작을 실행하기 전에 기다릴 페이지 로딩 상태(예: INTERACTIVE, COMPLETE). |
| 결과 <small>`Result`</small> | 출력 | `string` | 액티비티 실행 결과(출력). |
| 셀렉터 <small>`Selector`</small> | 입력 | `string` | 동작 대상 UI 요소를 식별하는 셀렉터. |

## 속성 가져오기  <small>`GetAttribute`</small>

셀렉터로 지정한 요소의 지정한 속성(attribute) 값을 읽어 반환합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
| 작업 전 타임아웃 <small>`BeforeTimeout`</small> | 입력 | `int` | 동작을 시작하기 전에 대기할 시간(밀리초). |
| 작업 후 타임아웃 <small>`AfterTimeout`</small> | 입력 | `int` | 동작을 마친 뒤 추가로 대기할 시간(밀리초). |
| 요소 찾기 대기 시간 <small>`WaitTimeout`</small> | 입력 | `int` | 대상 요소를 찾기까지 대기할 최대 시간(밀리초). |
| 속성 이름 <small>`AttrName`</small> | 입력 | `string` | 읽어올 요소 속성(attribute)의 이름. |
| 결과 <small>`Result`</small> | 출력 | `string` | 액티비티 실행 결과(출력). |
| 전체 속성 <small>`Attributes`</small> | 출력 | `Dictionary<string, string>` | 요소의 모든 속성을 이름-값 사전으로 담는 출력. |
| 셀렉터 <small>`Selector`</small> | 입력 | `string` | 동작 대상 UI 요소를 식별하는 셀렉터. |

## 단축키 실행  <small>`Hotkey`</small>

지정한 단축키(조합 키)를 대상 요소나 창에 전송합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `Alt` | 설정 | `bool` | 단축키에 Alt 키를 함께 누를지 여부. |
| `Ctrl` | 설정 | `bool` | 단축키에 Ctrl 키를 함께 누를지 여부. |
| `Shift` | 설정 | `bool` | 단축키에 Shift 키를 함께 누를지 여부. |
| `Win` | 설정 | `bool` | 단축키에 Windows 키를 함께 누를지 여부. |
| `SpecialKey` | 설정 | `bool` | 일반 문자 대신 특수 키(기능 키 등)를 입력할지 여부. |
| `InputDelay` | 입력 | `int` | 각 키 입력 사이에 둘 지연 시간(밀리초). |
| `Key` | 입력 | `string` | 누를 주 키. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 요소 존재 확인  <small>`ElementExists`</small>

셀렉터로 지정한 요소가 화면에 존재하는지 확인해 참/거짓을 반환합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
| `TimeOut` | 입력 | `int` | 대상 요소를 찾기까지 대기할 최대 시간(밀리초). |
| 존재 여부 <small>`IsExist`</small> | 출력 | `bool` | 대상 요소의 존재 여부(출력). |
| 셀렉터 <small>`Selector`</small> | 입력 | `string` | 동작 대상 UI 요소를 식별하는 셀렉터. |

## 스크린샷 캡처  <small>`TakeScreenshot`</small>

화면 전체 또는 지정한 요소/영역을 캡처해 이미지로 가져옵니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
| 작업 전 타임아웃 <small>`BeforeTimeout`</small> | 입력 | `int` | 동작을 시작하기 전에 대기할 시간(밀리초). |
| 작업 후 타임아웃 <small>`AfterTimeout`</small> | 입력 | `int` | 동작을 마친 뒤 추가로 대기할 시간(밀리초). |
| 요소 찾기 대기 시간 <small>`WaitTimeout`</small> | 입력 | `int` | 대상 요소를 찾기까지 대기할 최대 시간(밀리초). |
| 스크린샷 <small>`Screenshot`</small> | 출력 | `Image` | 캡처한 스크린샷 이미지(출력). |
| 셀렉터 <small>`Selector`</small> | 입력 | `string` | 동작 대상 UI 요소를 식별하는 셀렉터. |

## 이미지 저장  <small>`SaveImage`</small>

이미지를 지정한 경로에 파일로 저장합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
| 이미지 <small>`Image`</small> | 입력 | `Image` | 저장할 이미지 개체. |
| 클립보드 사용 <small>`UseClipboard`</small> | 입력 | `bool` | 클립보드에 있는 이미지를 사용할지 여부. |
| 디렉터리 <small>`Directory`</small> | 입력 | `string` | 이미지를 저장할 디렉터리 경로. |
| 파일 이름 <small>`FileName`</small> | 입력 | `string` | 대상 파일의 이름 또는 경로. |

## 코드 실행  <small>`InvokeCode`</small>

워크플로 안에서 직접 작성한 VB 코드를 실행합니다. 인자를 주고받을 수 있습니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| VB 코드 <small>`VBCode`</small> | 입력 | `string` | 실행할 VB 코드. |
| 인자 <small>`Arguments`</small> | 입력 | `List<ArgumentInfo>` | 호출 대상에 전달하거나 로그에 추가할 인자 모음(이름-값). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 워크플로 실행  <small>`InvokeWorkflowFile`</small>

다른 워크플로(.xaml) 파일을 호출해 실행하며, 인자를 주고받습니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `WorkflowFilePath` | 입력 | `string` | 호출할 워크플로(.xaml) 파일 경로. |
| 인자 <small>`Arguments`</small> | 입력 | `List<ArgumentInfo>` | 호출 대상에 전달하거나 로그에 추가할 인자 모음(이름-값). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 메시지 상자  <small>`MessageBox`</small>

메시지 상자를 띄워 사용자에게 안내 문구를 보여 줍니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 값 <small>`Value`</small> | 입력 | `string` | 메시지 상자에 표시할 값. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 메시지 상자 (데이터 테이블)  <small>`MessageBoxDataTable`</small>

DataTable의 내용을 표 형태로 메시지 상자에 표시합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 값 <small>`Value`</small> | 입력 | `DataTable` | 메시지 상자에 표시할 DataTable. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## PowerShell 실행  <small>`InvokePowerShell`</small>

PowerShell 명령이나 스크립트를 실행하고 결과를 가져옵니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `CommandText` | 입력 | `String` | 실행할 PowerShell 명령 또는 스크립트 텍스트. |
| `Input` | 입력 | `Collection<PSObject>` | PowerShell 파이프라인에 전달할 입력 개체 모음. |
| `Parameter` | 입력 | `Dictionary<String,InArgument>` | PowerShell에 전달할 매개변수(이름-값). |
| `PowerShellVariables` | 입력 | `Dictionary<String, Argument>` | 스크립트에서 사용할 PowerShell 변수(이름-값). |
| `IsScript` | 설정 | `bool` | 명령을 단일 명령이 아닌 스크립트로 실행할지 여부. |
| `TypeArgument` | 설정 | `Type` | 값의 데이터 형식(Type). |
| `Output` | 출력 | `Collection<PSObject>` | 실행 결과 개체(출력). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## Python 실행  <small>`StartPython`</small>

지정한 Python 스크립트 파일을 인자와 함께 실행합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 파일 이름 <small>`FileName`</small> | 입력 | `string` | 대상 파일의 이름 또는 경로. |
| `argument` | 입력 | `string` | 실행할 프로그램/스크립트에 전달할 명령줄 인수. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 경로 존재 여부 확인  <small>`PathExist`</small>

지정한 파일/폴더 경로가 존재하는지 확인해 참/거짓을 반환합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `Path` | 입력 | `string` | 존재 여부를 확인할 대상 경로. |
| `PathType` | 설정 | `PathType` | 확인할 경로의 종류(파일/폴더). |
| `Exists` | 출력 | `Boolean` | 지정한 경로의 존재 여부(출력). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 파일 복사  <small>`CopyFile`</small>

파일을 지정한 위치로 복사합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `overwrite` | 설정 | `bool` | 대상이 이미 있으면 덮어쓸지 여부. |
| `path` | 입력 | `string` | 대상 파일 또는 폴더의 경로. |
| `destination` | 입력 | `string` | 복사/이동할 대상 경로. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 파일 이동  <small>`MoveFile`</small>

파일을 지정한 위치로 이동합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `Overwrite` | 설정 | `bool` | 대상이 이미 있으면 덮어쓸지 여부. |
| `path` | 입력 | `string` | 대상 파일 또는 폴더의 경로. |
| `destination` | 입력 | `string` | 복사/이동할 대상 경로. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 파일 삭제  <small>`DeleteFile`</small>

지정한 파일을 삭제합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `path` | 입력 | `string` | 대상 파일 또는 폴더의 경로. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 프로세스 시작  <small>`StartProcess`</small>

지정한 프로그램(실행 파일)을 인자와 함께 실행합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 파일 이름 <small>`FileName`</small> | 입력 | `string` | 대상 파일의 이름 또는 경로. |
| `argument` | 입력 | `string` | 실행할 프로그램/스크립트에 전달할 명령줄 인수. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 창 최대화  <small>`MaximizeWindow`</small>

대상 창을 최대화합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 대상 창 <small>`Window`</small> | 입력 | `Process` | 동작 대상이 되는 창(프로세스). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 입력 대화 상자  <small>`InputDialog`</small>

입력 대화 상자를 띄워 사용자로부터 값을 입력받습니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 대화 상자 제목 <small>`DialogTitle`</small> | 입력 | `string` | 입력 대화 상자의 제목. |
| 입력 라벨 <small>`InputLabel`</small> | 입력 | `string` | 입력 대화 상자에 표시할 안내 라벨. |
| 입력 형식 <small>`InputType`</small> | 입력 | `string` | 입력 대화 상자에서 받을 값의 형식(텍스트/숫자/선택 등). |
| 옵션 <small>`Options`</small> | 입력 | `string` | 입력 대화 상자에서 선택할 수 있는 항목 목록. |
| 결과 <small>`Result`</small> | 출력 | `string` | 액티비티 실행 결과(출력). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 클립보드에서 가져오기  <small>`GetToClipBoard`</small>

클립보드에 들어 있는 텍스트를 가져옵니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `text` | 출력 | `string` | 클립보드로 주고받을 텍스트. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 클립보드로 설정  <small>`SetToClipBoard`</small>

지정한 텍스트를 클립보드에 복사합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `text` | 입력 | `string` | 클립보드로 주고받을 텍스트. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 폴더 생성  <small>`CreateDirectory`</small>

지정한 경로에 폴더를 생성합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `path` | 입력 | `string` | 대상 파일 또는 폴더의 경로. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 폴더 삭제  <small>`DeleteDirectory`</small>

지정한 폴더를 삭제합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `path` | 입력 | `string` | 대상 파일 또는 폴더의 경로. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 항목 삭제(파일/디렉토리)  <small>`DeleteFileOrDirectory`</small>

지정한 경로가 파일이면 파일을, 폴더면 하위 내용까지 포함해 삭제합니다. 경로가 존재하지 않으면 오류가 발생합니다. 파일과 폴더를 구분하지 않고 지울 때 `파일 삭제`·`디렉토리 삭제` 대신 사용합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `path` | 입력 | `string` | 삭제할 파일 또는 폴더 경로. 상대 경로는 프로젝트 루트 기준으로 해석됩니다. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 주석 처리  <small>`CommentOut`</small>

본문에 담긴 자식 액티비티를 실행하지 않고 건너뜁니다. 일부 단계를 임시로 비활성화(주석 처리)할 때 사용합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `Note` | 설정 | `string` | 액티비티에 남기는 메모(주석)로, 실행에는 영향을 주지 않는다. |
