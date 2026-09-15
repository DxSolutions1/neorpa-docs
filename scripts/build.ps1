<#
.SYNOPSIS
  NeoRPA 문서 사이트 로컬 빌드/미리보기.
.DESCRIPTION
  .venv 를 만들고 requirements.txt 를 설치한 뒤 `mkdocs build --strict` (CI 와 동일) 를 실행한다.
  -Serve 를 주면 mkdocs serve 로 http://127.0.0.1:8000 에서 미리보기.
  -NoBuild 를 주면 환경만 준비한다(생성기 실행 전 준비용).
.EXAMPLE
  pwsh -File scripts/build.ps1
  pwsh -File scripts/build.ps1 -Serve
#>
param(
    [switch]$Serve,
    [switch]$NoBuild,
    [string]$PythonExe = ""
)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

$venvPython = Join-Path $root ".venv\Scripts\python.exe"
if (-not (Test-Path $venvPython)) {
    if (-not $PythonExe) {
        $PythonExe = (Get-Command python -ErrorAction SilentlyContinue)?.Source
        if (-not $PythonExe) { $PythonExe = (Get-Command py -ErrorAction Stop).Source; $pyArgs = @("-3") } else { $pyArgs = @() }
    } else { $pyArgs = @() }
    Write-Host "[build] .venv 생성 ($PythonExe)"
    & $PythonExe @pyArgs -m venv (Join-Path $root ".venv")
}

Write-Host "[build] 의존성 설치 (requirements.txt)"
& $venvPython -m pip install -q -r (Join-Path $root "requirements.txt")
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

$env:PYTHONUTF8 = "1"
Write-Host "[build] python: $venvPython"
if ($NoBuild) { exit 0 }

if ($Serve) {
    & $venvPython -m mkdocs serve
} else {
    & $venvPython -m mkdocs build --strict
}
exit $LASTEXITCODE
