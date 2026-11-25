<!-- 이 파일은 scripts/gen_activities.py 로 자동 생성됩니다.
     직접 편집하지 말고 data/activities.yaml 을 고친 뒤 `python scripts/gen_activities.py --write` 를 다시 실행하세요. -->


# DB

데이터베이스(Oracle · SQL Server · MariaDB · MySQL)에 연결해 쿼리를 실행합니다. **쿼리에 넣을 값은 `매개 변수`로 넘기세요** — 쿼리에는 자리만 적고(SQL Server · MySQL · MariaDB 는 `@이름`, Oracle 은 `:이름`) 값은 이름과 함께 따로 줍니다. 예: 쿼리 `"SELECT * FROM 고객 WHERE 이름 = @name"`, 매개 변수 `New Dictionary(Of String, Object) From {{"name", 이름}}`. 값을 쿼리 글에 이어 붙이면(`"… WHERE 이름 = '" & 이름 & "'"`) 값에 따옴표가 있을 때 쿼리가 깨지고, 값이 쿼리의 일부로 실행될 수 있어(SQL 삽입) 경고가 표시됩니다. **DB 계정의 암호는 연결 문자열에 적지 말고** `보호된 비밀번호` 칸의 열쇠 버튼으로 자격 증명을 고르세요(자격 증명은 리본 `설정 › 자격 증명`에서 등록). 연결 문자열에 암호가 들어 있으면 속성 창에서는 `****` 로 가려 보이고 경고가 표시됩니다.

> 이 카테고리에는 2개의 액티비티가 있습니다. 각 액티비티의 **속성** 표는 소스에서 자동 추출되며(상속 포함), 표시명·설명은 리소스/설명 데이터에서 해석됩니다.

## DB 연결 (데이터 테이블)  <small>`DBConnectToDT`</small>

데이터베이스에 연결해 조회 쿼리를 실행하고 결과를 DataTable로 가져옵니다. 결과 표를 돌려주지 않는 쿼리(INSERT 등)는 `DB 쿼리 실행`을 쓰세요.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 연결 문자열 <small>`conn`</small> | 입력 | `string` | 데이터베이스 연결 문자열. 서버 · DB · 계정만 적고 암호는 `보호된 비밀번호`로 따로 주는 것을 권합니다(예: `Server=db01;Database=erp;User Id=rpa`). 암호까지 적으면 워크플로 파일에 그대로 저장되어 경고가 표시됩니다. |
| 보호된 연결 문자열 <small>`SecureConn`</small> | 입력 | `SecureString` | 보호된 연결 문자열(SecureString). 연결 문자열 전체를 자격 증명의 비밀번호 칸에 저장해 두고 열쇠 버튼으로 그 자격 증명을 고릅니다. 있으면 평문 연결 문자열(conn)보다 우선합니다. 암호만 따로 두려면 연결 문자열에는 암호를 빼고 `보호된 비밀번호`를 쓰세요. |
| 보호된 비밀번호 <small>`SecurePassword`</small> | 입력 | `SecureString` | DB 계정의 암호(SecureString). 속성 창의 열쇠 버튼으로 자격 증명을 고르면 실행할 때 연결 문자열의 암호 자리에 넣습니다. 연결 문자열에 암호가 있어도 이쪽이 우선합니다. |
| DB 종류 <small>`DBType`</small> | 설정 | `DBType` | 연결할 데이터베이스의 종류. |
| 쿼리 <small>`query`</small> | 입력 | `string` | 실행할 SQL 쿼리. 값이 들어갈 자리는 `@이름`(Oracle 은 `:이름`)으로 적고 값은 `매개 변수`로 넘깁니다. |
| 매개 변수 <small>`Parameters`</small> | 입력 | `IDictionary` | 쿼리의 매개 변수(이름 → 값 사전). 예: `New Dictionary(Of String, Object) From {{"id", 고객번호}, {"name", 이름}}`. 이름은 글자 · 숫자 · 밑줄만 쓰고 앞의 `@` · `:` 는 붙여도 되고 빼도 됩니다. 값이 `Nothing` 이면 NULL 로 넘어갑니다. |
| 데이터 테이블 <small>`DataTable`</small> | 출력 | `DataTable` | 작업 대상이 되는 DataTable. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## DB 쿼리 실행  <small>`DBQueryExecute`</small>

데이터베이스에 연결해 INSERT/UPDATE/DELETE 등 결과 표가 없는 쿼리를 실행합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 연결 문자열 <small>`conn`</small> | 입력 | `string` | 데이터베이스 연결 문자열. 서버 · DB · 계정만 적고 암호는 `보호된 비밀번호`로 따로 주는 것을 권합니다(예: `Server=db01;Database=erp;User Id=rpa`). 암호까지 적으면 워크플로 파일에 그대로 저장되어 경고가 표시됩니다. |
| 보호된 연결 문자열 <small>`SecureConn`</small> | 입력 | `SecureString` | 보호된 연결 문자열(SecureString). 연결 문자열 전체를 자격 증명의 비밀번호 칸에 저장해 두고 열쇠 버튼으로 그 자격 증명을 고릅니다. 있으면 평문 연결 문자열(conn)보다 우선합니다. 암호만 따로 두려면 연결 문자열에는 암호를 빼고 `보호된 비밀번호`를 쓰세요. |
| 보호된 비밀번호 <small>`SecurePassword`</small> | 입력 | `SecureString` | DB 계정의 암호(SecureString). 속성 창의 열쇠 버튼으로 자격 증명을 고르면 실행할 때 연결 문자열의 암호 자리에 넣습니다. 연결 문자열에 암호가 있어도 이쪽이 우선합니다. |
| DB 종류 <small>`DBType`</small> | 설정 | `DBType` | 연결할 데이터베이스의 종류. |
| 쿼리 <small>`query`</small> | 입력 | `string` | 실행할 SQL 쿼리. 값이 들어갈 자리는 `@이름`(Oracle 은 `:이름`)으로 적고 값은 `매개 변수`로 넘깁니다. |
| 매개 변수 <small>`Parameters`</small> | 입력 | `IDictionary` | 쿼리의 매개 변수(이름 → 값 사전). 예: `New Dictionary(Of String, Object) From {{"id", 고객번호}, {"name", 이름}}`. 이름은 글자 · 숫자 · 밑줄만 쓰고 앞의 `@` · `:` 는 붙여도 되고 빼도 됩니다. 값이 `Nothing` 이면 NULL 로 넘어갑니다. |
| 영향받은 행 수 <small>`AffectedRows`</small> | 출력 | `int` | 쿼리가 바꾼 행 수(출력). 드라이버가 알려 주지 않는 쿼리는 -1. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
