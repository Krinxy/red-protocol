# attack/

Executable half of the red team. `protocol/pasta/06_attack_modeling/<category>/README.md`
describes *what* to attack; this is *how* — one class per attack, run through `main.py`.

## Setup
```
pip install -r attack/requirements.txt
```
Target containers must be running (`docker ps`: `loader`, `chain`, `frontend`, `minio`,
`ollama`).

## Usage
```
python -m attack.main
```
Edit `Harness.run_list` in `main.py` to pick which attacks run and with what parameters.

Each run writes to `protocol/objects/<timestamp>_<ID>_<name>/`:
- `requests.jsonl` — every HTTP request/response, logged by `LoggingClient`.
- `summary.json` — the attack's return dict.

By hand afterwards: copy `templates/experiment.template.md` into the run folder as
`experiment.md`; on a confirmed hit, add `protocol/findings/FIND-xxx.md`.

## Layout
- `main.py` — `Harness`: builds a run folder per attack, calls it, writes the summary.
- `profiles/targetconfig.py` — `TargetConfig` dataclass, `PROFILES` registry by name.
- `client.py` — `LoggingClient`: the only thing that speaks HTTP and logs it.
- `modules/<id>_<name>.py` — one class per attack:
  ```python
  class SomeAttack:
      def __init__(self, ...): self.attack_id = "..."; self.name = "..."
      def run(self, cfg, run_dir) -> dict: ...
  ```

## Modules
| ID | Module | Code finding |
|---|---|---|
| RE-001 | `DiskLeakAsyncUpload` | `loader_api.py:288` — `tempfile.mkdtemp()` never deleted. Confirmed live. |
| PI-001 | `IndirectPromptInjectionViaDocument` | `load_chain.py:159-170` — document content goes unescaped into the system prompt; guardrails never see it. Confirmed live: planted instruction executed verbatim. |

Next candidate: **AUTHZ-001** — `POST /call_llm` with `user_roles: ["admin"]`, no login needed.
