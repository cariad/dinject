from pathlib import Path
from re import match
from shutil import move
from subprocess import run
from tempfile import NamedTemporaryFile
from typing import IO, Optional

from naughtty import NaughTTY
from thtml import Scope, write_html

from dinject.enums import Content, Host, Range
from dinject.executors import get_executor
from dinject.parser import Parser
from dinject.types import Block, Instruction


def execute(
    block: Block,
    instruction: Instruction,
    parser: Parser,
    writer: IO[str],
) -> None:
    """
    Executes `block` then writes the result to `writer`, with respect to
    `instruction`.
    """

    executor = get_executor(block)

    if not executor:
        # We don't support this language, so pass through.
        block.write(writer)
        return

    if instruction.host == Host.TERMINAL:
        n = NaughTTY(command=executor.arguments)
        n.execute()
        content = n.output
    else:
        process = run(executor.arguments, capture_output=True)
        content = process.stdout.decode("UTF-8")

    content = content.rstrip() + "\n"

    parser.write_range_start(instruction, writer)
    writer.write("\n")

    if instruction.content == Content.HTML:
        write_html(text=content, writer=writer, scope=Scope.FRAGMENT, theme="plain")
        writer.write("\n")
    else:
        Block(lang="text", lines=[content]).write(writer)

    writer.write("\n")
    parser.write_range_end(writer)


def inject(reader: IO[str], writer: IO[str], parser: Optional[Parser] = None) -> None:
    """Reads and injects from `reader` to `writer`."""

    block: Optional[Block] = None
    parser = parser or Parser()
    skip_to_emitted_end = False

    for line in reader:
        if not block or block.complete:
            din = parser.get_instruction(line)

            if skip_to_emitted_end:
                if din and din.range == Range.END:
                    skip_to_emitted_end = False
                continue

            if din and block:
                execute(
                    block=block,
                    instruction=din,
                    parser=parser,
                    writer=writer,
                )
                block = None
                if din.range == Range.START:
                    skip_to_emitted_end = True
                continue

        writer.write(line)

        if block:
            if not block.complete:
                if line == "```\n":
                    block.complete = True
                    continue

                block.lines.append(line)
                continue

        block = is_block_start(line) or block


def inject_file(path: Path, parser: Optional[Parser] = None) -> None:
    """
    Executes the code blocks and injects the results into the Markdown document
    at `path`.
    """

    with NamedTemporaryFile("a", delete=False) as writer:
        with open(path, "r") as reader:
            inject(
                parser=parser,
                reader=reader,
                writer=writer,
            )
        writer.flush()
        move(writer.name, path)


def is_block_start(line: str) -> Optional[Block]:
    m = match("^```(.+)$", line)
    if not m:
        return None
    return Block(lang=m.group(1), lines=[], complete=False)
