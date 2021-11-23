from pathlib import Path
from shutil import move
from tempfile import NamedTemporaryFile
from typing import IO, Iterable, Optional, Union

from dinject.injection_parser import InjectionParser
from dinject.parser import Parser

Reader = Union[str, IO[str]]


def inject(
    reader: Reader,
    writer: IO[str],
    parser: Optional[Parser] = None,
) -> None:
    """Reads and injects from `reader` to `writer`."""

    injection_parser = InjectionParser(parser=parser or Parser(), writer=writer)
    if isinstance(reader, str):
        injection_parser.feed(reader)
        injection_parser.close()
    else:
        injection_parser.read(reader)


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
        move(writer.name, path)


def iterate_lines(reader: Reader) -> Iterable[str]:
    """Returns an line iterator."""

    it = reader.split("\n") if isinstance(reader, str) else reader

    for line in it:
        yield line.rstrip()
