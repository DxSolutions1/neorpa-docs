<!-- 이 파일은 scripts/gen_activity_stubs.py 로 자동 생성됩니다.
     직접 편집하지 말고 website/data/activities.yaml 을 고친 뒤 스크립트를 다시 실행하세요. -->


# Statements (흐름 제어)

조건·반복·예외·시퀀스 등 워크플로 제어 구조. 대부분 WF 표준 액티비티입니다.

> 이 카테고리에는 17개의 액티비티가 있습니다. 각 액티비티의 **속성** 표는 소스에서 자동 추출되며(상속 포함), 표시명·설명은 리소스/설명 데이터에서 해석됩니다.

## Assign  <small>`Assign`</small>

변수에 값을 대입합니다.

**속성**

!!! note
    표준 WF 액티비티이거나 별도 인자가 없습니다.

## If  <small>`If`</small>

조건에 따라 분기합니다.

**속성**

!!! note
    표준 WF 액티비티이거나 별도 인자가 없습니다.

## Sequence  <small>`Sequence`</small>

자식 액티비티를 순서대로 실행합니다.

**속성**

!!! note
    표준 WF 액티비티이거나 별도 인자가 없습니다.

## Parallel  <small>`Parallel`</small>

여러 자식 액티비티를 병렬로 실행합니다.

**속성**

!!! note
    표준 WF 액티비티이거나 별도 인자가 없습니다.

## Try Catch  <small>`TryCatch`</small>

본문 실행 중 발생한 예외를 잡아 처리하고, 필요하면 마무리 작업을 수행합니다.

**속성**

!!! note
    표준 WF 액티비티이거나 별도 인자가 없습니다.

## Throw  <small>`Throw`</small>

지정한 예외를 발생시킵니다.

**속성**

!!! note
    표준 WF 액티비티이거나 별도 인자가 없습니다.

## Rethrow  <small>`Rethrow`</small>

Catch 블록에서 잡은 예외를 다시 던집니다.

**속성**

!!! note
    표준 WF 액티비티이거나 별도 인자가 없습니다.

## Write Line  <small>`WriteLine`</small>

지정한 텍스트를 출력합니다.

**속성**

!!! note
    표준 WF 액티비티이거나 별도 인자가 없습니다.

## Delay  <small>`Delay`</small>

지정한 시간만큼 실행을 대기합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `Duration` | 입력 | `TimeSpan` | 대기할 시간(TimeSpan 형식). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## Switch  <small>`Switch`</small>

식의 값에 따라 여러 갈래 중 하나로 분기합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `SwitchExpression` | 입력 | `object` | 분기를 결정하는 판단 식으로, 각 케이스 값과 비교된다. |

## For Each  <small>`ForEach`</small>

컬렉션의 각 요소에 대해 본문을 반복 실행합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `Collection` | 입력 | `object` | 반복 처리할 대상 컬렉션. |
| `Index` | 출력 | `int` | 현재 반복 항목의 인덱스(출력, 0부터 시작). |

## Retry Scope  <small>`RetryScope`</small>

본문이 성공하거나 지정한 횟수에 도달할 때까지 재시도합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `NumberOfRetries` | 입력 | `int` | 실패 시 시도할 최대 재시도 횟수. |
| `RetryInterval` | 입력 | `TimeSpan` | 재시도 사이에 대기할 간격(TimeSpan 형식). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
| `AttemptCount` | 출력 | `int` | 실제로 수행된 재시도 횟수(출력). |
| `Succeeded` | 출력 | `bool` | 재시도 끝에 성공했는지 여부(출력). |
| `LastFailureType` | 출력 | `string` | 마지막 실패의 예외 형식 이름(출력). |
| `LastExceptionMessage` | 출력 | `string` | 마지막 시도에서 발생한 예외 메시지(출력). |

## While  <small>`While`</small>

조건이 참인 동안 본문을 반복 실행합니다(선검사).

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `Condition` | 설정 | `Activity<bool>` | 반복을 계속할지 판단하는 조건식(결과가 참인 동안 반복). |
| `IterationCount` | 출력 | `int` | 반복이 수행된 총 횟수(출력). |

## Do While  <small>`DoWhile`</small>

본문을 먼저 실행한 뒤 조건이 참인 동안 반복합니다(후검사).

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `Condition` | 설정 | `Activity<bool>` | 반복을 계속할지 판단하는 조건식(결과가 참인 동안 반복). |
| `IterationCount` | 출력 | `int` | 반복이 수행된 총 횟수(출력). |

## Break  <small>`Break`</small>

반복문을 즉시 빠져나옵니다.

**속성**

!!! note
    표준 WF 액티비티이거나 별도 인자가 없습니다.

## Continue  <small>`Continue`</small>

반복문의 나머지를 건너뛰고 다음 반복으로 넘어갑니다.

**속성**

!!! note
    표준 WF 액티비티이거나 별도 인자가 없습니다.

## Add To Collection  <small>`AddToCollection`</small>

컬렉션에 항목을 추가합니다.

**속성**

!!! note
    표준 WF 액티비티이거나 별도 인자가 없습니다.

