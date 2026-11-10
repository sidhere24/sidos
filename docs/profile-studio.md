# Studio Profile — Detailed Spec (macOS-like)

> Status: draft v0.1 · Audience: Mac refugees · Switch anytime: Settings → Experience
> Depends on: `design-principles.md`, `experience-profiles.md`, `naming-and-trademarks.md`

**Promise:** a Mac user sits down and the machine *feels* like the one they left —
fast, calm, gesture-driven — minus the walled garden and the paid "fix the OS" tools.

---

## 1. Layout

```
┌──────────────────────────────────────────────────────────────┐
│ [SiD] AppMenu ……………… Focus • 12:30 • 🔊 • 📶 • 🔋            │  Top bar 28px
│                                                              │
│ ┌─────────────────────────────────────────────────────┐       │
│ │  Active window (full-height, no window bar)         │       │
│ └─────────────────────────────────────────────────────┘       │
│                                                              │
│        ▣ ▣ ▣ ▣ ▣ ▣ ▣ ▣   ← floating dock, centered          │
└──────────────────────────────────────────────────────────────┘
```

- **Top bar:** app name (global AppMenu) left, system tray right
  (Focus mode, clock, network, volume, battery, notification center — no ads)
- **Dock:** centered floating icons-only dock, magnification on hover (toggleable;
  off = minimal), autohide optional; running-app indicators (dot, our spin on the
  convention, not anyone's artwork)
- **Menu bar:** our implementation of a global menu (KDE AppMenu) — menus live in
  the top bar; follows focused app
- **Wallpaper:** calm gradient default (open art), one per release

## 2. Window management — "Expo + real snapping"

- `Super+W` = Exposé-analog (all windows tiled, keyboard-navigable)
- Full-screen = dedicated Space (per monitor), `Super+←/→` switches Spaces
- Three-finger vertical swipe = Exposé-analog; three-finger horizontal = switch
  Space; four-finger pinch = all desktops (libinput-gestures/KWin native)
- **Snapping that actually works**: halves, thirds, quarters, custom KWin layouts —
  plus `Super+Option+Arrows` fills left/right/top/bottom halves (the missing
  Windows-style muscle memory on a Mac, fixed here)
- `Super+Tab` = app switcher (grid), `Super+`+backtick = same-app switcher

## 3. Keyboard & mouse (Mac-flavored map)

- `⌘-style`: Ctrl+Space = launcher (search-first), Ctrl+Tab = switch Space,
  Ctrl+Q / Ctrl+, = quit/preferences (configurable to Super-parity for switchers)
- Full gesture set on touchpad; `tap-to-click` off by? (default on, matches Mac default? No — Mac default = **off** tap-to-click; ship off for fidelity, toggle one click away)
- Haptic-style clicks not possible on all hardware — see P2/P8 caveat: we tune for
  *feel* (smoothness), not force-touch parity
- `F3` = desktop, `F4` = launcher

## 4. File manager (Dolphin, Studio-configured)

- **Column view default** (Miller columns) — the one view people love from Finder;
  toggle: List / Grid / Column / Gallery
- **Spacebar quick-look** (kde-preview) — previews any file inline
- Path bar visible (editable breadcrumb); extensions always shown (we don't do hidden extensions)
- Sidebar renamed: Favorites (AirDrop-analog **absent** — see §7), Home, Desktop,
  Documents, Downloads, Devices, Network, Tags
- Cut/paste parity with classic expectations (Ctrl+X/C/V work exactly as anywhere)
- **Our Dolphin = the good parts of Finder without Finder's flaws** (cut-paste,
  always-visible path, real extensions, split panes)

## 5. Applications shipped in Studio

| Role | App | Mac parallel (descriptive only) |
|---|---|---|
| Browser | Firefox (clean) | Default browser |
| Files | Dolphin | Finder |
| Terminal | Konsole (visible option) | Terminal |
| Office suite | LibreOffice or OnlyOffice | iWork |
| Mail/Calendar | Thunderbird + calendar flyout | Mail/Calendar |
| Photos | Gwenview / Shotwell | Photos |
| Media | Haruna / Celluloid | QuickTime |
| PDF | Okular | Preview |
| Store | Flatpak-backed store, **zero promotions** | App Store |
| Launcher | Search-first launcher (Spotlight-analog UX, our implementation) | Spotlight |
| Screenshot/Recording | Spectacle (`Super+Shift+S`) | Screenshot |
| Backup | Borgmatic GUI — local system-image backup | Time Machine |

## 6. Updates & OOBE

Same wizard as Classic (`docs/onboarding.md`) with Studio pre-selected if
"Where do you come from? → Mac" was chosen. Battery-care GUI prominent (Mac users
wire-tied to charging habits). Rollback promise shown post-update.

## 7. What Studio must never do (regression list)

- Never paywall window management or clipboard history — both ship in-image, free
- Never lock the user to one cloud — Sync GUI is provider-agnostic
- Never ship fake "time machine" that eats disk silently — Borgmatic GUI shows
  target usage; user picks drive/schedule
- Never imitate trade dress: no SF Symbols, no Apple wallpaper, no traffic-light
  icons copied; our window controls are *inspired* (position, not shape)
- No "AirDrop" branding — direct LAN file sharing via KDE Connect (rename as
  "Nearby Share" in our UI) — interoperable, open, cross-platform

## 8. Settings — calm two menus

- **Essentials:** Wi-Fi, Bluetooth, Displays, Sound, Wallpaper, Battery & Power
  (charge cap!), Default apps, Experience, Updates, Privacy — one screen, no hunting
- **Advanced:** collapsed by default; kernel params, Flatpak remotes, thresholds,
  hibernation, accessibility
- Global search inside Settings for any setting name (keyboard-first)

## 9. Assets & identity

- Modern-light icon set, soft neutrals (Classic = higher contrast; Studio = softer)
- Studio humanist font stack (Noto/Open Sans + Inter); SF-metric-adjacent metrics,
  OFL-licensed only
- Dock/bar styling: translucency where the compositor allows, graceful fallback to opaque
- Sounds: subtle open set (chime on login, soft nudge) — no fanfare

## 10. Validation

- Mac usability test (≥8 recent switchers): "do this task with no tutorial" tasks;
  success metric ≥75% unaided (lower bar than Classic's Windows-refugee target —
  different onboarding defaults are acceptable if Settings is journey-simple)
- CI screenshot-diff: dock presence/position, top bar layout, window controls side
- Gesture smoke test on Wayland session
- Power-draw parity with Classic (P1 invariant)

## 11. Open questions

- Window-control button placement: left (Mac muscle memory) vs right (default on
  our base) — decide after user testing; both toggleable in Settings → Window buttons
- "Focus mode" naming vs "Do Not Disturb" — pick one, keep both keywords searchable
- Mail default: Thunderbird Island theme vs plain GTK-KDE bridge — visual unity test
