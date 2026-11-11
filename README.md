# SiD OS

[![CI](https://github.com/sidhere24/sidos/actions/workflows/ci.yml/badge.svg)](https://github.com/sidhere24/sidos/actions/workflows/ci.yml)
[![Discussions](https://img.shields.io/github/discussions/sidhere24/sidos)](https://github.com/sidhere24/sidos/discussions)
An open-source Linux distribution designed **laptop-first**: instant sleep/resume,
best-in-class battery life, atomic updates with automatic rollback, and a polished,
ad-free, telemetry-free experience — free, and friendly to contributors.

- Status: pre-alpha, Phase 2 complete (CI smoke-tests boot+login, sddm in Containerfile, calamares in manifest, install-media on main push); Phase 3 in progress (power stack tuning on Framework 13 + ThinkPad; Phase 4 pending desktop polish pass HIG_gestures_snap).
- License (tooling/docs): MIT/CC-BY-SA — see `LICENSE`, `docs/LICENSE.md`
- Docs: [`design-principles.md`](docs/design-principles.md) · [`experience-profiles.md`](docs/experience-profiles.md) · [`profile-classic.md`](docs/profile-classic.md) · [`profile-studio.md`](docs/profile-studio.md) · [`profile-flow.md`](docs/profile-flow.md) · [`assets.md`](docs/assets.md) · [`customization.md`](docs/customization.md) · [`download.md`](docs/download.md) · [`onboarding.md`](docs/onboarding.md) · [`faq.md`](docs/faq.md) · [`rfcs/0000-rfc-template.md`](docs/rfcs/0000-rfc-template.md) · [`naming-and-trademarks.md`](docs/naming-and-trademarks.md)
- Strategy: **default to the experience Windows users know, deliver the values Mac and
  Linux users love, exterminate everything they hate.** See below.

## A taste of SiD OS

Three one-button **Experience Profiles** on one desktop (Plasma 6). Switch anytime in
Settings → Experience or with `laptop-experiences switch <name>`. These are concept
renders pending the first VM screenshots — the visual direction, not the final pixels.

| Classic (default, Windows-refugee familiar) | Studio (calm, Mac-refugee) | Flow (tiling, Linux-native) |
|---|---|---|
| ![Classic profile concept](brand/screenshots/classic-concept.png) | ![Studio profile concept](brand/screenshots/studio-concept.png) | ![Flow profile concept](brand/screenshots/flow-concept.png) |
| Familiar taskbar + Start-style App Grid, snap layouts & window groups | Dock + top menu bar, gesture-first, global menu | Tiling by default, mono fonts, keyboard-first |

Full specs: [`profile-classic.md`](docs/profile-classic.md) ·
[`profile-studio.md`](docs/profile-studio.md) ·
[`profile-flow.md`](docs/profile-flow.md)

## What it is

A Linux distribution — not a kernel and not a desktop widget collection. The goal is
the best possible laptop experience out of the box, with zero compromises on privacy
or user control.

## What it is not

- Not a general-purpose distro for servers/embedded (laptops only, for now)
- Not a reskin of another distro with a wallpaper swap
- Not a closed product — everything is open source and designed for contributors

## Repository map

```
brand/                logo (SVG) + original CC0 wallpapers + profile concept renders
docs/                 design principles, experience profiles, profile specs, naming policy
image/                bootc image skeleton + Phase 2 package manifest
scripts/              repo gates (trademark scan, etc.)
.github/              CI, issue/PR templates
```

## Contributing

See `CONTRIBUTING.md`. Docs-first: the design docs in `docs/` are the source of
truth. DCO sign-off, no CLA. AI tools welcome, understanding mandatory.

## Status & how to try

Pre-alpha, Phase 2. **There is no installable ISO yet** — the image builds, passes
`bootc container lint`, and publishes to ghcr.io on every push. What follows is the
honest state + the install paths that exist.

## Download & Install (early adopters)

Full guide: [`docs/download.md`](docs/download.md)

- **Option A** — `sudo bootc switch --apply ghcr.io/sidhere24/sidos:latest` from any
  Fedora Atomic system. Works today.
- **Option B** — test the qcow2 from Releases in a VM (QEMU/VirtualBox/virt-manager).
- **Option C** — installable ISO arrives when the session is wired; watch Releases.

## Community

GitHub Discussions: **https://github.com/sidhere24/sidos/discussions**
— ask questions, share ideas, report hardware quirks. Bugs → Issues; security →
`SECURITY.md`; conduct → Contributor Covenant.
