# 액티비티 사용법

11개 카테고리 · 161개 액티비티를 카테고리별로 정리합니다. 각 카테고리 페이지는 `website/data/activities.yaml`(단일 소스) + resx 한국어 표시명으로 생성됩니다. 액티비티를 추가하거나 설명을 채울 때는 yaml을 수정한 뒤 `python scripts/gen_activity_stubs.py`를 다시 실행하세요.

!!! note "설명 채우는 중"
    표시명·목록은 완비되어 있고, 각 액티비티의 설명(`desc`)은 우선순위가 높은 카테고리부터 채워지고 있습니다.

## 카테고리 (툴박스 기준)

| 카테고리 | 내용 |
|---|---|
| Chrome | 전용 크롬(CDP) 자동화 |
| Chrome (일반) | 사용자 프로필 크롬(네이티브 메시징) |
| Control | 데스크톱 UI 자동화 + 파일·프로세스·클립보드·코드 실행 |
| Statements | 흐름 제어(조건·반복·예외·시퀀스) |
| Excel WorkBook | COM 워크북 직접 조작 |
| Excel Scope | 스코프 기반 Excel |
| DataTable | 데이터테이블 조작 |
| Mail | 메일 송수신(SMTP/POP3) |
| System | WF 구조·프로세스 유틸 |
| DB | 데이터베이스 질의 |
| OutLook | Outlook 메일 |

!!! tip "Excel WorkBook vs Excel Scope"
    이름이 비슷한 액티비티가 두 카테고리에 있습니다. 차이(스코프 유무·사용 시점)는 각 카테고리 개요에서 설명합니다.
