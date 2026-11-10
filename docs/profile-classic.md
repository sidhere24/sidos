# Classic Profile — Detailed Spec (Windows-like default)

> Status: draft v0.1 · Primary audience: Windows 10/11 refugees · Default profile, ships everywhere
> Depends on: `design-principles.md`, `experience-profiles.md`

**Promise:** after install, a Windows user sits down and *knows where things are* —
and none of the reasons they left Windows 11 are anywhere in sight.

---

## 1. Layout (the muscle-memory layer)

```
┌─────────────────────────────────────────────────────────────┐
│ Desktop icons (opt-in: Devices, Recycle Bin, Home)          │
│                                                             │
│ ┌─────────────────────────────────────────────────────┐      │
│ │ Active window(s) — snap, maximize, tile             │      │
│ └─────────────────────────────────────────────────────┘      │
│                                                             │
│ [Start]  [Pinned apps]            [Tray • 12:30 • 🔊 • 🌐]   │
└─────────────────────────────────────────────────────────────┘
  Bottom taskbar, 48px, always visible (auto-hide optional)
```

- **Taskbar:** bottom, always visible by default; app icons pinned (browser, Files,
  terminal, settings, store); running apps grouped; hover previews; right-side tray:
  clock, network, volume, battery (with charge threshold + "Battery Saver" one-click),
  notification center (zero promotional content, ever), backup status
- **Start-style launcher ("App Grid", opened by bottom-left "Home" button or Super)**: pinned grid + search-first (types to
  search/app/files/web-fallback clearly labeled), user folders (Documents/Pictures/
  Downloads), power button bottom-right (Sleep/Restart/Shut Down + "Update & Restart"
  with rollback promise shown)
- **System tray:** muscle-memory match for a modern taskbar, minus: widgets upsell,
  AI assistants, chat-tool autostart, "suggested content"
- **Desktop:** clean; wallpaper: one beautiful calm default (not a clone of any MS
  asset); icons opt-in
- **Clock:** 24h or locale default; calendar flyout = plain calendar + agenda, no ads

## 2. Window management — "Layouts, actually good"

- `Meta+Z` opens a **Layout Picker** (2/3/4/6-region layouts + restore-what-was-snapped)
- Dragging a window to screen edges snaps halves/quarters (with subtle preview)
- **Window Groups:** snapped groups survive minimize/maximize; reopening from taskbar
  restores the *group* arrangement, per-user, persistent — the restorable-group
  interaction users love, implemented in KWin + a small helper service
- Maximize = true maximize state (distinct from full-screen video)
- Win+Home minimize-others; Win+↑/↓ maximize/restore; Win+Shift+←/→ move across monitors
- Alt+Tab: app-scoped if many windows, window-scoped option in Settings;
  Ctrl+Alt+Tab for keyboard-driven picker

## 3. Keyboard & mouse (Windows map)

- Super = Home menu; Super+E = Files; Super+D = show desktop; Super+L = lock;
  Super+A = Quick Settings (VPN, Wi-Fi, battery saver, night light, Focus mode /
  Do Not Disturb) — zero promotional content inside it
- Alt+F4, Win+Shift+S screenshot-to-clipboard (built-in, no account)
- Right-click = full context menu, no nested "show more options", no store ads
- Mouse: double-click rename? No — rename via F2; right-click menu top item semantics
  match Windows (Open, Pin to taskbar, Rename, Delete…)
- Touchpad: 2-finger scroll, 2-finger right-click, 3/4-finger swipe = workspace
  (configurable off), tap-to-click on

## 4. File manager (Dolphin, configured for the familiar paradigm)

- Sidebar: Home, Documents, Pictures, Music, Downloads, Devices (drives), Network,
  Trash — drive-centric mental model, not POSIX paths
- Default view: Details list; column headers Name/Date/Type/Size (click to sort)
- **Cut/paste across folders works** (move semantics), with drag-and-drop move default
- Path bar visible (editable breadcrumb), address field accepts `C:\`-style and POSIX
- File extensions always shown (the anti-Finder)
- Quick-look preview with Spacebar (kde-preview; opt-out)
- Devices view: drive icons with free-space bars; volumes auto-mounted on click
- OneDrive-style sync? **No proprietary cloud** — opt-in Sync GUI (Syncthing/Filen/provider of choice), never a mandatory account
- Recycle Bin parity: icon on desktop (opt-in), right-click empty/restore, full-empty on demand

## 5. Applications shipped in Classic

| Role | App | Windows parallel |
|---|---|---|
| Browser | Firefox (default) + Chromium preinstalled — both clean, no upsells | Edge → Firefox |
| Files | Dolphin | File Explorer |
| Terminal | Konsole (hidden for novices; reachable) | Windows Terminal |

*(Windows parallels are comparative labels for internal design docs only — see `naming-and-trademarks.md`. Shipped UI uses our own names.)*
| Office suite | OnlyOffice / LibreOffice Writer+Calc+Impress | MS Office |
| Mail/Calendar | Thunderbird (Island-styled) + GNOME Calendar-like flyout | Outlook-lite |
| Photos | Gwenview/Shotwell | Photos |
| Media | VLC/Celluloid | Media Player |
| PDF | Okular | Edge PDF |
| Store | GNOME-Software-like (Laskale) with **zero promotions** | MS Store |
| Calculator/Search | KRunner-style launcher + calculator built in | Search |
| Screenshot/Recording | Spectacle (Meta+Shift+S) | Screen Capture equivalent |
| Backup | Borgmatic GUI (system-image backup to external drive) | Backup and Restore |

Rule: zero app pins the user in by default — all core apps swappable in Settings
("Default apps" screen), backed by Flatpak where possible.

## 6. Updates & OOBE (the anti-Windows-11 first-run)

First-run wizard (skippable, 90 seconds):
1. Keyboard layout & timezone (auto-detected)
2. Profile confirm: "You'll get the Classic layout — like Windows. Change anytime: Settings → Experience."
3. **Privacy:** one screen, one toggle: "Send anonymous crash/usage data? [OFF]" (default OFF; local logs only)
4. Update mode: "Automatic (recommended) / Ask me first / Scheduled (nights)" — never forced reboot; rollback always offered after update
5. Browser import: offer import of bookmarks/passwords from Edge/Chrome (local, user-consented file-based import — no account API)
6. Account: "Use without account (recommended) / Sign in to community sync (optional)" — local account is fully functional
7. Done → desktop in ≤90 s; no 365 trial, no Game Pass, no Copilot, no OneDrive, ever

Update UX:
- "Updates available" tray icon → changelog → "Restart to apply" (with "Later tonight"/"This weekend")
- Failed update → automatic rollback + notification explaining what happened + link to known-issue
- Driver updates: user-controlled opt-in (the Windows pain point we flip: security drivers auto; feature/display drivers ask)

## 7. What Classic must NEVER ship (regression list)

Ads · suggested apps · "recommendations" · search ads · Copilot equivalents ·
required sign-in · forced reboots · forced feature removal · mandatory driver installs ·
lock-screen upsell · OEM-style nags · "tips & tricks" notifications · app stubs that
download the real app · hardware upgrade nagging (TPM or otherwise)

## 8. Settings — exactly two menus, not thirty

- **Everything essentials:** Wi-Fi, Bluetooth, Display, Sound, Storage, Battery & Power,
  Default apps, Experience Profile, Updates, Privacy (with the one toggle), Users
- **Advanced (collapsed by default):** kernel params, Flatpak remotes, power thresholds
  (charge cap 20–100% GUI), hibernation, printing, accessibility
- No "Get more themes in the store" bait; themes shipped in-image; custom themes via files

## 9. Assets & visual identity

- Original modern-flat icon set (commissioned or OFL/MIT open set; no competitor artwork, no derivative logos)
- Open humanist sans: Open Sans / Noto Sans (no competitor font files embedded, ever)
- Calm default wallpaper: mountain/geometry gradient (commissioned or CC0)
- Accent color: familiar blue by default; 6 choices in Settings
- Sounds: subtle open set (nudge, notify, chime) — no startup sound (off by default)

## 10. Validation

- First-run usability test with ≥10 real Windows refugees ("find X, do Y" tasks):
  success metric ≥80% unaided completion; no task requires terminal or documentation
- Screenshot-diff CI: taskbar/start menu/settings pinned layouts match spec per release
- Keybind conflict lint: no Classic bind shadows a critical system bind
- Power: profile switch must not alter suspend/threshold behavior (P1 invariant)

## 11. Open questions

- Start menu exact visual (fluent tile? simple grid?) — user research will decide
- Browser default: Firefox clean vs Firefox+hardening; consider enabling uBlock by default — decide after community feedback
- "Devices" view branding: verify no conflicts pre-release (see `naming-and-trademarks.md`)
- Startup sound and lock-screen quotes: default off; community can vote to enable
