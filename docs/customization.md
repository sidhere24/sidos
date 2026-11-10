# Customization freedom — the anti "Apple knows best"

SiD OS ships opinionated defaults (the one blessed path, P5) **and full freedom**
for people who want it. Nothing about the curated look is a cage.

## The rule
Every default is one Settings click away from being changed — or removed. No
"engineering decision made for you and hidden," no paywalled customization.

## What users can swap (all free, all one click)

### Appearance
- **Global Theme** (Classic/Studio/Flow → any installed theme: Fluent, WhiteSur,
  Catppuccin, Layan, Arc, Nordic…)
- **Color scheme** — preset palettes + custom
- **Icons** — Papirus (default), Layan, WhiteSur, Adwaita, others
- **Cursors** — Breeze (default), Bibata-Modern, Layan
- **Widget style (Qt) / GTK theme** — via Kvantum; both swap in one place
- **Wallpaper** — bundled set + Wikimedia/NASA picks + any file on disk
- **Fonts & DPI** — Noto/Inter/JetBrains Mono presets + any installed font
- **Window decorations** — Breeze default; WhiteSur-styled, minimal 1px, etc.

### Sounds
- Sound theme picker (freedesktop-compatible): freedesktop default, Ocean,
  any user-installed set from store.kde.org or a local pack
- Per-event volume, per-event sound, or silent — including per-app overrides
  for notifications

### Interaction
- Keybind presets: default / i3-vim / Mac-flavored / Windows-flavored / custom
- Tiling mode: off / KWin tiling / dwindle; gaps, border width, animation speed (0–2x)
- Gestures: full Linux gesture stack; per-gesture action mapping (3-, 4-, 5-finger)

### Panels & layout
- Any panel arrangement, any widgets (KDE widget ecosystem), multiple panels,
  auto-hide, blend/opaque modes
- **Experience Profiles** stay one-click; "Reset to profile defaults" restores the
  shipped look in one click when you've gone too far down a rabbit hole

### Advanced freedom (expert mode, always free)
- Config files fully accessible (`~/.config/`), documented layout of our keys
- Flatpak permission overrides GUI; podman/docker choice (Flow)
- Alternate shells (zsh/fish/nushell via Settings → Shells for Flow; any for all)
- Alternative compositor/session (opt-in, e.g. niri) in later phases

## What we don't ship / don't hide
- No locked themes, no "Pro" appearance tier, no paid cosmetics — ever
- No telemetry tied to what you customize (P4)
- No restarting-from-scratch required — everything hot-reloads or says what does

## Why this matters vs. macOS
- macOS: great defaults, locked depth (paid Rectangle, no icon theming, dock fixed)
- Windows 11: forced redesigns, one-way UX decisions, ads even in search
- SiD OS: macOS-grade polish **and** Linux-grade freedom — you get both, or just one,
  with zero guilt

## Guardrails (so freedom ≠ foot-guns)
- Escape hatches always: **Settings → Experience → Reset to profile defaults**
- Atomic rollback if a custom config ever wedges the session (P3)
- Community themes clearly labeled "unverified" if fetched from store.kde.org
- Our screenshots for CI always show the shipped defaults, not a customized one
