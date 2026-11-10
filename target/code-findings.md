# Code Findings

Static analysis of `Enterprise_RAG_Blueprint`, file:line backed.

| ID | File:Line | Finding | Category | Status |
|---|---|---|---|---|
| PT-001 | `loader/loader_api.py:294,464` | `file.filename` unchecked in `temp_path / file.filename` → path traversal | path_traversal | open |
| RE-001 | `loader/loader_api.py:288` | `tempfile.mkdtemp()` in async upload never deleted | resource_exhaustion | **confirmed live** |
| RE-002 | `loader/loader_api.py:77-78` | `jobs_storage` global dict, no TTL/eviction | resource_exhaustion | open |
| RE-003 | `chain/chain_api.py:55-98` | `async def` endpoint, blocking LLM call, no cancel on disconnect | resource_exhaustion | open |
| AUTHZ-001 | `chain/chain_api.py:31`, `chain/retriever.py:40-45,169-173` | `user_roles` raw from client, no session check; `admin` in array lifts all filtering | authz_bypass | open |
| AUTHZ-002 | `chain/retriever.py:181-185` | Role "General" (bitmask==1) gets no filter by design | authz_bypass | open |
| AUTHZ-003 | `loader/loader_api.py` | No auth on upload/debug/download endpoints | authz_bypass | open |
| PI-001 | `chain/load_chain.py:159-170`, `chain/prompts/rag_source.j2:6-8` | Document content + filename unescaped into system prompt | prompt_injection | **confirmed live** |
| GB-001 | `chain/guardrails_manager.py:42-44` | Fail-open on guardrail LLM exception/timeout | guardrail_bypass | open |
| GB-002 | `chain/guardrails_manager.py`, `chain_api.py:58` | Only `question` is checked, never retrieved context | guardrail_bypass | open |
| SC-001 | `loader/requirements.txt`, `chain/requirements.txt` | No version pins | supply_chain | open |
| MISC-001 | `frontend/pages/upload_data.py:106` | `st.file_uploader` has no type whitelist | path_traversal / supply_chain | open |
| MISC-002 | `frontend/authentication/auth_service.py:36-37` | Unsalted SHA-256, no rate limiting | not core focus | open |

## Not confirmed
- No image/EXIF processing anywhere — metadata injection via images in Chroma isn't possible
  with the current code.
- No SQL injection (`auth_service.py` queries are parameterized).
- No streaming endpoint — abort attacks run through missing cancel handling (RE-003).
