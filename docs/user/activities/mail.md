<!-- 이 파일은 scripts/gen_activities.py 로 자동 생성됩니다.
     직접 편집하지 말고 data/activities.yaml 을 고친 뒤 `python scripts/gen_activities.py --write` 를 다시 실행하세요. -->


# Mail

SMTP로 메일을 보내고 IMAP·POP3로 받습니다. 받은 메일의 첨부는 `첨부 파일 저장`으로 꺼냅니다. 암호는 `보안 › 자격 증명 가져오기(GetCredential)`의 보호된 비밀번호를 연결하면 워크플로 파일에 남지 않습니다.

> 이 카테고리에는 5개의 액티비티가 있습니다. 각 액티비티의 **속성** 표는 소스에서 자동 추출되며(상속 포함), 표시명·설명은 리소스/설명 데이터에서 해석됩니다.

## 메일 보내기  <small>`SendMail`</small>

SMTP로 메일을 전송합니다(첨부 지원).

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 암호 <small>`logonPassword`</small> | 입력 | `string` | 메일 발송에 사용할 로그인 암호. |
| 보호된 비밀번호 <small>`SecurePassword`</small> | 입력 | `SecureString` | 보호된 비밀번호(SecureString). 속성 창의 열쇠 버튼으로 자격 증명을 고르면 워크플로 파일에는 자격 증명 이름만 남습니다. 자격 증명 가져오기(GetCredential)의 SecurePassword 출력(변수)을 연결해도 됩니다. 있으면 평문 비밀번호보다 우선합니다. |
| 이메일 <small>`logonEmail`</small> | 입력 | `string` | 메일 발송에 사용할 로그인 계정. |
| 발신 이메일 <small>`senderEmail`</small> | 입력 | `string` | 보내는 사람의 메일 주소. |
| 발신 이름 <small>`senderName`</small> | 입력 | `string` | 보내는 사람의 표시 이름. |
| 수신 이메일 <small>`receiverEmail`</small> | 입력 | `string` | 메일 수신자 주소. |
| 참조 <small>`ccEmails`</small> | 입력 | `string` | 메일 참조(CC) 수신자 주소. |
| 숨은 참조 <small>`bccEmails`</small> | 입력 | `string` | 메일 숨은 참조(BCC) 수신자 주소. |
| 본문 HTML 여부 <small>`isBodyHtml`</small> | 입력 | `bool` | 본문을 HTML 형식으로 보낼지 여부. |
| 오류 무시 <small>`continueOnError`</small> | 입력 | `bool` | 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
| 제목 <small>`subject`</small> | 입력 | `string` | 메일 제목. |
| 본문 <small>`body`</small> | 입력 | `string` | 메일 본문 내용. |
| 첨부 파일 <small>`staticAttachments`</small> | 입력 | `IEnumerable<string>` | 미리 지정한 고정 첨부 파일 경로 목록. |
| 첨부 파일(변수) <small>`dynamicAttachments`</small> | 입력 | `IEnumerable<string>` | 실행 중 값으로 지정하는 첨부 파일 경로 목록. |
| 서버 <small>`server`</small> | 입력 | `string` | 메일 서버 주소. |
| 포트 <small>`port`</small> | 입력 | `int` | 메일 서버 포트 번호. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 메일 받기 (POP3)  <small>`POP3Mail`</small>

POP3 서버에 접속해 메일을 수신하고 메시지 목록으로 가져옵니다. 첨부도 함께 가져오며 `첨부 파일 저장`으로 꺼냅니다. 메일 폴더를 고르거나 읽지 않은 메일만 가져오려면 `메일 받기 (IMAP)`를 쓰세요.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 타임아웃(ms) <small>`TimeoutMS`</small> | 입력 | `int` | 서버 연결을 기다릴 최대 시간(밀리초). |
| 이메일 <small>`Email`</small> | 입력 | `string` | 메일 로그인 계정(메일 주소). |
| 암호 <small>`Password`</small> | 입력 | `string` | 접근에 사용할 암호(파일 또는 메일 계정). |
| 보호된 비밀번호 <small>`SecurePassword`</small> | 입력 | `SecureString` | 보호된 비밀번호(SecureString). 속성 창의 열쇠 버튼으로 자격 증명을 고르면 워크플로 파일에는 자격 증명 이름만 남습니다. 자격 증명 가져오기(GetCredential)의 SecurePassword 출력(변수)을 연결해도 됩니다. 있으면 평문 비밀번호보다 우선합니다. |
| 메시지 삭제 <small>`DeleteMessages`</small> | 입력 | `bool` | 가져온 뒤 서버에서 메일을 삭제할지 여부. |
| 보안 연결 <small>`SecureConnection`</small> | 입력 | `string` | 메일 서버 보안 연결 방식(SSL/TLS 등). |
| 상위 메일 개수 <small>`Top`</small> | 입력 | `int` | 가져올 최대 메일 개수. |
| 메시지 목록 <small>`Messages`</small> | 출력 | `List<MailMessage>` | 가져온 메일 메시지 목록(출력). |
| 포트 <small>`Port`</small> | 입력 | `int` | 메일 서버 포트 번호. |
| 서버 <small>`Server`</small> | 입력 | `string` | 메일 서버 주소. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 메일 받기 (IMAP)  <small>`GetImapMail`</small>

IMAP 서버의 메일 폴더에서 메일을 가져옵니다. POP3 와 달리 메일이 서버에 남고, **메일 폴더를 고르고 읽지 않은 메일만** 가져올 수 있습니다. 가져오기만으로는 읽음으로 바뀌지 않습니다. 결과는 메일 목록이며 `반복(ForEach)`으로 한 통씩 처리합니다. UiPath Get IMAP Mail Messages 에 해당합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 메일 폴더 <small>`MailFolder`</small> | 입력 | `string` | 메일을 가져올 폴더. **비우면 받은 편지함**입니다. 하위 폴더는 `보관/2026` 처럼 적거나 맨 끝 이름(`2026`)만 적어도 됩니다. 없는 이름이면 서버에 있는 폴더 이름을 오류 문구로 알려 줍니다. |
| 읽지 않은 메일만 <small>`OnlyUnreadMessages`</small> | 설정 | `bool` | 읽지 않은 메일만 가져올지 여부(기본 true). |
| 읽음으로 표시 <small>`MarkAsRead`</small> | 설정 | `bool` | 가져온 메일을 읽음으로 표시할지 여부(기본 false). 꺼 두면 다음 실행에서 같은 메일을 다시 가져옵니다 — 처리한 메일은 `메일 이동 (IMAP)`으로 옮기거나 이 옵션을 켜세요. |
| 메시지 삭제 <small>`DeleteMessages`</small> | 설정 | `bool` | 가져온 메일을 서버에서 지울지 여부(기본 false). 가져온 메일만 지웁니다. |
| 상위 메일 개수 <small>`Top`</small> | 입력 | `int` | 가져올 최대 메일 수. 비우면 30. |
| 날짜 정렬 <small>`OrderByDate`</small> | 설정 | `OrderByDate` | 조건에 맞는 메일이 가져올 수보다 많을 때 어느 쪽부터 가져올지 — **최신순**(기본) 또는 **오래된 순**(받은 순서대로 처리할 때). 메일 폴더에 들어온 순서로 셉니다. |
| 본문을 HTML로 <small>`BodyAsHtml`</small> | 설정 | `bool` | 꺼 두면(기본) 메일의 본문(`Body`)은 **텍스트**입니다 — HTML 뿐인 메일은 글만 꺼냅니다. 켜면 HTML 본문을 그대로 줍니다. |
| 제목에 포함 <small>`SubjectContains`</small> | 입력 | `string` | 제목에 이 글이 들어 있는 메일만(대소문자 무시). 카드의 **제목에 포함** 칸입니다. |
| 보낸 사람에 포함 <small>`FromContains`</small> | 입력 | `string` | 보낸 사람의 이름이나 주소에 이 글이 들어 있는 메일만(대소문자 무시). |
| 이 시각부터 <small>`Since`</small> | 입력 | `DateTime` | 이 시각부터 받은 메일만(예: `Today`, `Now.AddHours(-3)`). 비우면 가리지 않습니다. |
| 메시지 목록 <small>`Messages`</small> | 출력 | `List<MailMessage>` | 가져온 메일 목록(출력, `List(Of MailMessage)`). 맞는 메일이 없으면 빈 목록입니다. 오류 무시를 켠 채 실패해도 빈 목록입니다. |
| 서버 <small>`Server`</small> | 입력 | `string` | IMAP 서버 주소(예: `imap.gmail.com`). |
| 포트 <small>`Port`</small> | 입력 | `int` | 포트. 비우면 보안 연결에 맞는 기본값 — 자동·SSL/TLS 는 993, 그 밖은 143. |
| 보안 연결 <small>`SecureConnection`</small> | 설정 | `SecureConnectionType` | 연결을 암호화하는 방식. **자동**(기본)이면 포트 993 은 SSL/TLS, 다른 포트는 서버가 받으면 STARTTLS 를 씁니다. 그 밖에 없음·SSL/TLS·STARTTLS·선택적 TLS. |
| 폐기 확인 생략 <small>`IgnoreCRL`</small> | 설정 | `bool` | 서버 인증서가 폐기됐는지 확인하는 단계를 건너뜁니다. 폐기 목록 서버에 닿지 못하는 **폐쇄망**에서 보안 연결이 실패할 때만 켜세요. 인증서 자체의 검증은 그대로 합니다. |
| 타임아웃(ms) <small>`TimeoutMS`</small> | 입력 | `int` | 서버의 응답을 기다리는 시간(밀리초). 비우면 30000(30초). 큰 메일을 받는 동안에는 데이터가 오는 한 끊지 않습니다. |
| 이메일 <small>`Email`</small> | 입력 | `string` | 로그인할 계정(메일 주소). |
| 암호 <small>`Password`</small> | 입력 | `string` | 암호(평문). 직접 적으면 워크플로 파일에 남아 경고가 표시됩니다 — **보호된 비밀번호**를 쓰세요. 카드에는 이 칸이 없고 속성 창에만 있습니다. |
| 보호된 비밀번호 <small>`SecurePassword`</small> | 입력 | `SecureString` | `자격 증명 가져오기(GetCredential)`의 보호된 비밀번호 출력을 연결합니다. 이 값이 있으면 암호보다 먼저 씁니다. |
| OAuth 사용 <small>`UseOAuth`</small> | 설정 | `bool` | 암호 자리에 넣은 값을 **OAuth 2.0 액세스 토큰**으로 써서 로그인합니다(XOAUTH2). 암호 로그인을 받지 않는 Microsoft 365 등에 씁니다. 토큰은 워크플로에서 따로 받아 와야 합니다. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

!!! note "제공 버전"
    메일 받기 (IMAP)·메일 이동 (IMAP)·첨부 파일 저장은 NeoRPA 2.2.4 다음 버전부터 제공됩니다. 툴박스 **Mail** 에 보이지 않으면 도움말 탭 → **버전 관리** 에서 새 버전을 확인하세요.

#### 쓰는 법 { #imap-how }

1. `보안 › 자격 증명 가져오기`로 계정의 암호를 꺼내 **보호된 비밀번호** 칸에 연결합니다(암호를 워크플로에 적지 않습니다).
2. **메일 받기 (IMAP)** 에 서버·이메일을 적고 **메시지 목록** 칸에 변수(`List(Of MailMessage)`)를 적습니다.
3. `반복(ForEach)`으로 메일을 한 통씩 꺼내 처리합니다 — 값 읽기, **첨부 파일 저장**.
4. 처리한 메일은 **메일 이동 (IMAP)** 으로 다른 폴더(예: `처리완료`)에 옮겨 두면 다음 실행이 다시 집지 않습니다.

#### 메일에서 꺼내 쓰는 값 { #imap-mail }

메일 변수 이름이 `mail` 일 때:

| 식 | 값 |
|---|---|
| `mail.Subject` | 제목 |
| `mail.From.Address` · `mail.From.DisplayName` | 보낸 사람의 주소 · 이름 |
| `mail.Body` | 본문(텍스트. **본문을 HTML로**를 켜면 HTML) |
| `CDate(mail.Headers("Date"))` | 보낸 때(이 PC 의 시각으로) |
| `mail.Attachments.Count` · `mail.Attachments(0).Name` | 첨부 수 · 첫 첨부의 이름 |
| `mail.To(0).Address` · `mail.CC.Count` | 받는 사람 · 참조 |

#### 메일 서비스별 설정 { #imap-servers }

| 서비스 | 서버 | 포트 | 로그인 |
|---|---|---|---|
| Gmail | `imap.gmail.com` | 993 | 2단계 인증을 켠 뒤 만든 **앱 비밀번호** |
| 네이버 메일 | `imap.naver.com` | 993 | 메일 환경설정에서 **IMAP/SMTP 사용**을 켬. 2단계 인증을 쓰면 애플리케이션 비밀번호 |
| Microsoft 365 | `outlook.office365.com` | 993 | 암호 로그인을 받지 않습니다 — **OAuth 사용**을 켜고 액세스 토큰을 넣습니다 |
| 회사 메일 서버 | 관리자에게 문의 | 993 또는 143 | 계정 암호. 폐쇄망에서 보안 연결이 실패하면 **폐기 확인 생략** |

서비스의 설정은 바뀔 수 있으니 각 서비스의 도움말을 함께 확인하세요.

!!! warning "오류가 날 때"
    - *로그인하지 못했습니다* — 암호가 계정 암호가 아니라 앱 비밀번호여야 하는 서비스인지, 메일 설정에서 IMAP 사용이 켜져 있는지 확인하세요.
    - *보안 연결(TLS)을 맺지 못했습니다* — 포트와 **보안 연결**이 맞는지 확인하세요(993 은 SSL/TLS, 143 은 STARTTLS).
    - *응답하지 않았습니다* — 서버 주소·포트·방화벽을 확인하고, 느린 서버면 **타임아웃(ms)** 을 늘리세요.

## 메일 이동 (IMAP)  <small>`MoveImapMail`</small>

`메일 받기 (IMAP)`로 가져온 메일을 같은 계정의 다른 메일 폴더로 옮깁니다. 처리한 메일을 `처리완료` 같은 폴더로 옮겨 두면 다음 실행이 같은 메일을 다시 집지 않습니다. UiPath Move IMAP Mail Message 에 해당합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 메시지 <small>`Message`</small> | 입력 | `MailMessage` | 옮길 메일. `메일 받기 (IMAP)`의 메시지 목록에서 꺼낸 메일이어야 합니다(POP3 로 받은 메일은 옮길 수 없습니다). |
| 옮길 폴더 <small>`ToFolder`</small> | 입력 | `string` | 옮길 폴더. 서버에 **이미 있는** 폴더여야 합니다(없으면 서버에 있는 폴더 이름을 알려 주며 멈춥니다). 하위 폴더는 `보관/2026` 처럼 적습니다. |
| 원래 폴더 <small>`FromFolder`</small> | 입력 | `string` | 메일이 지금 있는 폴더. 비우면 메일을 가져온 폴더입니다. |
| 서버 <small>`Server`</small> | 입력 | `string` | IMAP 서버 주소(예: `imap.gmail.com`). |
| 포트 <small>`Port`</small> | 입력 | `int` | 포트. 비우면 보안 연결에 맞는 기본값 — 자동·SSL/TLS 는 993, 그 밖은 143. |
| 보안 연결 <small>`SecureConnection`</small> | 설정 | `SecureConnectionType` | 연결을 암호화하는 방식. **자동**(기본)이면 포트 993 은 SSL/TLS, 다른 포트는 서버가 받으면 STARTTLS 를 씁니다. 그 밖에 없음·SSL/TLS·STARTTLS·선택적 TLS. |
| 폐기 확인 생략 <small>`IgnoreCRL`</small> | 설정 | `bool` | 서버 인증서가 폐기됐는지 확인하는 단계를 건너뜁니다. 폐기 목록 서버에 닿지 못하는 **폐쇄망**에서 보안 연결이 실패할 때만 켜세요. 인증서 자체의 검증은 그대로 합니다. |
| 타임아웃(ms) <small>`TimeoutMS`</small> | 입력 | `int` | 서버의 응답을 기다리는 시간(밀리초). 비우면 30000(30초). 큰 메일을 받는 동안에는 데이터가 오는 한 끊지 않습니다. |
| 이메일 <small>`Email`</small> | 입력 | `string` | 로그인할 계정(메일 주소). |
| 암호 <small>`Password`</small> | 입력 | `string` | 암호(평문). 직접 적으면 워크플로 파일에 남아 경고가 표시됩니다 — **보호된 비밀번호**를 쓰세요. 카드에는 이 칸이 없고 속성 창에만 있습니다. |
| 보호된 비밀번호 <small>`SecurePassword`</small> | 입력 | `SecureString` | `자격 증명 가져오기(GetCredential)`의 보호된 비밀번호 출력을 연결합니다. 이 값이 있으면 암호보다 먼저 씁니다. |
| OAuth 사용 <small>`UseOAuth`</small> | 설정 | `bool` | 암호 자리에 넣은 값을 **OAuth 2.0 액세스 토큰**으로 써서 로그인합니다(XOAUTH2). 암호 로그인을 받지 않는 Microsoft 365 등에 씁니다. 토큰은 워크플로에서 따로 받아 와야 합니다. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

- 이미 옮겼거나 지워진 메일이면 오류로 알립니다(없는 메일을 "옮겼다"고 넘어가지 않습니다).
- 같은 메일을 한 번 더 옮길 수 있습니다(처리완료 → 보관).
- 서버·계정은 메일을 가져올 때와 같게 적습니다.

## 첨부 파일 저장  <small>`SaveMailAttachments`</small>

메일의 첨부 파일을 폴더에 저장하고, 저장한 파일의 경로를 돌려줍니다. `메일 받기 (IMAP)`·`메일 받기 (POP3)`로 가져온 메일에 씁니다. UiPath Save Attachments 에 해당합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 메시지 <small>`Message`</small> | 입력 | `MailMessage` | 첨부를 꺼낼 메일(메시지 목록에서 꺼낸 한 통). |
| 저장할 폴더 <small>`FolderPath`</small> | 입력 | `string` | 저장할 폴더. 없으면 만듭니다. 상대 경로는 프로젝트 폴더 기준입니다. 카드의 📁 버튼으로 고를 수 있습니다. |
| 파일 이름 패턴 <small>`FileNamePattern`</small> | 입력 | `string` | 저장할 첨부의 이름 패턴(예: `*.xlsx`). 여러 개는 `;` 로 나눕니다(`*.xlsx; *.pdf`). 비우면 모두 저장합니다. |
| 같은 이름이면 <small>`IfExists`</small> | 설정 | `ExistingFileAction` | 저장할 폴더에 같은 이름의 파일이 이미 있을 때 — **덮어쓰기**(기본), **번호 붙임**(`주문서 (2).xlsx` 로 따로 저장), **오류**(아무것도 저장하지 않고 멈춤). 여러 메일의 첨부를 한 폴더에 모을 때는 번호 붙임을 쓰세요. |
| 본문 그림 포함 <small>`IncludeInline`</small> | 설정 | `bool` | 본문에 넣어 보여 주는 그림(서명의 로고 등)도 저장할지 여부(기본 false). |
| 파일 목록 <small>`Files`</small> | 출력 | `string[]` | 저장한 파일의 전체 경로들(출력, 문자열 배열 — 첨부 순서). 저장한 것이 없거나 오류 무시로 넘어가면 빈 배열입니다. 카드의 **저장한 파일** 칸에 변수를 적습니다. |
| 개수 <small>`Count`</small> | 출력 | `int` | 저장한 파일 수(출력). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

- 한 메일에 같은 이름의 첨부가 둘 이상이면 뒤의 것에 번호를 붙여 모두 저장합니다.
- 첨부 이름에 Windows 가 파일 이름으로 쓰지 못하는 글자가 있으면 `_` 로 바꿔 저장합니다. 실제로 저장된 이름은 **저장한 파일**(출력)로 확인하세요.
- 메일에 붙여 보낸 다른 메일은 `.eml` 파일로 저장됩니다.
