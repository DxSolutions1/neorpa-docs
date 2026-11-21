<!-- 이 파일은 scripts/gen_activities.py 로 자동 생성됩니다.
     직접 편집하지 말고 data/activities.yaml 을 고친 뒤 `python scripts/gen_activities.py --write` 를 다시 실행하세요. -->


# 액티비티 사용법

16개 카테고리 · 202개 액티비티를 툴박스 순서대로 정리합니다. 표시명·속성 표는 NeoRPA 소스에서 자동 추출되고, 설명은 `data/activities.yaml`에서 관리됩니다.

## 카테고리 (툴박스 기준)

| 카테고리 | 액티비티 수 | 내용 |
|---|---:|---|
| [Chrome (전용)](chrome.md) | 10 | 전용 크롬(CDP) 자동화 |
| [Chrome (일반)](chrome-native.md) | 8 | 사용자 프로필 크롬(네이티브 메시징) |
| [Control (데스크톱 UI · 파일 · 프로세스)](control.md) | 41 | 데스크톱 UI 자동화 + 파일·프로세스·클립보드·코드 실행 |
| [Statements (흐름 제어)](statements.md) | 19 | 흐름 제어(조건·반복·예외·시퀀스) |
| [Excel WorkBook](excel-workbook.md) | 28 | COM 워크북 직접 조작 |
| [Excel Scope](excel-scope.md) | 33 | 스코프 기반 Excel |
| [DataTable](datatable.md) | 16 | 데이터테이블 조작 · CSV 읽기·쓰기 |
| [Mail](mail.md) | 5 | 메일 보내기(SMTP)·받기(IMAP/POP3)·첨부 저장 |
| [Web (HTTP 요청 · JSON)](web.md) | 5 | REST API 호출과 JSON 읽기·만들기 |
| [Text (문자열 · 정규식 · 날짜)](text.md) | 11 | 텍스트 찾기·바꾸기·나누기·합치기와 날짜 변환 |
| [PDF (텍스트 읽기 · 페이지 · 합치기)](pdf.md) | 5 | PDF 텍스트 읽기(스캔본은 OCR)·페이지 수·페이지 추출·합치기·이미지로 내보내기 |
| [AI (AI 호출)](ai.md) | 1 | 이 PC 에 설치된 AI CLI(Claude Code · Codex · Gemini)에 일을 맡기고 결과를 변수로 받기 |
| [System (구조 · 프로세스)](system.md) | 12 | WF 구조·프로세스 유틸 |
| [DB](db.md) | 2 | 데이터베이스 질의 |
| [OutLook](outlook.md) | 3 | Outlook 메일 |
| [보안 (자격 증명)](security.md) | 3 | Windows 자격 증명 관리자에 비밀번호 보관 |

!!! tip "Excel WorkBook vs Excel Scope"
    이름이 비슷한 액티비티가 두 카테고리에 있습니다. 차이(스코프 유무·사용 시점)는 각 카테고리 개요에서 설명합니다.
