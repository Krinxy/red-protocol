from dataclasses import dataclass


@dataclass
class TargetConfig:
    loader_url: str = "http://localhost:8002"
    chain_url: str = "http://localhost:8000"
    frontend_url: str = "http://localhost:8501"
    loader_container: str = "loader"
    chain_container: str = "chain"


PROFILES = {
    "local": TargetConfig(),
}
