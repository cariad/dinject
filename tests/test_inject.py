from io import StringIO
from logging import basicConfig, getLogger
from os import unlink
from pathlib import Path
from shutil import copy

from comprehemd import CodeBlock, Fence
from pytest import mark

from dinject import Parser
from dinject.enums import Content, Host
from dinject.execute import execute
from dinject.inject import Reader, inject, inject_file, iterate_lines
from dinject.types import Instruction

basicConfig(level="DEBUG")
getLogger("comprehemd").setLevel("DEBUG")
getLogger("dinject").setLevel("DEBUG")


@mark.parametrize(
    "block, instruction, expect",
    [
        # Bash executor:
        (
            CodeBlock("python --version\n", language="bash"),
            Instruction(),
            """<!--dinject as=markdown fence=backticks host=shell range=start-->

```text
Python 3.10.0
```

<!--dinject range=end-->
""",
        ),
        # Python executor:
        (
            CodeBlock("print(1+2)\n", language="python"),
            Instruction(),
            """<!--dinject as=markdown fence=backticks host=shell range=start-->

```text
3
```

<!--dinject range=end-->
""",
        ),
        # Text pass-through:
        (
            CodeBlock("one\ntwo\n", language="text"),
            Instruction(),
            """```text
one
two
```
""",
        ),
        # As HTML:
        (
            CodeBlock("python --version\n", language="bash"),
            Instruction(content=Content.HTML),
            """<!--dinject as=html fence=backticks host=shell range=start-->

<pre class="nohighlight thtml"><code class="thtml-code">Python 3.10.0<br /></code></pre>

<!--dinject range=end-->
""",
        ),
        # Via terminal:
        (
            CodeBlock("python --version\n", language="bash"),
            Instruction(host=Host.TERMINAL),
            """<!--dinject as=markdown fence=backticks host=terminal range=start-->

```text
Python 3.10.0
```

<!--dinject range=end-->
""",
        ),
        # With tildes:
        (
            CodeBlock("python --version\n", language="bash"),
            Instruction(fence=Fence.TILDES),
            """<!--dinject as=markdown fence=tildes host=shell range=start-->

~~~text
Python 3.10.0
~~~

<!--dinject range=end-->
""",
        ),
    ],
)
def test_executor(block: CodeBlock, instruction: Instruction, expect: str) -> None:
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

<!--dinject as=markdown fence=backticks host=shell range=start-->

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


def test_error() -> None:
    reader = StringIO(
        """This is an example:

```python
print(foo)
```

<!--dinject-->
"""
    )

    expect = """This is an example:

```python
print(foo)
```

<!--dinject as=markdown fence=backticks host=shell range=start-->

```text
Traceback (most recent call last):
  File "<string>", line 1, in <module>
NameError: name 'foo' is not defined
```

<!--dinject range=end-->
"""

    writer = StringIO()
    inject(reader, writer)
    assert writer.getvalue() == expect


def test_inject__string() -> None:
    reader = """This is an example:

```python
print(1+2)
```

<!--dinject-->
"""

    expect = """This is an example:

```python
print(1+2)
```

<!--dinject as=markdown fence=backticks host=shell range=start-->

```text
3
```

<!--dinject range=end-->
"""

    writer = StringIO()
    inject(reader, writer)
    assert writer.getvalue() == expect


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
