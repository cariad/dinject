from enum import Enum, unique


@unique
class Emitted(Enum):
    NOT_EMITTED = 0
    START = 1
    END = 2
