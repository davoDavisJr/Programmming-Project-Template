$ErrorActionPreference = "Stop"

$root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$source = Join-Path $root "src\main.mas"

if ($env:MARIE_ROOT) {
    $marieRoot = $env:MARIE_ROOT
    $marieRootLabel = "MARIE_ROOT"
}
else {
    $marieRoot = Join-Path ([Environment]::GetFolderPath("UserProfile")) ".MARIE"
    $marieRootLabel = "default ~/.MARIE"
}

if (-not (Test-Path -LiteralPath $source)) {
    Write-Output "[MARIE] Missing MARIE source file: src/main.mas"
    exit 1
}

if (-not (Test-Path -LiteralPath $marieRoot)) {
    Write-Output "[MARIE] Missing MARIE simulator folder ($marieRootLabel). Set MARIE_ROOT to your local simulator folder."
    exit 1
}

Write-Output "MARIE source: src/main.mas"
Write-Output "MARIE root: $marieRootLabel"
Write-Output "MARIE setup looks ready."
