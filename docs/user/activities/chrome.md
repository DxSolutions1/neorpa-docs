<!-- 이 파일은 scripts/gen_activity_stubs.py 로 자동 생성됩니다.
     직접 편집하지 말고 website/data/activities.yaml 을 고친 뒤 스크립트를 다시 실행하세요. -->


# Chrome (전용)

디버그 포트(CDP) 기반 전용 크롬 자동화. 브라우저를 NeoRPA가 직접 띄워 제어합니다.

> 이 카테고리에는 10개의 액티비티가 있습니다. 각 액티비티의 **속성** 표는 소스에서 자동 추출되며(상속 포함), 표시명·설명은 리소스/설명 데이터에서 해석됩니다.

## 크롬 열기  <small>`OpenChrome`</small>

지정한 URL을 크롬(또는 엣지) 브라우저로 엽니다. 브라우저 자동화의 시작점으로 사용합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
| 브라우저 타입 <small>`BrowserType`</small> | 입력 | `string` | 동작에 사용할 브라우저 종류(Chrome, Edge 등). |
| URL <small>`Url`</small> | 입력 | `string` | 열거나 이동할 웹 페이지 주소. |
| 작업 전 타임아웃 <small>`BeforeTimeout`</small> | 입력 | `int` | 동작을 시작하기 전에 대기할 시간(밀리초). |

## 브라우저 열기  <small>`OpenBrowser`</small>

URL을 브라우저로 열고, 그 브라우저를 대상으로 하는 자식 액티비티들을 본문(스코프)에 담는 컨테이너입니다. 본문 액티비티는 대상 창을 따로 지정하지 않아도 이 브라우저에 동작합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
| 브라우저 타입 <small>`BrowserType`</small> | 입력 | `string` | 동작에 사용할 브라우저 종류(Chrome, Edge 등). |
| URL <small>`Url`</small> | 입력 | `string` | 열거나 이동할 웹 페이지 주소. |
| 작업 전 타임아웃 <small>`BeforeTimeout`</small> | 입력 | `int` | 동작을 시작하기 전에 대기할 시간(밀리초). |
| 애플리케이션 창 <small>`ApplicationWindow`</small> | 출력 | `Process` | 연결하거나 새로 연 애플리케이션 창(프로세스)을 담는 변수. |

## 브라우저 연결 (스코프)  <small>`AttachBrowserScope`</small>

이미 열려 있는 브라우저 창에 연결하는 스코프입니다. 본문에 놓인 자식 액티비티가 그 브라우저를 대상으로 동작합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 브라우저 타입 <small>`BrowserType`</small> | 입력 | `string` | 동작에 사용할 브라우저 종류(Chrome, Edge 등). |
| 셀렉터 <small>`Selector`</small> | 입력 | `string` | 동작 대상 UI 요소를 식별하는 셀렉터. |
| 타임아웃 <small>`Timeout`</small> | 입력 | `int` | 대상을 찾기까지 대기할 최대 시간(밀리초). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
| 애플리케이션 창 <small>`ApplicationWindow`</small> | 출력 | `Process` | 연결하거나 새로 연 애플리케이션 창(프로세스)을 담는 변수. |
| 이미지 정보 <small>`PicInfo`</small> | 입력 | `string` | 대상 요소를 재탐색하고 화면에 하이라이트하기 위해 캡처해 둔 이미지 정보. |

## 연결 (크롬)  <small>`AttachChrome`</small>

이미 실행 중인 크롬 창(탭)에 연결해 이후 크롬 액티비티의 대상으로 삼습니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
| 브라우저 타입 <small>`BrowserType`</small> | 입력 | `string` | 동작에 사용할 브라우저 종류(Chrome, Edge 등). |
| 탭 제목 <small>`TabTitle`</small> | 입력 | `string` | 연결할 브라우저 탭의 제목. |

## 클릭 (크롬)  <small>`ClickChrome`</small>

크롬 페이지에서 셀렉터로 지정한 웹 요소를 클릭합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 사각 영역 <small>`RectArea`</small> | 입력 | `string` | 대상 요소의 화면상 사각 영역(경계 좌표). |
| 위치 <small>`ClickPosition`</small> | 입력 | `string` | 요소 영역 안에서 클릭 기준으로 삼을 지점(가운데, 좌상단 등). |
| 오프셋 X <small>`OffsetX`</small> | 입력 | `int` | 클릭 기준점에서 가로로 이동할 오프셋(픽셀). |
| 오프셋 Y <small>`OffsetY`</small> | 입력 | `int` | 클릭 기준점에서 세로로 이동할 오프셋(픽셀). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
| 마우스 버튼 종류 <small>`MouseButton`</small> | 입력 | `string` | 클릭에 사용할 마우스 버튼(왼쪽/오른쪽/가운데). |
| 클릭 동작 <small>`ClickAction`</small> | 입력 | `string` | 클릭 동작의 종류(단일 클릭, 더블 클릭 등). |
| 시뮬레이터 사용 <small>`UseSimulator`</small> | 입력 | `bool` | 시뮬레이터(백그라운드 입력) 방식으로 동작할지 여부. |
| 작업 전 타임아웃 <small>`BeforeTimeout`</small> | 입력 | `int` | 동작을 시작하기 전에 대기할 시간(밀리초). |
| 작업 후 타임아웃 <small>`AfterTimeout`</small> | 입력 | `int` | 동작을 마친 뒤 추가로 대기할 시간(밀리초). |
| 브라우저 타입 <small>`BrowserType`</small> | 입력 | `string` | 동작에 사용할 브라우저 종류(Chrome, Edge 등). |
| 셀렉터 <small>`Selector`</small> | 입력 | `string` | 동작 대상 UI 요소를 식별하는 셀렉터. |
| 로딩 상태 <small>`ReadyState`</small> | 입력 | `string` | 동작을 실행하기 전에 기다릴 페이지 로딩 상태(예: INTERACTIVE, COMPLETE). |
| 요소 찾기 대기 시간 <small>`WaitTimeout`</small> | 입력 | `int` | 대상 요소를 찾기까지 대기할 최대 시간(밀리초). |
| 이미지 정보 <small>`PicInfo`</small> | 입력 | `string` | 대상 요소를 재탐색하고 화면에 하이라이트하기 위해 캡처해 둔 이미지 정보. |
| XPath <small>`Xpath`</small> | 입력 | `string` | 대상 요소를 찾는 데 사용하는 XPath 식. |

## 마우스 오버 (크롬)  <small>`HoverChrome`</small>

크롬 페이지에서 셀렉터로 지정한 웹 요소 위로 마우스를 올립니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 사각 영역 <small>`RectArea`</small> | 입력 | `string` | 대상 요소의 화면상 사각 영역(경계 좌표). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
| 작업 전 타임아웃 <small>`BeforeTimeout`</small> | 입력 | `int` | 동작을 시작하기 전에 대기할 시간(밀리초). |
| 작업 후 타임아웃 <small>`AfterTimeout`</small> | 입력 | `int` | 동작을 마친 뒤 추가로 대기할 시간(밀리초). |
| 브라우저 타입 <small>`BrowserType`</small> | 입력 | `string` | 동작에 사용할 브라우저 종류(Chrome, Edge 등). |
| 셀렉터 <small>`Selector`</small> | 입력 | `string` | 동작 대상 UI 요소를 식별하는 셀렉터. |
| 로딩 상태 <small>`ReadyState`</small> | 입력 | `string` | 동작을 실행하기 전에 기다릴 페이지 로딩 상태(예: INTERACTIVE, COMPLETE). |
| 요소 찾기 대기 시간 <small>`WaitTimeout`</small> | 입력 | `int` | 대상 요소를 찾기까지 대기할 최대 시간(밀리초). |
| 이미지 정보 <small>`PicInfo`</small> | 입력 | `string` | 대상 요소를 재탐색하고 화면에 하이라이트하기 위해 캡처해 둔 이미지 정보. |
| XPath <small>`Xpath`</small> | 입력 | `string` | 대상 요소를 찾는 데 사용하는 XPath 식. |

## 텍스트 입력 (크롬)  <small>`TypeIntoChrome`</small>

크롬 페이지의 입력 요소에 텍스트를 입력합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 사각 영역 <small>`RectArea`</small> | 입력 | `string` | 대상 요소의 화면상 사각 영역(경계 좌표). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
| 필드 비우기 <small>`EmptyField`</small> | 입력 | `bool` | 입력하기 전에 대상 필드를 비울지 여부. |
| 타이핑 전 클릭 <small>`ClickBeforeTyping`</small> | 입력 | `bool` | 텍스트를 입력하기 전에 대상 요소를 먼저 클릭할지 여부. |
| 값 <small>`Value`</small> | 입력 | `string` | 대상 요소에 입력할 텍스트. |
| 작업 전 타임아웃 <small>`BeforeTimeout`</small> | 입력 | `int` | 동작을 시작하기 전에 대기할 시간(밀리초). |
| 작업 후 타임아웃 <small>`AfterTimeout`</small> | 입력 | `int` | 동작을 마친 뒤 추가로 대기할 시간(밀리초). |
| 브라우저 타입 <small>`BrowserType`</small> | 입력 | `string` | 동작에 사용할 브라우저 종류(Chrome, Edge 등). |
| 셀렉터 <small>`Selector`</small> | 입력 | `string` | 동작 대상 UI 요소를 식별하는 셀렉터. |
| 로딩 상태 <small>`ReadyState`</small> | 입력 | `string` | 동작을 실행하기 전에 기다릴 페이지 로딩 상태(예: INTERACTIVE, COMPLETE). |
| 요소 찾기 대기 시간 <small>`WaitTimeout`</small> | 입력 | `int` | 대상 요소를 찾기까지 대기할 최대 시간(밀리초). |
| 이미지 정보 <small>`PicInfo`</small> | 입력 | `string` | 대상 요소를 재탐색하고 화면에 하이라이트하기 위해 캡처해 둔 이미지 정보. |
| XPath <small>`Xpath`</small> | 입력 | `string` | 대상 요소를 찾는 데 사용하는 XPath 식. |

## 텍스트 가져오기 (크롬)  <small>`GetTextChrome`</small>

크롬 페이지에서 셀렉터로 지정한 웹 요소의 텍스트를 읽어 반환합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
| 결과 <small>`Result`</small> | 출력 | `string` | 액티비티 실행 결과(출력). |
| 작업 전 타임아웃 <small>`BeforeTimeout`</small> | 입력 | `int` | 동작을 시작하기 전에 대기할 시간(밀리초). |
| 작업 후 타임아웃 <small>`AfterTimeout`</small> | 입력 | `int` | 동작을 마친 뒤 추가로 대기할 시간(밀리초). |
| 브라우저 타입 <small>`BrowserType`</small> | 입력 | `string` | 동작에 사용할 브라우저 종류(Chrome, Edge 등). |
| 셀렉터 <small>`Selector`</small> | 입력 | `string` | 동작 대상 UI 요소를 식별하는 셀렉터. |
| 로딩 상태 <small>`ReadyState`</small> | 입력 | `string` | 동작을 실행하기 전에 기다릴 페이지 로딩 상태(예: INTERACTIVE, COMPLETE). |
| 요소 찾기 대기 시간 <small>`WaitTimeout`</small> | 입력 | `int` | 대상 요소를 찾기까지 대기할 최대 시간(밀리초). |
| 이미지 정보 <small>`PicInfo`</small> | 입력 | `string` | 대상 요소를 재탐색하고 화면에 하이라이트하기 위해 캡처해 둔 이미지 정보. |
| XPath <small>`Xpath`</small> | 입력 | `string` | 대상 요소를 찾는 데 사용하는 XPath 식. |

## 속성 가져오기 (크롬)  <small>`GetAttributeChrome`</small>

크롬 페이지 웹 요소의 지정한 속성(attribute) 값을 읽어 반환합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
| 속성 이름 <small>`AttrName`</small> | 입력 | `string` | 읽어올 요소 속성(attribute)의 이름. |
| 결과 <small>`Result`</small> | 출력 | `string` | 액티비티 실행 결과(출력). |
| 작업 전 타임아웃 <small>`BeforeTimeout`</small> | 입력 | `int` | 동작을 시작하기 전에 대기할 시간(밀리초). |
| 작업 후 타임아웃 <small>`AfterTimeout`</small> | 입력 | `int` | 동작을 마친 뒤 추가로 대기할 시간(밀리초). |
| 브라우저 타입 <small>`BrowserType`</small> | 입력 | `string` | 동작에 사용할 브라우저 종류(Chrome, Edge 등). |
| 셀렉터 <small>`Selector`</small> | 입력 | `string` | 동작 대상 UI 요소를 식별하는 셀렉터. |
| 로딩 상태 <small>`ReadyState`</small> | 입력 | `string` | 동작을 실행하기 전에 기다릴 페이지 로딩 상태(예: INTERACTIVE, COMPLETE). |
| 요소 찾기 대기 시간 <small>`WaitTimeout`</small> | 입력 | `int` | 대상 요소를 찾기까지 대기할 최대 시간(밀리초). |
| 이미지 정보 <small>`PicInfo`</small> | 입력 | `string` | 대상 요소를 재탐색하고 화면에 하이라이트하기 위해 캡처해 둔 이미지 정보. |
| XPath <small>`Xpath`</small> | 입력 | `string` | 대상 요소를 찾는 데 사용하는 XPath 식. |

## 요소 존재 확인 (크롬)  <small>`ElementExistsChrome`</small>

크롬 페이지에 셀렉터로 지정한 웹 요소가 존재하는지 확인해 참/거짓을 반환합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
| 결과 <small>`Result`</small> | 출력 | `bool` | 액티비티 실행 결과(출력). |
| 작업 전 타임아웃 <small>`BeforeTimeout`</small> | 입력 | `int` | 동작을 시작하기 전에 대기할 시간(밀리초). |
| 작업 후 타임아웃 <small>`AfterTimeout`</small> | 입력 | `int` | 동작을 마친 뒤 추가로 대기할 시간(밀리초). |
| 브라우저 타입 <small>`BrowserType`</small> | 입력 | `string` | 동작에 사용할 브라우저 종류(Chrome, Edge 등). |
| 셀렉터 <small>`Selector`</small> | 입력 | `string` | 동작 대상 UI 요소를 식별하는 셀렉터. |
| 로딩 상태 <small>`ReadyState`</small> | 입력 | `string` | 동작을 실행하기 전에 기다릴 페이지 로딩 상태(예: INTERACTIVE, COMPLETE). |
| 요소 찾기 대기 시간 <small>`WaitTimeout`</small> | 입력 | `int` | 대상 요소를 찾기까지 대기할 최대 시간(밀리초). |
| 이미지 정보 <small>`PicInfo`</small> | 입력 | `string` | 대상 요소를 재탐색하고 화면에 하이라이트하기 위해 캡처해 둔 이미지 정보. |
| XPath <small>`Xpath`</small> | 입력 | `string` | 대상 요소를 찾는 데 사용하는 XPath 식. |

