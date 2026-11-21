# Security Policy

SiD OS is pre-alpha. There are no releases yet and no supported versions.

## Reporting a vulnerability

Do **not** open a public issue for security problems.

Until the public launch and a security mailing list exist: report via GitHub's
**private vulnerability reporting** — https://github.com/sidhere24/sidos/security/advisories/new
(only maintainers see it). If that isn't enabled yet, open a normal issue titled
"SECURITY: contact request" with no details, and we'll reach out from a maintainer account.

Please include: affected component, reproduction steps, impact, and any suggested
fix. We aim to acknowledge within 72 hours and provide a timeline within 7 days.

## Scope

- The OS image build and its configuration
- Scripts and tooling in this repository
- Default privacy posture (telemetry/data-flow regressions count as security bugs)

Third-party packages are upstream security issues — report them upstream, then to
us if our default config exposes them.
