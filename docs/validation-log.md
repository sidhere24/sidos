# SiD OS — validation log (real hardware & VM results)

> Entries are facts, not promises. Every row = what actually ran, when, and on what.

## 2026-11-12 — first boot (local Windows 10 Pro, WHPX, q35)
- Image: `localhost/sidos:ci` built from `main` @ `77b9f70` (plasmalogin + F45, Firefox+Chromium, Plasma 6 installed to spec)
- Disk: `qcow2` built by `quay.io/centos-bootc/bootc-image-builder:latest` (rootful podman in WSL2 Ubuntu 24.04)
- Boot: GRUB → Plasma Desktop first-run "Welcome to Plasma Desktop — Begin Setup" screen (Fedora branding — our installer that creates the user lands with the installer work)
- Result: **boots successfully to graphical OOBE**; no kernel panic; no test failures in console log
- Tooling: `scripts/vm_gui_test.py` via QEMU 11.1.0 (Windows); screenshots captured to a temp dir (not committed — contains no release art)
- Known gaps:
  - No user account inside the qcow2 (expected: bootc-image-builder builds system images, not installed desktops); first-boot creates it interactively
  - No Branding/user defaults applied yet (Phase: profile wiring) — desktop renders stock Fedora Plasma, not SiD OS themes
  - i440FX machine type panics (`IO-APIC + timer doesn't work`) — test harness now defaults to `q35`
  - WHPX accel works; writes are emulated slower than real hardware
- Status: **boot smoke test — PASS**. Session UX, updates/rollback, and battery behavior not yet tested.

## Pending
- ISO build (`--type iso`) — first attempt failed with transient `NoReposError` (depsolve mirror hiccup); retry in progress
- Re-run VM test with brand/theme packages once the profile work lands
- Hardware pass (Framework 13 / ThinkPad) — needs physical laptop
