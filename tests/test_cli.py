from pathlib import Path

from mock import call, patch

from dinject.cli import make_response


def test_make_response__version() -> None:
    assert make_response(["--version"]) == ("-1.-1.-1", 0)


def test_make_response__no_files() -> None:
    assert make_response([]) == ("You must specify at least one Markdown file.", 1)


def test_make_response__files() -> None:
    with patch("dinject.cli.inject_file") as inject_file:
        assert make_response(["foo.md", "bar.md"]) == ("", 0)

    assert inject_file.call_count == 2

    inject_file.assert_has_calls(
        [
            call(path=Path("foo.md")),
            call(path=Path("bar.md")),
        ]
    )
