# Stage 6 — Attack Modeling

## Definition (PASTA)
Attack surface analysis, attack tree development, attack-to-vulnerability mapping.

## For this project
What to attack; `attack/` is the executable counterpart (how).

| Folder | Code finding | Status |
|---|---|---|
| `prompt_injection/` | PI-001 | confirmed live |
| `authz_bypass/` | AUTHZ-001/002/003 | open |
| `resource_exhaustion/` | RE-001/002/003 | RE-001 confirmed live |
| `supply_chain/` | SC-001 | open |
| `guardrail_bypass/` | GB-001/002 | open |
| `path_traversal/` | PT-001 | open |
| `rag_poisoning/` | none yet, literature only | to verify |
| `vector_embedding_leakage/` | none yet, literature only | to verify |

Workflow: build a module in `attack/modules/`, run it, log in `protocol/objects/`, on a hit add
`protocol/findings/FIND-xxx`.
