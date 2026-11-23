# Changelog

All notable changes to SiD OS. Format: keep a human-readable entry per release;
pre-alpha builds are identified by the commit SHA in ghcr.io tags.

## 2026-11-23
- Built a real installable ISO (6.4 GB) using Fedora 45 WSL + image-builder's
  `bootc-installer`; documented the helper image and build recipe. Not published to
  Releases due to GitHub's 2 GB asset limit.
- Verified image branding + switcher inside the published image; real boot screenshot added.
- Added SiD OS identity to the bootc image: original CC0 wallpapers (Classic/Studio/Flow),
  SVG logo, Papirus icons, Kvantum, Noto Sans + JetBrains Mono, Flathub pre-registered.
- Added `laptop-experiences` CLI with `switch`, `list`, `current` and a first-boot
  Classic autostart; full panel-layout switching remains planned.
- Fixed trademark gate violation in shipped config comments.
- CI: image built from repository root (`-f image/Containerfile .`); profile script syntax checked.

## 2026-11-12
- First real VM boot proof: image boots to Plasma first-run screen (WHPX/q35);
  recorded in `docs/validation-log.md`.
- Bootc-image-builder proved impossible on GitHub-hosted runners; those CI jobs disabled.
- ISO build documented as needing a Fedora host (F45 repo relocation).

## 2026-11-10
- Repo initialized, design principles, three profile specs, naming policy, forum and badges.
- Fedora Atomic (bootc) base confirmed; image builds and publishes to ghcr.io.
- QEMU smoke-test tooling and screenshot concepts added.
