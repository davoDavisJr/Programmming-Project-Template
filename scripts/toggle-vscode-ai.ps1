param(
    [ValidateSet("enable", "disable", "status")]
    [string]$Mode = "status"
)

$settingsPath = Join-Path (Get-Location).Path ".vscode\settings.json"
if (-not (Test-Path $settingsPath)) {
    throw "VS Code settings file not found. Run this script from repository root."
}

$raw = Get-Content -Raw $settingsPath

function Write-Utf8NoBom {
    param(
        [string]$Path,
        [string]$Content
    )

    $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllText($Path, $Content, $utf8NoBom)
}

function Set-BoolSetting {
    param(
        [string]$InputText,
        [string]$Key,
        [bool]$Value
    )

    $boolText = if ($Value) { "true" } else { "false" }
    $escapedKey = [regex]::Escape($Key)
    $pattern = '"' + $escapedKey + '"\s*:\s*(true|false)'
    if ([regex]::IsMatch($InputText, $pattern)) {
        return [regex]::Replace($InputText, $pattern, '"' + $Key + '": ' + $boolText, 1)
    }
    return $InputText
}

function Set-CopilotObject {
    param(
        [string]$InputText,
        [bool]$Value
    )

    $boolText = if ($Value) { "true" } else { "false" }
    $pattern = '"github\.copilot\.enable"\s*:\s*\{[^\}]*\}'
    $replacement = '"github.copilot.enable": {' + [Environment]::NewLine + '    "*": ' + $boolText + [Environment]::NewLine + '  }'
    $rx = New-Object System.Text.RegularExpressions.Regex($pattern, [System.Text.RegularExpressions.RegexOptions]::Singleline)
    if ($rx.IsMatch($InputText)) {
        return $rx.Replace($InputText, $replacement, 1)
    }
    return $InputText
}

if ($Mode -eq "status") {
    if ($raw -match '"github\.copilot\.enable"\s*:\s*\{[^\}]*"\*"\s*:\s*false') {
        Write-Output "AI status: disabled"
    }
    else {
        Write-Output "AI status: enabled"
    }
    exit 0
}

$disable = $Mode -eq "disable"
$raw = Set-CopilotObject -InputText $raw -Value (-not $disable)
$raw = Set-BoolSetting -InputText $raw -Key "github.copilot.editor.enableAutoCompletions" -Value (-not $disable)
$raw = Set-BoolSetting -InputText $raw -Key "github.copilot.chat.enable" -Value (-not $disable)
$raw = Set-BoolSetting -InputText $raw -Key "chat.commandCenter.enabled" -Value (-not $disable)

Write-Utf8NoBom -Path $settingsPath -Content $raw
Write-Output "AI settings updated to mode: $Mode"
