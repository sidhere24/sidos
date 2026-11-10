# Image build (bootc, pending decision D1)

> **Do not build/ship from this directory yet.** The bootc vs classic Fedora base
> decision (design-principles.md §10 question 1, decision D1) is not final.

Plan once decided:

- Base: Fedora Atomic-style image (bootc) — read-only `/usr`, atomic upgrades,
  rollback on failed boot (P3)
- SRPM/tooling: rpm-ostree/bootc, fedora-bootc base image
- Contents: curated Plasma 6 session, our configs, Flatpak remotes preconfigured,
  Classic experience profile default, power stack (TLP *or* ppd — Phase 3 benchmark)
- Update channel: stable + testing; kernel stable tracked promptly (7.4 expected LTS)
- CI: build image per PR, boot smoke-test in QEMU, rollback test, then (hardware lab)
  Framework 13 + 2017 ThinkPad runs (P10, P7, P8)

`Containerfile` in this directory is a **skeleton, not a working build**.
