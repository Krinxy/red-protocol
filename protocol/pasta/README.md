# PASTA — Process for Attack Simulation and Threat Analysis

Each stage folder holds a `def.md`: short definition + project context, no reference lists.

| Stage | Folder | Question |
|---|---|---|
| 1+2 | `01_02_define_objectives_and_technical_scope` | What's protected, and what's in play? |
| 3+4 | `03_04_application_decomposition_and_threat_analysis` | How is it built, which threats are realistic? |
| 5 | `05_vulnerability_analysis` | Which vulnerabilities exist (CWE/CVSS)? |
| 6 | `06_attack_modeling` | How is each one exploited? |
| 7 | `07_risk_impact_analysis` | What's the business impact, what's the fix? |

Stage 6 is the attack library. `attack/` is the executable counterpart (how).
`protocol/objects|findings|mitigations/` is the record.
