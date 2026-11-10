import json
import time
from pathlib import Path

from .modules.pi001_indirect_injection import IndirectPromptInjectionViaDocument
from .modules.re001_disk_leak import DiskLeakAsyncUpload
from .profiles.targetconfig import PROFILES


class Harness:
    def __init__(self):
        self.repo_root = Path(__file__).resolve().parent.parent
        self.objects_dir = self.repo_root / "protocol" / "objects"
        self.profile = PROFILES["local"]
        self.run_list = [
            DiskLeakAsyncUpload(),
            IndirectPromptInjectionViaDocument(),
        ]

    def run_one(self, attack, cfg) -> None:
        (run_dir := self.objects_dir / f"{time.strftime('%Y%m%d_%H%M%S')}_{attack.attack_id}_{attack.name}")\
                .mkdir(parents=True,
                       exist_ok=True)

        result = attack.run(cfg,
                            run_dir
                            )

        (run_dir / "summary.json")\
            .write_text(json.dumps(result,indent=2),
                       encoding="utf-8"
                       )
        print(json.dumps(result,
                         indent=2)
                         )

    def run(self) -> None:
        for attack in self.run_list:
            self.run_one(attack=attack, cfg=self.profile)


if __name__ == "__main__":
    Harness().run()
