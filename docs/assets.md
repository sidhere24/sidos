# Assets shortlist — open-licensed, no trade dress copied

> Status: v0.1 · All items verified at bundle time; licenses re-checked before each
> release (naming-and-trademarks.md §5). "Like" = visual influence only, never files.

## Icon themes
| Profile | Candidate | License | Notes |
|---|---|---|---|
| Classic | **Papirus-Light** (re-skinned accent to our blue) | GPL-3.0 | Largest coverage; original art, no competitor files |
| Studio | **Papirus-Light** soft neutral variant / **KDE Breeze Icons** | GPLv3 / LGPL-3.0 | Breeze is native to Plasma — best consistency |
| Flow | **Papirus-Dark** high-contrast | GPL-3.0 | Dark density, zero ambiguity at small sizes |

All shipped as re-colored *derivatives* with proper license+attribution in
`/usr/share/licenses/sidos-icons/`.

## Cursors
KDE Breeze cursors (LGPL-3.0) with two re-skins (light Classic, dark Flow) — stock,
no custom artwork needed for Phase 2.

## Fonts (all OFL-1.1)
| Role | Font | Profile |
|---|---|---|
| UI text | **Noto Sans** | Classic / Studio |
| UI display | **Inter** | Studio headings |
| UI mono | **JetBrains Mono** (OFL) | Flow default, all profiles' terminals |
| Docs/code | JetBrains Mono | repo |

## Wallpapers
One original per release — commissioned CC0 works (geometric gradients, terrain
silhouettes). No stock photo-of-photography risks. Store sources in `brand/`.

## Sounds
freedesktop sound theme components (CC BY-SA 3.0) — nudge, notify, login chime —
re-embedded with attribution. No startup fanfare by default.

## GTK/Kvantum bridge assets
Kvantum (LGPLv3) configs shipped to theme Qt+GTK apps uniformly per profile —
config files are ours (MIT), engine is theirs.

## Explicitly rejected
SF Symbols / SF Pro / Segoe UI / Segoe Icons / Aptos Fluent icons — **never** bundled.
Papirus is re-skinned, not traced, from any competitor asset. If a contributor
wants to "make it look more like X," the answer is: make it look like *our* thing,
better.

## Brand assets to create (open items, need designer or commission budget)
- Logo (mark + wordmark) for "SiD OS"
- 3 default wallpapers (Classic/Studio/Flow)
- Boot/splash artwork (Plymouth theme)
- Installer artwork (Calamares theme)
- Icon set accent color QA pass
