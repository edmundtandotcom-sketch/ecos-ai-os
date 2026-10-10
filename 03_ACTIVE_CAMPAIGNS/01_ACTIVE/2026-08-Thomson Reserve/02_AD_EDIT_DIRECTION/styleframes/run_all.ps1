# All Longer-Ads variations (31 ads) in one run. Run from this folder in PowerShell:   .\run_all.ps1
# Re-running only renders the ads that are not there yet.
$ErrorActionPreference = "Stop"
$folder = "H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\04_Video Editor\Webinar Daughter Spin Off"
Set-Location $PSScriptRoot
python -m pip install --quiet pillow numpy opencv-python-headless imageio-ffmpeg sherpa-onnx pymupdf
python batch_tr.py --folder $folder
$renders = Join-Path $folder "Longer Ads\RENDERS"
if (Test-Path $renders) { Invoke-Item $renders }
