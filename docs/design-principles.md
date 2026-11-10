# SiD OS — Distro Design Principles

> Status: draft v0.3 · name: **SiD OS** · laptop-first Linux distribution
> Audience: maintainers, contributors, and future-us

---

## 1. Mission

Build the **best Linux distribution for laptops** — the one that makes a laptop feel
finished: all-day battery life, instant sleep/resume, rock-solid updates, and a
coherent, polished desktop. Free, open source, and welcoming to contributors.

**The one-sentence positioning:**
> Everything you love about Windows' familiarity, a MacBook's battery and polish, and
> Linux's freedom — with none of the ads, telemetry, walled gardens, or forced
> hardware retirement. Primary target: Windows refugees; Mac and Linux users are
> first-class citizens, not secondary targets. See §6 for the positioning rules.

We do not aim to be "another Arch respin." We win by being **opinionated about the
laptop experience** above all else.

---

## 2. Research summary — what people actually like and dislike

Sources: Stack Overflow Developer Survey 2025, JumpCloud/Computerworld IT survey
2025, Bulldogjob 2025, NixOS 2025 community survey, Windows Central, Gizmodo,
XDA, HowToGeek, Ars Technica, Engadget, Abanoub Hanna, PrestoMyPC, CommandLinux,
ComputeForGeeks, LWN.net, The New Stack, The Register, Tom's Hardware, and threads on
r/linux, r/mac, r/windows, r/linuxquestions, r/Fedora, r/debian, r/desktops,
Framework Community forums.

### 2.1 What people love about Windows (and will miss/expect)
- **Familiarity** — muscle memory, conventional UI, nothing to re-learn
- **Software & game compatibility** — decades of apps and games "just work"
- **Gaming ecosystem** — Game Pass, Steam day-one support, DX11/12, anti-cheat
- **Microsoft Office** — real, native, ubiquitous
- **Snap Layouts & Snap Groups** — restorable window arrangements users "can't live without"
- **Hardware breadth** — any laptop, any peripheral, usually plug-and-play
- **Cost flexibility** — from budget to premium
- **WinPE / troubleshooting culture** — documented fixes for everything

### 2.2 Why people hate Windows 11 (our opening)
- **Ads & upsells everywhere** — Start menu, lock screen, Settings, Widgets, Notepad
- **Forced telemetry** — required diagnostics can't be fully disabled; hundreds of
  tracking settings to hunt down; no single off switch
- **Copilot/AI forced on users** — dedicated key, taskbar pin, AI in Notepad/Paint,
  Recall continuous screenshots; feels like a marketing mandate, not a user benefit
- **Mandatory Microsoft account** — local account hidden in OOBE; OneDrive/M365 nagging
- **Bloatware & legacy cruft** — preinstalled app stubs, background services eat RAM
- **Windows Update reboots** — forced, long, unskippable driver updates
- **TPM 2.0 hardware gatekeeping** — told perfectly good PCs they were obsolete
  (this directly drove the 2025 "switch to Linux" wave after Windows 10 EOL)
- **UI regressions with no upside** — extra clicks for common tasks, ads in search results

### 2.3 What people love about macOS (our design bar)
- **Battery life** — Apple Silicon: all-day, often 2–3x x86; #1 most-repeated praise
- **Sleep/resume is instant** — milliseconds, not minutes
- **Best-in-class trackpad** — glass, haptics, gestures; "the feature I'd miss most"
- **Stability** — "it just doesn't crash"; no bluescreens; uptimes measured in months
- **The ecosystem** — Handoff, AirDrop, Universal Clipboard, iCloud sync, iPhone
  Mirroring; the #1 lock-in reason switchers cite
- **Build quality & screens** — unibody, calibrated displays, silent operation
- **Unix base + polish** — real terminal, Linux-familiar tooling, commercial finish
- **Clean, ad-free out of the box** — no bloat, no upsells
- **Coherent design language** — every app follows HIG; quick look, preview, spotlight

### 2.4 Why people hate macOS (our anti-goals)
- **Price & walled garden** — premium hardware, paid basics, glued-in repairs
- **Weak window management** — no real tiling until recently; paid Rectangle required
- **Finder is bad** — no file cut/paste, weird defaults, .DS_Store litter
- **Vendor lock-in** — iOS/iCloud siren call; leaving is the real cost
- **Limited customization** — "Apple knows best"; system apps unremovable
- **Dock ≠ taskbar** — shows apps not windows; Mission Control jumbles everything
- **No gaming** — weak native library
- **Opaque debugging** — "reboot" is the fix; opaque internals

### 2.5 What people love about Linux (our foundation)
- **Freedom & control** — inspect, modify, own the machine; no telemetry
- **Package managers** — safe, centralized install/remove; the most-cited killer feature
- **Performance & lightness** — sips resources, runs great on old hardware
- **No bloat/ads/telemetry** — you're the user, not the product
- **Customizability** — themes, keybinds, dotfiles, any DE/WM
- **Free and open** — no license fee; huge FOSS ecosystem
- **Developer workflows** — containers, servers, scripting, reproducible setups
- **Update-model choice** — rolling vs LTS; rollback via snapshots

### 2.6 Why people hate Linux desktop (our enemies)
- **Fragmentation** — too many distros/DEs/package managers; search results never
  match your setup; decision paralysis; "which distro should I pick?"
- **Software gaps** — no native Photoshop/Office/Creative Suite; DAWs/video editors weaker
- **Hardware friction** — printers, fingerprint readers, Broadcom WiFi, NVIDIA
  (nouveau ~20x slower), HiDPI/refresh-rate quirks; new hardware months behind
- **Learning curve** — "trivial" tasks still need a terminal; elitist culture alienates
- **Polish deficit** — no universal HIG; inconsistent shortcuts, dialogs, theming
- **Documentation** — wikis read like ancient scrolls; great for experts, hostile to newcomers
- **Stability regressions** — kernel/userspace breakage; rolling releases break;
  LTS lacks new hardware support
- **Backward compatibility** — old closed-source apps often simply cannot run
- **Update terror** — updates can break the system; nobody promises otherwise
- **Battery life** — historically lags macOS (loosely-coupled userspace)
- **Fragmented packaging** — apt vs dnf vs pacman vs flatpak vs snap for the same app

### 2.7 Idle RAM footprint — the "Windows wastes RAM" claim, verified (2026 data)
| System | Idle RAM |
|---|---|
| Windows 11 (clean 24H2/25H2) | ~2.2–3.1 GB; ~4 GB+ with SysMain caching |
| Windows 10 (ESU) | ~1.8–2.2 GB |
| Linux Mint XFCE (same machines) | ~620–780 MB |
| Ubuntu GNOME | ~0.89 GB |
| Ubuntu KDE Plasma (Kubuntu) | ~1.21 GB |
| KDE neon (curated flagship) | ~1.4 GB |
| Fedora KDE (vanilla spin) | ~2.0–2.7 GB |
| Ubuntu headless (no DE) | ~0.43 GB |
| macOS (Apple Silicon) | ~3.5–4.5 GB reported — but ~2.3x memory compression makes it misleading |

External tests (Linus Tech Tips) showed Windows using ~4–5 GB more RAM than Linux
Mint across browsing/Discord/game loading. Caveat: idle RAM is partly caching —
Windows' SysMain deliberately preloads; Linux/macOS numbers aren't cache-identical.
**Real lesson: distro curation decides the idle budget, not the kernel.**
Design implication: **Classic targets ≤1.5 GB idle** — curation (no snapd, no ad
indexers, minimal autostart), not heroics. See P8.

### 2.8 Linux kernel & the AI-assisted development flood (2026)
- Kernel **7.0** (late 2025) added LLM-contribution guidance: an `Assisted-by:` tag
  for AI-generated patches, after Linux Foundation TAB/list discussion
- **7.4-rc1** (Nov 2026): ~20,000 commits (vs ~15,000 typical) — a big window *because
  of AI-driven fixes*; 7.4 expected to be the next **LTS**; Torvalds calls AI fixes
  part of "normal development"
- **`Assisted-by` tag deprecated** at Oct 2026 Maintainers Summit: ~1,200 carrying
  commits, many untagged AI patches, "free advertising for LLM vendors" — disclosure
  now optional; Torvalds: treat AI like compilers; **understanding > tools**
  ("stop using compilers, then")
- **AI as reviewer > AI as author:** Sashiko (agentic review) catches ~53.6% of
  bugs humans later fix; false positives <20%; maintainers increasingly expect
  Sashiko-class review before merging ("bots talking to bots")
- **Real-world wins:** AI found flaws in drivers untouched for 20 years; BPF now sees
  more AI-generated fixes than AI-authored bug reports; Torvalds' own first
  LLM-assisted patch (shared-file read cache contention) claims 23x synthetic gain
- **The controversy is ethics/quality, not tools:** maintainer stress (3 of 4
  Maintainers Summit talks), employer-forced "10x" pressure with no code review,
  rank-and-file devs can't simply "walk away," calls for ethics-based bans
  (Torvalds: keep ethics personal; only technical merit is on the table)
- Torvalds (Jan 2026): no AI-slop branch of docs; "just a tool" stance; by Jul 2026:
  pro-AI foot-down — any anti-AI objection can fork or walk away

**Implications for SiD OS (P10):**
- CONTRIBUTING will **not ban AI** (kernel norm) — but requires the author to state
  their *understanding* of the patch; CI runs static analysis + automated review
- Expect AI-generated drive-by PRs; templates must demand test evidence & motivation
- Track kernel stable promptly — AI-fix floods land in big merge windows; our update
  pipeline tests them in QEMU before release (see P3/P10)
- No "AI-free" marketing — honest tooling, like the kernel's stance

---

## 3. Arch vs Debian vs Fedora — base selection

### 3.1 Arch
| Likes | Dislikes |
|---|---|
| AUR ("a thing of beauty") | Rolling breakage if updates skipped >1 week |
| `pacman -Syu` — one command, always current | Manual install; hard for newcomers/contributors to onboard |
| Perfect for custom kernels / minimal setups | Constant maintenance; "sweating the small stuff" |
| Strong enthusiast culture | Docs assume expertise; unfriendly to normies |

**Verdict:** best upstream software freshness + AUR, worst safety story for "best
laptop experience for everyone." Arch-based would make us lean heavily on our own
guardrails.

### 3.2 Debian
| Likes | Dislikes |
|---|---|
| Rock-solid stability (servers, Raspberry Pi) | Packages too old for desktop (6–24 mo stale) |
| Largest non-commercial volunteer community | "Too serious"; desktop UX as afterthought |
| Lightest resource usage (XFCE ~1.1 GB idle) | Blank-slate minimalism — no strong defaults |
| Massive archive; great documentation | Mixing repos to get current software → broken systems |

**Verdict:** best server pedigree, worst desktop freshness. Not the base for a
modern laptop experience without heavy lifting.

### 3.3 Fedora
| Likes | Dislikes |
|---|---|
| "Leading edge, not bleeding edge" — near-current + reliable | Vanilla/unconfigured GNOME feels bare |
| **Best laptop power management out of the box** (daily-drivers explicitly chose it for this) | No proprietary drivers/codecs by default (needs RPM Fusion) |
| Excellent GNOME/KDE implementations; sane defaults | DNF slower than pacman |
| First-mover technologies: PipeWire, Wayland, systemd, bootc | 6-month release cycle; kernel trails upstream 1–2 minor |
| Atomic variants (Silverblue/Kinoite) = read-only root + rollback | Third-party repo management gets tedious |
| dnf automatic updates; strong security defaults | nvidia setup still painful |

**Verdict:** best fit for **laptop-first** — power management, Wayland/PipeWire
leadership, and a proven atomic (immutable + rollback) architecture that directly
solves the Linux "update terror" problem. The dislikes are all fixable in a distro:
bundle drivers/codecs, ship great power defaults, configure the desktop properly.

### 3.4 Recommendation
**Decision (2026-11, D1): Fedora Atomic (bootc/rpm-ostree-style image-based) base.**
- Read-only `/usr` + atomic upgrades + instant rollback → updates can't brick a laptop
- SteamOS (read-only, atomic) is the existence proof that this UX wins normal users
- Fedora's power-management defaults + our tuning = best battery experience
- dnf/rpm + Flatpak for apps → one blessed path, no package-manager roulette

---

## 4. Design principles (the ten rules)

Every feature, default, and PR is measured against these. If it conflicts, the
principle wins.

### P1 — Battery is a feature, not a tweak
- Power-profiles-daemon or TLP preconfigured with sane battery thresholds (e.g. 80% cap)
- Aggressive suspend/hibernate tuning; suspend-then-hibernate by default
- Lightweight session option; sips resources; deep C-state friendly
- Target: measurably better battery than Fedora/Arch defaults out of the box;
  publish power-draw numbers in CI on reference hardware (e.g. Framework 13)
- Success metric: ≥10% longer battery life than stock Fedora GNOME baseline

### P2 — Instant wake, zero ritual
- Sub-second resume from suspend; s2idle + appropriate rtcwake settings
- No "resume requires re-entering password + waiting for network + file manager hang"
- NetworkManager with fast reconnect; lid-close behavior that never loses work

### P3 — Updates never brick the laptop
- Atomic, image-based updates with automatic rollback on failed boot
- Read-only system root; user data separate; no half-applied upgrades
- Battery-aware update scheduling (never on low battery / during video calls)
- Success metric: a failed update costs one reboot, never one afternoon

### P4 — Zero telemetry, zero ads, zero upsell — as one switch
- No data collected, ever, unless the user opts in to a local-only diagnostic bundle
- One obvious privacy toggle that disables every optional network call we ship
- No promotional content, no "suggested apps," no notification nagging
- Success metric: uninstalling net-connectivity analysis shows zero OS beacons

### P5 — One blessed path, no roulette
- One desktop environment (curated, configured) — not a DE zoo
- Flatpak (Flathub) for third-party GUI apps; one native package flow; done
- One installer (Calamares); one update UI; one settings app; no "which tool do I use?"
- Contributors must never answer "which package manager do you use?" with a shrug

### P6 — macOS-grade polish, Linux's freedom
- One design language per experience profile: icon theme, font stack, spacing grid, motion, sound
- Consistent HIG across every shipped app — shortcuts, dialogs, file pickers
- Best-in-class touchpad gestures (libinput-gestures or compositor-native)
- Snap layouts + restorable window groups
- **Experience Profiles: one flip of a button switches the whole interaction paradigm
  (Classic = Windows-like, Studio = macOS-like, Flow = Linux-native/tiling).**
  See `docs/experience-profiles.md`. Plasma-only implementation — one desktop, three
  curated personalities, not three DEs.
- Success metric: a Mac user switches and never reaches for Rectangle/BetterTouchTool;
  a Windows refugee recognizes their muscle memory; a Linux power user gets a tiling setup

### P7 — It just works: drivers, codecs, firmware
- Proprietary drivers preinstalled where legally redistributable (NVIDIA, Wi-Fi firmware)
- Full media codec support out of the box (RPM Fusion Free/NonFree or equivalent)
- fwupd/LVFS firmware updates exposed in the GUI
- Fingerprint readers, function keys, webcams, audio jacks: tested on reference hardware list
- Success metric: install → Wi-Fi, Bluetooth, audio, video calls, printing all work, zero terminal

### P8 — Old hardware is a first-class citizen
- RAM floor target: **≤1.5 GB idle** on the curated Classic session (≤2 GB hard ceiling)
- 32-bit support not required, but 8-year-old laptops run well
- Anti-gatekeeping: no TPM/CPU generation requirements — ever
- Success metric: meaningful, snappy experience on a 2017 ThinkPad/XPS/Framework

### P9 — Safe by default, powerful when asked
- Sandboxed apps (Flatpak/portal) with clear permissions UI
- No sudo prompts for ordinary tasks; polkit rules done right
- "Expert mode" escape hatch: full terminal, full config access, documented
- No forced root, no scary errors without an explanation and a fix path

### P10 — Open by default, contributor-first
- Public repo from day one; CONTRIBUTING.md, CoC, issue/PR templates
- CI builds the image on every PR; smoke-tested in QEMU (boot, suspend, update, rollback)
- Reproducible builds; signed releases; public changelog
- Docs are a product, not an afterthought: quickstart, FAQ, troubleshooting, design doc

---

## 5. Non-goals

- Gaming-first features (we run Steam/Proton fine, but SteamOS exists; we don't chase it)
- Server/cloud/embedded profiles
- Being the "most customizable" distro — customization is allowed, not the headline
- macOS/iOS app compatibility (impossible; we run the Linux ecosystem instead)
- Proprietary anything that phones home

## 6. Target user & positioning

**Positioning (one line):** the Windows laptop experience you already know — without
Windows 11's ads, telemetry, forced accounts, or forced hardware retirement.

**Primary: Windows refugees.** People who want out of Windows 10/11 (EOL, TPM
gatekeeping, ads, Copilot) but don't want to re-learn their computer. They are served
by the default **Classic** experience profile and by zero-terminal onboarding.

**Secondary: Mac and Linux enthusiasts.** They are served by **Studio** and **Flow**
profiles respectively. They don't need converting — they need a reason not to leave:
nothing here may make them feel like a second-class citizen.

**The rule:** every design decision is evaluated against all three groups:

| Audience | Must keep | Must never do |
|---|---|---|
| Windows refugee | Familiar UI, snap layouts/groups, taskbar, Office-ish workflows, zero re-learning | Ads, upsells, forced accounts/telemetry, update terror, "buy a new PC" |
| Mac enthusiast | Battery life, instant wake, trackpad gestures, polish/consistency, ad-free | Walled-garden lock-in, paid "fix the OS" apps, no window management |
| Linux native | Freedom, telemetry-free, package manager, customizability, old hardware support | Fragmentation confusion, terminal-required basics, elitist onboarding |

**Anti-target:** tinkerers who want a blank slate (Arch exists, lovingly)

### 6.1 The "steal Windows users" playbook (and still love Mac/Linux users)
- Default install = **Classic** profile, zero prompts to "choose a DE" — installing
  SiD OS must feel like reinstalling Windows minus the 3 years of accumulated regret
- Onboarding asks: "Where do you come from?" (Windows / Mac / Linux / other) and
  pre-selects the matching profile — one click, still reversible anytime
- **Familiarity is the feature** for Classic; **polish is the feature** for Studio;
  **power is the feature** for Flow — but the P1–P10 principles are non-negotiable in all three
- Windows pain points we may never ship: mandatory accounts, ads anywhere, telemetry
  anyone can't turn off, forced feature updates, hardware gatekeeping
- Mac/Linux must-haves we may never remove: full offline use, local-only settings,
  user-repairable system, rollback after any update, zero nag notifications
- Marketing language: "It just works" — honest for once, backed by CI on reference hardware.

## 7. Reference hardware & validation

| Class | Example | Why |
|---|---|---|
| Reference "modern" laptop | Framework 13 (AMD/Intel) | Open-firmware-friendly, community, LVFS |
| Reference "old" laptop | 2017–2019 ThinkPad (X1C5/T470 class) | Proves P8 |
| Reference ARM laptop | (future) | Fedora ARM momentum |

CI matrix: boot, suspend/resume cycle ×20, update+rollback, Wi-Fi/BT connect,
audio jack detect, suspend battery drain measurement.

## 8. Licensing & governance

- Docs/tooling: **MIT or CC-BY-SA 4.0**; packages retain upstream licenses
- Contributor CLA: **none** (DCO sign-off is enough) — lowers the barrier
- Governance: benevolent lead + public RFC process for "principles vs. features"
- Trademark: name/logo reserved; community may build spins under clear rules

## 9. Roadmap sketch

- **Phase 0 (now):** design principles (this doc), name, brand, repo scaffolding
- **Phase 1:** base decision (bootc vs classic), build system, CI image builds
- **Phase 2:** minimal bootable image → Calamares installer → first ISO
- **Phase 3:** power stack tuning on reference hardware; publish benchmarks
- **Phase 4:** desktop polish pass (HIG, gestures, snap layouts)
- **Phase 5:** public alpha → feedback loop → beta

## 10. Open questions

1. ~~bootc/atomic vs classic Fedora base?~~ **Decided: bootc (2026-11, D1).**
2. ~~KDE Plasma vs GNOME~~ **Decided: KDE Plasma, with three one-button Experience
   Profiles (Classic/Studio/Flow)** — see `docs/experience-profiles.md`. Remaining:
   exact visual assets, and whether to ship a later Community GNOME Spin.
3. ~~Project name~~ **Decided: SiD OS (2026-11, D17).** Remaining: logo, domain,
   trademark/domain check before public launch.
4. CoC choice (Contributor Covenant) and communication channels (Matrix/Discord/forum)
5. Release cadence: 6-month with atomic upgrades, vs fixed point releases

---

## 11. Decision log — top best selections (2026-11)

Single source of truth for the big calls. Change = RFC + principle check.

| # | Decision | Choice | Rationale / evidence |
|---|---|---|---|
| D1 | **Base distro** | **Fedora Atomic (bootc) — CONFIRMED 2026-11** | Best laptop power defaults out of the box; atomic read-only root + rollback kills update terror (SteamOS proof); near-current packages with Debian-grade stability (§3) |
| D2 | **Desktop environment** | **KDE Plasma 6 (heavily curated, KDE alignment for power + familiarity)** | Built-in tiling + window rules (P6), best battery anecdotes on Ryzen laptops, configures the Windows-refugee paradigm without extensions (§3, §2.7, profile docs) |
| D3 | **Three Experience Profiles, one button** | **Classic (default, Windows-refugee) / Studio (macOS-flavored) / Flow (Linux-power)** | One desktop, three paradigms; switch in ~2 s, transactional, rollback-safe; Plasma Look-and-Feel packages + `laptop-experiences` CLI; a11y parity required (`docs/experience-profiles.md`) |
| D4 | **Default browser** | **Firefox** | No Edge/Chrome default; independent engine; best privacy posture; ad-blocker friendly; part of P4 zero-upsell |
| D5 | **App distribution** | **Flatpak (Flathub) for third-party GUI apps; rpm/dnf for system/native** | One blessed path (P5); sandboxed; no package-manager roulette; Steam/Proton available but not chased (non-goals) |
| D6 | **Update model** | **Atomic image updates + automatic rollback on failed boot; battery-aware scheduling** | P3 non-negotiable; never on <20% battery; never mid-call; user chooses timing (Classic OOBE) |
| D7 | **OOBE / onboarding** | **"Where do you come from?" wizard (Windows/Mac/Linux) → preselect profile; no account required; privacy OFF by default** | Windows-refugee primary goal (§6.1); ≤90 s to desktop; zero nag screens |
| D8 | **Idle memory budget** | **≤1.5 GB idle target (Classic), ≤2 GB hard ceiling** | §2.7 data: curated Plasma sits ~1.2–1.4 GB vs Windows 11's 2.2–4+ GB; biggest non-price pitch for switchers |
| D9 | **Battery stack** | **power-profiles-daemon OR TLP (final pick in Phase 3 benchmarks) + 80% charge cap GUI option; suspend-then-hibernate default** | P1; TLP wins floor tests; ppd wins integration; decide on reference hardware |
| D10 | **Naming & assets** | **Own/generic names only; open OFL/MIT/CC assets; competitor names only in internal comparative docs** | `docs/naming-and-trademarks.md`; evoke not impersonate; pre-release grep gate |
| D11 | **Privacy** | **Zero telemetry/ads/upsells; one master privacy switch; offline-first** | P4; the #1 reason Win11 users hate their OS (§2.2); distinguishing marketing claim ("honest for once") |
| D12 | **Licensing & governance** | **MIT/CC-BY-SA docs+tooling; DCO (no CLA); benevolent lead + RFC; public repo day one** | P10; contributor-first; lowers barrier; matches laptop-open positioning |
| D13 | **Reference hardware** | **Framework 13 (primary) + 2017 ThinkPad/XPS (P8 proof) + future ARM** | LVFS/fwupd-friendly; community darling; CI in QEMU + hardware lab |
| D14 | **Project layout** | **`SiD OS/` next to other workspaces; docs-first; design → decision → code** | This repo |
| D15 | **Kernel/AI stance** | **No AI-bans in contributions; author must show understanding; CI automated review; track stable kernel promptly (7.4 LTS expected)** | §2.8; matches kernel community norm; shields maintainers from slop (P10) |
| D16 | **Anti-goals** | No gaming-first features; no server/cloud profiles; no "most customizable" contest; no macOS app compat promises | §5 |
| D17 | **Project name** | **SiD OS** (confirmed 2026-11); internal codename | see `docs/naming-and-trademarks.md` §6 — check domain/trademark before public launch; association with Debian Sid noted |
| D18 | **Image architecture** | **bootc image, `quay.io/fedora/fedora-bootc` base, GitHub Actions build + QEMU smoke test** | D1; P3 rollback-safe updates; Phase 1 |

*Everything in this table has a home elsewhere in the docs — this is the index, not the detail.*

---

*If a design choice isn't in this document, write the RFC before shipping it.*
