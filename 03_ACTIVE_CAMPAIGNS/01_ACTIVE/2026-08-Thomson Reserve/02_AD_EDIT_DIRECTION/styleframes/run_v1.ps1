# One-shot: install, fetch model + assets, render V1 from the takes folder, open the result.
# Run from this folder in PowerShell:   .\run_v1.ps1
$ErrorActionPreference = "Stop"
$folder = "H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\04_Video Editor\Webinar Daughter Spin Off"
Set-Location $PSScriptRoot
python -m pip install --quiet pillow numpy opencv-python-headless imageio-ffmpeg sherpa-onnx pymupdf
python render_v1.py --folder $folder
if (Test-Path (Join-Path $folder "TR_V1_Receipt_9x16.mp4")) {
  Invoke-Item (Join-Path $folder "TR_V1_Receipt_9x16.mp4")
  Invoke-Item (Join-Path $folder "TR_V1_contact_sheet.jpg")
}
