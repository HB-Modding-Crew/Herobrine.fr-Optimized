from __future__ import annotations

from dacite import from_dict
from dataclasses import dataclass
from typing import Dict, Any, List, Optional

from src.Step.StepConfig import StepConfig


@dataclass
class ProjectConfig:
    name: Optional[str]
    variables: Dict[str, Any]
    workflows: List[str]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        return from_dict(data_class=ProjectConfig, data=data)