# Attributes

A code block will be executed only if it's followed by a `dinject` tag:

```text
<!--dinject-->
```

## Fence

By default, `dinject` fences code blocks with backticks.

To fence the code with tildes, set `fence=tildes`:

```text
<!--dinject fence=tildes-->
```

## Injection content type

By default, `dinject` injects the result as a plain text Markdown block.

To inject the result as a HTML fragment, set `as=html`:

```text
<!--dinject as=html-->
```

## Execution host

By default, `dinject` executes the code in a subshell.

To execute the code in a pseudo terminal (i.e. if you need to capture escape codes), set `host=terminal`:

```text
<!--dinject host=terminal-->
```

!!! warning
    Pseudo terminals must be supported by your operating system. GNU/Linux distributions tend to be great. Windows tends to not.
