from __future__ import annotations

from dacite import from_dict
from dataclasses import dataclass
from typing import Dict, Any, List, Optional

from src.Step.StepConfig import StepConfig


@dataclass
class WorkflowConfig:
    name: Optional[str]
    steps: List[StepConfig]
    variables: Dict[str, Any]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        return from_dict(data_class=WorkflowConfig, data=data)