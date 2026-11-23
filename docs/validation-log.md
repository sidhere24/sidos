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

## 2026-11-21 — branded image (Phase 2 identity pass)
- Image `localhost/sidos:ci` @ `8f0733cf22df`: SiD wallpapers/logo, Papirus/Kvantum,
  Noto/JetBrains fonts, Flathub, `laptop-experiences` CLI and first-boot Classic
  autostart. Verified inside the image (configs/quoting/trademark scan all clean).
- CI green (docs gates + profile script syntax + image build + ghcr.io publish).
- qcow2 boot + screenshot: **PASS** — branded qcow2 booted to Plasma first-run screen
  (WHPX/q35); real screenshot committed at `brand/screenshots/real-boot.png`.
  Serial log ends at a clean `fedora login:` (no panic), lint passed with 4 harmless warnings.
- Known gap: the first-run screen still shows "Fedora Linux" branding; SiD assets are
  installed and apply after account creation (first-boot hook + CLI). Full boot branding
  needs OOBE customization later.
- Known lint warning: flatpak repo metadata lives in /var; harmless, non-fatal.

## 2026-11-23 — installable ISO (Fedora 45 WSL)
- `image-builder` + `bootc-installer` produced a **6.4 GB installable ISO** from the
  published ghcr.io image (manifest finished successfully; MD5 implanted).
- Needed `image/Containerfile.iso` helper: copy EFI shim/grub into `/boot/efi`,
  gcdx64 alias, `/var/mnt`, and installer tooling (anaconda, mako, lorax, dracut deps).
- ISO copied to the user's Windows Downloads folder; not published to Releases
  (6.4 GB > GitHub's 2 GB asset cap). Build recipe documented in `docs/download.md`.
- Fedora WSL is now the supported local build environment; old Ubuntu WSL removed.

## Pending
- Verify the ISO actually installs on hardware/VM (only the build is verified).
- Re-run VM test with brand/theme packages once the profile work lands
- Hardware pass (Framework 13 / ThinkPad) — needs physical laptop
