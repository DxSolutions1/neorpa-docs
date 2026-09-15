<!-- 이 파일은 scripts/gen_activities.py 로 자동 생성됩니다.
     직접 편집하지 말고 data/activities.yaml 을 고친 뒤 `python scripts/gen_activities.py --write` 를 다시 실행하세요. -->


# Chrome (일반)

사용자 프로필 크롬을 확장 프로그램 + 네이티브 메시징으로 자동화합니다(디버그 포트 미사용).

> 이 카테고리에는 8개의 액티비티가 있습니다. 각 액티비티의 **속성** 표는 소스에서 자동 추출되며(상속 포함), 표시명·설명은 리소스/설명 데이터에서 해석됩니다.

## 연결 (일반 크롬)  <small>`AttachBrowserNative`</small>

사용자가 평소 쓰는 일반 크롬(확장 프로그램 채널)에 연결해 이후 일반 크롬 액티비티의 대상으로 삼습니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
| 브라우저 타입 <small>`BrowserType`</small> | 입력 | `string` | 동작에 사용할 브라우저 종류(Chrome, Edge 등). |
| 탭 제목 <small>`TabTitle`</small> | 입력 | `string` | 연결할 브라우저 탭의 제목. |

## 클릭 (일반 크롬)  <small>`ClickBrowserNative`</small>

일반 크롬 페이지에서 셀렉터로 지정한 웹 요소를 클릭합니다.

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
| 작업 전 타임아웃 <small>`BeforeTimeout`</small> | 입력 | `int` | 동작을 시작하기 전에 대기할 시간(밀리초). |
| 작업 후 타임아웃 <small>`AfterTimeout`</small> | 입력 | `int` | 동작을 마친 뒤 추가로 대기할 시간(밀리초). |
| 브라우저 타입 <small>`BrowserType`</small> | 입력 | `string` | 동작에 사용할 브라우저 종류(Chrome, Edge 등). |
| 셀렉터 <small>`Selector`</small> | 입력 | `string` | 동작 대상 UI 요소를 식별하는 셀렉터. |
| 로딩 상태 <small>`ReadyState`</small> | 입력 | `string` | 동작을 실행하기 전에 기다릴 페이지 로딩 상태(예: INTERACTIVE, COMPLETE). |
| 요소 찾기 대기 시간 <small>`WaitTimeout`</small> | 입력 | `int` | 대상 요소를 찾기까지 대기할 최대 시간(밀리초). |

## 마우스 오버 (일반 크롬)  <small>`HoverBrowserNative`</small>

일반 크롬 페이지에서 셀렉터로 지정한 웹 요소 위로 마우스를 올립니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 사각 영역 <small>`RectArea`</small> | 입력 | `string` | 대상 요소의 화면상 사각 영역(경계 좌표). |
| 위치 <small>`ClickPosition`</small> | 입력 | `string` | 요소 영역 안에서 클릭 기준으로 삼을 지점(가운데, 좌상단 등). |
| 오프셋 X <small>`OffsetX`</small> | 입력 | `int` | 클릭 기준점에서 가로로 이동할 오프셋(픽셀). |
| 오프셋 Y <small>`OffsetY`</small> | 입력 | `int` | 클릭 기준점에서 세로로 이동할 오프셋(픽셀). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
| 작업 전 타임아웃 <small>`BeforeTimeout`</small> | 입력 | `int` | 동작을 시작하기 전에 대기할 시간(밀리초). |
| 작업 후 타임아웃 <small>`AfterTimeout`</small> | 입력 | `int` | 동작을 마친 뒤 추가로 대기할 시간(밀리초). |
| 브라우저 타입 <small>`BrowserType`</small> | 입력 | `string` | 동작에 사용할 브라우저 종류(Chrome, Edge 등). |
| 셀렉터 <small>`Selector`</small> | 입력 | `string` | 동작 대상 UI 요소를 식별하는 셀렉터. |
| 로딩 상태 <small>`ReadyState`</small> | 입력 | `string` | 동작을 실행하기 전에 기다릴 페이지 로딩 상태(예: INTERACTIVE, COMPLETE). |
| 요소 찾기 대기 시간 <small>`WaitTimeout`</small> | 입력 | `int` | 대상 요소를 찾기까지 대기할 최대 시간(밀리초). |

## 텍스트 입력 (일반 크롬)  <small>`TypeIntoBrowserNative`</small>

일반 크롬 페이지의 입력 요소에 텍스트를 입력합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 사각 영역 <small>`RectArea`</small> | 입력 | `string` | 대상 요소의 화면상 사각 영역(경계 좌표). |
| 값 <small>`Value`</small> | 입력 | `string` | 대상 요소에 입력할 텍스트. |
| 필드 비우기 <small>`EmptyField`</small> | 입력 | `bool` | 입력하기 전에 대상 필드를 비울지 여부. |
| 타이핑 전 클릭 <small>`ClickBeforeTyping`</small> | 입력 | `bool` | 텍스트를 입력하기 전에 대상 요소를 먼저 클릭할지 여부. |
| 위치 <small>`ClickPosition`</small> | 입력 | `string` | 요소 영역 안에서 클릭 기준으로 삼을 지점(가운데, 좌상단 등). |
| 오프셋 X <small>`OffsetX`</small> | 입력 | `int` | 클릭 기준점에서 가로로 이동할 오프셋(픽셀). |
| 오프셋 Y <small>`OffsetY`</small> | 입력 | `int` | 클릭 기준점에서 세로로 이동할 오프셋(픽셀). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
| 작업 전 타임아웃 <small>`BeforeTimeout`</small> | 입력 | `int` | 동작을 시작하기 전에 대기할 시간(밀리초). |
| 작업 후 타임아웃 <small>`AfterTimeout`</small> | 입력 | `int` | 동작을 마친 뒤 추가로 대기할 시간(밀리초). |
| 브라우저 타입 <small>`BrowserType`</small> | 입력 | `string` | 동작에 사용할 브라우저 종류(Chrome, Edge 등). |
| 셀렉터 <small>`Selector`</small> | 입력 | `string` | 동작 대상 UI 요소를 식별하는 셀렉터. |
| 로딩 상태 <small>`ReadyState`</small> | 입력 | `string` | 동작을 실행하기 전에 기다릴 페이지 로딩 상태(예: INTERACTIVE, COMPLETE). |
| 요소 찾기 대기 시간 <small>`WaitTimeout`</small> | 입력 | `int` | 대상 요소를 찾기까지 대기할 최대 시간(밀리초). |

## 텍스트 가져오기 (일반 크롬)  <small>`GetTextBrowserNative`</small>

일반 크롬 페이지에서 셀렉터로 지정한 웹 요소의 텍스트를 읽어 반환합니다.

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

## 속성 가져오기 (일반 크롬)  <small>`GetAttributeBrowserNative`</small>

일반 크롬 페이지 웹 요소의 지정한 속성(attribute) 값을 읽어 반환합니다.

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

## 요소 존재 확인 (일반 크롬)  <small>`ElementExistsBrowserNative`</small>

일반 크롬 페이지에 셀렉터로 지정한 웹 요소가 존재하는지 확인해 참/거짓을 반환합니다.

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

## 데이터 추출 (일반 크롬)  <small>`ExtractDataBrowserNative`</small>

일반 크롬 페이지의 표/목록에서 여러 행 데이터를 DataTable로 추출합니다. 다음 링크를 지정하면 페이지를 넘겨 가며 여러 페이지를 누적 추출합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
| 최대 개수 <small>`MaxCount`</small> | 입력 | `int` | 추출할 최대 항목(행) 수. |
| 다음 링크 <small>`NextLink`</small> | 입력 | `string` | 다음 페이지로 이동하는 링크/버튼을 식별하는 셀렉터. |
| 다음 링크 클릭 전 타임아웃 <small>`NextLinkTimeout`</small> | 입력 | `int` | 다음 링크를 클릭하기 전에 대기할 시간(밀리초). |
| 메타데이터 <small>`MetaData`</small> | 입력 | `string` | 추출할 데이터의 구조(열 구성 등)를 정의하는 메타데이터. |
| 데이터 테이블 (출력) <small>`OutDataTable`</small> | 출력 | `DataTable` | 추출 결과를 담는 DataTable(출력). |
| 작업 전 타임아웃 <small>`BeforeTimeout`</small> | 입력 | `int` | 동작을 시작하기 전에 대기할 시간(밀리초). |
| 작업 후 타임아웃 <small>`AfterTimeout`</small> | 입력 | `int` | 동작을 마친 뒤 추가로 대기할 시간(밀리초). |
| 브라우저 타입 <small>`BrowserType`</small> | 입력 | `string` | 동작에 사용할 브라우저 종류(Chrome, Edge 등). |
| 셀렉터 <small>`Selector`</small> | 입력 | `string` | 동작 대상 UI 요소를 식별하는 셀렉터. |
| 로딩 상태 <small>`ReadyState`</small> | 입력 | `string` | 동작을 실행하기 전에 기다릴 페이지 로딩 상태(예: INTERACTIVE, COMPLETE). |
| 요소 찾기 대기 시간 <small>`WaitTimeout`</small> | 입력 | `int` | 대상 요소를 찾기까지 대기할 최대 시간(밀리초). |
