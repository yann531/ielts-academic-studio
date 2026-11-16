param([string]$ScriptFile = 'audio-scripts.json')
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Speech
$projectRoot = Split-Path -Parent $PSScriptRoot
$segments = Get-Content -LiteralPath (Join-Path $PSScriptRoot $ScriptFile) -Raw | ConvertFrom-Json
$synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
$synth.SelectVoice('Microsoft Zira Desktop')
$synth.Rate = -1
try {
  foreach ($segment in $segments) {
    $audioPath = Join-Path $projectRoot ('public/audio/' + $segment.id + '.wav')
    $format = New-Object System.Speech.AudioFormat.SpeechAudioFormatInfo(16000, [System.Speech.AudioFormat.AudioBitsPerSample]::Sixteen, [System.Speech.AudioFormat.AudioChannel]::Mono)
    $synth.SetOutputToWaveFile($audioPath, $format)
    $synth.Speak($segment.text)
    $synth.SetOutputToNull()
    Write-Output ('Generated ' + $segment.id)
  }
} finally { $synth.Dispose() }
