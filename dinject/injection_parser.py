from typing import IO, Optional

from comprehemd import Block, CodeBlock, MarkdownParser

from dinject.enums.range import Range
from dinject.execute import execute
from dinject.parser import Parser


class InjectionParser(MarkdownParser):
    def __init__(self, writer: IO[str], parser: Optional[Parser] = None) -> None:
        super().__init__()
        self._parser = parser or Parser()
        self._writer = writer
        self._last_block: Optional[CodeBlock] = None
        self._skipping_range = False

    def handle_block(self, block: Block) -> None:
        din = self._parser.get_instruction(block.source)

        if self._skipping_range:
            if din and din.range == Range.END:
                self._skipping_range = False
            return

        if din and self._last_block:
            execute(
                block=self._last_block,
                instruction=din,
                parser=self._parser,
                writer=self._writer,
            )
            self._last_block = None
            if din.range == Range.START:
                self._skipping_range = True
            return

        if isinstance(block, CodeBlock):
            self._last_block = block

        self._writer.write(block.source)
