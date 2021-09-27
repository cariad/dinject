from io import StringIO

from pytest import mark, raises

from dinject.enums import Content, Host, Range
from dinject.exceptions import InstructionParseError
from dinject.types.instruction import Instruction


@mark.parametrize(
    "line, expect",
    [
        ("", None),
        (
            "<!--dinject-->",
            Instruction(
                content=Content.MARKDOWN,
                range=Range.NONE,
                host=Host.SHELL,
            ),
        ),
        (
            "<!--dinject as=html-->",
            Instruction(
                content=Content.HTML,
                range=Range.NONE,
                host=Host.SHELL,
            ),
        ),
        (
            "<!--dinject range=start-->",
            Instruction(
                content=Content.MARKDOWN,
                range=Range.START,
                host=Host.SHELL,
            ),
        ),
        (
            "<!--dinject host=terminal-->",
            Instruction(
                content=Content.MARKDOWN,
                range=Range.NONE,
                host=Host.TERMINAL,
            ),
        ),
    ],
)
def test_parse(line: str, expect: Instruction) -> None:
    assert Instruction.parse(line) == expect


def test_parse__fail() -> None:
    with raises(InstructionParseError):
        # Parse expects "key=value":
        Instruction.parse("<!--dinject key value -->")


def test_write_range_end() -> None:
    writer = StringIO()
    Instruction.write_range_end(writer)
    assert writer.getvalue() == "<!--dinject range=end-->\n"


def test_write_range_start() -> None:
    writer = StringIO()

    Instruction(
        content=Content.MARKDOWN,
        range=Range.NONE,
        host=Host.SHELL,
    ).write_range_start(writer)

    assert writer.getvalue() == "<!--dinject as=markdown host=shell range=start-->\n"
