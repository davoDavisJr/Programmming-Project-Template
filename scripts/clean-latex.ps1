$ErrorActionPreference = "Stop"

. (Join-Path $PSScriptRoot "latex-tools.ps1")

$root = Get-ProjectRoot
$build = Join-Path $root "build\latex"
$exportPdf = Join-Path $root "docs\export\ENG1005_LaTeX_Template.pdf"

foreach ($path in @($build, $exportPdf)) {
    if (Test-Path -LiteralPath $path) {
        Remove-Item -LiteralPath $path -Recurse -Force
    }
}
