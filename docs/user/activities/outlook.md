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
| `Filter` | 입력 | `string` | 메일을 걸러낼 필터 조건. |
| `FilterByIDs` | 입력 | `List<string>` | 지정한 메일 ID 목록만 가져오도록 거르는 조건. |
| `MarkAsRead` | 설정 | `bool` | 가져온 메일을 읽음으로 표시할지 여부. |
| `OnlyUnreadMessage` | 설정 | `bool` | 읽지 않은 메일만 가져올지 여부. |
| `OrderByDate` | 입력 | `OrderByDate` | 메일을 날짜 기준으로 정렬하는 기준. |
| `Top` | 입력 | `int` | 가져올 최대 메일 개수. |
| `Account` | 입력 | `string` | 메일에 사용할 Outlook 계정(메일 주소). |
| `MailFolder` | 입력 | `string` | 메일을 가져올 대상 폴더 이름. |
| `Messages` | 출력 | `List<MailMessage>` | 가져온 메일 메시지 목록(출력). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## Outlook 메일 보내기  <small>`OutlookSendMessage`</small>

설치된 Outlook을 통해 메일을 보냅니다(첨부 지원).

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `TO` | 입력 | `string` | 메일 수신자 주소. |
| `CC` | 입력 | `string` | 메일 참조(CC) 수신자 주소. |
| `Body` | 입력 | `string` | 메일 본문 내용. |
| `Subject` | 입력 | `string` | 메일 제목. |
| `Attachment` | 입력 | `string` | 메일에 첨부할 파일 경로. |
| `Account` | 입력 | `string` | 메일에 사용할 Outlook 계정(메일 주소). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## Outlook 메일 삭제  <small>`OutlookDeleteMessage`</small>

설치된 Outlook에서 지정한 메일을 삭제합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `MailMessage` | 입력 | `MailMessage` | 삭제할 대상 메일 메시지. |
| `PermanentlyDelete` | 입력 | `bool` | 메일을 휴지통을 거치지 않고 영구 삭제할지 여부. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
