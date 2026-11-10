#!/bin/sh
# Trademark hygiene gate (docs/naming-and-trademarks.md §5).
# Fails if *product artifacts* (image/, packaging/, any future user-facing tree)
# contain competitor terms. docs/ is allowed to use them comparatively.
set -eu

ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
STATUS=0

# Directories that ship to users (extend as they appear).
SCAN_DIRS="image packaging brand"
for dir in $SCAN_DIRS; do
  [ -d "$ROOT/$dir" ] || continue
  # Competitor terms that must never appear in product artifacts.
  for term in Windows macOS "Start menu" "This PC" "Action Center" "OneDrive" Copilot "Game Pass" Segoe; do
    if grep -rniI --exclude-dir=.git "$term" "$ROOT/$dir"; then
      echo "ERROR: competitor term '$term' found in shippable tree '$dir/'" >&2
      STATUS=1
    fi
  done
done

# The naming policy must exist for this script to be meaningful.
[ -f "$ROOT/docs/naming-and-trademarks.md" ] || { echo "ERROR: docs/naming-and-trademarks.md missing" >&2; STATUS=1; }

if [ "$STATUS" -eq 0 ]; then
  echo "Trademark scan OK (shippable trees clean)."
fi
exit "$STATUS"
