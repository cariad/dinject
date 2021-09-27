from io import StringIO

from dinject.types.block import Block


def test_script() -> None:
    block = Block(lang="foo", lines=["one\n", "two\n"])
    assert block.script == "one\ntwo\n"


def test_write() -> None:
    writer = StringIO()
    Block(lang="foo", lines=["one\n", "two\n"]).write(writer)
    assert (
        writer.getvalue()
        == """```foo
one
two
```
"""
    )
