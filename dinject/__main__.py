def cli_entry() -> None:
    from dinject.cli import make_response

    msg, code = make_response()
    print(msg)
    exit(code)


if __name__ == "__main__":

    cli_entry()
