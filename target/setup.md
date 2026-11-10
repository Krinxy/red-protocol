# Target setup

1. Clone/update the Blueprint, pin a commit:
   ```
   cd ../Enterprise_RAG_Blueprint
   git log -1 --format=%H
   ```
2. Copy `.env` from `example.env`, use test values only.
3. `docker-compose up -d`

Addresses (verified against `docker-compose.yml` + `docker ps`): Loader `:8002`, Chain `:8000`,
Frontend `:8501` — see `attack/profiles/targetconfig.py`. Attacks run over HTTP via
`attack/client.py`, not manual curl — see `attack/README.md` for the module list and order.
