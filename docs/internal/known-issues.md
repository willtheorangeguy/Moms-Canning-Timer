# Known Issues — Moms-Canning-Timer

Concrete defects and gaps found while writing this repository's documentation in
August 2026. **Nothing here was changed** — each one needs a code, configuration, or
licensing decision rather than a documentation one.

Ordered by severity. See [`docs/roadmap.md`](../roadmap.md) for the narrative version,
which also covers deliberate non-goals.


**2 open:** 1 medium, 1 low.

## 1. Logo and screenshot never rendered — /blob/ URLs serve HTML, not images

**Severity:** Medium  
**Where:** `README.md`, the logo and hero `<img src>`

**What:** Both pointed at `github.com/willtheorangeguy/Moms-Canning-Timer/blob/master/docs/images/...`. A `/blob/` URL returns a GitHub HTML page rather than image bytes.

**Why it matters:** Neither image has been displaying, on github.com or on PyPI, which renders the README as the package long description. The project has shipped without its logo or its screenshot.

**Suggested fix:** Fixed in this sweep — both now come from `.github/icons/Moms-Canning-Timer/` via `raw.githubusercontent.com`. Recorded because the same mistake is easy to reintroduce.

## 2. Self-links were missing /blob/ and pointed at the wrong branch

**Severity:** Low  
**Where:** `README.md`, the How To Use intro

**What:** Links were written as `github.com/willtheorangeguy/Moms-Canning-Timer/main/README.md#git`. They omit the `/blob/` segment **and** name `main`, while this repository's default branch is `master`.

**Why it matters:** Two independent faults in one URL, so it could never have resolved.

**Suggested fix:** Fixed in this sweep by replacing them with in-page anchors. Worth noting the default branch is `master` when writing links by hand.


---

## Also, across every repository

**`.bandit` is present on disk but untracked in git.** Verified in PyWorkout, treklogger,
skyscanner-cli, booking-cli, piggy, and aibot — the config file exists locally in each but
`git ls-files` does not know about it, so none of it reached GitHub.

The August 2026 security sweep therefore looks complete locally and landed nowhere. Worth
checking across all 44 repositories it covered.
