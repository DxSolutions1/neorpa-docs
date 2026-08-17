<!-- 이 파일은 scripts/gen_activity_stubs.py 로 자동 생성됩니다.
     직접 편집하지 말고 website/data/activities.yaml 을 고친 뒤 스크립트를 다시 실행하세요. -->


# System (구조 · 프로세스)

플로차트·스테이트머신 등 WF 구조와 프로세스·로그 유틸.

> 이 카테고리에는 11개의 액티비티가 있습니다. 각 액티비티의 **속성** 표는 소스에서 자동 추출되며(상속 포함), 표시명·설명은 리소스/설명 데이터에서 해석됩니다.

## Flowchart  <small>`Flowchart`</small>

노드와 연결선으로 흐름을 구성하는 플로차트 컨테이너입니다.

**속성**

!!! note
    표준 WF 액티비티이거나 별도 인자가 없습니다.

## Flow Switch  <small>`FlowSwitch`</small>

플로차트에서 식의 값에 따라 여러 갈래로 분기합니다.

**속성**

!!! note
    표준 WF 액티비티이거나 별도 인자가 없습니다.

## Flow Decision  <small>`FlowDecision`</small>

플로차트에서 조건에 따라 참/거짓 두 갈래로 분기합니다.

**속성**

!!! note
    표준 WF 액티비티이거나 별도 인자가 없습니다.

## Invoke Method  <small>`InvokeMethod`</small>

지정한 객체나 형식의 메서드를 호출합니다.

**속성**

!!! note
    표준 WF 액티비티이거나 별도 인자가 없습니다.

## State  <small>`State`</small>

스테이트 머신의 상태를 정의합니다(진입/이탈 동작과 전이 포함).

**속성**

!!! note
    표준 WF 액티비티이거나 별도 인자가 없습니다.

## Final State  <small>`FinalState`</small>

스테이트 머신의 종료 상태를 정의합니다.

**속성**

!!! note
    표준 WF 액티비티이거나 별도 인자가 없습니다.

## State Machine  <small>`StateMachine`</small>

상태와 전이로 흐름을 구성하는 스테이트 머신 컨테이너입니다.

**속성**

!!! note
    표준 WF 액티비티이거나 별도 인자가 없습니다.

## 로그 메시지 출력  <small>`PrintLogMessage`</small>

지정한 메시지를 실행 로그에 출력합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `Message` | 입력 | `string` | 기록할 로그 메시지 내용. |
| `LogType` | 입력 | `string` | 기록할 로그의 수준/종류(정보/경고/오류 등). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 프로세스 종료  <small>`KillProcess`</small>

지정한 프로세스를 강제로 종료합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `process` | 입력 | `Process` | 종료할 대상 프로세스. |
| `processName` | 입력 | `string` | 종료할 대상 프로세스 이름. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 프로세스 목록 가져오기  <small>`GetProcesses`</small>

현재 실행 중인 프로세스 목록을 가져옵니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `Processes` | 출력 | `Collection<Process>` | 조회된 프로세스 목록(출력). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## AddLogFields  <small>`AddLogFields`</small>

이후 실행 로그(JSON)에 사용자 정의 필드를 덧붙입니다. 다음 호출 시 새 값으로 교체됩니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 인자 <small>`Arguments`</small> | 입력 | `List<ArgumentInfo>` | 호출 대상에 전달하거나 로그에 추가할 인자 모음(이름-값). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

