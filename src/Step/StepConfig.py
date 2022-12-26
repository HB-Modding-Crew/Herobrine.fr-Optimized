from __future__ import annotations

from dacite import from_dict
from dataclasses import dataclass
from typing import Dict, Any, Optional


@dataclass
class StepConfig:
    type: str
    id: str
    name: Optional[str]
    variables: Dict[str, Any]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        return from_dict(data_class=StepConfig, data=data)
