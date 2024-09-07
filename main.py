import typer

app = typer.Typer()


@app.command()
def hello(name: str) -> None:
    print(f"Hello, {name}!")


@app.command()
def goodbye(name: str, formal: bool = False) -> None:
    if formal:
        print(f"Goodbye {name}. Have a nice day.")
    else:
        print(f"Bye {name}!")


if __name__ == "__main__":
    app()
