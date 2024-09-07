import typer
from datetime import datetime

app = typer.Typer()
now = datetime.now()


@app.command()
def hello(name: str) -> None:
    print(f"Hello, {name}!")


@app.command()
def goodbye(name: str, formal: bool = False) -> None:
    if formal:
        print(f"Goodbye {name}. Have a nice day.")
    else:
        print(f"Bye {name}!")


@app.command()
def time() -> None:
    time: str = now.strftime("%I:%M %p")
    print(time)


@app.command()
def date() -> None:
    date: str = now.strftime("%A, %d %B, %Y")
    print(date)


@app.command()
def date_time() -> None:
    date_time: str = now.strftime("%A, %d %B, %Y at %I:%M %p")
    print(date_time)


if __name__ == "__main__":
    app()
