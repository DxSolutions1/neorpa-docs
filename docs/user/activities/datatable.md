<!-- 이 파일은 scripts/gen_activities.py 로 자동 생성됩니다.
     직접 편집하지 말고 data/activities.yaml 을 고친 뒤 `python scripts/gen_activities.py --write` 를 다시 실행하세요. -->


# DataTable

System.Data.DataTable을 만들고 병합·조인·필터·정렬·행·열을 조작합니다. CSV 파일을 표로 읽고(CSV 읽기), 표를 CSV 파일로 씁니다(CSV 쓰기).

> 이 카테고리에는 16개의 액티비티가 있습니다. 각 액티비티의 **속성** 표는 소스에서 자동 추출되며(상속 포함), 표시명·설명은 리소스/설명 데이터에서 해석됩니다.

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
| 데이터 테이블 <small>`dataTable`</small> | 출력 | `DataTable` | 작업 대상이 되는 DataTable. |
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
| 데이터 테이블 <small>`DataTable`</small> | 입력 | `DataTable` | 작업 대상이 되는 DataTable. |
| 열 이름 <small>`ColumnName`</small> | 입력 | `string` | 대상 열의 이름. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 데이터 테이블 정렬  <small>`SortDataTable`</small>

DataTable을 지정한 열 기준으로 정렬합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `Column` | 입력 | `DataColumn` | 대상이 되는 DataTable 열(DataColumn 개체). |
| `ColumnIndex` | 입력 | `int` | 대상 열의 인덱스(0부터 시작). |
| 열 이름 <small>`ColumnName`</small> | 입력 | `string` | 대상 열의 이름. |
| 정렬 순서 <small>`Order`</small> | 입력 | `string` | 정렬 순서(오름차순/내림차순). |
| 데이터 테이블 <small>`DataTable`</small> | 입력 | `DataTable` | 작업 대상이 되는 DataTable. |
| DataTable <small>`DataTable2`</small> | 출력 | `DataTable` | 조인/정렬할 두 번째 DataTable. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 데이터 테이블 초기화  <small>`ClearDataTable`</small>

DataTable의 모든 행을 삭제해 초기화합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 데이터 테이블 <small>`DataTable`</small> | 입력 | `DataTable` | 작업 대상이 되는 DataTable. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 데이터 테이블 출력  <small>`OutputDataTable`</small>

DataTable의 내용을 읽기 좋은 문자열(텍스트 표)로 변환합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 데이터 테이블 <small>`DataTable`</small> | 입력 | `DataTable` | 작업 대상이 되는 DataTable. |
| 텍스트 <small>`Text`</small> | 출력 | `string` | DataTable을 문자열로 변환한 결과(출력). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 데이터 테이블 행 반복  <small>`ForEachRowTable`</small>

DataTable의 각 행에 대해 본문을 반복 실행합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 테이블 <small>`table`</small> | 입력 | `DataTable` | 대상 테이블(DataTable 또는 테이블 이름). |
| 인덱스 <small>`Index`</small> | 출력 | `int` | 현재 반복 항목의 인덱스(출력, 0부터 시작). |

## 데이터 테이블 행 추가  <small>`AddRowDataTable`</small>

DataTable에 새 행을 추가합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `DataRow` | 입력 | `DataRow` | 추가할 DataRow 개체. |
| 데이터 테이블 <small>`DataTable`</small> | 입력 | `DataTable` | 작업 대상이 되는 DataTable. |
| `ArrayRow` | 입력 | `Object[]` | 새 행으로 추가할 값들의 배열(열 순서대로). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 열 삭제 (데이터 테이블)  <small>`RemoveColumnDataTable`</small>

DataTable에서 지정한 열을 삭제합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `Column` | 입력 | `DataColumn` | 대상이 되는 DataTable 열(DataColumn 개체). |
| `ColumnIndex` | 입력 | `int` | 대상 열의 인덱스(0부터 시작). |
| 데이터 테이블 <small>`DataTable`</small> | 입력 | `DataTable` | 작업 대상이 되는 DataTable. |
| 열 이름 <small>`ColumnName`</small> | 입력 | `string` | 대상 열의 이름. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 중복 행 제거  <small>`RemoveDuplicateRows`</small>

DataTable에서 중복된 행을 제거합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 데이터 테이블 <small>`DataTable`</small> | 입력 | `DataTable` | 작업 대상이 되는 DataTable. |
| 데이터 테이블 (출력) <small>`OutDataTable`</small> | 출력 | `DataTable` | 추출 결과를 담는 DataTable(출력). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 행 삭제 (데이터 테이블)  <small>`RemoveRowDataTable`</small>

DataTable에서 지정한 행을 삭제합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `Row` | 입력 | `DataRow` | 대상 DataRow 개체. |
| `RowIndex` | 입력 | `int` | 대상 행의 인덱스(0부터 시작). |
| 데이터 테이블 <small>`DataTable`</small> | 입력 | `DataTable` | 작업 대상이 되는 DataTable. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 행 항목 가져오기  <small>`GetRowItem`</small>

DataTable 행에서 지정한 열의 값을 가져옵니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `Column` | 입력 | `DataColumn` | 대상이 되는 DataTable 열(DataColumn 개체). |
| `ColumnIndex` | 입력 | `int` | 대상 열의 인덱스(0부터 시작). |
| 열 이름 <small>`ColumnName`</small> | 입력 | `string` | 대상 열의 이름. |
| `Row` | 입력 | `DataRow` | 대상 DataRow 개체. |
| 결과 <small>`Result`</small> | 출력 | `string` | 액티비티 실행 결과(출력). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## CSV 읽기  <small>`ReadCsv`</small>

CSV 파일을 DataTable 로 읽습니다. 쉼표·세미콜론·탭 같은 **구분자**와 **인코딩**(UTF-8·CP949)은 비워 두면 파일을 보고 정합니다. 큰따옴표로 감싼 값 안의 쉼표·줄바꿈을 그대로 읽고, **모든 열을 텍스트로** 읽어 `007` 이나 전화번호가 숫자로 바뀌지 않습니다. UiPath Read CSV 에 해당합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 파일 경로 <small>`FilePath`</small> | 입력 | `string` | 읽을 CSV 파일(.csv · .tsv · .txt). 상대 경로는 프로젝트 폴더 기준입니다. 카드의 […] 버튼으로 고를 수 있습니다. Excel 로 열어 둔 파일도 읽습니다. |
| 인코딩 <small>`Encoding`</small> | 입력 | `string` | 인코딩 이름(`utf-8`, `euc-kr` …)이나 코드 페이지 번호(`949`). **비우면 자동**입니다 — [인코딩](#csv-encoding). 한글이 깨질 때만 적으세요. |
| 구분자 <small>`Delimiter`</small> | 설정 | `CsvDelimiter` | 칸을 나누는 글자. **자동**(기본 — [파일을 보고 판단](#csv-delimiter)) · **쉼표 (,)** · **세미콜론 (;)** · **탭** · **세로선 (\|)** · **캐럿 (^)**. |
| 첫 줄 머리글 <small>`HasHeaders`</small> | 설정 | `bool` | 첫 줄을 열 이름으로 쓸지 여부(기본 true). 끄면 첫 줄부터 데이터이고 열 이름은 `Column1`, `Column2` … 입니다. |
| 따옴표 무시 <small>`IgnoreQuotes`</small> | 설정 | `bool` | 큰따옴표를 감싸는 표시로 보지 않고 글자 그대로 읽을지 여부(기본 false). 따옴표의 짝이 맞지 않아 "큰따옴표가 닫히지 않았습니다" 오류가 나는 파일에만 켭니다. |
| 데이터 테이블 <small>`DataTable`</small> | 출력 | `DataTable` | 읽은 표(출력). 카드의 **결과 표** 칸에 DataTable 변수를 적습니다. 모든 열이 텍스트(String)입니다. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

!!! note "제공 버전"
    CSV 읽기와, CSV 쓰기의 옵션(구분자·이어 쓰기·인코딩 등)은 NeoRPA 2.2.4 다음 버전부터 제공됩니다. 툴박스 **DataTable** 에 **CSV 읽기** 가 보이지 않으면 도움말 탭 → **버전 관리** 에서 새 버전을 확인하세요.

#### 읽는 규칙 { #csv-read }

| 파일에 적힌 모습 | 읽은 값 |
|---|---|
| `"김, 철수",서울` | `김, 철수` · `서울` — 큰따옴표 안의 구분자는 값의 일부입니다 |
| `"그는 ""네"" 라고 했다"` | `그는 "네" 라고 했다` — 값 안의 큰따옴표는 두 번 적혀 있습니다 |
| `"첫 줄` ⏎ `둘째 줄",1` | 줄바꿈이 든 값 하나 · `1` |
| `27" 모니터,2` | `27" 모니터` · `2` — 칸 중간의 큰따옴표는 글자입니다 |
| `007,01012345678` | `007` · `01012345678` — 텍스트 그대로 |
| 빈 줄 | 건너뜁니다 |
| 다른 줄보다 칸이 적은 줄 | 모자란 칸은 빈 텍스트 |
| 다른 줄보다 칸이 많은 줄 | 열을 더 만듭니다(`Column4` …) |
| 이름이 빈 열 · 같은 이름이 또 나온 열 | `Column3` · `이름_2` |

- 모든 값이 텍스트이므로 계산하려면 식에서 바꿉니다: `CInt(row("수량"))`, `CDec(row("단가"))`. 날짜는 [텍스트를 날짜로](text.md) 액티비티를 쓰세요.
- 빈 칸은 Nothing 이 아니라 빈 텍스트(`""`)입니다. `row("메모").ToString()` 이나 `CStr(row("메모"))` 가 실패하지 않습니다.
- 열 이름의 앞뒤 공백은 뗍니다. 값의 공백은 그대로 둡니다.
- 열린 큰따옴표가 파일 끝까지 닫히지 않으면 **오류로 멈춥니다**(몇 번째 줄에서 열렸는지 알려 줍니다). 나머지 파일이 통째로 한 칸에 들어간 표를 조용히 넘기지 않습니다.

#### 구분자 자동 판단 { #csv-delimiter }

**자동**은 파일 앞부분(50줄까지)을 쉼표·탭·세미콜론·세로선·캐럿으로 각각 나눠 보고, **모든 줄이 같은 칸 수로 나뉘는 것**을 고릅니다. 글자 수만 세지 않으므로 소수점 쉼표(`1,5;2,5`)나 주소 속의 쉼표에 끌려가지 않습니다. 큰따옴표 안의 구분자는 세지 않습니다. 두 칸 이상으로 고르게 나뉘는 것이 없으면 쉼표로 읽습니다.

쉼표가 아닌 구분자를 골랐을 때는 로그에 `파일을 보고 정했습니다: 구분자 세미콜론(;)` 처럼 남깁니다. 한 칸짜리 표처럼 판단할 근거가 없는 파일이거나 결과가 기대와 다르면 구분자를 직접 고르세요.

#### 인코딩 { #csv-encoding }

**인코딩**을 비워 두면 이 순서로 정합니다.

1. 파일 머리에 표시(BOM)가 있으면 그 인코딩 — Excel 의 "CSV UTF-8", NeoRPA 의 CSV 쓰기가 만든 파일.
2. 표시가 없어도 **파일 전체가** UTF-8 로 읽히면 UTF-8 — 웹 시스템이 내려 주는 파일 대부분.
3. 아니면 Windows 시스템 코드 페이지(한국어 Windows 는 CP949) — Excel 의 "CSV (쉼표로 분리)", 오래된 사내 시스템. 이때는 로그에 어떤 인코딩으로 읽었는지 남깁니다.

영문 Windows 에서 한국어 CP949 파일을 읽는 것처럼 3번이 맞지 않는 환경에서는 **인코딩**에 `euc-kr`(또는 `949`)을 적으세요.

## CSV 쓰기  <small>`DTToCSV`</small>

DataTable 을 CSV 파일로 씁니다. 옵션을 건드리지 않으면 쉼표로 나눈 UTF-8(BOM) 파일이라 Excel 에서 한글이 그대로 열립니다. 구분자·인코딩을 바꾸거나 있는 파일 끝에 **이어 쓸** 수 있습니다. 구분자·줄바꿈·큰따옴표가 든 값은 큰따옴표로 감싸 칸이 밀리지 않습니다. UiPath Write CSV · Append To CSV 에 해당합니다. (예전 이름: 데이터 테이블 → CSV 변환)

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 파일 경로 <small>`filepath`</small> | 입력 | `string` | 쓸 CSV 파일 경로. 상대 경로는 프로젝트 폴더 기준입니다. 카드의 […] 버튼으로 저장 대화상자를 열 수 있습니다. **폴더는 미리 있어야 합니다**(없으면 오류로 멈춥니다 — `폴더 생성` 을 앞에 두세요). |
| 데이터 테이블 <small>`DataTable`</small> | 입력 | `DataTable` | 쓸 DataTable. |
| 인코딩 <small>`Encoding`</small> | 입력 | `string` | 인코딩 이름이나 코드 페이지 번호. **비우면** 새 파일은 UTF-8(BOM), 이어 쓸 때는 있는 파일의 인코딩입니다. `utf-8`(BOM 없음) · `utf-8-bom` · `euc-kr`(= `949`) 등. |
| 구분자 <small>`Delimiter`</small> | 설정 | `CsvDelimiter` | 칸을 나누는 글자. **자동**(기본 — 쉼표. 이어 쓸 때는 있는 파일의 구분자) · **쉼표 (,)** · **세미콜론 (;)** · **탭** · **세로선 (\|)** · **캐럿 (^)**. |
| 쓰기 방식 <small>`WriteMode`</small> | 설정 | `CsvWriteMode` | **덮어쓰기**(기본 — 파일을 새로 씁니다) · **이어 쓰기**(있는 파일 끝에 행을 덧붙입니다. 파일이 없으면 만듭니다) — [이어 쓰기](#csv-append). |
| 머리글 쓰기 <small>`AddHeaders`</small> | 설정 | `bool` | 첫 줄에 열 이름을 쓸지 여부(기본 true). 이어 쓸 때는 파일이 없거나 비어 있을 때만 씁니다. |
| 모두 따옴표 <small>`QuoteAll`</small> | 설정 | `bool` | 모든 값을 큰따옴표로 감쌀지 여부(기본 false — 구분자·큰따옴표·줄바꿈이 든 값만 감쌉니다). 받는 쪽 시스템이 모든 값에 따옴표를 요구할 때 켭니다. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

#### 이어 쓰기 { #csv-append }

실행할 때마다 결과를 한 파일에 쌓을 때 **쓰기 방식**을 **이어 쓰기**로 둡니다.

| 파일의 상태 | 하는 일 |
|---|---|
| 없음 · 비어 있음 | 새로 씁니다(머리글 쓰기가 켜져 있으면 머리글부터) |
| 내용이 있음 | 머리글 없이 **행만** 끝에 덧붙입니다 |
| 마지막 줄이 줄바꿈 없이 끝남 | 줄바꿈을 먼저 쓰고 덧붙입니다(두 행이 한 줄로 붙지 않게) |

- 구분자와 인코딩을 **자동**·비움으로 두면 **있는 파일에 맞춥니다**(세미콜론 파일에는 세미콜론으로, CP949 파일에는 CP949 로).
- 열의 개수와 순서는 맞춰 보지 않습니다. 같은 모양의 표를 이어 쓰세요.
- 덮어쓰기는 임시 파일에 다 쓴 뒤 바꿔 넣으므로 도중에 실패해도 있던 파일이 반쪽이 되지 않습니다. 이어 쓰기는 파일에 바로 덧붙입니다.
- Excel 로 열어 둔 파일에는 쓸 수 없습니다(오류로 멈춥니다). 먼저 닫으세요.

!!! tip "Excel 에서 열 때"
    기본값(쉼표 + UTF-8 BOM)으로 쓴 파일은 더블클릭하면 한글이 깨지지 않고 열립니다. `007` 같은 값은 Excel 이 열면서 숫자 `7` 로 **보여 줍니다**(파일에는 `007` 그대로 있습니다) — 그대로 보려면 Excel 의 데이터 → 텍스트/CSV 가져오기에서 열 형식을 텍스트로 정하세요.

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
| 데이터 테이블 <small>`DataTable`</small> | 입력 | `DataTable` | 작업 대상이 되는 DataTable. |
| `OutputDataTable` | 출력 | `DataTable` | 필터링 결과를 담는 DataTable(출력). |
| `FilterRowsMode` | 설정 | `FilterMode` | 조건에 맞는 행을 남길지 제거할지 지정하는 모드. |
| `SelectColumnsMode` | 설정 | `FilterMode` | 지정한 열을 남길지 제거할지 지정하는 모드. |
| `Filters` | 설정 | `List<FilterOperationArgument>` | 적용할 행 필터 조건 목록. |
| `SelectColumns` | 설정 | `List<InArgument<object>>` | 결과에 포함할 열 목록. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
