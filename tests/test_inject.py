from io import StringIO
from os import unlink
from pathlib import Path
from shutil import copy

from mdcode import Block
from pytest import mark

from dinject import Parser
from dinject.enums import Content, Host
from dinject.inject import Reader, execute, inject, inject_file, iterate_lines
from dinject.types import Instruction


@mark.parametrize(
    "block, instruction, expect",
    [
        # Bash executor:
        (
            Block(lang="bash", lines=["python --version"]),
            Instruction(),
            """<!--dinject as=markdown host=shell range=start-->

```text
Python 3.10.0
```

<!--dinject range=end-->
""",
        ),
        # Python executor:
        (
            Block(lang="python", lines=["print(1+2)"]),
            Instruction(),
            """<!--dinject as=markdown host=shell range=start-->

```text
3
```

<!--dinject range=end-->
""",
        ),
        # Text pass-through:
        (
            Block(lang="text", lines=["one\n", "two\n"]),
            Instruction(),
            """```text
one
two
```
""",
        ),
        # As HTML:
        (
            Block(lang="bash", lines=["python --version"]),
            Instruction(content=Content.HTML),
            """<!--dinject as=html host=shell range=start-->

<pre class="nohighlight thtml"><code class="thtml-code">Python 3.10.0<br /></code></pre>

<!--dinject range=end-->
""",
        ),
        # Via terminal:
        (
            Block(lang="bash", lines=["python --version"]),
            Instruction(host=Host.TERMINAL),
            """<!--dinject as=markdown host=terminal range=start-->

```text
Python 3.10.0
```

<!--dinject range=end-->
""",
        ),
    ],
)
def test_executor(block: Block, instruction: Instruction, expect: str) -> None:
    writer = StringIO()
    execute(
        block=block,
        instruction=instruction,
        parser=Parser(),
        writer=writer,
    )
    assert writer.getvalue() == expect


def test_inject() -> None:
    reader = StringIO(
        """This is an example:

```python
print(1+2)
```

<!--dinject-->
"""
    )

    expect = """This is an example:

```python
print(1+2)
```

<!--dinject as=markdown host=shell range=start-->

```text
3
```

<!--dinject range=end-->
"""

    writer = StringIO()

    inject(reader, writer)
    assert writer.getvalue() == expect

    # Assert that a second injection makes no changes:
    second_writer = StringIO()

    writer.seek(0)
    inject(writer, second_writer)
    assert second_writer.getvalue() == expect


def test_inject_file() -> None:
    tests = Path() / "tests"
    in_file = tests / "example.md"
    expect_file = tests / "expect.md"
    backup_file = tests / "example.backup"
    copy(in_file, backup_file)
    inject_file(path=in_file)

    with open(in_file, "r") as i:
        with open(expect_file, "r") as e:
            assert i.read() == e.read()
    copy(backup_file, in_file)
    unlink(backup_file)


@mark.parametrize("reader", ["one\ntwo", StringIO("one\ntwo")])
def test_iterate_lines(reader: Reader) -> None:
    assert list(iterate_lines(reader)) == ["one", "two"]
