from enum import Enum, unique


@unique
class Emit(Enum):
    MARKDOWN = 0
    HTML = 1
