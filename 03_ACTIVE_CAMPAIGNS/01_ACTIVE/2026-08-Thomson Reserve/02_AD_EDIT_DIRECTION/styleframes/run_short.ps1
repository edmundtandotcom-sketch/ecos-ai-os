# One-shot: the one-file ad from "Selfie Daughter Hook 1" (hook + short webinar CTA), rendered from the takes folder.
# Run from this folder in PowerShell:   .\run_short.ps1
$ErrorActionPreference = "Stop"
$folder = "H:\Shared drives\00_E.C.O.S\03_ACTIVE_CAMPAIGNS\04_Video Editor\Webinar Daughter Spin Off"
Set-Location $PSScriptRoot
python -m pip install --quiet pillow numpy opencv-python-headless imageio-ffmpeg sherpa-onnx pymupdf
python render_v1.py --folder $folder --single "Selfie Daughter Hook 1"
if (Test-Path (Join-Path $folder "TR_SHORT_Receipt_9x16.mp4")) {
  Invoke-Item (Join-Path $folder "TR_SHORT_Receipt_9x16.mp4")
  Invoke-Item (Join-Path $folder "TR_SHORT_contact_sheet.jpg")
}
