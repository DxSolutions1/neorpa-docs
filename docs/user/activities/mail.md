<!-- 이 파일은 scripts/gen_activity_stubs.py 로 자동 생성됩니다.
     직접 편집하지 말고 website/data/activities.yaml 을 고친 뒤 스크립트를 다시 실행하세요. -->


# Mail

SMTP로 메일을 보내고 POP3로 받습니다.

> 이 카테고리에는 2개의 액티비티가 있습니다. 각 액티비티의 **속성** 표는 소스에서 자동 추출되며(상속 포함), 표시명·설명은 리소스/설명 데이터에서 해석됩니다.

## 메일 보내기  <small>`SendMail`</small>

SMTP로 메일을 전송합니다(첨부 지원).

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `logonPassword` | 입력 | `string` | 메일 발송에 사용할 로그인 암호. |
| `logonEmail` | 입력 | `string` | 메일 발송에 사용할 로그인 계정. |
| `senderEmail` | 입력 | `string` | 보내는 사람의 메일 주소. |
| `senderName` | 입력 | `string` | 보내는 사람의 표시 이름. |
| `receiverEmail` | 입력 | `string` | 메일 수신자 주소. |
| `ccEmails` | 입력 | `string` | 메일 참조(CC) 수신자 주소. |
| `bccEmails` | 입력 | `string` | 메일 숨은 참조(BCC) 수신자 주소. |
| `isBodyHtml` | 입력 | `bool` | 본문을 HTML 형식으로 보낼지 여부. |
| `continueOnError` | 입력 | `bool` | 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
| `subject` | 입력 | `string` | 메일 제목. |
| `body` | 입력 | `string` | 메일 본문 내용. |
| `staticAttachments` | 입력 | `IEnumerable<string>` | 미리 지정한 고정 첨부 파일 경로 목록. |
| `dynamicAttachments` | 입력 | `IEnumerable<string>` | 실행 중 값으로 지정하는 첨부 파일 경로 목록. |
| `server` | 입력 | `string` | 메일 서버 주소. |
| `port` | 입력 | `int` | 메일 서버 포트 번호. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## POP3Mail  <small>`POP3Mail`</small>

POP3 서버에 접속해 메일을 수신하고 메시지 목록으로 가져옵니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `TimeoutMS` | 입력 | `int` | 서버 연결을 기다릴 최대 시간(밀리초). |
| `Email` | 입력 | `string` | 메일 로그인 계정(메일 주소). |
| `Password` | 입력 | `string` | 접근에 사용할 암호(파일 또는 메일 계정). |
| `DeleteMessages` | 입력 | `bool` | 가져온 뒤 서버에서 메일을 삭제할지 여부. |
| `SecureConnection` | 입력 | `string` | 메일 서버 보안 연결 방식(SSL/TLS 등). |
| `Top` | 입력 | `int` | 가져올 최대 메일 개수. |
| `Messages` | 출력 | `List<MailMessage>` | 가져온 메일 메시지 목록(출력). |
| `Port` | 입력 | `int` | 메일 서버 포트 번호. |
| `Server` | 입력 | `string` | 메일 서버 주소. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

