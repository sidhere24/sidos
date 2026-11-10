# Onboarding — "Where do you come from?" (OOBE copy, v0.1)

> Goal: ≤90 seconds to a working desktop, zero mandatory accounts, zero ads,
> zero nags. Skippable except the legal minimum.

## Screen 1 — Welcome (no brand assault)
> **Welcome to SiD OS.**
> A laptop that just works — your way, in about a minute.
>
> [ Get started → ]

## Screen 2 — Where do you come from? (the fork that isn't)
> **Pick a starting point.** You can change this anytime — Settings → Experience.
>
> ◧ **Classic** — the familiar taskbar & start-style menu (default)
> ◭ **Studio** — calm, gesture-first desktop with a dock & top bar
> ◫ **Flow** — keyboard-first, tiling, zero chrome
>
> _Not sure? Pick Classic — it's the safest place to start._

(The fork is pre-selected by answer to the question in order: Windows → Classic,
 Mac → Studio, Linux/other → Flow. Everyone can change it later.)

## Screen 3 — Privacy (the moment of truth)
> **Does SiD OS phone home? Never.**
> We collect nothing by default. Optionally you can send anonymous crash reports
> (stack traces, hardware profile, SiD OS version — never content, never accounts,
> never file names). You can turn it off forever, right now:
>
> [ ] Send anonymous crash reports — OFF by default
>
> [ Continue → ]

## Screen 4 — Updates
> **Updates should be boring.**
> We update automatically in the background, verify on the next boot, and roll back
> if anything fails. You'll never be forced to reboot mid-task.
>
> (•) Automatic (recommended)
> ( ) Ask me first — I'll choose when to apply
> ( ) Nightly window — install between 02:00 and 05:00
>
> [ Continue → ]

## Screen 5 — Your stuff
> **Bring what you can.**
> We can import bookmarks and passwords from Edge, Chrome, Brave (local files —
> nothing leaves this machine unless you say so):
>
> [ ✓ Import browser profile ]  [ Skip ]

## Screen 6 — Account (none required)
> **No account needed.**
> SiD OS works fully offline. If you want to sync settings/dotfiles across machines
> later, you can create a community account in Settings — optional, forever.
>
> [ Continue without account → ]   (default, emphasized)
> [ Create account… ]              (secondary text button)

## Screen 7 — Done
> **You're in.** Try:
> - `Meta` — search anything
> - `Meta+Z` — snap layouts   (Classic)   ·   `Meta+W` — all windows   (Studio)
> - `Meta+Enter` — terminal   (Flow)
>
> [ Finish ]

## Empty states & microcopy rules (enforced in CI screenshots)
- Never show "ads", "recommended for you", "try pro", "don't you love…?" anywhere
- Always pair a warning with the fix; never a bare error
- The privacy toggle must remain a single switch, never buried
- Update failure copy: "Something went wrong with the last update — we rolled back
  automatically. You're safe. Here's what happened:" + one-line reason + one link
