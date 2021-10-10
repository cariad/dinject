from io import StringIO

from pytest import mark

from dinject.enums import Content, Host
from dinject.inject import execute, inject
from dinject.types import Block, Instruction


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
    execute(block=block, instruction=instruction, writer=writer)
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
