# Supply Chain

Goal: find a vulnerable dependency version that actually gets installed. No version pins in any
`requirements.txt` (SC-001). Static check, no live traffic.

Try: `pip-audit`/`osv-scanner` against each service's `requirements.txt`.

Success: a concrete CVE in an actually installed version, or a reproducible version drift
between two installs.
