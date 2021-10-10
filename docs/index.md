# dinject

`dinject` (**d**ocument **inject**ion) is a CLI tool for executing code blocks in Markdown documents then injecting the results.

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

## Licence

The source for `dinject` is available at [github.com/cariad/dinject](https://github.com/cariad/dinject) under the MIT licence.

## Feedback

Please raise bugs, request features and ask questions at [github.com/cariad/dinject/issues](https://github.com/cariad/dinject/issues).

Mention if you're a [sponsor](https://github.com/sponsors/cariad) to ensure I respond as a priority. Thank you!

## The Author

**Hello!** I'm [Cariad Eccleston](https://cariad.io) and I'm an independent/freelance software engineer. If my work has value to you, please consider [sponsoring](https://github.com/sponsors/cariad/).
