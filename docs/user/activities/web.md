<!-- 이 파일은 scripts/gen_activities.py 로 자동 생성됩니다.
     직접 편집하지 말고 data/activities.yaml 을 고친 뒤 `python scripts/gen_activities.py --write` 를 다시 실행하세요. -->


# Web (HTTP 요청 · JSON)

HTTP(S) 요청을 보내고 응답을 받으며, JSON 문자열을 읽거나 만듭니다. UiPath 의 HTTP Request·Deserialize JSON 에 해당합니다. 인증 비밀은 `보안 › 자격 증명 가져오기(GetCredential)` 의 보호된 비밀번호를 연결하면 워크플로 파일에 남지 않습니다.

> 이 카테고리에는 5개의 액티비티가 있습니다. 각 액티비티의 **속성** 표는 소스에서 자동 추출되며(상속 포함), 표시명·설명은 리소스/설명 데이터에서 해석됩니다.

## HTTP 요청  <small>`HttpRequest`</small>

HTTP(S) 요청을 보내고 상태 코드·응답 본문·응답 헤더를 돌려줍니다. 헤더는 한 줄에 하나씩 `이름: 값` 으로 적고, 본문이 있는데 콘텐츠 형식을 비우면 `application/json` 으로 보냅니다. 상태 코드 400 이상은 기본적으로 오류가 아니라 상태 코드로 돌려주며(UiPath 와 같음), 오류로 받고 싶으면 `오류 상태면 실패` 를 켭니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `Url` | 입력 | `string` | 요청 주소(http:// 또는 https:// 로 시작하는 절대 주소). 쿼리 문자열은 주소에 직접 적습니다. |
| 메서드 <small>`Method`</small> | 설정 | `HttpRequestMethod` | HTTP 메서드(GET·POST·PUT·PATCH·DELETE·HEAD·OPTIONS). 카드의 콤보에서 고릅니다. |
| 헤더 <small>`Headers`</small> | 입력 | `string` | 요청 헤더. 한 줄에 하나씩 `이름: 값`(예: `Accept: application/json`). Content-Type 을 적으면 본문 형식으로 씁니다. |
| 본문 <small>`Body`</small> | 입력 | `string` | 요청 본문(JSON 등). GET·HEAD 에는 보낼 수 없습니다. |
| 콘텐츠 형식 <small>`ContentType`</small> | 입력 | `string` | 본문의 Content-Type. 비우면 application/json(헤더에 적은 Content-Type 이 있으면 그것). 문자 집합은 UTF-8. |
| 타임아웃(ms) <small>`TimeoutMS`</small> | 입력 | `int` | 응답을 기다릴 최대 시간(밀리초). 0 또는 비우면 30000. |
| 인증 방식 <small>`AuthType`</small> | 설정 | `HttpAuthType` | 인증 방식. None(없음) · Basic(사용자 이름+비밀번호) · Bearer(토큰) · ApiKey(헤더에 키). |
| 사용자 이름 <small>`Username`</small> | 입력 | `string` | Basic 인증의 사용자 이름. |
| 암호 <small>`Password`</small> | 입력 | `string` | Basic 비밀번호·Bearer 토큰·API 키(평문). 직접 적으면 워크플로 파일에 남아 설계 시점에 경고가 납니다. 보호된 비밀번호가 있으면 그쪽이 우선합니다. |
| 보호된 비밀번호 <small>`SecurePassword`</small> | 입력 | `SecureString` | 보호된 비밀(SecureString). `자격 증명 가져오기(GetCredential)` 의 SecurePassword 출력을 연결합니다. |
| API 키 헤더 이름 <small>`ApiKeyHeader`</small> | 입력 | `string` | ApiKey 인증에서 키를 실을 헤더 이름. 비우면 X-API-Key. |
| 파일로 저장 <small>`SaveToFile`</small> | 입력 | `string` | 비우지 않으면 응답 본문을 이 파일에 저장합니다(파일 다운로드). 이때 `결과` 에는 저장한 파일 경로가 들어갑니다. |
| 오류 상태면 실패 <small>`FailOnErrorStatus`</small> | 설정 | `bool` | true 면 상태 코드 400 이상을 오류로 던집니다. 기본 false. |
| 결과 <small>`Result`</small> | 출력 | `string` | 응답 본문 문자열(출력). 파일로 저장했으면 저장한 경로. |
| 상태 코드 <small>`StatusCode`</small> | 출력 | `int` | HTTP 상태 코드(출력, 예 200·404). |
| 응답 헤더 <small>`ResponseHeaders`</small> | 출력 | `Dictionary<string, string>` | 응답 헤더 사전(출력, Dictionary(Of String, String)). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## JSON 읽기  <small>`DeserializeJson`</small>

JSON 문자열을 JObject 로 풉니다. 결과는 식에서 `obj("name").ToString()`, `obj("items")(0)("id")` 처럼 읽습니다. 최상위가 배열이면 `JSON 배열 읽기` 를 쓰세요. UiPath Deserialize JSON 에 해당합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| JSON 문자열 <small>`JsonString`</small> | 입력 | `string` | 풀 JSON 문자열(보통 HTTP 요청의 결과 변수). |
| 결과 <small>`Result`</small> | 출력 | `JObject` | JObject(출력). 변수 타입은 Newtonsoft.Json.Linq.JObject. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## JSON 배열 읽기  <small>`DeserializeJsonArray`</small>

JSON 배열 문자열을 JArray 로 풀고, 같은 내용을 데이터 테이블로도 돌려줍니다(열 = 모든 개체의 키, 중첩 값은 JSON 문자열). UiPath Deserialize JSON Array 에 해당합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| JSON 문자열 <small>`JsonString`</small> | 입력 | `string` | 풀 JSON 배열 문자열. |
| 결과 <small>`Result`</small> | 출력 | `JArray` | JArray(출력). 변수 타입은 Newtonsoft.Json.Linq.JArray. |
| 데이터 테이블 <small>`DataTable`</small> | 출력 | `DataTable` | 배열을 표로 만든 데이터 테이블(출력). 개체가 아닌 원소는 Value 열에 들어갑니다. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## JSON 값 가져오기  <small>`GetJsonValue`</small>

JSON 문자열에서 경로(JSONPath)의 값 하나를 문자열로 꺼냅니다. 변수 타입을 JObject 로 두지 않고 값 하나만 필요할 때 씁니다. 값이 없으면 빈 문자열(`없으면 실패` 를 켜면 오류).

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| JSON 문자열 <small>`JsonString`</small> | 입력 | `string` | 값을 꺼낼 JSON 문자열. |
| JSON 경로 <small>`JsonPath`</small> | 입력 | `string` | 경로. 예: `data.items[0].name`, `$.total`, `[1]`. 앞의 `$.` 는 생략할 수 있습니다. |
| 없으면 실패 <small>`FailIfMissing`</small> | 설정 | `bool` | 경로에 값이 없을 때 오류로 처리할지 여부(기본 false = 빈 문자열). |
| 결과 <small>`Result`</small> | 출력 | `string` | 꺼낸 값(출력). 문자열은 따옴표 없이, 개체·배열은 한 줄 JSON 으로. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## JSON 만들기  <small>`SerializeJson`</small>

개체(데이터 테이블·Dictionary·List·JObject·일반 개체)를 JSON 문자열로 만듭니다. HTTP 요청 본문을 만들 때 씁니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 입력 <small>`Input`</small> | 입력 | `object` | JSON 으로 만들 개체. 예: `New Dictionary(Of String, Object) From {{"name", 이름}, {"count", 3}}`, 데이터 테이블 변수. |
| 들여쓰기 <small>`Indented`</small> | 설정 | `bool` | true 면 줄 바꿈·들여쓰기를 넣어 읽기 좋게 만듭니다(기본 false = 한 줄). |
| 결과 <small>`Result`</small> | 출력 | `string` | JSON 문자열(출력). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
