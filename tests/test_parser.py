from pytest import raises

from dinject.exceptions import InstructionParseError
from dinject.parser import Parser


def test_get_instruction__invalid() -> None:
    parser = Parser()

    with raises(InstructionParseError):
        parser.get_instruction("<!--dinject foo-->")
