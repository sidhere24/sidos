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

## Option C — Installable ISO (verified working 2026-11-23)
A bootable bootc-installer ISO was built successfully in Fedora 45 WSL (6.4 GB).
It is **not hosted on GitHub Releases** — 6.4 GB exceeds the 2 GB per-asset limit —
so it must be built locally or via a self-hosted runner.

Verified build (Fedora 45 WSL):
```
sudo dnf5 install podman image-builder python3-mako
podman pull ghcr.io/sidhere24/sidos:latest
# build the helper image from image/Containerfile.iso (adds EFI files + installer tools):
podman build -f image/Containerfile.iso -t localhost/sidos-iso:ci image/
cd iso-out && image-builder build \
  --bootc-ref localhost/sidos-iso:ci \
  --bootc-installer-payload-ref ghcr.io/sidhere24/sidos:latest \
  --bootc-default-fs ext4 bootc-installer
```
Output: `bootc-fedora-45-bootc-installer-x86_64/bootiso/install.iso`.

Flash it to a **16 GB or larger** USB stick with balenaEtcher, or Rufus in **DD image
mode** (Windows; an ISO >4 GB cannot be written in ISO-image mode to a FAT32 stick).
Boot from USB → Anaconda → install; the installed system is the current ghcr.io
SiD OS image, with atomic rollback.

## Verification after install
```bash
bootc status     # shows: ghcr.io/sidhere24/sidos:<sha>, booted, rollbacks
cat /etc/os-release
laptop-experiences list    # classic / studio / flow
laptop-experiences switch flow   # dark, mono, high-contrast profile (applies instantly)
```

## Want to help?
Bugs → Issues (label: `hardware`, `boot`, `session`). Discussion #1 welcomes
hardware reports. Read `docs/testing.md` for the 20-minute VM protocol.
