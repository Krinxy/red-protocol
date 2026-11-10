# Stage 1+2 — Define Objectives / Technical Scope

## Definition (PASTA)
- Identify Business Objectives, Security/Compliance Requirements, Business Impact
- Capture Technical Environment Boundaries, Infrastructure/Application/Software Dependencies

## For this project
Business objective: role-based document search (`category_bitmask`) via an LLM chain —
category confidentiality is the core promise. No cross-category leaks, no uncontrolled
execution of document-embedded instructions.

Environment: local `docker-compose` (`frontend` Streamlit, `chain` FastAPI + guardrails +
retriever, `loader` FastAPI + MinIO + Chroma). No version pins anywhere (SC-001) — the
dependency tree isn't reproducible without a lockfile.

Rough impact ranking: AUTHZ-001/002 (breaks RBAC, highest) > PI-001 (answer manipulation,
potential exfiltration) > RE-001..003 (availability/cost, reversible) > SC-001 (latent).
