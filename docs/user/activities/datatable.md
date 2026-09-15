<!-- 이 파일은 scripts/gen_activities.py 로 자동 생성됩니다.
     직접 편집하지 말고 data/activities.yaml 을 고친 뒤 `python scripts/gen_activities.py --write` 를 다시 실행하세요. -->


# DataTable

System.Data.DataTable을 만들고 병합·조인·필터·정렬·행·열을 조작합니다.

> 이 카테고리에는 15개의 액티비티가 있습니다. 각 액티비티의 **속성** 표는 소스에서 자동 추출되며(상속 포함), 표시명·설명은 리소스/설명 데이터에서 해석됩니다.

## 데이터 테이블 병합  <small>`MergeDataTable`</small>

두 DataTable을 하나로 병합합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| Target <small>`TargetTable`</small> | 입출력 | `DataTable` | 병합 결과를 받을 대상 DataTable. |
| Source <small>`SourceTable`</small> | 입력 | `DataTable` | 병합할 원본 DataTable. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 데이터 테이블 생성  <small>`BuildDataTable`</small>

빈 DataTable을 컬럼 정의와 함께 만듭니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `dataTable` | 출력 | `DataTable` | 작업 대상이 되는 DataTable. |
| `tableXml` | 입력 | `string` | 테이블의 구조와 데이터를 정의한 XML. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 데이터 테이블 열 추가  <small>`AddColumnDataTable`</small>

DataTable에 새 열을 추가합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `AllowDBNull` | 설정 | `bool` | 이 열에 DBNull(빈 값)을 허용할지 여부. |
| `AutoIncrement` | 설정 | `bool` | 이 열의 값을 자동으로 1씩 증가시킬지 여부. |
| `DefaultValue` | 입력 | `string` | 새 열에 채울 기본값. |
| `MaxLength` | 입력 | `Int32` | 이 문자열 열이 가질 수 있는 최대 길이. |
| `Unique` | 설정 | `bool` | 이 열의 값이 중복 없이 고유해야 하는지 여부. |
| `Column` | 입력 | `DataColumn` | 대상이 되는 DataTable 열(DataColumn 개체). |
| `DataTable` | 입력 | `DataTable` | 작업 대상이 되는 DataTable. |
| `ColumnName` | 입력 | `string` | 대상 열의 이름. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 데이터 테이블 정렬  <small>`SortDataTable`</small>

DataTable을 지정한 열 기준으로 정렬합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `Column` | 입력 | `DataColumn` | 대상이 되는 DataTable 열(DataColumn 개체). |
| `ColumnIndex` | 입력 | `int` | 대상 열의 인덱스(0부터 시작). |
| `ColumnName` | 입력 | `string` | 대상 열의 이름. |
| `Order` | 입력 | `string` | 정렬 순서(오름차순/내림차순). |
| `DataTable` | 입력 | `DataTable` | 작업 대상이 되는 DataTable. |
| DataTable <small>`DataTable2`</small> | 출력 | `DataTable` | 조인/정렬할 두 번째 DataTable. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 데이터 테이블 초기화  <small>`ClearDataTable`</small>

DataTable의 모든 행을 삭제해 초기화합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `DataTable` | 입력 | `DataTable` | 작업 대상이 되는 DataTable. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 데이터 테이블 출력  <small>`OutputDataTable`</small>

DataTable의 내용을 읽기 좋은 문자열(텍스트 표)로 변환합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `DataTable` | 입력 | `DataTable` | 작업 대상이 되는 DataTable. |
| `Text` | 출력 | `string` | DataTable을 문자열로 변환한 결과(출력). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 데이터 테이블 행 반복  <small>`ForEachRowTable`</small>

DataTable의 각 행에 대해 본문을 반복 실행합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `table` | 입력 | `DataTable` | 대상 테이블(DataTable 또는 테이블 이름). |
| `Index` | 출력 | `int` | 현재 반복 항목의 인덱스(출력, 0부터 시작). |

## 데이터 테이블 행 추가  <small>`AddRowDataTable`</small>

DataTable에 새 행을 추가합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `DataRow` | 입력 | `DataRow` | 추가할 DataRow 개체. |
| `DataTable` | 입력 | `DataTable` | 작업 대상이 되는 DataTable. |
| `ArrayRow` | 입력 | `Object[]` | 새 행으로 추가할 값들의 배열(열 순서대로). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 열 삭제 (데이터 테이블)  <small>`RemoveColumnDataTable`</small>

DataTable에서 지정한 열을 삭제합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `Column` | 입력 | `DataColumn` | 대상이 되는 DataTable 열(DataColumn 개체). |
| `ColumnIndex` | 입력 | `int` | 대상 열의 인덱스(0부터 시작). |
| `DataTable` | 입력 | `DataTable` | 작업 대상이 되는 DataTable. |
| `ColumnName` | 입력 | `string` | 대상 열의 이름. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 중복 행 제거  <small>`RemoveDuplicateRows`</small>

DataTable에서 중복된 행을 제거합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `DataTable` | 입력 | `DataTable` | 작업 대상이 되는 DataTable. |
| 데이터 테이블 (출력) <small>`OutDataTable`</small> | 출력 | `DataTable` | 추출 결과를 담는 DataTable(출력). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 행 삭제 (데이터 테이블)  <small>`RemoveRowDataTable`</small>

DataTable에서 지정한 행을 삭제합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `Row` | 입력 | `DataRow` | 대상 DataRow 개체. |
| `RowIndex` | 입력 | `int` | 대상 행의 인덱스(0부터 시작). |
| `DataTable` | 입력 | `DataTable` | 작업 대상이 되는 DataTable. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 행 항목 가져오기  <small>`GetRowItem`</small>

DataTable 행에서 지정한 열의 값을 가져옵니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `Column` | 입력 | `DataColumn` | 대상이 되는 DataTable 열(DataColumn 개체). |
| `ColumnIndex` | 입력 | `int` | 대상 열의 인덱스(0부터 시작). |
| `ColumnName` | 입력 | `string` | 대상 열의 이름. |
| `Row` | 입력 | `DataRow` | 대상 DataRow 개체. |
| 결과 <small>`Result`</small> | 출력 | `string` | 액티비티 실행 결과(출력). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 데이터 테이블 → CSV 변환  <small>`DTToCSV`</small>

DataTable을 CSV 파일로 저장합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `filepath` | 입력 | `string` | 대상 파일의 경로. |
| `DataTable` | 입력 | `DataTable` | 작업 대상이 되는 DataTable. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 데이터 테이블 조인 (병합)  <small>`JoinDataTable`</small>

두 DataTable을 지정한 키 기준으로 조인해 하나로 합칩니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `DataTable1` | 입력 | `DataTable` | 조인할 첫 번째 DataTable. |
| `DataTable2` | 입력 | `DataTable` | 조인/정렬할 두 번째 DataTable. |
| 결과 <small>`Result`</small> | 출력 | `DataTable` | 액티비티 실행 결과(출력). |
| `JoinConfiguration` | 입력 | `string` | 두 테이블을 조인하는 방식(조인 종류·키 매핑)을 정의하는 설정. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 데이터 테이블 필터  <small>`FilterDataTable`</small>

조건에 맞는 행만 남기도록 DataTable을 필터링합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `DataTable` | 입력 | `DataTable` | 작업 대상이 되는 DataTable. |
| `OutputDataTable` | 출력 | `DataTable` | 필터링 결과를 담는 DataTable(출력). |
| `FilterRowsMode` | 설정 | `FilterMode` | 조건에 맞는 행을 남길지 제거할지 지정하는 모드. |
| `SelectColumnsMode` | 설정 | `FilterMode` | 지정한 열을 남길지 제거할지 지정하는 모드. |
| `Filters` | 설정 | `List<FilterOperationArgument>` | 적용할 행 필터 조건 목록. |
| `SelectColumns` | 설정 | `List<InArgument<object>>` | 결과에 포함할 열 목록. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
