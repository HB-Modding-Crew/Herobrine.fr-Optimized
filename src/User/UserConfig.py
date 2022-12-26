from __future__ import annotations

from dacite import from_dict
from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class UserConfig:
    variables: Dict[str, Any]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        return from_dict(data_class=UserConfig, data=data)
