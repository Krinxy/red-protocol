import json
import time

import requests


class LoggingClient:
    def __init__(self, base_url: str, run_dir, log_name: str = "requests.jsonl"):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.log_path = run_dir / log_name
        self.log_path.parent.mkdir(parents=True, exist_ok=True)

    def request(self, method: str, path: str, timeout: float = 30, **kwargs) -> requests.Response:
        t0 = time.time()
        resp = self.session.request(method, f"{self.base_url}{path}",
                                    timeout=timeout, **kwargs)
        entry = {
            "ts": t0,
            "method": method,
            "url": resp.url,
            "data": kwargs.get("data"),
            "status": resp.status_code,
            "elapsed_s": round(time.time() - t0, 3),
            "response_preview": resp.text[:500],
        }
        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        return resp
