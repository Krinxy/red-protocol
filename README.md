# red-protocol

Red-team practice range for [Enterprise_RAG_Blueprint](../Enterprise_RAG_Blueprint). Local
instance only, no third-party deployments. Thesis context.

## Scope
- Target: local `docker-compose` instance of `Enterprise_RAG_Blueprint` (see `target/setup.md`).
- Allowed: Chain API (`:8000`), Loader API (`:8002`), Frontend (`:8501`), MinIO (`:9000/9001`),
  Chroma — within the compose network or localhost only.
- No real secrets or production keys. No attacks on third parties.

## Structure

| Folder | Purpose |
|---|---|
| `pasta/` | Method: 7 PASTA stages, definition + project context + references each. Stage 6 is the payload library. |
| `attack/` | Executable harness: registry + modules (see `attack/README.md`). |
| `target/` | Target setup + code findings (file:line). |
| `protocol/objects/` | One folder per run (auto-generated): request log + summary + notes. |
| `protocol/findings/` | Confirmed findings, severity, fix proposal. |
| `protocol/mitigations/` | Countermeasures + re-test results. |
| `templates/` | Experiment/finding templates. |

`pasta/` is the method. `attack/` runs it. `protocol/` is the record of what happened.

## Workflow
1. Read `target/code-findings.md`.
2. Pick/write a module in `attack/modules/`, add it to `attack/main.py`'s `run_list`.
3. `python -m attack.main`.
4. Copy `templates/experiment.template.md` into the run folder under `protocol/objects/`, fill
   in hypothesis/observation.
5. On a hit: `protocol/findings/FIND-xxx.md`, list it in `findings-index.md`.
6. Fix it, re-run the same payload, compare.

## ID scheme
`PI-` Prompt Injection · `AUTHZ-` Authorization · `RE-` Resource Exhaustion/DoS ·
`SC-` Supply Chain · `GB-` Guardrail Bypass · `PT-` Path Traversal
