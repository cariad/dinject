# dinject

`dinject` (**d**ocument **inject**ion) is a CLI tool for executing code blocks in Markdown documents then injecting the results.

## What?

Say you have a project documented in Markdown:

    The `script` property returns the block's `lines` as a single script.

    For example:

    ```python
    from dinject.types import Block

    block = Block(lang="foo", lines=["line 1\n", "line 2\n"])
    print(block.script)
    ```

If you wanted to include the example's output then you could append a `text` block, like this:

    The `script` property returns the block's `lines` as a single script.

    For example:

    ```python
    from dinject.types import Block

    block = Block(lang="foo", lines=["line 1\n", "line 2\n"])
    print(block.script)
    ```

    ```text
    line 1
    line 2
    ```

...but if the demonstrated function's response ever changes then you'll need to remember to update the example.

`dinject` automates the execution of embedded code. Rather than append the example yourself, append a `<!--dinject-->` tag instead:

    The `script` property returns the block's `lines` as a single script.

    For example:

    ```python
    from dinject.types import Block

    block = Block(lang="foo", lines=["line 1\n", "line 2\n"])
    print(block.script)
    ```

    <!--dinject-->

To execute the embedded code and inject the result, run `dinject YOUR_DOC.md`.

The result will be:

    The `script` property returns the block's `lines` as a single script.

    For example:

    ```python
    from dinject.types import Block

    block = Block(lang="foo", lines=["line 1\n", "line 2\n"])
    print(block.script)
    ```

    <!--dinject as=markdown host=shell range=start-->

    ```text
    line 1
    line 2
    ```

    <!--dinject range=end-->

## Installation

`dinject` requires Python 3.8 or later:

```bash
pip install dinject
```

## Live example

Here's a Python code block, with the result injected automatically by running `dinject README.md`:

```python
from mdcode import Block

block = Block(lang="foo", lines=["line 1", "line 2"])
print(block.lines)
```

<!--dinject as=markdown fence=backticks host=shell range=start-->

```text
['line 1', 'line 2']
```

<!--dinject range=end-->

## 👋 Hello!

**Hello!** I'm [Cariad Eccleston](https://cariad.io) and I'm an independent/freelance software engineer. If my work has value to you, please consider [sponsoring](https://github.com/sponsors/cariad/).

If you ever raise a bug, request a feature or ask a question then mention that you're a sponsor and I'll respond as a priority. Thank you!
