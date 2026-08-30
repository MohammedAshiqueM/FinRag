from dataclasses import dataclass
from typing import Any


@dataclass
class Chunk:
    text: str
    metadata: dict[str, Any]
    id: str | None = None