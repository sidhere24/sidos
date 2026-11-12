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
1. The qcow2 built for the smoke test is 5.6 GB and exceeds GitHub's 2 GB Release asset
   limit, so it is not published. If you want to try it, ask in Discussions and a
   contributor can share a build. (Building your own: Actions → CI → "Build ISO + qcow2".)
2. Linux (virt-manager): File → Import existing disk image
   macOS/Windows: install QEMU (`winget install SoftwareFreedomConservancy.QEMU`)
   ```
   qemu-img convert -O raw sidos-phase2.qcow2 disk.img   # if your hypervisor prefers raw
   qemu-system-x86_64 -m 4096 -smp 2 -accel tcg -drive file=sidos-phase2.qcow2,format=qcow2 -display gtk
   ```
3. Boot → GRUB → Plasma login screen → poke around

## Option C — Installable ISO (blocked, pending one Fedora host)
The ISO build is blocked on this machine: F45 moved RPM repo configs to `/usr`
(bootc relocatable repos), so the CentOS-based image-builder finds no repositories
for the Anaconda installer. Two working paths forward:
- A Fedora host once (any spare Fedora machine, or a Fedora container in WSL):
  `dnf install image-builder`, then
  `image-builder build --bootc-ref localhost/sidos:ci generic-iso`
- The bootc-installer ISO flow per Fedora's official ISO generation guide
Until then, Option A/B are the only download paths.

## Verification after install
```bash
bootc status     # shows: ghcr.io/sidhere24/sidos:<sha>, booted, rollbacks
cat /etc/os-release
```

## Want to help?
Bugs → Issues (label: `hardware`, `boot`, `session`). Discussion #1 welcomes
hardware reports. Read `docs/testing.md` for the 20-minute VM protocol.
