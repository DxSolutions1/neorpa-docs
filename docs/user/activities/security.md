<!-- 이 파일은 scripts/gen_activities.py 로 자동 생성됩니다.
     직접 편집하지 말고 data/activities.yaml 을 고친 뒤 `python scripts/gen_activities.py --write` 를 다시 실행하세요. -->


# 보안 (자격 증명)

비밀번호를 워크플로 파일에 적지 않기 위한 기능입니다. **가장 쉬운 방법은 액티비티가 필요 없습니다**: ① 리본 `설정 › 자격 증명`에서 이름 · 사용자 이름 · 비밀번호를 등록합니다(비밀번호는 가려져 입력되고, 저장한 뒤에는 다시 표시되지 않습니다). ② 비밀번호를 쓰는 액티비티의 속성 창에서 `보호된 비밀번호`(또는 `보호된 입력값` · `보호된 연결 문자열` · `API 키(보호)`) 칸의 **열쇠 버튼**을 눌러 그 자격 증명을 고릅니다. 칸에 열쇠와 이름이 보이면 연결된 것이고, 워크플로 파일에는 자격 증명 이름만 남습니다. 자격 증명은 Windows 자격 증명 관리자(제어판 › 자격 증명 관리자 › Windows 자격 증명)에 `NeoRPA:{이름}` 으로 저장되며 **PC 와 Windows 사용자 계정마다 따로**입니다 — 워크플로를 실행할 PC · 계정(작업 스케줄러가 쓰는 계정 포함)에 같은 이름으로 등록되어 있어야 합니다(없으면 설계할 때 경고, 실행할 때 오류). 아래 액티비티는 사용자 이름까지 읽어야 하거나, 워크플로 안에서 자격 증명을 저장 · 삭제해야 할 때 씁니다.

> 이 카테고리에는 3개의 액티비티가 있습니다. 각 액티비티의 **속성** 표는 소스에서 자동 추출되며(상속 포함), 표시명·설명은 리소스/설명 데이터에서 해석됩니다.

## 자격 증명 가져오기  <small>`GetCredential`</small>

Windows 자격 증명 관리자에서 이름으로 자격 증명을 읽어 사용자 이름과 보호된 비밀번호(SecureString)를 돌려줍니다. 대상은 `NeoRPA:{이름}` 으로 저장되어 있어야 합니다(없으면 오류).

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 자격 증명 이름 <small>`CredentialName`</small> | 입력 | `string` | 자격 증명 이름(접두 `NeoRPA:` 를 뺀 이름). |
| 사용자 이름 <small>`Username`</small> | 출력 | `string` | 저장된 사용자 이름(출력). |
| 보호된 비밀번호 <small>`SecurePassword`</small> | 출력 | `SecureString` | 저장된 비밀번호(출력, SecureString). HTTP 요청·메일·DB·텍스트 입력 액티비티의 보호된 인자에 연결합니다. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 자격 증명 저장  <small>`SetCredential`</small>

자격 증명을 Windows 자격 증명 관리자에 저장합니다. 처음 한 번 저장할 때 쓰고, 비밀번호를 직접 적은 워크플로는 저장 뒤 지웁니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 자격 증명 이름 <small>`CredentialName`</small> | 입력 | `string` | 저장할 자격 증명 이름. |
| 사용자 이름 <small>`Username`</small> | 입력 | `string` | 저장할 사용자 이름. |
| 암호 <small>`Password`</small> | 입력 | `string` | 저장할 비밀번호(평문). 직접 적으면 워크플로 파일에 남아 설계 시점에 경고가 납니다. |
| 보호된 비밀번호 <small>`SecurePassword`</small> | 입력 | `SecureString` | 저장할 비밀번호(SecureString). 있으면 평문보다 우선합니다. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 자격 증명 삭제  <small>`DeleteCredential`</small>

Windows 자격 증명 관리자에서 자격 증명을 지웁니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 자격 증명 이름 <small>`CredentialName`</small> | 입력 | `string` | 지울 자격 증명 이름. |
| 삭제됨 <small>`Deleted`</small> | 출력 | `bool` | 실제로 지웠으면 true, 없었으면 false(출력). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
