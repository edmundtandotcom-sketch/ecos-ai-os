# All Longer-Ads variations (31 ads) in one run. Run from this folder in PowerShell:   .\run_all.ps1
# Re-running only renders the ads that are not there yet.
$ErrorActionPreference = "Stop"
$folder = "H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\04_Video Editor\Webinar Daughter Spin Off"
Set-Location $PSScriptRoot
# Google Drive on this PC sometimes keeps a replaced file as "name (1).py" next to, or instead of, "name.py".
# Put the newest copy under the right name before anything runs.
$need = @("batch_tr.py", "render_v1.py", "looks.py", "styleframes.py", "tr_scripts.py", "prep_assets.py")
$missing = @()
foreach ($f in $need) {
  $base = [IO.Path]::GetFileNameWithoutExtension($f); $ext = [IO.Path]::GetExtension($f)
  $alts = @(Get-ChildItem -File -Filter "$base (*)$ext" | Sort-Object LastWriteTime -Descending)
  if ($alts.Count -gt 0) {
    $newest = $alts[0]
    if (-not (Test-Path $f) -or $newest.LastWriteTime -gt (Get-Item $f).LastWriteTime) {
      Copy-Item $newest.FullName $f -Force; Write-Host "using $($newest.Name) as $f"
    }
  }
  if (-not (Test-Path $f)) { $missing += $f }
}
if ($missing.Count -gt 0) {
  Write-Host ""
  Write-Host "These files have not arrived from Google Drive yet: $($missing -join ', ')"
  Write-Host "Open this folder in File Explorer, wait until every file shows a green tick, then run RUN_ALL.bat again."
  exit 1
}
python -m pip install --quiet pillow numpy opencv-python-headless imageio-ffmpeg sherpa-onnx pymupdf
python batch_tr.py --folder $folder
$renders = Join-Path $folder "Longer Ads\RENDERS"
if (Test-Path $renders) { Invoke-Item $renders }
