param(
    [switch]$Export
)

$ErrorActionPreference = "Stop"

. (Join-Path $PSScriptRoot "latex-tools.ps1")

$root = Get-ProjectRoot
$latexDir = Join-Path $root "LaTeX"
$main = Join-Path $latexDir "main.tex"
$build = Join-Path $root "build\latex"
$exportDir = Join-Path $root "docs\export"
$exportPdf = Join-Path $exportDir "ENG1005_LaTeX_Template.pdf"

if (-not (Test-Path -LiteralPath $main)) {
    throw "LaTeX entrypoint not found: LaTeX/main.tex"
}

New-Item -ItemType Directory -Force -Path $build | Out-Null

$latexmk = Find-LaTeXTool "latexmk.exe"
$pdflatex = Find-LaTeXTool "pdflatex.exe"
$biber = Find-LaTeXTool "biber.exe"

Push-Location $latexDir
try {
    if ($latexmk) {
        & $latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir="$build" "main.tex"
    } elseif ($pdflatex) {
        & $pdflatex -interaction=nonstopmode -halt-on-error -output-directory="$build" "main.tex"
        if ($biber -and (Test-Path (Join-Path $build "main.bcf"))) {
            & $biber --input-directory "$build" --output-directory "$build" "main"
        }
        & $pdflatex -interaction=nonstopmode -halt-on-error -output-directory="$build" "main.tex"
        & $pdflatex -interaction=nonstopmode -halt-on-error -output-directory="$build" "main.tex"
    } else {
        throw "No LaTeX engine found. Install MiKTeX or TeX Live, or run scripts/latex-doctor.ps1 for diagnostics."
    }
} finally {
    Pop-Location
}

if ($Export) {
    $builtPdf = Join-Path $build "main.pdf"
    if (-not (Test-Path -LiteralPath $builtPdf)) {
        throw "Expected PDF was not produced: build/latex/main.pdf"
    }

    New-Item -ItemType Directory -Force -Path $exportDir | Out-Null
    Copy-Item $builtPdf $exportPdf -Force
    $item = Get-Item $exportPdf
    [PSCustomObject]@{
        Path = "docs/export/ENG1005_LaTeX_Template.pdf"
        Length = $item.Length
        LastWriteTime = $item.LastWriteTime
    }
}
