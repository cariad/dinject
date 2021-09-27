from typing import Dict, Optional, Type

from dinject.executors.bash import BashExecutor
from dinject.executors.python import PythonExecutor
from dinject.types import Executor

executors: Dict[str, Type[Executor]] = {
    "bash": BashExecutor,
    "python": PythonExecutor,
}


def get_executor(language: str) -> Optional[Type[Executor]]:
    """Gets the executor for `language`."""

    return executors.get(language, None)
