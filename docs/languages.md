# Languages

## Bash

`dinject` executes Bash code blocks via `/usr/bin/env bash -c CODE`.

This will require a Linux-like operating system or operating system layer.

## Python

`dinject` executes Bash code blocks via `python -c CODE`.

The first Python interpreter available in your path will be used; this includes your virtual environment if you're in one. `dinject` will rely on that interpreter/virtual environment to perform the imports.

## Text

Text blocks will be passed-through unchanged.
