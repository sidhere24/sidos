# SiD OS

An open-source Linux distribution designed **laptop-first**: instant sleep/resume,
best-in-class battery life, atomic updates with automatic rollback, and a polished,
ad-free, telemetry-free experience — free, and friendly to contributors.

- Status: pre-alpha, Phase 2 skeleton (bootc image + docs complete)
- License (tooling/docs): MIT/CC-BY-SA — see `LICENSE`, `docs/LICENSE.md`
- Docs: [`design-principles.md`](docs/design-principles.md) · [`experience-profiles.md`](docs/experience-profiles.md) · [`profile-classic.md`](docs/profile-classic.md) · [`profile-studio.md`](docs/profile-studio.md) · [`profile-flow.md`](docs/profile-flow.md) · [`assets.md`](docs/assets.md) · [`onboarding.md`](docs/onboarding.md) · [`faq.md`](docs/faq.md) · [`rfcs/0000-rfc-template.md`](docs/rfcs/0000-rfc-template.md) · [`naming-and-trademarks.md`](docs/naming-and-trademarks.md)
- Strategy: **default to the experience Windows users know, deliver the values Mac and
  Linux users love, exterminate everything they hate.** See below.

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
brand/                logo (SVG) + original CC0 wallpapers
docs/                 design principles, experience profiles, profile specs, naming policy
image/                bootc image skeleton + Phase 2 package manifest
scripts/              repo gates (trademark scan, etc.)
.github/              CI, issue/PR templates
```

## Contributing

See `CONTRIBUTING.md`. Docs-first: the design docs in `docs/` are the source of
truth. DCO sign-off, no CLA. AI tools welcome, understanding mandatory.

## Status & how to try

Pre-alpha, Phase 2 skeleton. There is no ISO yet — nothing to install. The full
design is written (principles, three experience profiles, onboarding, assets,
FAQ, naming policy). The image build is scaffolded and runs in CI. Watch this
repo; first bootable images land with Phase 2 completion.
