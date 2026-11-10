# SiD OS image (bootc)

> Status: bootc base confirmed (D1, 2026-11). This builds in CI as a skeleton;
> it is not a working OS yet.

What this will become:

- Base: `quay.io/fedora/fedora-bootc:latest` (pin a digest before first public
  tag for reproducibility — track Fedora releases deliberately, not blindly)
- Read-only `/usr`, atomic upgrades, automatic rollback on failed boot (P3)
- Contents (Phase 2): curated Plasma 6 session, Classic experience profile as
  default, Flatpak remotes preconfigured, power stack tuned (TLP *or* ppd —
  Phase 3 benchmarks on Framework 13), fwupd, RPM Fusion codecs, Firefox
- CI: per-PR image build; then QEMU smoke test (boot, suspend, update, rollback);
  then hardware runs (Framework 13 + 2017 ThinkPad)

Build locally (once podman + network are available):

```
podman build -t sidos image/
```
