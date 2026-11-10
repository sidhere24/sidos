# Trademark hygiene gate (docs/naming-and-trademarks.md §5) — Windows twin of check-trademarks.sh
$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$status = 0

$scanDirs = @('image', 'packaging', 'brand')
$banned = @('Windows', 'macOS', 'Start menu', 'This PC', 'Action Center', 'OneDrive', 'Copilot', 'Game Pass', 'Segoe')

foreach ($dir in $scanDirs) {
  $path = Join-Path $root $dir
  if (-not (Test-Path $path)) { continue }
  foreach ($term in $banned) {
    $hits = Get-ChildItem -Recurse -File $path | Select-String -SimpleMatch -Pattern $term -CaseSensitive:$false
    if ($hits) {
      $hits | ForEach-Object { Write-Host "ERROR: competitor term '$term' found in shippable tree '$dir/' -> $($_.Path):$($_.LineNumber)" }
      $status = 1
    }
  }
}

if (-not (Test-Path (Join-Path $root 'docs\naming-and-trademarks.md'))) {
  Write-Host 'ERROR: docs/naming-and-trademarks.md missing'
  $status = 1
}

if ($status -eq 0) { Write-Host 'Trademark scan OK (shippable trees clean).' }
exit $status
