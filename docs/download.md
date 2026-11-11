# Download & install SiD OS (early adopters)

> Status: pre-alpha. Nothing here is tested on real hardware yet. Use at your own risk.
> Official artifacts live on GitHub only — no separate site yet.

## Where things live
| Artifact | Where | Cost |
|---|---|---|
| OCI image (`ghcr.io/sidhere24/sidos:latest`) | GitHub Container Registry | free, public |
| ISO / qcow2 pre-releases | GitHub Releases tag `release-v0.0.0-phase2` | free, no account needed to download |
| Discussions (forum) | github.com/sidhere24/sidos/discussions | free |

## Option A — `bootc switch` from any Fedora Atomic system (works today)
Best for developers/testers on Silverblue / Kinoite / KDE Plasma Atomic:

```bash
sudo bootc switch --apply ghcr.io/sidhere24/sidos:latest
sudo systemctl reboot  # or: sudo bootc switch && sudo systemctl reboot
```

Your `/home` and data are kept. Rollback is built in: hold Shift at the GRUB menu
(or set a boot timeout) and pick the previous deployment — no admin skills needed.

## Option B — Test in a VM
1. Grab the qcow2 from Releases (or build your own: Actions → CI → "Build ISO + qcow2" → Run)
2. Linux (virt-manager): File → Import existing disk image
   macOS/Windows: install QEMU (`winget install SoftwareFreedomConservancy.QEMU`)
   ```
   qemu-img convert -O raw sidos-phase2.qcow2 disk.img   # if your hypervisor prefers raw
   qemu-system-x86_64 -m 4096 -smp 2 -accel tcg -drive file=sidos-phase2.qcow2,format=qcow2 -display gtk
   ```
3. Boot → GRUB → Plasma login screen → poke around

## Option C — Installable ISO (once the session is wired)
1. Download `sidos-phase2.iso` from Releases
2. Flash to USB with balenaEtcher (Win/Mac/Linux GUI) or `dd if=sidos-phase2.iso of=/dev/sdX bs=4M` (Linux)
3. Boot USB → installer → done (needs 15 min + 32 GB)

## Verification after install
```bash
bootc status     # shows: ghcr.io/sidhere24/sidos:<sha>, booted, rollbacks
cat /etc/os-release
```

## Want to help?
Bugs → Issues (label: `hardware`, `boot`, `session`). Discussion #1 welcomes
hardware reports. Read `docs/testing.md` for the 20-minute VM protocol.
