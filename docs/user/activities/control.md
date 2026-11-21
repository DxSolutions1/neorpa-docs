<!-- 이 파일은 scripts/gen_activities.py 로 자동 생성됩니다.
     직접 편집하지 말고 data/activities.yaml 을 고친 뒤 `python scripts/gen_activities.py --write` 를 다시 실행하세요. -->


# Control (데스크톱 UI · 파일 · 프로세스)

데스크톱 애플리케이션 UI 자동화(셀렉터·이미지·OCR)와 파일·클립보드·프로세스·코드 실행 유틸.

> 이 카테고리에는 41개의 액티비티가 있습니다. 각 액티비티의 **속성** 표는 소스에서 자동 추출되며(상속 포함), 표시명·설명은 리소스/설명 데이터에서 해석됩니다.

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
| 보호된 입력값 <small>`SecureValue`</small> | 입력 | `SecureString` | 보호된 값(SecureString). 자격 증명 가져오기(GetCredential)의 SecurePassword 출력을 연결하면 값이 워크플로 파일·로그에 남지 않습니다. 있으면 평문 인자보다 우선합니다. |
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

## 이미지 존재 확인  <small>`ImageExists`</small>

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
| 특수 키 <small>`SpecialKey`</small> | 설정 | `bool` | 일반 문자 대신 특수 키(기능 키 등)를 입력할지 여부. |
| 입력 지연 <small>`InputDelay`</small> | 입력 | `int` | 각 키 입력 사이에 둘 지연 시간(밀리초). |
| 키 <small>`Key`</small> | 입력 | `string` | 누를 주 키. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 요소 존재 확인  <small>`ElementExists`</small>

셀렉터로 지정한 요소가 화면에 존재하는지 확인해 참/거짓을 반환합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
| 타임아웃 <small>`TimeOut`</small> | 입력 | `int` | 대상 요소를 찾기까지 대기할 최대 시간(밀리초). |
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
| 워크플로 파일 경로 <small>`WorkflowFilePath`</small> | 입력 | `string` | 호출할 워크플로(.xaml) 파일 경로. |
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
| 명령 텍스트 <small>`CommandText`</small> | 입력 | `String` | 실행할 PowerShell 명령 또는 스크립트 텍스트. |
| 입력 <small>`Input`</small> | 입력 | `Collection<PSObject>` | PowerShell 파이프라인에 전달할 입력 개체 모음. |
| 매개 변수 <small>`Parameter`</small> | 입력 | `Dictionary<String,InArgument>` | PowerShell에 전달할 매개변수(이름-값). |
| PowerShell 변수 <small>`PowerShellVariables`</small> | 입력 | `Dictionary<String, Argument>` | 스크립트에서 사용할 PowerShell 변수(이름-값). |
| 스크립트 여부 <small>`IsScript`</small> | 설정 | `bool` | 명령을 단일 명령이 아닌 스크립트로 실행할지 여부. |
| 형식 인수 <small>`TypeArgument`</small> | 설정 | `Type` | 값의 데이터 형식(Type). |
| 출력 <small>`Output`</small> | 출력 | `Collection<PSObject>` | 실행 결과 개체(출력). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## Python 실행  <small>`StartPython`</small>

지정한 Python 스크립트 파일을 인자와 함께 실행합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 파일 이름 <small>`FileName`</small> | 입력 | `string` | 대상 파일의 이름 또는 경로. |
| 인수 <small>`argument`</small> | 입력 | `string` | 실행할 프로그램/스크립트에 전달할 명령줄 인수. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 경로 존재 여부 확인  <small>`PathExist`</small>

지정한 파일/폴더 경로가 존재하는지 확인해 참/거짓을 반환합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 경로 <small>`Path`</small> | 입력 | `string` | 존재 여부를 확인할 대상 경로. |
| 경로 종류 <small>`PathType`</small> | 설정 | `PathType` | 확인할 경로의 종류(파일/폴더). |
| 존재 여부 <small>`Exists`</small> | 출력 | `Boolean` | 지정한 경로의 존재 여부(출력). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 파일 복사  <small>`CopyFile`</small>

파일을 지정한 위치로 복사합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 덮어쓰기 <small>`overwrite`</small> | 설정 | `bool` | 대상이 이미 있으면 덮어쓸지 여부. |
| 경로 <small>`path`</small> | 입력 | `string` | 대상 파일 또는 폴더의 경로. |
| 대상 경로 <small>`destination`</small> | 입력 | `string` | 복사/이동할 대상 경로. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 파일 이동  <small>`MoveFile`</small>

파일을 지정한 위치로 이동합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 덮어쓰기 <small>`Overwrite`</small> | 설정 | `bool` | 대상이 이미 있으면 덮어쓸지 여부. |
| 경로 <small>`path`</small> | 입력 | `string` | 대상 파일 또는 폴더의 경로. |
| 대상 경로 <small>`destination`</small> | 입력 | `string` | 복사/이동할 대상 경로. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 파일 삭제  <small>`DeleteFile`</small>

지정한 파일을 삭제합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 경로 <small>`path`</small> | 입력 | `string` | 대상 파일 또는 폴더의 경로. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 텍스트 파일 읽기  <small>`ReadTextFile`</small>

텍스트 파일을 읽어 문자열로 돌려줍니다. 인코딩을 비우면 UTF-8(BOM 자동 인식)로 읽습니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 파일 경로 <small>`filePath`</small> | 입력 | `string` | 읽을 텍스트 파일 경로. 상대 경로는 프로젝트 폴더 기준입니다. |
| 인코딩 <small>`Encoding`</small> | 입력 | `string` | 파일 인코딩 이름(예: utf-8, euc-kr). 비우면 UTF-8. |
| 결과 <small>`Result`</small> | 출력 | `string` | 읽은 텍스트 전체(출력). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 텍스트 파일 쓰기  <small>`WriteTextFile`</small>

텍스트를 파일에 씁니다. 파일이 있으면 통째로 덮어쓰고, 없는 폴더는 만듭니다. 임시 파일에 다 쓴 뒤 바꿔 넣으므로 쓰는 도중 실패해도 반쪽짜리 파일이 남지 않습니다. UiPath Write Text File 에 해당합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 파일 경로 <small>`filePath`</small> | 입력 | `string` | 쓸 파일 경로. 상대 경로는 프로젝트 폴더 기준입니다. […] 버튼으로 저장 대화상자를 열 수 있습니다. |
| 텍스트 <small>`Text`</small> | 입력 | `string` | 파일에 쓸 텍스트. |
| 인코딩 <small>`Encoding`</small> | 입력 | `string` | 인코딩 이름. 비우거나 utf-8 이면 BOM 없는 UTF-8, BOM 이 필요하면 utf-8-bom, 그 밖에 euc-kr 등 .NET 인코딩 이름. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 줄 추가  <small>`AppendLine`</small>

파일 끝에 텍스트 한 줄(끝에 줄 바꿈)을 덧붙입니다. 파일이 없으면 만듭니다. 실행 로그·결과 기록을 쌓을 때 씁니다. UiPath Append Line 에 해당합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 파일 경로 <small>`filePath`</small> | 입력 | `string` | 덧붙일 파일 경로. 상대 경로는 프로젝트 폴더 기준입니다. |
| 텍스트 <small>`Text`</small> | 입력 | `string` | 덧붙일 한 줄 텍스트(줄 바꿈은 자동으로 붙습니다). |
| 인코딩 <small>`Encoding`</small> | 입력 | `string` | 인코딩 이름. 비우거나 utf-8 이면 BOM 없는 UTF-8, BOM 이 필요하면 utf-8-bom. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 파일 생성  <small>`CreateFile`</small>

빈 파일을 만듭니다. 이미 있으면 덮어쓰기 옵션이 켜졌을 때만 비우고, 꺼져 있으면 그대로 둡니다. UiPath Create File 에 해당합니다(폴더+이름 대신 전체 경로 하나).

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 파일 경로 <small>`filePath`</small> | 입력 | `string` | 만들 파일 경로. 없는 폴더는 함께 만듭니다. |
| 덮어쓰기 <small>`Overwrite`</small> | 설정 | `bool` | 이미 있는 파일을 비울지 여부(기본 false = 있는 파일 그대로). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 파일 압축 (Zip)  <small>`CompressFiles`</small>

파일·폴더를 zip 하나로 묶습니다. 대상은 파일, 폴더, 또는 `보고서\*.xlsx` 같은 파일 이름 패턴이고, 여러 개면 **대상 목록**에 경로 목록을 줍니다. 한글 파일 이름은 다른 프로그램에서도 깨지지 않게 적고, 암호를 주면 내용을 잠급니다. 임시 파일에 다 쓴 뒤 바꿔 넣으므로 도중에 실패해도 반쪽짜리 zip 이 남지 않습니다. UiPath Compress/Zip Files 에 해당합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 압축할 대상 <small>`SourcePath`</small> | 입력 | `string` | 압축할 파일이나 폴더의 경로. 마지막 조각에 `*`(여러 글자)·`?`(한 글자)를 쓰면 그 폴더에서 이름이 맞는 파일만 넣습니다(예: `out\*.xlsx` — 하위 폴더는 보지 않습니다). 상대 경로는 프로젝트 폴더 기준입니다. 카드의 📄(파일)·📁(폴더) 버튼으로 고를 수 있습니다. |
| 대상 목록 <small>`SourcePaths`</small> | 입력 | `IEnumerable<string>` | 압축할 것이 여러 개일 때의 경로 목록(문자열 배열이나 `List(Of String)` 변수). 예: `New String() {"견적서.xlsx", "첨부", "로그\*.txt"}`. **압축할 대상**과 함께 주면 합칩니다. 이름이 같은 파일 둘을 한 번에 넣으면 오류로 멈춥니다(하나가 사라지지 않게). |
| 압축 파일 <small>`ZipFilePath`</small> | 입력 | `string` | 만들 압축 파일(.zip). 없는 폴더는 만듭니다. 카드의 […] 버튼으로 저장 대화상자를 열 수 있습니다. 이름이 .zip 으로 끝나지 않으면 경고가 표시됩니다. |
| 덮어쓰기 <small>`Overwrite`</small> | 설정 | `bool` | 같은 이름의 압축 파일이 있으면 바꿔 쓸지 여부(기본 true). 끄면 이미 있을 때 오류로 멈추고 있던 파일은 그대로 둡니다. |
| 폴더 이름 포함 <small>`IncludeBaseFolder`</small> | 설정 | `bool` | 폴더를 압축할 때 그 폴더 이름째 넣을지 여부(기본 true — Windows 탐색기의 압축과 같습니다). 끄면 폴더 안의 파일·하위 폴더만 넣습니다. |
| 압축 수준 <small>`Compression`</small> | 설정 | `ZipCompression` | 압축 수준. **보통**(기본) · **빠르게**(덜 줄이는 대신 빠름) · **압축 안 함**(묶기만 — 이미 압축된 그림·xlsx·pdf 를 묶을 때). |
| 암호 <small>`Password`</small> | 입력 | `string` | 압축 파일 암호(평문). 직접 적으면 워크플로 파일에 그대로 저장되어 경고가 표시됩니다 — **보호된 비밀번호**를 쓰세요. 비우면 잠그지 않습니다. |
| 보호된 비밀번호 <small>`SecurePassword`</small> | 입력 | `SecureString` | 보호된 비밀번호(SecureString). 자격 증명 가져오기(GetCredential)의 SecurePassword 출력을 연결합니다. 있으면 평문 비밀번호보다 우선합니다. |
| 암호화 방식 <small>`Encryption`</small> | 설정 | `ZipEncryption` | 암호를 줬을 때 잠그는 방식. **AES-256**(기본, 안전 — 반디집·알집·7-Zip 으로 엽니다) · **ZipCrypto**(Windows 탐색기로도 열리지만 쉽게 풀리는 예전 방식). 암호가 없으면 쓰이지 않습니다. |
| 결과 <small>`Result`</small> | 출력 | `string` | 만든 압축 파일의 전체 경로(출력). 메일 첨부 등 다음 액티비티에 그대로 넘길 수 있습니다. |
| 개수 <small>`Count`</small> | 출력 | `int` | 넣은 파일 수(출력). 빈 폴더는 세지 않습니다. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

!!! note "제공 버전"
    파일 압축·압축 풀기는 NeoRPA 2.2.4 다음 버전부터 제공됩니다. 툴박스 **Control** 에 보이지 않으면 도움말 탭 → **버전 관리** 에서 새 버전을 확인하세요.

#### 대상을 적는 법 { #zip-source }

| 압축할 것 | 압축할 대상 | 압축 파일 안의 모습 |
|---|---|---|
| 파일 하나 | `out\보고서.xlsx` | `보고서.xlsx` |
| 폴더 통째로 | `out\11월` | `11월\…` (폴더 이름 포함을 끄면 폴더 안의 것만) |
| 한 폴더의 특정 파일들 | `out\*.xlsx` | 이름이 맞는 파일들(하위 폴더 제외) |
| 서로 다른 곳의 여러 개 | **대상 목록**에 `New String() {"a.xlsx", "첨부", "로그\*.txt"}` | 파일은 이름으로, 폴더는 폴더 이름으로 |

- 빈 폴더도 들어갑니다. 다른 프로그램이 쓰고 있는 로그 파일은 그 순간의 내용까지 넣습니다. Excel 로 열어 둔 통합 문서처럼 **잠긴 파일**은 읽을 수 없어 오류로 멈추니 먼저 닫으세요.
- 압축 파일을 압축할 폴더 **안에** 만들어도 됩니다(자기 자신은 넣지 않습니다).
- 패턴에 맞는 파일이 하나도 없거나 대상을 찾을 수 없으면 빈 zip 을 만들지 않고 오류로 멈춥니다.

!!! warning "암호를 쓸 때"
    - 받는 사람이 **Windows 탐색기만** 쓴다면 암호화 방식을 **ZipCrypto** 로 바꾸세요. 기본인 AES-256 은 탐색기가 열지 못할 수 있습니다(반디집·알집·7-Zip 은 엽니다).
    - 암호는 **영문·숫자·기호**로 정하세요. 한글 암호는 프로그램마다 다르게 읽어 풀리지 않을 수 있습니다.
    - 암호는 파일 **내용**만 잠급니다. 압축 파일 안의 파일 이름은 암호 없이도 보입니다.

## 압축 풀기 (Unzip)  <small>`ExtractFiles`</small>

zip 을 폴더에 풉니다. 풀기 전에 안의 항목을 모두 검사해서, 풀 폴더 밖을 가리키는 이름이 있거나 암호가 틀리면 **아무것도 쓰지 않고** 오류로 멈춥니다. 예전 Windows 도구나 macOS 에서 만든 압축 파일의 한글 이름도 알아서 읽습니다. UiPath Extract/Unzip Files 에 해당합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 압축 파일 <small>`ZipFilePath`</small> | 입력 | `string` | 풀 압축 파일(.zip). 상대 경로는 프로젝트 폴더 기준입니다. 카드의 […] 버튼으로 고를 수 있습니다. |
| 풀 폴더 <small>`DestinationFolder`</small> | 입력 | `string` | 풀 폴더. 없으면 만듭니다. **비우면 압축 파일 옆에 압축 파일 이름으로 된 폴더**에 풉니다(`받은 자료.zip` → `받은 자료\`). 어디에 풀렸는지는 **푼 폴더** 출력으로 받습니다. |
| 덮어쓰기 <small>`Overwrite`</small> | 설정 | `bool` | 풀 자리에 같은 이름의 파일이 있으면 바꿔 쓸지 여부(기본 true). 끄면 하나라도 있을 때 아무것도 풀지 않고 오류로 멈춥니다. |
| 이름 인코딩 <small>`NameEncoding`</small> | 입력 | `string` | 풀린 파일 이름이 깨질 때만 씁니다. UTF-8 표시가 없는 이름을 읽을 인코딩 이름이나 코드 페이지 번호(예: `euc-kr`, `shift_jis`, `949`). 비우면 자동입니다 — 아래 [한글 파일 이름](#zip-names) 참고. |
| 암호 <small>`Password`</small> | 입력 | `string` | 압축 파일 암호(평문). 직접 적으면 워크플로 파일에 그대로 저장되어 경고가 표시됩니다 — **보호된 비밀번호**를 쓰세요. 암호가 걸린 압축 파일인데 비우면 오류로 멈춥니다. |
| 보호된 비밀번호 <small>`SecurePassword`</small> | 입력 | `SecureString` | 보호된 비밀번호(SecureString). 자격 증명 가져오기(GetCredential)의 SecurePassword 출력을 연결합니다. 있으면 평문 비밀번호보다 우선합니다. |
| 결과 <small>`Result`</small> | 출력 | `string[]` | 푼 파일의 전체 경로 목록(출력, 문자열 배열 — 압축 파일 안의 순서). `반복(ForEach)` 에 연결해 파일을 하나씩 처리할 수 있습니다. |
| 개수 <small>`Count`</small> | 출력 | `int` | 푼 파일 수(출력). |
| 푼 폴더 <small>`OutputFolder`</small> | 출력 | `string` | 실제로 푼 폴더의 전체 경로(출력). 풀 폴더를 비웠을 때 어디에 풀렸는지 알 수 있습니다. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

#### 풀기 전에 하는 검사 { #zip-checks }

압축 파일은 밖에서 받는 경우가 많아, 쓰기 전에 모든 항목을 먼저 봅니다. 하나라도 걸리면 **풀 폴더에 아무것도 만들지 않습니다.**

| 상황 | 결과 |
|---|---|
| 이름에 `..\` 이 들어 풀 폴더 **밖**에 풀리는 항목 | 오류 — 풀지 않음 |
| Windows 에서 파일 이름으로 쓸 수 없는 글자(`?` `*` `:` `<` `>` 등)가 든 항목 | 오류 — 풀지 않음 |
| 대소문자만 다른 두 항목(`Readme.txt`·`README.TXT`) | 오류 — 풀지 않음 |
| 암호가 걸렸는데 암호가 없거나 틀림 | 오류 — 풀지 않음 |
| 덮어쓰기를 껐는데 같은 이름의 파일이 이미 있음 | 오류 — 풀지 않음 |
| 디스크 공간이 모자람 | 오류 — 풀지 않음 |
| 내용이 손상된 항목 | 오류 — 그 앞까지 푼 파일은 남고, 손상된 파일은 만들지 않음 |

`C:\…` 처럼 드라이브로 시작하는 이름은 드라이브를 떼고 풀 폴더 안에 풉니다. 파일의 수정 시각은 압축 파일에 적힌 대로 맞춥니다.

#### 한글 파일 이름 { #zip-names }

zip 은 파일 이름마다 "UTF-8 이다"라는 표시를 둘 수 있습니다. NeoRPA 가 만든 압축 파일은 늘 이 표시가 있어 어디서든 이름이 그대로 보입니다. 다른 곳에서 받은 압축 파일은 이렇게 읽습니다.

| 압축 파일 | 읽는 방법 |
|---|---|
| UTF-8 표시가 있음(요즘 프로그램 대부분) | UTF-8 |
| 표시가 없고 이름이 모두 UTF-8 로 읽힘(macOS 에서 만든 것) | UTF-8 |
| 표시가 없고 UTF-8 이 아님(예전 Windows 도구) | Windows 시스템 코드 페이지 — 한국어 Windows 는 CP949 |
| 위로도 깨질 때(일본어 Windows 에서 만든 것 등) | **이름 인코딩**에 `shift_jis` 처럼 직접 지정 |

macOS 에서 만든 압축 파일은 한글을 자소로 풀어 적습니다(탐색기에 `ㅎㅏㄴㄱㅡㄹ` 처럼 보이는 이름). 풀 때 합친 글자로 바꿉니다.

```
' 받은 압축 파일을 풀어 엑셀 파일만 처리하기
압축 풀기      압축 파일: "in\받은 자료.zip"   결과: files
반복(ForEach)  files 의 각 file
    조건(If)   file.EndsWith(".xlsx")
        ...
```

## 다운로드 대기  <small>`WaitForDownload`</small>

안에 놓은 작업(다운로드 버튼 클릭 등)이 시작한 다운로드가 **끝날 때까지 기다려**, 받은 파일의 경로를 돌려줍니다. 클릭한 뒤 "몇 초 기다리기"를 넣고 가장 최근 파일을 찾는 대신 씁니다 — 작업을 실행하기 전에 폴더를 봐 두었다가 그 뒤에 새로 생긴 파일을 찾으므로, 큰 파일이어도 다 받은 뒤에 넘어가고 예전부터 있던 파일과 헷갈리지 않습니다. 브라우저가 아닌 프로그램의 내보내기에도 씁니다. UiPath Wait for Download 에 해당합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 지켜볼 폴더 <small>`MonitoredFolder`</small> | 입력 | `string` | 파일이 받아지는 폴더. **비우면 Windows 의 다운로드 폴더**(브라우저의 기본 저장 위치)입니다. 상대 경로는 프로젝트 폴더 기준이고, 폴더는 미리 있어야 합니다. 하위 폴더는 보지 않습니다. 카드의 📁 버튼으로 고를 수 있습니다. |
| 파일 이름 패턴 <small>`FileNamePattern`</small> | 입력 | `string` | 받을 파일 이름의 패턴(예: `*.xlsx`, `주문_*.csv`). 여러 개는 `;` 로 나눕니다(`*.xlsx; *.csv`). 비우면 모든 파일. 다운로드 폴더에 다른 파일이 함께 생길 수 있을 때 적으세요. |
| 시간 제한(초) <small>`TimeoutSeconds`</small> | 입력 | `int` | 안의 작업이 끝난 뒤 다운로드가 끝나기를 기다리는 최대 시간(초). 0 이거나 비우면 300(5분). 넘기면 오류로 멈춥니다. |
| 옮길 곳 <small>`MoveTo`</small> | 입력 | `string` | 받은 파일을 옮길 곳. **파일 경로**(`out\11월 보고서.xlsx`)를 적으면 그 이름으로 바꿔 옮기고, **있는 폴더이거나 `\` 로 끝나면**(`받은 것\`) 그 폴더 안으로 이름 그대로 옮깁니다(없는 폴더는 만듭니다). 비우면 옮기지 않습니다 — [받은 파일 옮기기](#download-move). |
| 덮어쓰기 <small>`Overwrite`</small> | 설정 | `bool` | 옮길 곳에 같은 이름의 파일이 있으면 바꿔 쓸지 여부(기본 true). 끄면 오류로 멈추고 받은 파일은 받은 폴더에 그대로 둡니다. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 시간 안에 받지 못해도 멈추지 않고 다음으로 넘어갈지 여부(true/false). 넘어가면 결과는 비어 있고 개수는 0 입니다. |
| 결과 <small>`Result`</small> | 출력 | `string` | 받은 파일의 전체 경로(출력). 옮겼으면 옮긴 뒤의 경로입니다. 카드의 **받은 파일** 칸에 변수를 적습니다. 여러 개를 받았으면 먼저 보인 파일입니다. |
| 파일 목록 <small>`Files`</small> | 출력 | `string[]` | 받은 파일 전부의 전체 경로(출력, 문자열 배열 — 처음 보인 순서). `반복(ForEach)` 에 연결해 하나씩 처리할 수 있습니다. |
| 개수 <small>`Count`</small> | 출력 | `int` | 받은 파일 수(출력). |

!!! note "제공 버전"
    다운로드 대기는 NeoRPA 2.2.4 다음 버전부터 제공됩니다. 툴박스 **Control** 에 보이지 않으면 도움말 탭 → **버전 관리** 에서 새 버전을 확인하세요.

#### 쓰는 법 { #download-how }

1. **다운로드 대기**를 놓고, 카드의 **다운로드를 시작하는 작업** 칸 안에 다운로드를 시작하는 액티비티(클릭 등)를 넣습니다.
2. **받은 파일** 칸에 경로를 담을 변수(String)를 적습니다.
3. 다음 액티비티에서 그 변수를 씁니다 — Excel 열기, [CSV 읽기](datatable.md), 압축 풀기, 메일 첨부 등.

시작하는 작업을 **안에** 넣는 까닭: 작업을 실행하기 **전에** 폴더를 봐 둬야, 클릭하자마자 다 받아지는 작은 파일도 "새 파일"로 알아봅니다.

#### 다 받았다고 보는 기준 { #download-done }

| 폴더의 모습 | 판단 |
|---|---|
| 브라우저가 받는 동안 쓰는 임시 이름(`.crdownload` · `.part` · `.partial` · `.tmp`)이 새로 생겨 있음 | 받는 중 — 기다립니다 |
| 새 파일을 다른 프로그램이 쓰려고 열어 두고 있음 | 받는 중 — 기다립니다 |
| 새 파일이 잠깐(0.5초) 그대로이고 임시 파일이 없음 | 다 받음 |
| 예전부터 있던 파일 | 세지 않습니다(이름이 같아도 **내용이 바뀌었으면** 새 파일로 봅니다) |
| 예전에 받다 만 임시 파일 | 무시합니다 |

- 여러 파일을 한꺼번에 받기 시작하면 **모두 끝날 때까지** 기다리고 **파일 목록**에 전부 담습니다. 한 파일이 끝난 뒤에 다음 파일이 시작되는 사이트라면 파일마다 다운로드 대기를 하나씩 쓰세요.
- 시간 안에 끝나지 않으면 오류 문구가 까닭을 가려 줍니다 — *새 파일이 생기지 않았습니다*(다른 폴더에 저장됐거나, 저장 위치를 묻는 창이 떴거나, 다운로드가 시작되지 않음) 또는 *다운로드가 끝나지 않았습니다*(받는 중 — 시간 제한을 늘리세요).

!!! tip "브라우저 설정"
    브라우저가 **저장할 위치를 묻는 창**을 띄우면 그 창을 닫을 때까지 파일이 생기지 않습니다. 자동화에 쓰는 브라우저는 설정 → 다운로드에서 "다운로드 전에 각 파일의 저장 위치 확인"을 **끄세요**. 저장 위치를 다운로드 폴더가 아닌 곳으로 바꿨다면 **지켜볼 폴더**에 그 폴더를 적습니다.

#### 받은 파일 옮기기 { #download-move }

브라우저는 같은 이름을 다시 받으면 `보고서 (1).xlsx`, `보고서 (2).xlsx` 로 이름을 바꿉니다. **옮길 곳**을 적어 두면 받은 파일을 늘 같은 자리·같은 이름으로 받을 수 있습니다.

| 옮길 곳 | 결과 |
|---|---|
| `out\11월 보고서.xlsx` | 그 이름으로 바꿔 옮김(받은 파일이 하나일 때) |
| `받은 것\` (끝에 `\`) | 그 폴더 안으로 이름 그대로 — 없는 폴더는 만듦 |
| 이미 있는 폴더 경로 | 그 폴더 안으로 이름 그대로 |

받은 파일이 여럿인데 옮길 곳이 파일 이름이면 오류로 멈춥니다. 덮어쓰기를 껐는데 같은 이름이 이미 있으면 **아무것도 옮기지 않고** 멈춥니다.

## 프로세스 시작  <small>`StartProcess`</small>

지정한 프로그램(실행 파일)을 인자와 함께 실행합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 파일 이름 <small>`FileName`</small> | 입력 | `string` | 대상 파일의 이름 또는 경로. |
| 인수 <small>`argument`</small> | 입력 | `string` | 실행할 프로그램/스크립트에 전달할 명령줄 인수. |
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
| 텍스트 <small>`text`</small> | 출력 | `string` | 클립보드로 주고받을 텍스트. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 클립보드로 설정  <small>`SetToClipBoard`</small>

지정한 텍스트를 클립보드에 복사합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 텍스트 <small>`text`</small> | 입력 | `string` | 클립보드로 주고받을 텍스트. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 폴더 생성  <small>`CreateDirectory`</small>

지정한 경로에 폴더를 생성합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 경로 <small>`path`</small> | 입력 | `string` | 대상 파일 또는 폴더의 경로. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 폴더 삭제  <small>`DeleteDirectory`</small>

지정한 폴더를 삭제합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 경로 <small>`path`</small> | 입력 | `string` | 대상 파일 또는 폴더의 경로. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 항목 삭제(파일/디렉토리)  <small>`DeleteFileOrDirectory`</small>

지정한 경로가 파일이면 파일을, 폴더면 하위 내용까지 포함해 삭제합니다. 경로가 존재하지 않으면 오류가 발생합니다. 파일과 폴더를 구분하지 않고 지울 때 `파일 삭제`·`디렉토리 삭제` 대신 사용합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 경로 <small>`path`</small> | 입력 | `string` | 삭제할 파일 또는 폴더 경로. 상대 경로는 프로젝트 루트 기준으로 해석됩니다. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 주석 처리  <small>`CommentOut`</small>

본문에 담긴 자식 액티비티를 실행하지 않고 건너뜁니다. 일부 단계를 임시로 비활성화(주석 처리)할 때 사용합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 메모 <small>`Note`</small> | 설정 | `string` | 액티비티에 남기는 메모(주석)로, 실행에는 영향을 주지 않는다. |
