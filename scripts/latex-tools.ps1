function Get-ProjectRoot {
    return (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
}

function Find-LaTeXTool {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Name
    )

    $command = Get-Command $Name -ErrorAction SilentlyContinue
    if ($command) {
        return $command.Source
    }

    $candidateDirs = @(
        "C:\Program Files\MiKTeX\miktex\bin\x64",
        "C:\Program Files (x86)\MiKTeX\miktex\bin",
        "C:\texlive\2026\bin\windows",
        "C:\texlive\2025\bin\windows",
        "C:\texlive\2024\bin\windows"
    )

    foreach ($dir in $candidateDirs) {
        if (-not $dir) {
            continue
        }

        $candidate = Join-Path $dir $Name
        if (Test-Path -LiteralPath $candidate) {
            if (($env:Path -split ";") -notcontains $dir) {
                $env:Path = "$dir;$env:Path"
            }
            return $candidate
        }
    }

    return $null
}
