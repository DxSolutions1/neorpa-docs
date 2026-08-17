<!-- 이 파일은 scripts/gen_activity_stubs.py 로 자동 생성됩니다.
     직접 편집하지 말고 website/data/activities.yaml 을 고친 뒤 스크립트를 다시 실행하세요. -->


# Excel WorkBook

Excel 워크북을 COM으로 직접 조작합니다(스코프 없이 파일 단위).

> 이 카테고리에는 28개의 액티비티가 있습니다. 각 액티비티의 **속성** 표는 소스에서 자동 추출되며(상속 포함), 표시명·설명은 리소스/설명 데이터에서 해석됩니다.

## 엑셀 VBA 실행  <small>`ExcelInvokeVBA`</small>

워크북을 직접 열어 외부 VBA 파일을 불러온 뒤 지정한 함수를 실행합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `autoSave` | 설정 | `bool` | 작업 후 워크북을 자동 저장할지 여부. |
| `ExcelFilePath` | 입력 | `string` | 대상 엑셀 파일의 경로. |
| `VBAfilePath` | 입력 | `string` | 가져올 VBA 매크로 파일의 경로. |
| `FunctionName` | 입력 | `string` | 실행할 VBA 함수/매크로 이름. |
| `Parameters` | 입력 | `object[]` | VBA 함수에 전달할 인수 배열. |
| `Output` | 출력 | `object` | 실행 결과 개체(출력). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 쓰기  <small>`ExcelWrite`</small>

워크북 파일을 직접 열어 지정한 셀/범위에 값을 씁니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `autoSave` | 설정 | `bool` | 작업 후 워크북을 자동 저장할지 여부. |
| `filePath` | 입력 | `string` | 대상 엑셀 파일의 경로. |
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `range` | 입력 | `string` | 대상 셀 범위(예: A1:C10). |
| `value` | 입력 | `string` | 기록하거나 조회할 값. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 필터 적용  <small>`ExcelFilter`</small>

워크북을 직접 열어 지정한 범위에 필터를 적용합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `autoSave` | 설정 | `bool` | 작업 후 워크북을 자동 저장할지 여부. |
| `filePath` | 입력 | `string` | 대상 엑셀 파일의 경로. |
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `columnName` | 입력 | `string` | 대상 열 이름. |
| `tableName` | 입력 | `string` | 대상 테이블 이름. |
| `filterOption` | 입력 | `string[]` | 적용할 필터 조건 목록. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 범위 복사  <small>`CopyRange`</small>

워크북에서 지정한 범위를 다른 위치로 복사합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `autoSave` | 설정 | `bool` | 작업 후 워크북을 자동 저장할지 여부. |
| `filePath` | 입력 | `string` | 대상 엑셀 파일의 경로. |
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `range` | 입력 | `string` | 대상 셀 범위(예: A1:C10). |
| `CopyValue` | 설정 | `bool` | 셀 값을 복사할지 여부. |
| `CopyNumberFormat` | 설정 | `bool` | 숫자 표시 형식을 함께 복사할지 여부. |
| `CopyCellFormat` | 설정 | `bool` | 셀 서식을 함께 복사할지 여부. |
| `CopyFormula` | 설정 | `bool` | 수식을 함께 복사할지 여부. |
| `CopyAll` | 설정 | `bool` | 원본 범위의 모든 항목(값·서식·수식)을 복사할지 여부. |
| `DestinationCell` | 입력 | `string` | 붙여넣을 대상 셀 위치(예: A1). |
| `DestinationSheet` | 입력 | `string` | 대상 시트 이름. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 범위 삭제  <small>`DeleteRange`</small>

워크북에서 지정한 범위를 삭제합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `autoSave` | 설정 | `bool` | 작업 후 워크북을 자동 저장할지 여부. |
| `shiftCells` | 설정 | `bool` | 셀을 삭제한 뒤 남은 셀을 이동시킬지 여부. |
| `shiftUp` | 설정 | `bool` | 셀을 삭제한 뒤 남은 셀을 위로 이동시킬지 여부. |
| `shiftLeft` | 설정 | `bool` | 셀을 삭제한 뒤 남은 셀을 왼쪽으로 이동시킬지 여부. |
| `EntireRow` | 설정 | `bool` | 행 전체를 대상으로 삭제할지 여부. |
| `EntireColumn` | 설정 | `bool` | 열 전체를 대상으로 삭제할지 여부. |
| `filePath` | 입력 | `string` | 대상 엑셀 파일의 경로. |
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `range` | 입력 | `string` | 대상 셀 범위(예: A1:C10). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 범위 색상 설정  <small>`SetRangeColor`</small>

워크북에서 지정한 범위의 배경 색상을 설정합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `autoSave` | 설정 | `bool` | 작업 후 워크북을 자동 저장할지 여부. |
| `filePath` | 입력 | `string` | 대상 엑셀 파일의 경로. |
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `range` | 입력 | `string` | 대상 셀 범위(예: A1:C10). |
| `color` | 입력 | `string` | 셀 색상. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 범위 선택  <small>`SelectRange`</small>

워크북에서 지정한 범위를 선택합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `filePath` | 입력 | `string` | 대상 엑셀 파일의 경로. |
| `autoSave` | 설정 | `bool` | 작업 후 워크북을 자동 저장할지 여부. |
| `range` | 입력 | `string` | 대상 셀 범위(예: A1:C10). |
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 범위 읽기  <small>`ReadRange`</small>

워크북 파일을 직접 열어 지정한 범위를 읽어 DataTable로 반환합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `autoSave` | 설정 | `bool` | 작업 후 워크북을 자동 저장할지 여부. |
| `PreserveFormat` | 설정 | `bool` | 셀의 표시 서식을 유지한 채 값을 읽을지 여부. |
| `AddHeader` | 설정 | `bool` | 첫 행을 열 머리글로 포함할지 여부. |
| `useFilter` | 설정 | `bool` | 읽을 때 적용된 필터를 반영할지 여부. |
| `filePath` | 입력 | `string` | 대상 엑셀 파일의 경로. |
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `range` | 입력 | `string` | 대상 셀 범위(예: A1:C10). |
| `output` | 출력 | `DataTable` | 실행 결과를 담을 변수(출력). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 범위 추가  <small>`AppendRange`</small>

워크북 시트의 기존 데이터 끝에 DataTable 내용을 이어서 추가합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `autoSave` | 설정 | `bool` | 작업 후 워크북을 자동 저장할지 여부. |
| `filePath` | 입력 | `string` | 대상 엑셀 파일의 경로. |
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `dataTable` | 입력 | `DataTable` | 작업 대상이 되는 DataTable. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 선택 범위 가져오기  <small>`GetSelectedRange`</small>

워크북에서 현재 선택된 범위의 주소를 가져옵니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `filePath` | 입력 | `string` | 대상 엑셀 파일의 경로. |
| `range` | 출력 | `string` | 대상 셀 범위(예: A1:C10). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 셀 색상 가져오기  <small>`GetCellColor`</small>

워크북에서 지정한 셀의 배경 색상을 가져옵니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `filePath` | 입력 | `string` | 대상 엑셀 파일의 경로. |
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `cell` | 입력 | `string` | 대상 셀 위치(예: A1). |
| `color` | 출력 | `string` | 셀 색상. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 셀 수식 읽기  <small>`ReadCellFormula`</small>

워크북에서 지정한 셀에 들어 있는 수식을 읽어 반환합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `autoSave` | 설정 | `bool` | 작업 후 워크북을 자동 저장할지 여부. |
| `filePath` | 입력 | `string` | 대상 엑셀 파일의 경로. |
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `cell` | 입력 | `string` | 대상 셀 위치(예: A1). |
| `output` | 출력 | `string` | 실행 결과를 담을 변수(출력). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 셀 읽기  <small>`ReadCell`</small>

워크북에서 지정한 셀의 값을 읽어 반환합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `autoSave` | 설정 | `bool` | 작업 후 워크북을 자동 저장할지 여부. |
| `filePath` | 입력 | `string` | 대상 엑셀 파일의 경로. |
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `cell` | 입력 | `string` | 대상 셀 위치(예: A1). |
| `output` | 출력 | `string` | 실행 결과를 담을 변수(출력). |

## 엑셀 시트 복사  <small>`CopySheet`</small>

워크북 안에서 시트를 복사합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `autoSave` | 설정 | `bool` | 작업 후 워크북을 자동 저장할지 여부. |
| `filePath` | 입력 | `string` | 대상 엑셀 파일의 경로. |
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `DestinationSheet` | 입력 | `string` | 대상 시트 이름. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 열 삽입/삭제  <small>`InsertDeleteCol`</small>

워크북 시트에 열을 삽입하거나 삭제합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `autoSave` | 설정 | `bool` | 작업 후 워크북을 자동 저장할지 여부. |
| `columnNo` | 입력 | `int` | 대상 열 번호(또는 열 문자). |
| `position` | 입력 | `int` | 삽입하거나 읽을 대상 위치(행/열 번호). |
| `filePath` | 입력 | `string` | 대상 엑셀 파일의 경로. |
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `Mode` | 입력 | `string` | 수행할 동작의 모드(삽입/삭제, 읽기 방향 등). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 열 읽기  <small>`ReadColumn`</small>

워크북에서 지정한 열 전체를 읽어 반환합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `autoSave` | 설정 | `bool` | 작업 후 워크북을 자동 저장할지 여부. |
| `columnNo` | 입력 | `string` | 대상 열 번호(또는 열 문자). |
| `position` | 입력 | `string` | 삽입하거나 읽을 대상 위치(행/열 번호). |
| `filePath` | 입력 | `string` | 대상 엑셀 파일의 경로. |
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `Mode` | 입력 | `string` | 수행할 동작의 모드(삽입/삭제, 읽기 방향 등). |
| `result` | 출력 | `string` | 읽어온 결과(출력). |

## 엑셀 워크북 닫기  <small>`CloseWorkbook`</small>

열려 있는 워크북을 닫습니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `filePath` | 입력 | `string` | 대상 엑셀 파일의 경로. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 워크북 시트 가져오기  <small>`GetWorkbookSheet`</small>

워크북에서 지정한 이름의 시트를 가져옵니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `autoSave` | 설정 | `bool` | 작업 후 워크북을 자동 저장할지 여부. |
| `filePath` | 입력 | `string` | 대상 엑셀 파일의 경로. |
| `index` | 입력 | `string` | 대상 시트의 인덱스(번호). |
| `Sheet` | 출력 | `string` | 조회된 시트 이름(출력). |

## 엑셀 워크북 시트 목록 가져오기  <small>`GetWorkbookSheets`</small>

워크북에 있는 모든 시트 이름 목록을 가져옵니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `filePath` | 입력 | `string` | 대상 엑셀 파일의 경로. |
| `sheets` | 출력 | `List<string>` | 워크북에 있는 시트 이름 목록(출력). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 범위 자동 채우기  <small>`AutoFillRange`</small>

원본 범위를 기준으로 대상 범위를 자동 채우기(수식·연속 값)합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `autoSave` | 설정 | `bool` | 작업 후 워크북을 자동 저장할지 여부. |
| `FillRange` | 입력 | `string` | 자동 채우기를 확장할 대상 범위(예: A1:A10). |
| `filePath` | 입력 | `string` | 대상 엑셀 파일의 경로. |
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `range` | 입력 | `string` | 대상 셀 범위(예: A1:C10). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 저장  <small>`Save`</small>

열려 있는 워크북을 파일로 저장합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `filePath` | 입력 | `string` | 대상 엑셀 파일의 경로. |
| `saveName` | 입력 | `string` | 저장할 파일 이름 또는 경로. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 정렬  <small>`Sort`</small>

워크북의 범위를 지정한 기준으로 정렬합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `autoSave` | 설정 | `bool` | 작업 후 워크북을 자동 저장할지 여부. |
| `filePath` | 입력 | `string` | 대상 엑셀 파일의 경로. |
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `columnName` | 입력 | `string` | 대상 열 이름. |
| `tableName` | 입력 | `string` | 대상 테이블 이름. |
| `order` | 입력 | `string` | 정렬 순서(오름차순/내림차순). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 조회  <small>`LookUp`</small>

워크북의 지정한 범위에서 특정 값을 찾아 그 위치(셀 주소)를 반환합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `autoSave` | 설정 | `bool` | 작업 후 워크북을 자동 저장할지 여부. |
| `filePath` | 입력 | `string` | 대상 엑셀 파일의 경로. |
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `range` | 입력 | `string` | 대상 셀 범위(예: A1:C10). |
| `value` | 입력 | `string` | 기록하거나 조회할 값. |
| `output` | 출력 | `string` | 실행 결과를 담을 변수(출력). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 범위 중복 제거  <small>`RemoveDuplicatesRange`</small>

워크북 범위에서 중복된 행을 제거합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `autoSave` | 설정 | `bool` | 작업 후 워크북을 자동 저장할지 여부. |
| `filePath` | 입력 | `string` | 대상 엑셀 파일의 경로. |
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `range` | 입력 | `string` | 대상 셀 범위(예: A1:C10). |

## 엑셀 테이블 범위 가져오기  <small>`GetTableRange`</small>

워크북에서 지정한 표(테이블)가 차지하는 범위 주소를 가져옵니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `filePath` | 입력 | `string` | 대상 엑셀 파일의 경로. |
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `table` | 입력 | `string` | 대상 테이블(DataTable 또는 테이블 이름). |
| `range` | 출력 | `string` | 대상 셀 범위(예: A1:C10). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 피벗 테이블 생성  <small>`CreatePivotTable`</small>

워크북에 피벗 테이블을 생성합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `autoSave` | 설정 | `bool` | 작업 후 워크북을 자동 저장할지 여부. |
| `filePath` | 입력 | `string` | 대상 엑셀 파일의 경로. |
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `sourceTableName` | 입력 | `string` | 피벗의 원본이 되는 테이블 이름. |
| `tableName` | 입력 | `string` | 대상 테이블 이름. |
| `range` | 입력 | `string` | 대상 셀 범위(예: A1:C10). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 행 삽입/삭제  <small>`InsertDeleteRow`</small>

워크북 시트에 행을 삽입하거나 삭제합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `autoSave` | 설정 | `bool` | 작업 후 워크북을 자동 저장할지 여부. |
| `filePath` | 입력 | `string` | 대상 엑셀 파일의 경로. |
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `Mode` | 입력 | `string` | 수행할 동작의 모드(삽입/삭제, 읽기 방향 등). |
| `rowNo` | 입력 | `int` | 대상 행 번호. |
| `position` | 입력 | `int` | 삽입하거나 읽을 대상 위치(행/열 번호). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 행 읽기  <small>`ReadRow`</small>

워크북에서 지정한 행 전체를 읽어 반환합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `autoSave` | 설정 | `bool` | 작업 후 워크북을 자동 저장할지 여부. |
| `rowNo` | 입력 | `string` | 대상 행 번호. |
| `position` | 입력 | `string` | 삽입하거나 읽을 대상 위치(행/열 번호). |
| `filePath` | 입력 | `string` | 대상 엑셀 파일의 경로. |
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `Mode` | 입력 | `string` | 수행할 동작의 모드(삽입/삭제, 읽기 방향 등). |
| `result` | 출력 | `string` | 읽어온 결과(출력). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

