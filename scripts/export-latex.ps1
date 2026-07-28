$ErrorActionPreference = "Stop"

& (Join-Path $PSScriptRoot "build-latex.ps1") -Export
