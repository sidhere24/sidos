# VM testing protocol

> Status: draft v0.1 · For maintainers with a local x86_64 machine
> Automated via `scripts/vm_gui_test.py`

## Building locally (verified on Windows + WSL Ubuntu, free)
```
# after installing WSL Ubuntu + podman inside it:
cp -r <repo> ~/sidos && cd ~/sidos
sudo podman build -f image/Containerfile -t localhost/sidos:ci .
sudo podman run --rm --privileged -v /var/tmp/out:/output \
  -v /var/lib/containers/storage:/var/lib/containers/storage \
  quay.io/centos-bootc/bootc-image-builder:latest build --type qcow2 --rootfs btrfs localhost/sidos:ci
```
NOTE: the ISO build needs a Fedora host; F45 moved repo configs to `/usr` and the
CentOS-based builder can't find them. GitHub hosted runners cannot run the builder
either (mount permission denied) — those CI jobs are intentionally disabled.

## What CI already guarantees
- bootc image builds (`bootc container lint` passes)
- Required docs present; trademark scan of shippable trees
- Image boots to a graphical login in QEMU (`.github/workflows/ci.yml` `qemu-smoke-test` job; screenshots + serial log archived as artifacts)

## What CI does NOT yet check (this doc exists for that)
- Sessions start (Plasma Wayland, theme applied)
- Update flow and automatic rollback
- Idle RAM, netstat telemetry sweep

## Local test — 20 minutes, free, no special hardware
1. Pull the latest install media from Releases:
   `sidos-phase2.qcow2` (pre-tagged `release-v0.0.0-phase2`), or build your own from
   `main` (`ci` workflow → "Build ISO + qcow2", manual dispatch).
2. Windows: `winget install SoftwareFreedomConservancy.QEMU` (Linux: `apt install qemu-system-x86 qemu-utils`; macOS: `brew install qemu`)
3. Run the smoke test:

   ```
   python scripts/vm_gui_test.py --disk sidos-phase2.qcow2 --out shots/ --count 5 --interval 20
   ```

4. Open `shots/shot-*.png` + `shots/serial.log`:
   - Expect: grub → boot output → SDDM/Plasma login → desktop
   - Fail fast on: kernel panic, stuck on `dracut`, black screen after login, missing display-manager
5. Update/rollback test (manual, once Phase 2 session is wired):
   boot → `rpm-ostree status` → pull an intentionally-broken commit → reboot → confirm previous image selected automatically
6. Telemetry sweep (after session is up):
   `guest$ sudo ss -tulpn` and grep for unexpected outbound connections beyond user's own traffic

## Hardware pass (when hardware exists)
Framework 13 + 2017 ThinkPad: boot, suspend/resume ×20, charge-cap GUI, Wi-Fi/BT, fingerprint, brightness keys.
Record results in docs/validation-log.md (create on first pass).
