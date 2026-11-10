# Stage 3+4 — Application Decomposition / Threat Analysis

## Definition (PASTA)
- Identify use cases, entry points & trust levels, actors/assets/services/roles/data sources,
  data flow diagrams and trust boundaries.
- Probabilistic attack scenario analysis, threat intelligence correlation.

## For this project
Entry points: Frontend (login), Chain API (`/call_llm`), Loader API (upload, debug/admin).
Assets: uploaded documents (MinIO + Chroma, some confidential via bitmask roles), system
prompt/guardrail config, LLM access, user credentials.

Intended trust chain: Frontend → session → role → Chain API. Real: the role comes raw from the
client body, no session check on either API (AUTHZ-001/003) — the boundary doesn't exist in
code. Data flow: Uploader → Loader → MinIO + Chroma → Retriever → system prompt (unchecked,
PI-001, guardrails never see it either, GB-002) → answer to any user.

| Trust boundary | Threat | STRIDE |
|---|---|---|
| Client → Chain API (role in body) | Identity/role spoofing | Spoofing, Elevation of Privilege |
| Uploader → retrieval context → prompt | Injected instructions in document content | Tampering |
| Guardrail check → LLM call | Bypassed or fails open | Tampering, Elevation of Privilege |
| Client ↔ API on abort | Server keeps computing, resources fill up | Denial of Service |
| Dependency install | Unpinned package pulls a vulnerable version | Tampering (Supply Chain) |
| Uploader → Chroma/MinIO | Filename/path taken over unchecked | Tampering (Path Traversal) |

Realistic attacker: anonymous network access to the Chain/Loader API (no login needed) is the
most likely profile here.

Details: `target/code-findings.md`. OWASP mapping: `05_vulnerability_analysis/owasp.md`.
