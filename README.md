# NeoRPA 문서 (공개 사이트)

NeoRPA **사용자 문서**를 GitHub Pages로 배포하는 저장소입니다. MkDocs Material 기반.

- 배포 URL: https://dxsolutions1.github.io/neorpa-docs/
- 배포: `main` 에 push 하면 GitHub Actions(`.github/workflows/deploy.yml`)가 빌드·배포합니다.
  - 최초 1회: **Settings → Pages → Source = "GitHub Actions"**.

## 콘텐츠 출처 (중요)

이 저장소는 **배포 미러**입니다. 문서 원본과 생성 도구는 NeoRPA 본 저장소(비공개)의 `website/` 에 있습니다.
액티비티 문서·속성 표는 본 저장소의 소스(resx·.cs)에서 생성되므로, **직접 편집하지 말고** 본 저장소에서 갱신한 뒤 동기화하세요.

```powershell
# (본 저장소) rpa-designer/website 에서
python scripts/gen_activity_stubs.py            # 필요 시 액티비티 문서 재생성
pwsh -File scripts/sync-public-repo.ps1         # 공개 콘텐츠를 이 저장소로 복사(개발자 문서 제외)
# 이후 이 저장소에서 commit & push
```

> 개발자 문서(`dev/`)는 RPA 관리자 전용이라 이 공개 저장소에 **포함되지 않습니다**.

## 로컬 미리보기

```bash
pip install -r requirements.txt
mkdocs serve
```
