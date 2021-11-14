from io import StringIO

from pytest import mark, raises

from dinject import Parser
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
def test_get_instruction(line: str, expect: Instruction) -> None:
    assert Parser().get_instruction(line) == expect


def test_get_instruction__custom_keyword() -> None:
    parser = Parser(keyword="foo")
    assert parser.get_instruction("<!--foo host=terminal-->") == Instruction(
        content=Content.MARKDOWN,
        range=Range.NONE,
        host=Host.TERMINAL,
    )


def test_get_instruction__fail() -> None:
    with raises(InstructionParseError):
        # Parse expects "key=value":
        Parser().get_instruction("<!--dinject key value -->")


def test_write_range_end() -> None:
    writer = StringIO()
    Parser().write_range_end(writer)
    assert writer.getvalue() == "<!--dinject range=end-->\n"


def test_write_range_end__custom_keyword() -> None:
    writer = StringIO()
    Parser(keyword="foo").write_range_end(writer)
    assert writer.getvalue() == "<!--foo range=end-->\n"


def test_write_range_start() -> None:
    writer = StringIO()

    instruction = Instruction(
        content=Content.MARKDOWN,
        range=Range.NONE,
        host=Host.SHELL,
    )

    Parser().write_range_start(instruction=instruction, writer=writer)
    assert writer.getvalue() == "<!--dinject as=markdown host=shell range=start-->\n"


def test_write_range_start__custom_keyword() -> None:
    writer = StringIO()

    instruction = Instruction(
        content=Content.MARKDOWN,
        range=Range.NONE,
        host=Host.SHELL,
    )

    Parser(keyword="foo").write_range_start(instruction=instruction, writer=writer)
    assert writer.getvalue() == "<!--foo as=markdown host=shell range=start-->\n"
