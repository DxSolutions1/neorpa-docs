<!-- 이 파일은 scripts/gen_activities.py 로 자동 생성됩니다.
     직접 편집하지 말고 data/activities.yaml 을 고친 뒤 `python scripts/gen_activities.py --write` 를 다시 실행하세요. -->


# DB

데이터베이스에 연결해 질의를 실행합니다.

> 이 카테고리에는 2개의 액티비티가 있습니다. 각 액티비티의 **속성** 표는 소스에서 자동 추출되며(상속 포함), 표시명·설명은 리소스/설명 데이터에서 해석됩니다.

## DB 연결 (데이터 테이블)  <small>`DBConnectToDT`</small>

데이터베이스에 연결해 조회 쿼리를 실행하고 결과를 DataTable로 가져옵니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 연결 문자열 <small>`conn`</small> | 입력 | `string` | 데이터베이스 연결 문자열. |
| 보호된 연결 문자열 <small>`SecureConn`</small> | 입력 | `SecureString` | 보호된 연결 문자열(SecureString). 자격 증명 관리자에 연결 문자열 전체를 비밀번호로 저장해 두고 자격 증명 가져오기(GetCredential)로 읽어 연결합니다. 있으면 평문 연결 문자열(conn)보다 우선합니다. |
| DB 종류 <small>`DBType`</small> | 설정 | `DBType` | 연결할 데이터베이스의 종류. |
| 쿼리 <small>`query`</small> | 입력 | `string` | 실행할 SQL 쿼리. |
| 데이터 테이블 <small>`DataTable`</small> | 출력 | `DataTable` | 작업 대상이 되는 DataTable. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## DB 쿼리 실행  <small>`DBQueryExecute`</small>

데이터베이스에 연결해 INSERT/UPDATE/DELETE 등 쿼리를 실행합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 연결 문자열 <small>`conn`</small> | 입력 | `string` | 데이터베이스 연결 문자열. |
| 보호된 연결 문자열 <small>`SecureConn`</small> | 입력 | `SecureString` | 보호된 연결 문자열(SecureString). 자격 증명 관리자에 연결 문자열 전체를 비밀번호로 저장해 두고 자격 증명 가져오기(GetCredential)로 읽어 연결합니다. 있으면 평문 연결 문자열(conn)보다 우선합니다. |
| DB 종류 <small>`DBType`</small> | 설정 | `DBType` | 연결할 데이터베이스의 종류. |
| 쿼리 <small>`query`</small> | 입력 | `string` | 실행할 SQL 쿼리. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
