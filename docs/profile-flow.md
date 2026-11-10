# Flow Profile — Detailed Spec (Linux-native / power user)

> Status: draft v0.1 · Audience: Linux natives, devs, enthusiasts
> Depends on: `design-principles.md`, `experience-profiles.md`

**Promise:** the machine disappears into the task. Nothing between you and the
kernel — but also nothing between you and safety: rollback is still one reboot away.

---

## 1. Layout — tiling first, panels last

```
┌──────────────────────────────────────────────────────────────┐
│ Terminal (60%)        │ Editor (40%)                          │
│                       │                                        │
├───────────────────────┴────────────────────────────────────────┤
│ Browser (full width, workspace 2)                              │
└──────────────────────────────────────────────────────────────┘
  No persistent panels by default (toggle one: bottom thin bar)
  Bottom-left workspace indicator only (mono font)
```

- **No decorative chrome**: windows borderless or 1px accent border; client-side
  decorations preferred (native Wayland)
- **KWin tiling layouts** active (or `niri`-style dwindle via KWin scripts) —
  full-screen, halves, thirds, grid; master-stack option
- **Workspace-centric**: 4 vertical workspaces + zoom; `Super+1..4` jumps
- Launcher: **KRunner/fuzzel-class dense launcher** — type-to-run, calculations,
  unit conversion, dictionary, calculator DSL built in
- **Mono font default** (JetBrains Mono / Noto Sans Mono, OFL); high-contrast dark

## 2. Keyboard — vim-friendly, zero mouse required

- `Super+Enter` terminal; `Super+Q` close window; `Super+F` fullscreen; `Super+H/V` split
- `Super+arrows` focus between windows; `Super+Shift+arrows` move window
- `Super+Space` focus-next-window (cyclic); `Super+1..9` workspace select
- **Terminal = tmux-like everywhere**: `Super+T` new tab, `Super+W` close tab
  (mappable in Settings; Wayland-safe conflicts avoided via keybind lint)
- Optional **i3/sway-parity bindings** toggle (full vim mode: `Super+hjkl` focus,
  `Super+Shift+hjkl` move) — one checkbox, default off

## 3. Power user defaults (the part we don't hide)

- Konsole full chrome visible (tabs, splits, transparency optional)
- Dolphin toolbar fully visible + terminal panel toggle (`F4`)
- `flatpak permissions` exposed in app context menu (right-click → Permissions)
- System tray includes: Network, Bluetooth, Battery (with TLP thresholds),
  KDE Connect, Night Color, **update available** (subtle, informative)
- htop/btop pinned in launcher results; system info one command (`sidos-info`)

## 4. Applications shipped in Flow

| Role | App | Notes |
|---|---|---|
| Browser | Firefox (default) + Chromium | Proton runs Steam natively (available, opt-in) |
| Files | Dolphin | Full toolbar, splits |
| Terminal | Konsole | zsh default? (no — bash; zsh snap-in via Settings → Shell) |
| Editor | Kate | Preconfigured sane defaults; LSP ready |
| VCS | git + delta + lazygit preinstalled | opt-out per component |
| Office | LibreOffice | Plus OnlyOffice Flatpak in store |
| Containers | podman preinstalled | daemonless; no docker shim unless opted-in |
| Debug | gdb, strace, perf | Flow is the debug-friendly profile |

## 5. OOBE & updates

Same wizard; "Linux" origin pre-selects Flow. Update story identical (atomic image,
rollback). Flow shows **kernel changelog** inline on update screen — Linux natives
actually read it (and they'll thank us when 7.4 LTS lands).

## 6. What Flow must never do

- Never force a visible launcher you didn't ask for
- Never hide logs: `journalctl -f` is one command away; boot analysis exposed
  (`systemd-analyze`); no "we simplified this away"
- Never disable sandbox escapes for "safety" without disclosure (polkit rules are
  documented, audit-friendly)
- Never nag about Expert Mode toggles — Flow's Settings page lists every default
  with a toggle, with honest impact notes (plain English, no shame)

## 7. Settings — one screen, everything exposed

- **Flow settings:** single scrollable page: keybind presets (i3/vim/mac/Windows/default),
  tiling mode, gaps, border size/color, mono font size, terminal choice, shell choice,
  flatpak defaults, podman, Flatpak remotes list — keyboard-navigable, searchable

## 8. Assets & identity

- Dark, high-contrast icon set (Papirus-Dark class); accent: green (#3DA639-ish,
  ours, not anyone's brand)
- Mono fonts, 1px borders, zero gradients
- Sounds: minimal; terminal bell = soft off by default

## 9. Validation

- Power-user test: install from ISO, reach dev-ready (git clone + podman run +
  Flatpak install) in ≤10 minutes unaided
- Keybind linter: zero conflicts across Flow presets
- tiling smoke test: 10 windows across 4 workspaces, focus/move cycle matrix
- Power-draw parity with Classic/Studio (P1 invariant)

## 10. Open questions

- zsh vs bash default for Flow? (currently bash — least surprise; vote pre-alpha)
- Ship `lazygit`/`btop` in-image vs first Flatpak install? (lean: in-image; Flow users expect them)
- Tiling via KWin scripts vs offering `niri` as an opt-in compositor session in Phase 4+
