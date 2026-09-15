<!-- 이 파일은 scripts/gen_activities.py 로 자동 생성됩니다.
     직접 편집하지 말고 data/activities.yaml 을 고친 뒤 `python scripts/gen_activities.py --write` 를 다시 실행하세요. -->


# 액티비티 사용법

11개 카테고리 · 166개 액티비티를 툴박스 순서대로 정리합니다. 표시명·속성 표는 NeoRPA 소스에서 자동 추출되고, 설명은 `data/activities.yaml`에서 관리됩니다.

## 카테고리 (툴박스 기준)

| 카테고리 | 액티비티 수 | 내용 |
|---|---:|---|
| [Chrome (전용)](chrome.md) | 10 | 전용 크롬(CDP) 자동화 |
| [Chrome (일반)](chrome-native.md) | 8 | 사용자 프로필 크롬(네이티브 메시징) |
| [Control (데스크톱 UI · 파일 · 프로세스)](control.md) | 34 | 데스크톱 UI 자동화 + 파일·프로세스·클립보드·코드 실행 |
| [Statements (흐름 제어)](statements.md) | 19 | 흐름 제어(조건·반복·예외·시퀀스) |
| [Excel WorkBook](excel-workbook.md) | 28 | COM 워크북 직접 조작 |
| [Excel Scope](excel-scope.md) | 33 | 스코프 기반 Excel |
| [DataTable](datatable.md) | 15 | 데이터테이블 조작 |
| [Mail](mail.md) | 2 | 메일 송수신(SMTP/POP3) |
| [System (구조 · 프로세스)](system.md) | 12 | WF 구조·프로세스 유틸 |
| [DB](db.md) | 2 | 데이터베이스 질의 |
| [OutLook](outlook.md) | 3 | Outlook 메일 |

!!! tip "Excel WorkBook vs Excel Scope"
    이름이 비슷한 액티비티가 두 카테고리에 있습니다. 차이(스코프 유무·사용 시점)는 각 카테고리 개요에서 설명합니다.
