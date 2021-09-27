from dataclasses import dataclass
from re import match
from typing import IO, Dict

from dinject.enums import Emit, Emitted, Host


@dataclass
class Instruction:
    """dinject instruction"""

    emit: Emit
    """Type to emit."""

    emitted: Emitted
    """Injection demarcation."""

    host: Host
    """How to execute the script."""

    @staticmethod
    def parse(text: str) -> "Instruction":
        """Parses a plain text line as an instruction."""

        pairs = text.split(" ")
        wip: Dict[str, str] = {}
        for pair in pairs:
            m = match("([a-z]+)=([a-z]+)", pair)
            if not m:
                continue

            key = m.group(1)
            value = m.group(2)

            wip[key] = value

        return Instruction(
            emit=Emit[wip.get("emit", Emit.MARKDOWN.name).upper()],
            emitted=Emitted[wip.get("emitted", Emitted.NOT_EMITTED.name).upper()],
            host=Host[wip.get("host", Host.SHELL.name).upper()],
        )

    def write_emitted_start(self, writer: IO[str]) -> None:
        """Writes an instruction to mark the start of an injection."""

        writer.write("<!--dinject")
        writer.write(f" emit={self.emit.name.lower()}")
        writer.write(f" emitted={Emitted.START.name.lower()}")
        writer.write(f" host={self.host.name.lower()}")
        writer.write("-->\n\n")

    def write_emitted_end(self, writer: IO[str]) -> None:
        """Writes an instruction to mark the end of an injection."""

        writer.write("<!--dinject")
        writer.write(f" emitted={Emitted.END.name.lower()}")
        writer.write("-->\n")
