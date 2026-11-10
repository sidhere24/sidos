# SiD OS — Naming & Trademark Policy

> Status: v0.1 · Applies to all shipped UI, assets, docs, and marketing

## 1. Rules

1. **In-product names must be our own or generic** ("taskbar", "menu", "devices").
   Never ship competitor UI names as our feature names.
2. **Assets must be original or open-licensed** (CC0/CC-BY/OFL/MIT/GPL). Never use
   Apple/Microsoft logos, glyphs, wallpapers, sounds, or their proprietary fonts.
3. **Competitor names may appear in internal docs only** as nominative, comparative
   references ("like the Windows Start menu"). Never in shipped UI strings, screenshots,
   icons, or marketing.
4. Evoke the familiar, never impersonate. If a name/asset could pass as the real thing,
   it's rejected.
5. Release checklist includes a trademark scan of all user-facing strings.
6. When in doubt: rename. There is no brand equity in "This PC".

## 2. Rename table (competitor term → our term)

| Competitor (docs only) | SiD OS in-product name |
|---|---|
| Start / Start menu | **Home** (bottom-left button; Super opens it) |
| Start-like launcher / Launchpad | **App Grid** (search-first grid) |
| This PC | **Devices** (drives & folders view) |
| Action Center | **Quick Settings** (VPN, Wi-Fi, battery saver…) |
| Snap Layouts / Snap Groups | **Layouts** / **Window Groups** (Meta+Z layout picker) |
| Fluent design / Fluent icons | **original modern-flat iconography** (commissioned, MIT) |
| Segoe | **Open Sans / Noto Sans** (humanist sans stack) |
| Snipping Tool | **Screen Capture** (Spectacle) |
| OneDrive / cloud lock-in | **Sync GUI** (provider-agnostic: Syncthing/Filen/…) |
| Windows Terminal | **Terminal** (Konsole) |
| Outlook | **Mail** (Thunderbird) |
| Edge PDF | **PDF** (Okular) |
| "Windows-like" / "macOS-like" / "MacBook polish" | allowed in design docs only; external name: **Classic** / **Studio** / **Flow** |

## 3. What stays legal-safe by default

- Generic terms: taskbar, desktop, folder, window, battery, wifi, theme — fine
- Descriptive compatibility claims in docs: "runs your existing apps" — fine with
  substantiation, no competitor logos implied
- OFL fonts (Open Sans, Noto, Inter), Papirus/GPL icons — fine with attribution
- Our own codenames: Classic, Studio, Flow, SiD OS — check domain/trademark before public launch

## 4. Not allowed, ever

- Microsoft/Apple logos, Start-flag glyph, SF Symbols, product wallpapers, their SFX
- Marketing lines implying affiliation ("the Windows replacement" is OK as comparison;
  "Windows 11, but better" as a slogan is borderline — use "familiar, minus the ads")
- Shipped UI copy using "Windows/macOS/Copilot/OneDrive" labels
- Font embedding of Segoe/SF

## 5. Release gate

Before any ISO ships: grep user-facing strings + all assets against §2 table;
icon set diff review; counsel spot-check on names. Failure = release blocked.

## 6. The SiD OS name — launch checklist

- "SiD OS" has no existing Linux distribution match (searched 2026-11); hits are
  Debian "sid" references (Debian unstable) — expect **"it's a Debian Sid respin?"
  confusion**; our answer in FAQ: unrelated, bootc/Fedora base
- Before public launch: domain availability (`sidos.org`/`sid-os.org`), trademark
  search (USPTO/EUIPO) for "SiD OS"/"SiD", and social handles
- Side-effect association some will read into it: Toy Story's Sid (works in our favor
  for a playful brand — but assets must not use character likenesses or the IP)
- Legal review of: name, logo, tagline, and the "SiD" styling in wordmarks
- Until then, all artifacts are internal; no store listings, no press, no public repos under the brand
