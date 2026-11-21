<!-- 이 파일은 scripts/gen_activities.py 로 자동 생성됩니다.
     직접 편집하지 말고 data/activities.yaml 을 고친 뒤 `python scripts/gen_activities.py --write` 를 다시 실행하세요. -->


# PDF (텍스트 읽기 · 페이지 · 합치기)

PDF 에서 텍스트를 읽고, 페이지를 뽑거나 여러 PDF 를 하나로 잇고, 페이지를 그림 파일로 저장합니다. 글자가 없는 스캔본은 글자 인식(OCR)으로 읽습니다. UiPath 의 Read PDF Text · Read PDF With OCR · Get PDF Page Count · Extract PDF Page Range · Join PDF Files · Export PDF Page As Image 에 해당합니다.

> 이 카테고리에는 5개의 액티비티가 있습니다. 각 액티비티의 **속성** 표는 소스에서 자동 추출되며(상속 포함), 표시명·설명은 리소스/설명 데이터에서 해석됩니다.

!!! note "제공 버전"
    PDF 카테고리는 NeoRPA 2.2.4 다음 버전부터 제공됩니다. 툴박스에 **PDF** 가 보이지 않으면 도움말 탭 → **버전 관리** 에서 새 버전을 확인하세요.

!!! tip "어느 것을 쓸까요"
    | 하려는 일 | 액티비티 |
    |---|---|
    | PDF 의 글을 변수로 읽기(스캔본 포함) | `PDF 텍스트 읽기` |
    | 표의 한 줄을 칸으로 나누기 | `PDF 텍스트 읽기`(텍스트 배치 **칸 맞춤**) → [텍스트 나누기·정규식](text.md) |
    | 몇 페이지인지 알기(페이지마다 반복) | `PDF 페이지 수` |
    | 특정 페이지만 떼어 새 PDF 로 | `PDF 페이지 추출` |
    | 여러 PDF 를 하나로 | `PDF 합치기` |
    | 페이지를 그림 파일로(메일 본문·AI 첨부) | `PDF 페이지를 이미지로` |

### 페이지 범위 적는 법 { #pdf-pages }

**페이지** 칸은 세 액티비티(텍스트 읽기·페이지 추출·이미지로)가 같은 규칙으로 읽습니다. 번호는 1부터입니다.

| 적는 값 | 뜻 |
|---|---|
| (비움) · `All` · `전체` | 모든 페이지 |
| `2` | 2페이지만 |
| `1-3, 5` | 1·2·3·5페이지 (`1~3` 도 됩니다) |
| `3-` | 3페이지부터 끝까지 |
| `-3` | 처음부터 3페이지까지 |
| `End` · `Last` · `끝` · `마지막` | 마지막 페이지 (`3-End`) |
| `3, 1, 2` | 적은 순서대로 — 페이지 추출에서는 순서를 바꾼 PDF 가 됩니다 |
| `5-1` | 거꾸로 |

없는 페이지를 적으면(3페이지 PDF 에 `2-9`) 있는 만큼만 주지 않고 **오류로 멈춥니다**. 페이지 수가 바뀌는 문서는 `3-` 이나 `End` 로 적으세요.

### 텍스트 배치 { #pdf-layout }

PDF 안에는 "줄"이 없고 글자마다 자리만 있습니다. **텍스트 배치**(속성 창)로 어떻게 늘어놓을지 고릅니다.

| 배치 | 결과 | 쓰는 곳 |
|---|---|---|
| **줄 단위**(기본) | 같은 높이의 낱말을 한 줄로, 낱말 사이는 빈칸 하나 | 대부분의 문서. 줄마다 처리할 때 |
| **칸 맞춤** | 줄 단위 + 가로 자리를 빈칸으로 맞춤. **떨어진 칸 사이는 빈칸 둘 이상** | 표. 한 줄을 칸으로 나눌 때 |
| **문서 순서** | PDF 에 적힌 순서 그대로 | 2단 편집 문서처럼 단을 따라 읽어야 할 때 |

```
줄 단위:  사과 (부사) 30 1,200 36,000
칸 맞춤:  사과 (부사)              30        1,200      36,000
```

칸 맞춤으로 읽은 줄은 **빈칸 둘 이상**으로 나누면 칸이 됩니다. [텍스트 나누기](text.md)에서 구분 기호를 **직접 입력**으로 두고 빈칸 두 개(`"  "`)를 적은 뒤 **빈 항목 제거**와 **항목 다듬기**를 켜세요. 품목 이름에 빈칸이 있어도(`사과 (부사)`) 한 칸으로 남습니다.

세로로 돌려 넣은 표처럼 **옆으로 누운 글**도 읽는 방향에 맞춰 줄로 세웁니다. 비스듬한 글(워터마크)은 페이지 끝에 한 줄로 붙습니다.

### 스캔본과 OCR { #pdf-ocr }

종이를 스캔한 PDF 에는 글자가 없고 그림만 있습니다. 카드의 **OCR** 콤보가 이럴 때 어떻게 할지 정합니다.

| OCR | 동작 |
|---|---|
| **스캔 쪽만**(기본) | 글자가 든 페이지는 그대로 읽고, 글자가 하나도 없는 페이지만 그림으로 그려 글자 인식으로 읽습니다. 글자 페이지와 스캔 페이지가 섞인 PDF 도 한 번에 읽힙니다 |
| **안 함** | 글자 인식을 쓰지 않습니다. 스캔 페이지는 빈 텍스트가 되고 출력 패널에 경고가 남습니다 |
| **모든 쪽** | 모든 페이지를 글자 인식으로 읽습니다. 글자가 깨져 나오는 PDF(글꼴 정보가 잘못된 것)에 씁니다 |

- 어느 페이지를 OCR 로 읽었는지는 출력 패널에 한 줄로 남습니다(`글자가 없는 2개 페이지를 OCR 로 읽었습니다: 3, 4`).
- 글자 인식은 **틀릴 수 있습니다.** 금액·계좌번호처럼 한 글자가 중요한 값은 결과를 그대로 믿지 말고 형식 검사(정규식 일치 확인)나 사람의 확인을 넣으세요.
- 작은 글자가 틀리게 읽히면 속성 창의 **OCR 해상도**를 300 으로 올립니다(기본 200, 올릴수록 느려집니다).
- 글자 인식은 [클릭 (Vision)](control.md) 과 같은 엔진을 쓰고, 처음 한 번은 엔진을 띄우느라 몇 초 더 걸립니다.

### 암호가 걸린 PDF { #pdf-password }

여는 암호가 있는 PDF 는 **암호**(또는 **보호된 비밀번호**)를 주어야 읽습니다. 없거나 틀리면 오류로 멈춥니다. 인쇄·복사만 막아 둔 PDF(여는 암호 없음)는 암호 없이 읽힙니다.

**페이지 추출·합치기로 만든 PDF 에는 암호가 걸리지 않습니다.** 암호가 걸린 원본에서 뽑은 페이지도 마찬가지이니, 민감한 문서는 만든 파일의 보관 위치에 주의하세요. 보내기 전에 잠가야 하면 [파일 압축](control.md) 의 암호를 쓰세요.

## PDF 텍스트 읽기  <small>`ReadPdfText`</small>

PDF 의 텍스트를 읽어 변수에 담습니다. 글자가 든 페이지는 그대로 읽고, 글자가 없는 페이지(스캔본)는 글자 인식(OCR)으로 읽습니다. 표를 다루려면 텍스트 배치를 **칸 맞춤**으로 두세요. UiPath Read PDF Text 와 Read PDF With OCR 을 하나로 합친 액티비티입니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 파일 경로 <small>`FilePath`</small> | 입력 | `string` | 읽을 PDF. 상대 경로는 프로젝트 폴더 기준입니다. 카드의 […] 버튼으로 고를 수 있습니다. |
| 페이지 <small>`Pages`</small> | 입력 | `string` | 읽을 페이지. 비우면 전체. 예: `1-3, 5`, `2-`, `End` — [페이지 범위 적는 법](#pdf-pages). |
| 텍스트 배치 <small>`TextLayout`</small> | 설정 | `PdfTextLayout` | 낱말을 텍스트로 늘어놓는 방식. **줄 단위**(기본) · **칸 맞춤**(표의 칸 사이에 빈칸 둘 이상) · **문서 순서** — [텍스트 배치](#pdf-layout). |
| OCR <small>`OcrMode`</small> | 설정 | `PdfOcrMode` | 글자 인식(OCR)을 언제 쓸지. **스캔 쪽만**(기본 — 글자가 없는 페이지만) · **안 함** · **모든 쪽** — [스캔본과 OCR](#pdf-ocr). |
| OCR 해상도 <small>`OcrDpi`</small> | 입력 | `int` | OCR 할 때 페이지를 그리는 해상도(DPI). 0 이거나 비우면 200. 작은 글자가 틀리게 읽히면 300. |
| 암호 <small>`Password`</small> | 입력 | `string` | PDF 여는 암호(평문). 직접 적으면 워크플로 파일에 그대로 저장되어 경고가 표시됩니다 — **보호된 비밀번호**를 쓰세요. |
| 보호된 비밀번호 <small>`SecurePassword`</small> | 입력 | `SecureString` | 보호된 비밀번호(SecureString). 자격 증명 가져오기(GetCredential)의 SecurePassword 출력을 연결합니다. 있으면 평문 비밀번호보다 우선합니다. |
| 결과 <small>`Result`</small> | 출력 | `string` | 읽은 텍스트(출력). 고른 페이지를 줄바꿈으로 이은 것입니다. |
| 페이지별 텍스트 <small>`PageTexts`</small> | 출력 | `string[]` | 페이지마다의 텍스트(출력, 문자열 배열 — 고른 페이지 순서). `반복(ForEach)` 으로 페이지마다 처리할 때 씁니다. |
| 페이지 수 <small>`PageCount`</small> | 출력 | `int` | 문서의 전체 페이지 수(출력). 읽은 페이지 수가 아니라 문서 전체입니다. |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## PDF 페이지 수  <small>`GetPdfPageCount`</small>

PDF 의 페이지 수를 돌려줍니다. 페이지마다 나눠 처리하는 반복의 끝을 정할 때 씁니다. UiPath Get PDF Page Count 에 해당합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 파일 경로 <small>`FilePath`</small> | 입력 | `string` | 페이지 수를 셀 PDF. 상대 경로는 프로젝트 폴더 기준입니다. |
| 암호 <small>`Password`</small> | 입력 | `string` | PDF 여는 암호(평문). 직접 적으면 경고가 표시됩니다 — **보호된 비밀번호**를 쓰세요. |
| 보호된 비밀번호 <small>`SecurePassword`</small> | 입력 | `SecureString` | 보호된 비밀번호(SecureString). 자격 증명 가져오기(GetCredential)의 SecurePassword 출력을 연결합니다. 있으면 평문 비밀번호보다 우선합니다. |
| 결과 <small>`Result`</small> | 출력 | `int` | 페이지 수(출력). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## PDF 페이지 추출  <small>`ExtractPdfPages`</small>

PDF 에서 고른 페이지만으로 새 PDF 를 만듭니다. 페이지는 적은 순서대로 들어가므로 한 페이지만 떼어 내거나 순서를 바꿀 수 있습니다. 임시 파일에 다 쓴 뒤 바꿔 넣어 도중에 실패해도 반쪽짜리 파일이 남지 않습니다. UiPath Extract PDF Page Range 에 해당합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 파일 경로 <small>`FilePath`</small> | 입력 | `string` | 원본 PDF. |
| 페이지 <small>`Pages`</small> | 입력 | `string` | 뽑을 페이지. 예: `2-3`, `1, 5-` — [페이지 범위 적는 법](#pdf-pages). 비우면 전체(사본). |
| 저장할 파일 <small>`OutputPath`</small> | 입력 | `string` | 저장할 PDF(.pdf). 없는 폴더는 만듭니다. 원본과 같은 파일로는 저장할 수 없습니다. |
| 덮어쓰기 <small>`Overwrite`</small> | 설정 | `bool` | 같은 이름의 파일이 있으면 바꿔 쓸지 여부(기본 true). 끄면 이미 있을 때 오류로 멈춥니다. |
| 암호 <small>`Password`</small> | 입력 | `string` | 원본 PDF 여는 암호(평문). 만든 PDF 에는 암호가 걸리지 않습니다 — [암호가 걸린 PDF](#pdf-password). |
| 보호된 비밀번호 <small>`SecurePassword`</small> | 입력 | `SecureString` | 보호된 비밀번호(SecureString). 자격 증명 가져오기(GetCredential)의 SecurePassword 출력을 연결합니다. 있으면 평문 비밀번호보다 우선합니다. |
| 결과 <small>`Result`</small> | 출력 | `string` | 저장한 PDF 의 전체 경로(출력). |
| 페이지 수 <small>`PageCount`</small> | 출력 | `int` | 저장한 PDF 의 페이지 수(출력). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

```
' PDF 를 페이지마다 한 파일로 나누기
PDF 페이지 수      파일 경로: "in\전체.pdf"            결과: count
반복(For)          i = 1 부터 count 까지
    PDF 페이지 추출   파일 경로: "in\전체.pdf"   페이지: i.ToString()
                      저장할 파일: "out\page-" & i.ToString("00") & ".pdf"
```

책갈피(목차)와 양식 필드는 새 PDF 로 옮겨지지 않을 수 있습니다. 링크·주석은 가능한 만큼 옮깁니다.

## PDF 합치기  <small>`JoinPdfFiles`</small>

PDF 여러 개를 하나로 잇습니다. 합칠 것은 PDF 파일, 폴더(그 안의 PDF 전부), 또는 `out\*.pdf` 같은 파일 이름 패턴이고, 순서를 직접 정하려면 **PDF 목록**에 경로 목록을 줍니다. UiPath Join PDF Files 에 해당합니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 합칠 PDF <small>`InputPath`</small> | 입력 | `string` | 합칠 PDF 파일·폴더, 또는 파일 이름 패턴(`out\report-*.pdf`). 폴더와 패턴에서 나온 파일은 **탐색기와 같은 이름 순서**(`2.pdf` 가 `10.pdf` 앞)로 잇습니다. 카드의 📄·📁 버튼으로 고를 수 있습니다. |
| PDF 목록 <small>`InputPaths`</small> | 입력 | `IEnumerable<string>` | 합칠 PDF 경로 목록(문자열 배열이나 `List(Of String)` 변수). 목록의 순서대로 잇습니다. 예: `New String() {"표지.pdf", "본문.pdf", "부록"}`. **합칠 PDF** 와 함께 주면 그쪽이 먼저입니다. |
| 저장할 파일 <small>`OutputPath`</small> | 입력 | `string` | 저장할 PDF(.pdf). 없는 폴더는 만듭니다. 합칠 폴더 안에 저장해도 됩니다(자기 자신은 다시 넣지 않습니다). |
| 덮어쓰기 <small>`Overwrite`</small> | 설정 | `bool` | 같은 이름의 파일이 있으면 바꿔 쓸지 여부(기본 true). |
| 암호 <small>`Password`</small> | 입력 | `string` | 암호가 걸린 원본을 여는 암호(평문, 모든 원본에 같은 암호). 만든 PDF 에는 암호가 걸리지 않습니다. |
| 보호된 비밀번호 <small>`SecurePassword`</small> | 입력 | `SecureString` | 보호된 비밀번호(SecureString). 자격 증명 가져오기(GetCredential)의 SecurePassword 출력을 연결합니다. 있으면 평문 비밀번호보다 우선합니다. |
| 결과 <small>`Result`</small> | 출력 | `string` | 저장한 PDF 의 전체 경로(출력). |
| 페이지 수 <small>`PageCount`</small> | 출력 | `int` | 저장한 PDF 의 전체 페이지 수(출력). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |

## PDF 페이지를 이미지로  <small>`ExportPdfPageAsImage`</small>

PDF 페이지를 그림 파일로 저장합니다. 형식은 저장할 이름의 확장자가 정합니다(.png · .jpg · .bmp · .gif · .tif). UiPath Export PDF Page As Image 에 해당하며 여러 페이지를 한 번에 낼 수 있습니다.

**속성**

| 속성 | 방향 | 타입 | 설명 |
|------|------|------|------|
| 파일 경로 <small>`FilePath`</small> | 입력 | `string` | 그림으로 낼 PDF. |
| 페이지 <small>`Pages`</small> | 입력 | `string` | 그림으로 낼 페이지. 비우면 전체 — [페이지 범위 적는 법](#pdf-pages). |
| 저장할 파일 <small>`OutputPath`</small> | 입력 | `string` | 저장할 이미지. **한 페이지면 적은 이름 그대로**, 여러 페이지면 이름 뒤에 `-페이지번호` 가 붙습니다(`page.png` → `page-01.png`, `page-02.png` …). 없는 폴더는 만듭니다. |
| 해상도 (DPI) <small>`Dpi`</small> | 입력 | `int` | 해상도(DPI). 0 이거나 비우면 150. 화면에서 보는 용도면 96~150, 인쇄·글자 인식 용도면 200~300. 36~600 사이로 맞춥니다. |
| 덮어쓰기 <small>`Overwrite`</small> | 설정 | `bool` | 같은 이름의 파일이 있으면 바꿔 쓸지 여부(기본 true). 끄면 하나라도 있을 때 아무것도 만들지 않고 오류로 멈춥니다. |
| 암호 <small>`Password`</small> | 입력 | `string` | PDF 여는 암호(평문). 직접 적으면 경고가 표시됩니다 — **보호된 비밀번호**를 쓰세요. |
| 보호된 비밀번호 <small>`SecurePassword`</small> | 입력 | `SecureString` | 보호된 비밀번호(SecureString). 자격 증명 가져오기(GetCredential)의 SecurePassword 출력을 연결합니다. 있으면 평문 비밀번호보다 우선합니다. |
| 결과 <small>`Result`</small> | 출력 | `string[]` | 저장한 이미지 파일의 전체 경로 목록(출력, 문자열 배열 — 페이지 순서). |
| 개수 <small>`Count`</small> | 출력 | `int` | 저장한 이미지 수(출력). |
| 오류 무시 <small>`ContinueOnError`</small> | 입력 | `bool` | 이 액티비티에서 오류가 발생해도 워크플로를 멈추지 않고 계속 진행할지 여부(true/false). |
