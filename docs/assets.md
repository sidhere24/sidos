# Assets — open-licensed themes & artwork (researched 2026-11)

> All items are open-licensed. Licenses re-checked at bundle time (naming-and-trademarks.md §5).
> "Like" = visual influence; never bundled competitor files.

## GTK / Qt theming per profile
| Profile | GTK theme | License | Notes |
|---|---|---|---|
| Classic | **Fluent-gtk-theme** (vinceliuice) — Light, accent #4B8AC4 | GPL | Fluent-design-styled; Light+Dark; GTK3/GTK4/libadwaita(ish); actively maintained |
| Studio | **WhiteSur-gtk-theme** (vinceliuice) — macOS-BigSur-inspired | GPL | Full port incl. window decorations; use Light for default Studio |
| Flow | **Catppuccin (Frappe/Mocha)** for GTK + Kvantum | MIT palette / GPL forks | Dark, high-contrast friendly; pairs with JetBrains Mono |

Qt side: all three driven through **Kvantum** (LGPLv3) with matching upstream
Kvantum configs (Fluent and WhiteSur ship Kvantum variants; Catppuccin has Kvantum
ports). Breeze remains fallback for any unstyled widget.

## Icons
| Profile | Theme | License |
|---|---|---|
| Classic | **Papirus-Light** + recolored accent | GPL-3.0 |
| Studio | **Papirus-Light (soft)** or **WhiteSur icon theme** | GPL-3.0 |
| Flow | **Papirus-Dark** (high density) | GPL-3.0 |

Papirus ships with cp/fossplanet-compatible recolors; we ship pre-bundled accent
variants so users never recolor.

## Cursors
- **KDE Breeze cursors** (LGPL-3.0) — all profiles, default
- **Bibata-Modern** (vinceliuice, GPL-family) — optional re-skins (light/dark),
  verify license line at bundle time

## Fonts (OFL-1.1)
Noto Sans (UI), Inter (Studio display), JetBrains Mono (Flow/terminals).

## Sounds
freedesktop sound theme components (CC BY-SA 3.0) — nudge, notify, login chime;
attributed in /usr/share/licenses. No startup fanfare by default.

## Wallpapers (original, Phase 2 deliverable)
- Classic — calm blue gradient ridge, generated/commissioned CC0 (`brand/wallpapers/`)
- Studio — soft neutral horizon (`brand/wallpapers/`)
- Flow — near-black with single green accent line (`brand/wallpapers/`)

## Logo / brand
Hand-built SVG mark (`brand/logo.svg`) — original, ours, no influence claims.
Plymouth boot theme + Calamares theme = Phase 2 (art once approved by project).

## Explicitly rejected (all three profiles)
SF Symbols, SF Pro, Segoe UI/Icons, Aptos/Fluent icons as files, WhiteSur *files*
used unchanged as "Apple assets" (they're GPL artwork — fine to bundle with
attribution, never rebranded as Apple's), generated "looks exactly like macOS" art.

## Attribution file
`/usr/share/licenses/sidos-assets/` must list every bundled theme/icon/font with
name, upstream URL, license, and modification note (recolors count as modifications).
