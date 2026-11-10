<!-- 이 파일은 scripts/gen_activities.py 로 자동 생성됩니다.
     직접 편집하지 말고 data/activities.yaml 을 고친 뒤 `python scripts/gen_activities.py --write` 를 다시 실행하세요. -->


# OutLook

설치된 Outlook을 통해 메일을 가져오고 보내고 삭제합니다.

> 이 카테고리에는 3개의 액티비티가 있습니다. 각 액티비티의 **속성** 표는 소스에서 자동 추출되며(상속 포함), 표시명·설명은 리소스/설명 데이터에서 해석됩니다.

## Outlook 메일 가져오기  <small>`OutlookGetMailMessage`</small>

설치된 Outlook에서 지정한 폴더의 메일을 가져옵니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 필터 <small>`Filter`</small> | 입력 | `string` | 메일을 걸러낼 필터 조건. |
| ID로 필터 <small>`FilterByIDs`</small> | 입력 | `List<string>` | 지정한 메일 ID 목록만 가져오도록 거르는 조건. |
| 읽음으로 표시 <small>`MarkAsRead`</small> | 설정 | `bool` | 가져온 메일을 읽음으로 표시할지 여부. |
| 읽지 않은 메일만 <small>`OnlyUnreadMessage`</small> | 설정 | `bool` | 읽지 않은 메일만 가져올지 여부. |
| 날짜 정렬 <small>`OrderByDate`</small> | 입력 | `OrderByDate` | 메일을 날짜 기준으로 정렬하는 기준. |
| 상위 메일 개수 <small>`Top`</small> | 입력 | `int` | 가져올 최대 메일 개수. |
| 계정 <small>`Account`</small> | 입력 | `string` | 메일에 사용할 Outlook 계정(메일 주소). |
| 메일 폴더 <small>`MailFolder`</small> | 입력 | `string` | 메일을 가져올 대상 폴더 이름. |
| 메시지 목록 <small>`Messages`</small> | 출력 | `List<MailMessage>` | 가져온 메일 메시지 목록(출력). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## Outlook 메일 보내기  <small>`OutlookSendMessage`</small>

설치된 Outlook을 통해 메일을 보냅니다(첨부 지원).

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 받는 사람 <small>`TO`</small> | 입력 | `string` | 메일 수신자 주소. |
| 참조 <small>`CC`</small> | 입력 | `string` | 메일 참조(CC) 수신자 주소. |
| 본문 <small>`Body`</small> | 입력 | `string` | 메일 본문 내용. |
| 제목 <small>`Subject`</small> | 입력 | `string` | 메일 제목. |
| 첨부 파일 <small>`Attachment`</small> | 입력 | `string` | 메일에 첨부할 파일 경로. |
| 계정 <small>`Account`</small> | 입력 | `string` | 메일에 사용할 Outlook 계정(메일 주소). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## Outlook 메일 삭제  <small>`OutlookDeleteMessage`</small>

설치된 Outlook에서 지정한 메일을 삭제합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 메일 메시지 <small>`MailMessage`</small> | 입력 | `MailMessage` | 삭제할 대상 메일 메시지. |
| 영구 삭제 <small>`PermanentlyDelete`</small> | 입력 | `bool` | 메일을 휴지통을 거치지 않고 영구 삭제할지 여부. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
