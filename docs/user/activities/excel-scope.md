<!-- 이 파일은 scripts/gen_activities.py 로 자동 생성됩니다.
     직접 편집하지 말고 data/activities.yaml 을 고친 뒤 `python scripts/gen_activities.py --write` 를 다시 실행하세요. -->


# Excel Scope

Excel Scope 안에서 워크북/시트를 열어 두고 자식 액티비티가 그 컨텍스트를 공유합니다. 여러 작업을 한 세션으로 묶을 때 사용.

> 이 카테고리에는 33개의 액티비티가 있습니다. 각 액티비티의 **속성** 표는 소스에서 자동 추출되며(상속 포함), 표시명·설명은 리소스/설명 데이터에서 해석됩니다.

## 엑셀 VBA 실행  <small>`ExcelInvokeVBA`</small>

Excel Scope 안에서 외부 VBA 파일을 불러와 지정한 함수를 실행합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `VBAfilePath` | 입력 | `string` | 가져올 VBA 매크로 파일의 경로. |
| `FunctionName` | 입력 | `string` | 실행할 VBA 함수/매크로 이름. |
| `Parameters` | 입력 | `object[]` | VBA 함수에 전달할 인수 배열. |
| `Output` | 출력 | `object` | 실행 결과 개체(출력). |
| `RestoreExcelUiState` | 설정 | `bool` | VBA 실행 전 Excel 애플리케이션의 UI 상태(화면 갱신·경고 표시·이벤트·계산 모드·표시 여부 등)를 기억해 두고 실행 후 되돌릴지 여부(기본 true). |
| Accessibility Recovery Timeout (ms) <small>`AccessibilityRecoveryTimeoutMs`</small> | 설정 | `int` | VBA 실행 후 Excel이 다시 응답(Ready) 상태가 될 때까지 기다릴 최대 시간(밀리초, 기본 5000). |
| `RestartOwnedExcelOnAccessibilityFailure` | 설정 | `bool` | 대기 시간 안에 Excel이 응답하지 않으면, 이 스코프가 직접 연 Excel인 경우 Excel을 다시 시작해 복구할지 여부(기본 true). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 스코프  <small>`ExcelScope`</small>

워크북/시트를 열어 두고 본문의 자식 액티비티가 그 Excel 세션을 공유하도록 하는 컨테이너입니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `filepath` | 입력 | `string` | 대상 파일의 경로. |
| Workbook <small>`InputWorkbook`</small> | 입력 | `Workbook` | 작업 대상으로 사용할, 이미 열려 있는 워크북 개체. |
| `CreateFile` | 설정 | `bool` | 대상 파일이 없으면 새로 만들지 여부. |
| `Visible` | 설정 | `bool` | 엑셀 애플리케이션 창을 화면에 표시할지 여부. |
| `Save` | 설정 | `bool` | 스코프를 마칠 때 워크북을 저장할지 여부. |
| `ReadOnly` | 설정 | `bool` | 워크북을 읽기 전용으로 열지 여부. |
| `OpenMode` | 설정 | `ExcelOpenMode` | 워크북을 여는 방식(읽기/쓰기 등). |
| `Macro` | 설정 | `bool` | 매크로가 포함된 워크북으로 처리할지 여부. |
| `InstanceCachePeriod` | 입력 | `int` | 엑셀 인스턴스를 캐시로 유지할 시간(밀리초). |
| `Workbook` | 출력 | `Workbook` | 대상 워크북 개체(입력/출력). |
| `EditPassword` | 입력 | `string` | 엑셀 파일의 편집(쓰기) 암호. |
| `WorkbookPath` | 입력 | `string` | 열 워크북 파일의 경로. |
| `Password` | 입력 | `string` | 접근에 사용할 암호(파일 또는 메일 계정). |

## 엑셀 쓰기  <small>`ExcelWrite`</small>

Excel Scope 안에서 지정한 셀/범위에 값을 씁니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `range` | 입력 | `string` | 대상 셀 범위(예: A1:C10). |
| `value` | 입력 | `string` | 기록하거나 조회할 값. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 파일 열기  <small>`ExcelOpen`</small>

Excel Scope 안에서 워크북 파일을 엽니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `filePath` | 입력 | `string` | 대상 엑셀 파일의 경로. |

## 엑셀 필터 적용  <small>`ExcelFilter`</small>

Excel Scope 안에서 지정한 범위에 필터를 적용합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `columnName` | 입력 | `string` | 대상 열 이름. |
| `tableName` | 입력 | `string` | 대상 테이블 이름. |
| `filterOption` | 입력 | `string[]` | 적용할 필터 조건 목록. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 매크로 실행  <small>`ExecuteMacro`</small>

Excel Scope 안에서 워크북에 저장된 매크로를 이름으로 실행합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `macroName` | 입력 | `string` | 실행할 매크로 이름. |
| `macroParameters` | 입력 | `IEnumerable<object>` | 매크로에 전달할 인수. |
| `macroOutput` | 출력 | `object` | 매크로 실행 결과(출력). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 범위 복사  <small>`CopyRange`</small>

Excel Scope 안에서 지정한 범위를 다른 위치로 복사합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
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

Excel Scope 안에서 지정한 범위를 삭제합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `shiftCells` | 설정 | `bool` | 셀을 삭제한 뒤 남은 셀을 이동시킬지 여부. |
| `ShiftOption` | 설정 | `ShiftOption` | 셀을 삭제한 뒤 남은 셀을 이동시키는 방식. |
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `range` | 입력 | `string` | 대상 셀 범위(예: A1:C10). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 범위 색상 설정  <small>`SetRangeColor`</small>

Excel Scope 안에서 지정한 범위의 배경 색상을 설정합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `range` | 입력 | `string` | 대상 셀 범위(예: A1:C10). |
| `color` | 입력 | `Color` | 셀 색상. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 범위 선택  <small>`SelectRange`</small>

Excel Scope 안에서 지정한 범위를 선택합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `range` | 입력 | `string` | 대상 셀 범위(예: A1:C10). |
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 범위 쓰기  <small>`WriteRange`</small>

Excel Scope 안에서 DataTable 내용을 지정한 위치부터 범위에 씁니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `AddHeader` | 설정 | `bool` | 첫 행을 열 머리글로 포함할지 여부. |
| `StartingCell` | 입력 | `string` | 작업을 시작할 기준 셀 위치(예: A1). |
| `DataTable` | 입력 | `DataTable` | 작업 대상이 되는 DataTable. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 범위 읽기  <small>`ReadRange`</small>

Excel Scope 안에서 지정한 범위를 읽어 DataTable로 반환합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `PreserveFormat` | 설정 | `bool` | 셀의 표시 서식을 유지한 채 값을 읽을지 여부. |
| `AddHeader` | 설정 | `bool` | 첫 행을 열 머리글로 포함할지 여부. |
| `useFilter` | 설정 | `bool` | 읽을 때 적용된 필터를 반영할지 여부. |
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `range` | 입력 | `string` | 대상 셀 범위(예: A1:C10). |
| `output` | 출력 | `DataTable` | 실행 결과를 담을 변수(출력). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 범위 추가  <small>`AppendRange`</small>

Excel Scope 안에서 기존 데이터 끝에 DataTable 내용을 이어서 추가합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `dataTable` | 입력 | `DataTable` | 작업 대상이 되는 DataTable. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 선택 범위 가져오기  <small>`GetSelectedRange`</small>

Excel Scope 안에서 현재 선택된 범위의 주소를 가져옵니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `range` | 출력 | `string` | 대상 셀 범위(예: A1:C10). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 셀 색상 가져오기  <small>`GetCellColor`</small>

Excel Scope 안에서 지정한 셀의 배경 색상을 가져옵니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| cell <small>`range`</small> | 입력 | `string` | 대상 셀 범위(예: A1:C10). |
| `color` | 출력 | `Color` | 셀 색상. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## Read Cell  <small>`ReadCell<T>`</small>

Excel Scope 안에서 지정한 셀의 값을 읽어 반환합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| Cell <small>`range`</small> | 입력 | `string` | 대상 셀 범위(예: A1:C10). |
| `output` | 출력 | `T` | 실행 결과를 담을 변수(출력). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 시트 복사  <small>`CopySheet`</small>

Excel Scope 안에서 시트를 복사합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `DestinationSheet` | 입력 | `string` | 대상 시트 이름. |
| `DestinationFilePath` | 입력 | `string` | 복사 대상 파일의 경로. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 열 삽입/삭제  <small>`InsertDeleteCol`</small>

Excel Scope 안에서 열을 삽입하거나 삭제합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `columnNo` | 입력 | `int` | 대상 열 번호(또는 열 문자). |
| `position` | 입력 | `int` | 삽입하거나 읽을 대상 위치(행/열 번호). |
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `Mode` | 설정 | `ChangeMode` | 수행할 동작의 모드(삽입/삭제, 읽기 방향 등). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 워크북 닫기  <small>`CloseWorkbook`</small>

Excel Scope 안에서 워크북을 닫습니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `Workbook` | 입력 | `Workbook` | 대상 워크북 개체(입력/출력). |
| `SaveChanges` | 설정 | `bool` | 워크북을 닫을 때 변경 내용을 저장할지 여부. |
| `QuitApplicationIfOwned` | 설정 | `bool` | 이 워크북이 직접 연 엑셀이라면 닫을 때 애플리케이션도 함께 종료할지 여부. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 워크북 시트 가져오기  <small>`GetWorkbookSheet`</small>

Excel Scope 안에서 지정한 이름의 시트를 가져옵니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `index` | 입력 | `int` | 대상 시트의 인덱스(번호). |
| `sheet` | 출력 | `string` | 조회된 시트 이름(출력). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 워크북 시트 목록 가져오기  <small>`GetWorkbookSheets`</small>

Excel Scope 안에서 모든 시트 이름 목록을 가져옵니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `sheets` | 출력 | `List<string>` | 워크북에 있는 시트 이름 목록(출력). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 범위 자동 채우기  <small>`AutoFillRange`</small>

Excel Scope 안에서 원본 범위를 기준으로 대상 범위를 자동 채우기합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `FillRange` | 입력 | `string` | 자동 채우기를 확장할 대상 범위(예: A1:A10). |
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `range` | 입력 | `string` | 대상 셀 범위(예: A1:C10). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 저장  <small>`Save`</small>

Excel Scope 안에서 워크북을 저장합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `saveName` | 입력 | `string` | 저장할 파일 이름 또는 경로. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 정렬  <small>`Sort`</small>

Excel Scope 안에서 범위를 지정한 기준으로 정렬합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `columnName` | 입력 | `string` | 대상 열 이름. |
| `tableName` | 입력 | `string` | 대상 테이블 이름. |
| `order` | 설정 | `OrderType` | 정렬 순서(오름차순/내림차순). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 조회  <small>`LookUp`</small>

Excel Scope 안에서 지정한 범위에서 특정 값을 찾아 그 위치(셀 주소)를 반환합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `range` | 입력 | `string` | 대상 셀 범위(예: A1:C10). |
| `value` | 입력 | `string` | 기록하거나 조회할 값. |
| 검색 조건 <small>`MatchMode`</small> | 설정 | `LookupMatchMode` | 값을 조회할 때 일치시키는 방식(정확히 일치, 부분 일치 등). |
| `output` | 출력 | `string` | 실행 결과를 담을 변수(출력). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 범위 중복 제거  <small>`RemoveDuplicatesRange`</small>

Excel Scope 안에서 범위의 중복된 행을 제거합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `range` | 입력 | `string` | 대상 셀 범위(예: A1:C10). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 컬럼 삭제  <small>`DeleteColumn`</small>

Excel Scope 안에서 지정한 열을 삭제합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `columnName` | 입력 | `string` | 대상 열 이름. |
| `tableName` | 입력 | `string` | 대상 테이블 이름. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 열 삽입  <small>`InsertColumn`</small>

Excel Scope 안에서 지정한 위치에 열을 삽입합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `position` | 입력 | `int` | 삽입하거나 읽을 대상 위치(행/열 번호). |
| `columnName` | 입력 | `string` | 대상 열 이름. |
| `tableName` | 입력 | `string` | 대상 테이블 이름. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 테이블 범위 가져오기  <small>`GetTableRange`</small>

Excel Scope 안에서 지정한 표(테이블)가 차지하는 범위 주소를 가져옵니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `IsPivot` | 설정 | `bool` | 대상 테이블이 피벗 테이블인지 여부. |
| `table` | 입력 | `string` | 대상 테이블(DataTable 또는 테이블 이름). |
| `range` | 출력 | `string` | 대상 셀 범위(예: A1:C10). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 테이블 생성  <small>`CreateTable`</small>

Excel Scope 안에서 지정한 범위를 표(테이블)로 만듭니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `tableName` | 입력 | `string` | 대상 테이블 이름. |
| `range` | 입력 | `string` | 대상 셀 범위(예: A1:C10). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 피벗 테이블 생성  <small>`CreatePivotTable`</small>

Excel Scope 안에서 피벗 테이블을 생성합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `sourceTableName` | 입력 | `string` | 피벗의 원본이 되는 테이블 이름. |
| `tableName` | 입력 | `string` | 대상 테이블 이름. |
| `range` | 입력 | `string` | 대상 셀 범위(예: A1:C10). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 행 삽입/삭제  <small>`InsertDeleteRow`</small>

Excel Scope 안에서 행을 삽입하거나 삭제합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `Mode` | 설정 | `ChangeMode` | 수행할 동작의 모드(삽입/삭제, 읽기 방향 등). |
| `rowNo` | 입력 | `int` | 대상 행 번호. |
| `position` | 입력 | `int` | 삽입하거나 읽을 대상 위치(행/열 번호). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## 엑셀 행 읽기  <small>`ReadRow`</small>

Excel Scope 안에서 지정한 행 전체를 읽어 반환합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| `StartingCell` | 입력 | `string` | 작업을 시작할 기준 셀 위치(예: A1). |
| `sheetName` | 입력 | `string` | 대상 시트 이름. |
| `result` | 출력 | `IEnumerable<object>` | 읽어온 결과(출력). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
