# LaptopOS — Experience Profiles ("One flip of a button")

> Status: draft v0.1
> Depends on: `design-principles.md`
> Target: KDE Plasma 6.x, curated

## 1. The idea

Users don't want a Linux distro. They want *an* experience they already trust:
Windows' familiarity, macOS's polish, or the Linux power-user setup. Instead of
picking one and disappointing two camps, LaptopOS ships **three curated experience
profiles on top of one desktop**, switchable with a single toggle — like switching
a phone's theme, but the *entire* interaction paradigm flips with it.

This is not three DEs. It is **one Plasma 6 base, three skins-with-behavior**.

## 2. The three profiles

**Default profile: Classic (Windows-like)** — primary audience is Windows refugees;
Stock feel of a familiar modern taskbar machine (taskbar, Home button, Window Groups) minus every pain
point that drove them out. The installer/onboarding asks "Where do you come from?" and
pre-selects the matching profile; one click to switch later.

### 2.1 "Classic" — Windows-like (DEFAULT)
For users fleeing Windows 10/11. Familiarity is the feature.
Full spec: [`profile-classic.md`](profile-classic.md).
- Bottom taskbar + Start-like launcher (pinned apps left, tray right)
- Layouts + restorable Window Groups (`Meta+Z`-style layout picker) — see `profile-classic.md`
- File manager (Dolphin) preconfigured for the drive-centric paradigm: Devices view
- AI-assistant pain-points inverted: zero ads, zero suggestions, no upsell
- Default font stack: Open Sans / Noto Sans (humanist)
- Keyboard model: familiar map (Super = Home menu, Alt-Tab window cycling)

### 2.2 "Studio" — macOS-like
For Mac refugees. Polish and calm are the features.
- Floating bottom dock (Window Button/Icons-Only Task Manager), top menu/panel with app name + clock + tray
- Global-menu approximation: KDE's Appmenu widget in the top panel (menu bar per app)
- Finder-style file manager: column/gallery view defaults, quick-look previews, path bar visible
- Gesture-first: 3/4-finger swipes for spaces/Exposé-analog
- Traffic-light-inspired window controls on the left (configurable; kept familiar to switchers)
- Keyboard model: ⌘-flavored shortcut map (Cmd/Ctrl remix — we control keybinds, so offer "Mac-style binds")
- Open assets only — **never Apple trademarks/logos/wallpapers**; evoke, don't impersonate

### 2.3 "Flow" — Linux-native / power
For enthusiasts and devs. Speed and control are the features.
- Tiling-first: KWin tiling layouts + optional `niri`/`Hyprland`-style layouts (KWin 6 tiling covers most)
- Minimal panels, keyboard launcher front and center (KRunner / fuzzel)
- Monospace presets, dense information display, power-user defaults (full Dolphin toolbar, terminal integration)
- Tiling shortcuts, focus-follows-mouse optional, virtual-desktop-centric workflow
- For users who read this doc and smiled at "dotfiles"

## 3. What the one button actually flips

Plasma **Look-and-Feel packages** + a settings hook flip, atomically:

| Layer | Classic | Studio | Flow |
|---|---|---|---|
| Panel layout | taskbar | dock + top bar | minimal/launcher |
| Color scheme / Kvantum | light, blue accent | light, soft neutral | dark, high contrast |
| Icon theme | fluent-like open set | SF-Symbols-like open set | Papirus-Dark |
| Cursor | Classic open cursor | Studio open cursor | distro-native |
| Font & DPI | Open Sans / Noto | Studio humanist stack | mono-leaning |
| Keybinds | Windows map | Mac map | vim-friendly map |
| Gestures | basic snap | full spaces swipes | tiling gestures |
| Window rules | snap-group presets | focusedsingle-app rules | tiling + floats |
| Launcher | kickoff-like | Spotlight-like search | KRunner dense |
| Sounds | Classic open set | chime-like open set | subtle only |

One `lookandfeel-applet` / `laptop-experiences` CLI (`laptop-experiences switch studio`) does:
checkout L&F package → `plasmashell --replace` → swap kwin configs → swap input/gesture
profiles → done in <2 s, no logout. KRunner action + Settings module + first-boot wizard
all call the same switch.

## 4. What the button cannot flip (and we won't pretend it can)

- Toolkit: Qt vs GTK apps keep their own look; we ship Kvantum/GTK theme bridges to make it 90% seamless
- App semantics: e.g., Studio can't teach Finder's muscle memory to Dolphin — but we preconfigure views/keys to match 90% of it
- Screen-reader and a11y: all three profiles must pass the same accessibility gate (P6)
- Login screen: one greeter, themed neutrally

## 5. Implementation notes

- Plasma base only. **Do not** bundle GNOME/Xfce as selectable DEs — different session,
  different bugs, triple support. A future "Community GNOME Spin" is a separate image.
- Assets: open licenses only (Papirus, KDE Breeze derivatives, Google Fonts, OFL sounds).
  No Apple/Microsoft assets; legal review before publishing each profile.
- Reversibility: switching is transactional — failed switch reverts to previous profile;
  btrfs snapshot taken on profile switch (fits P3 rollback philosophy).
- Determinism: profiles are versioned packages in our repo; CI builds + screenshots each
  profile on every PR; releases signed (P10).
- Telemetry: none. Profile choice is local, stored in `~/.config/laptop-experiences.conf`.

## 6. CI & validation

- Boot → switch Classic→Studio→Flow ×10 — no crash, session intact
- Screenshot-diff smoke tests (panel presence, dock position, taskbar icons)
- Keybind conflicts linted per profile; gesture maps validated on Wayland
- Power-draw regression: profile switch must not alter power defaults (P1 invariant)

## 7. Risks & mitigations

| Risk | Mitigation |
|---|---|
| 3x QA/support burden | Profiles are config packages, not forks; shared CI matrix; user picks one, docs cover all |
| Theme drift / broken after Plasma update | Pin profile packages to Plasma versions; CI screenshot gates |
| "Why does my file manager look different?" | Onboarding tour + profile name shown in Settings; switch docs |
| Trademark complaints (macOS-like) | Evoke-only rule; legal review; open assets; rename if needed ("Studio" is our name, not theirs) |
| A11y parity slips | A11y test per profile is a release blocker |

## 8. Decision recorded

KDE Plasma is the base DE precisely because of this feature (see desktop analysis).
GTK/GNOME purists are not the target; a future Community GNOME Spin is the escape valve.
GNOME-vs-KDE "which is better" debates become moot for users: they taste both paradigms
and pick per-machine on one click.

## 9. Non-negotiables across ALL profiles (the Mac/Linux floor)

Whatever profile is active, these never change:
- Offline-first: full functionality with zero network access; no mandatory sign-in, ever
- Zero ads, zero telemetry, zero upsell — in Settings, search, notifications, taskbar
- One obvious privacy switch disabling every optional network call we ship
- Atomic updates with automatic rollback on failed boot
- Battery/IEEE defaults: charging thresholds, suspend behavior, power profiles as GUI controls
- Full local admin rights — the user owns the machine; repairable, inspectable, documented
- No forced features, no forced redesigns, no forced accounts, no expiration dates
- A11y parity: every profile passes the same accessibility gate before release
