import os
from typing import Any


def get_env_var(var_name: str) -> Any:
    return os.environ[var_name]
