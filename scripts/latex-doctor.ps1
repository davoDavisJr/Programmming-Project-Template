$ErrorActionPreference = "Stop"

. (Join-Path $PSScriptRoot "latex-tools.ps1")

$root = Get-ProjectRoot
$tools = @(
    "latexmk.exe",
    "pdflatex.exe",
    "xelatex.exe",
    "lualatex.exe",
    "biber.exe",
    "kpsewhich.exe",
    "texcount.exe"
)

Write-Output "Project root: ."
Write-Output "Main document: LaTeX/main.tex"
Write-Output ""
Write-Output "Tool resolution:"

foreach ($tool in $tools) {
    $path = Find-LaTeXTool $tool
    if ($path) {
        Write-Output "OK      $tool"
    } else {
        Write-Output "MISSING $tool"
    }
}

$kpsewhich = Find-LaTeXTool "kpsewhich.exe"
if ($kpsewhich) {
    Write-Output ""
    Write-Output "Required LaTeX files:"
    $files = @(
        "article.cls",
        "geometry.sty",
        "amsmath.sty",
        "amssymb.sty",
        "amsthm.sty",
        "mathtools.sty",
        "siunitx.sty",
        "tikz.sty",
        "pgfplots.sty",
        "biblatex.sty",
        "apa.bbx",
        "booktabs.sty",
        "microtype.sty",
        "subcaption.sty",
        "pdflscape.sty"
    )

    foreach ($file in $files) {
        try {
            $result = & $kpsewhich $file 2>$null
            if ($LASTEXITCODE -eq 0 -and $result) {
                Write-Output "OK      $file"
            } else {
                Write-Output "MISSING $file"
            }
        } catch {
            Write-Output "COULD NOT EXECUTE kpsewhich.exe: $($_.Exception.Message)"
            break
        }
    }
}
