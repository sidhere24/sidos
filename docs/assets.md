# Assets — the best free themes, wallpapers & sounds (researched 2026-11)

> Goal: the finest free/open assets on the web, chosen deliberately. All licenses
> re-verified at bundle time (naming-and-trademarks.md §5).
> "Like" = visual influence; never bundled competitor files.

## GTK / Qt theming per profile
| Profile | Theme | Where | License |
|---|---|---|---|
| Classic | **Fluent-gtk-theme** (vinceliuice) Light, accent ours | github.com/vinceliuice/Fluent-gtk-theme | GPL-3.0 |
| Studio | **WhiteSur-gtk-theme** (vinceliuice) — macOS-BigSur-inspired | github.com/vinceliuice/whitesur-gtk-theme | GPL-3.0 |
| Flow | **Catppuccin** (Mocha) GTK + Kvantum | github.com/catppuccin/catppuccin · catppuccin/kde · catppuccin/kvantum | MIT palette / GPL forks (verify per repo) |
| All (Extras) | **Layan** (modern flat) | store.kde.org · AUR `layan-*` | GPL-3.0 / CC-BY-SA (verify) |
| All (Extras) | **Arc / Nordic** (high-contrast alternates) | store.kde.org | GPL / CC-BY-SA |

Qt side: every profile driven through **Kvantum** (LGPLv3) with upstream Kvantum
configs; Breeze fallback for any unstyled widget.

## Icons
| Profile | Icons | License |
|---|---|---|
| Classic | **Papirus-Light** (+ recolored accent) | GPL-3.0 |
| Studio | **Papirus-Light (soft)** / **WhiteSur icon theme** | GPL-3.0 |
| Flow | **Papirus-Dark** (high density) | GPL-3.0 |
| All (Extras) | **Layan-icon-theme** | CC-BY-SA / GPL (verify) |

Pre-bundled accent variants ship in-image so users never recolor.

## Cursors
- **KDE Breeze** (LGPL-3.0) — default, all profiles
- **Bibata-Modern** (Light/Ice/Amber/Classic) (GPL-family) — optional
- **Layan cursors** — alternate (GPL / CC-BY-SA, verify)

## Notification & event sounds
- **sound-theme-freedesktop** (CC BY-SA 3.0) — spec-compliant default; full event
  set; ships everywhere, freedesktop notification-sound spec compatible
- **KDE Ocean** sounds — Studio/Classic default feel; clean, no fanfare (verify license line)
- Community sets, user-installed via Settings → Notifications/Sound from store.kde.org:
  **Wood**, **Maple**, other top-rated sets — we link to them, we never re-license or
  bundle them; the user's sound theme choice stays theirs
- No startup fanfare by default; Classic/Studio subtle; Flow near-silent

## Wallpapers — bundle web finds, not only generated art
1. **NASA public-domain imagery** (public domain) — Earth/Landsat/Blue Marble —
   ideal deep-blue Classic backdrop. https://www.nasa.gov/multimedia/imagegallery
2. **Wikimedia Commons CC0 / CC-BY** — 2 per theme; verify each file's license line;
   keep attribution in `/usr/share/doc/sidos-wallpapers/ATTRIBUTION`
3. **GNOME / KDE official backgrounds** (CC BY-SA 3.0) — gorgeous; bundle with attribution
4. Our generated CC0 set (`brand/wallpapers/`) stays as placeholders/fallback;
   final picks get screenshot-diffed into CI before release

## Fonts (OFL-1.1)
Noto Sans (Classic/Studio UI), Inter (Studio display), JetBrains Mono (Flow/mono),
CaskaydiaCove (user opt-in).

## Theme freedom (the differentiator vs. macOS's "Apple knows best")
Every theme above is user-installable in one click from Settings → Appearance.
See `docs/customization.md`.

## Explicitly rejected (all profiles)
SF Symbols, SF Pro, Segoe UI/Icons, Aptos/Fluent *files* as proprietary art,
any asset without a clear license line, AI "lookalike" of Apple/Microsoft art.

## Attribution file
`/usr/share/licenses/sidos-assets/` lists every bundled theme/icon/font with name,
upstream URL, license, and modification note (recolors count as modifications).
