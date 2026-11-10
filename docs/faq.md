# SiD OS — FAQ (v0.1)

**Q: Is this a Debian Sid respin?** (most common question)
A: No. SiD OS is built on the **Fedora Atomic (bootc)** base — it shares nothing
with Debian's sid except a memorable name. "SiD" is a name we love, not a Debian fork.

**Q: What does "SiD" stand for?**
A: Nothing acronymic — it's short, sharp, and ours. (Side note we hear a lot: no
characters from any film are involved; our artwork is original.)

**Q: Do I need to know Linux to use this?**
A: No. The default Classic experience is designed for people who know Windows.
Zero terminal required for setup, updates, drivers, printers, or firmware.

**Q: Does SiD OS collect telemetry?**
A: Default: zero. Optional: anonymous crash reports (stack traces + hardware profile
only), off by default, one toggle to kill everything. Nothing else exists.

**Q: Can updates break my system?**
A: They shouldn't. The system is image-based — an update applies atomically or not
at all; if a boot fails, the previous image is used automatically. Worst case: one
reboot, not one afternoon.

**Q: When can I download an ISO?**
A: Not yet — the project is pre-alpha (Phase 1). Watch this repo; first bootable
images land in Phase 2. We publish honest progress, not vaporware timelines.

**Q: Which apps can I install?**
A: Everything on Flathub via the built-in store, plus native RPM packages for system
components. Steam works via Flatpak or native package. Proton/GE-Proton available
soon after first beta.

**Q: Can I try it without installing?**
A: Live-USB & VM images come with Phase 2. Early ISO language = experimental.

**Q: Will my printer/fingerprint/Wi-Fi work?**
A: We target "install → Wi-Fi, audio, Bluetooth, printing, webcam, fingerprint — zero
terminal" on reference hardware (Framework 13, ThinkPad X1/T series). Report misses
as bugs; we take hardware matrix seriously (see docs/design-principles.md P7).

**Q: How do I switch between Classic / Studio / Flow?**
A: Settings → Experience → pick one. It applies in ~2 seconds, no logout, and rolls
back automatically if anything goes wrong.

**Q: Why is the default Firefox?**
A: Independent engine, no bundled store/upsell, best privacy posture of the mainstream
browsers. Chrome/Chromium/Edge run fine as Flatpaks if you want them.

**Q: Is SiD OS free?**
A: Yes. Free as in freedom (MIT/CC-BY-SA content; packages keep upstream licenses)
and free as in zero cost. No paid tier exists.

**Q: How do I contribute?**
A: Read `CONTRIBUTING.md`: docs-first, DCO sign-off (no CLA), AI tools welcome but
you must understand your patch. Good-first-issues are tagged.

**Q: Windows migration — what about my apps?**
A: Browser-based work: flawless. Office: OnlyOffice/LibreOffice opens your files.
Adobe: no native equivalents — use alternatives (GIMP/Krita/Inkscape/DaVinci) or a
Windows VM. Games: Proton compatibility is excellent for Steam titles.
