# Contributing to LaptopOS

Thanks for caring about laptops. This project is docs-first: the design docs in
`docs/` are the source of truth — read `docs/design-principles.md` (especially the
P1–P10 principles and the decision log §11) before opening a PR.

## Ground rules

1. **Principles win.** If your feature fights a principle, the principle wins.
   Propose an RFC first (`docs/rfcs/0000-rfc-template.md`) instead.
2. **One blessed path** (P5): don't add alternatives to things we've already blessed
   (one desktop session, Flatpak-first apps, Calamares, one update UI).
3. **No telemetry, ads, or upsells** — ever (P4). PRs adding any are rejected.
4. **Trademark hygiene** (`docs/naming-and-trademarks.md`): in-product names are ours
   or generic; assets open-licensed (OFL/MIT/CC0/CC-BY); competitor names only in
   internal comparative docs. Run `scripts/check-trademarks.sh` before pushing.

## DCO sign-off (no CLA)

We use the Developer Certificate of Origin. Sign off every commit:

```
git commit -s -m "area: what and why"
```

That certifies the patch is yours to contribute under our license. There is no CLA.

## AI-assisted contributions — the kernel-style stance

LaptopOS follows the Linux community norm (see `docs/design-principles.md` §2.8):

- **AI tools are welcome as tools.** We do not require an `Assisted-by:` tag and we
  do not ban AI-generated code.
- **Understanding is mandatory.** In your commit message (or PR description) state
  *what* the change does and *why it's correct* — enough that a maintainer can
  review it without re-deriving it. If you can't explain it, don't send it.
- **CI reviews your patch anyway**: static analysis, trademark string scan, and
  automated review. Expect findings; fix them before review.
- **No AI-generated walls of text** in issues/PRs. Thin, specific, testable.
- Documentation that reads like it was written by neither human nor machine will be
  sent back, however correct the facts.

## How to contribute

1. Find an issue labeled `good-first-issue`, or open one describing the problem.
2. For anything touching principles, update/extend the design doc in the same PR —
   code without doc updates will be asked to add it.
3. Branch naming: `topic/short-description`. Conventional-ish commits: `area: summary`
   (e.g. `power: enable 80% charge cap option in Quick Settings`).
4. Tests before behavior: at minimum, extend CI smoke checks; for system changes,
   describe manual verification on a reference laptop (Framework 13 / 2017 ThinkPad).
5. Sign off every commit (DCO).

## Community

- Chat: Matrix/Discord (link TBD before public launch — see open question Q4)
- Conduct: `CODE_OF_CONDUCT.md` (Contributor Covenant v2.1)
- Security issues: see `SECURITY.md`

## Licensing

Code and tooling: MIT (see `LICENSE`). Docs: CC-BY-SA 4.0.
Upstream packages retain their own licenses.
