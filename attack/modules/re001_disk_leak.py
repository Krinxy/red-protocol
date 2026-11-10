import io
import subprocess
from typing import Optional

from ..client import LoggingClient


class DiskLeakAsyncUpload:
    def __init__(self, n: int = 10, measure_disk: bool = True):
        self.attack_id = "RE-001"
        self.name = "disk_leak_async_upload"
        self.n = n
        self.measure_disk = measure_disk

    def _tmp_usage_kb(self, container: str) -> Optional[int]:
        try:
            out = subprocess.run(
                ["docker", "exec", container, "du", "-sk", "/tmp"],
                capture_output=True,
                text=True,
                timeout=10,
                check=True,
            )
            return int(out.stdout.split()[0])
        except Exception:
            return None

    def _probe_file(self, name: str):
        content = (b"red-protocol RE-001 probe\n" * 100)
        return (name, io.BytesIO(content), "text/plain")

    def run(self, cfg, run_dir) -> dict:
        client = LoggingClient(cfg.loader_url,
                               run_dir
                               )
        before_kb = self._tmp_usage_kb(cfg.loader_container) if self.measure_disk else None

        ok = 0
        for i in range(self.n):
            resp = client.request(
                "POST", "/upload-documents-async",
                files=[("files", self._probe_file(f"re001_probe_{i}.txt"))],
                data={"document_tag": "General"},
            )
            if resp.status_code == 200:
                ok += 1

        after_kb = self._tmp_usage_kb(cfg.loader_container) if self.measure_disk else None
        delta_kb = (after_kb - before_kb) if before_kb is not None and after_kb is not None else None

        return {
            "attack_id": self.attack_id,
            "requests_sent": self.n,
            "requests_ok": ok,
            "tmp_kb_before": before_kb,
            "tmp_kb_after": after_kb,
            "tmp_kb_delta": delta_kb,
            "hypothesis_confirmed": (delta_kb is not None and delta_kb > 0) if delta_kb is not None else None,
        }
