<!-- 이 파일은 scripts/gen_activities.py 로 자동 생성됩니다.
     직접 편집하지 말고 data/activities.yaml 을 고친 뒤 `python scripts/gen_activities.py --write` 를 다시 실행하세요. -->


# Mail

SMTP로 메일을 보내고 POP3로 받습니다.

> 이 카테고리에는 2개의 액티비티가 있습니다. 각 액티비티의 **속성** 표는 소스에서 자동 추출되며(상속 포함), 표시명·설명은 리소스/설명 데이터에서 해석됩니다.

## 메일 보내기  <small>`SendMail`</small>

SMTP로 메일을 전송합니다(첨부 지원).

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 암호 <small>`logonPassword`</small> | 입력 | `string` | 메일 발송에 사용할 로그인 암호. |
| 이메일 <small>`logonEmail`</small> | 입력 | `string` | 메일 발송에 사용할 로그인 계정. |
| 발신 이메일 <small>`senderEmail`</small> | 입력 | `string` | 보내는 사람의 메일 주소. |
| 발신 이름 <small>`senderName`</small> | 입력 | `string` | 보내는 사람의 표시 이름. |
| 수신 이메일 <small>`receiverEmail`</small> | 입력 | `string` | 메일 수신자 주소. |
| 참조 <small>`ccEmails`</small> | 입력 | `string` | 메일 참조(CC) 수신자 주소. |
| 숨은 참조 <small>`bccEmails`</small> | 입력 | `string` | 메일 숨은 참조(BCC) 수신자 주소. |
| `isBodyHtml` | 입력 | `bool` | 본문을 HTML 형식으로 보낼지 여부. |
| `continueOnError` | 입력 | `bool` | 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
| 제목 <small>`subject`</small> | 입력 | `string` | 메일 제목. |
| 본문 <small>`body`</small> | 입력 | `string` | 메일 본문 내용. |
| 첨부 파일 <small>`staticAttachments`</small> | 입력 | `IEnumerable<string>` | 미리 지정한 고정 첨부 파일 경로 목록. |
| 첨부 파일(변수) <small>`dynamicAttachments`</small> | 입력 | `IEnumerable<string>` | 실행 중 값으로 지정하는 첨부 파일 경로 목록. |
| 서버 <small>`server`</small> | 입력 | `string` | 메일 서버 주소. |
| 포트 <small>`port`</small> | 입력 | `int` | 메일 서버 포트 번호. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## POP3Mail  <small>`POP3Mail`</small>

POP3 서버에 접속해 메일을 수신하고 메시지 목록으로 가져옵니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 타임아웃(ms) <small>`TimeoutMS`</small> | 입력 | `int` | 서버 연결을 기다릴 최대 시간(밀리초). |
| 이메일 <small>`Email`</small> | 입력 | `string` | 메일 로그인 계정(메일 주소). |
| 암호 <small>`Password`</small> | 입력 | `string` | 접근에 사용할 암호(파일 또는 메일 계정). |
| 메시지 삭제 <small>`DeleteMessages`</small> | 입력 | `bool` | 가져온 뒤 서버에서 메일을 삭제할지 여부. |
| 보안 연결 <small>`SecureConnection`</small> | 입력 | `string` | 메일 서버 보안 연결 방식(SSL/TLS 등). |
| 상위 메일 개수 <small>`Top`</small> | 입력 | `int` | 가져올 최대 메일 개수. |
| 메시지 목록 <small>`Messages`</small> | 출력 | `List<MailMessage>` | 가져온 메일 메시지 목록(출력). |
| 포트 <small>`Port`</small> | 입력 | `int` | 메일 서버 포트 번호. |
| 서버 <small>`Server`</small> | 입력 | `string` | 메일 서버 주소. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
