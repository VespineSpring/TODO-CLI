import typer
from datetime import datetime

from rich import print
from rich.console import Console
from rich.table import Table

data = {
    "name": "Rick",
    "age": 42,
    "items": [{"name": "Portal Gun"}, {"name": "Plumbus"}],
    "active": True,
    "affiliation": None,
}

app = typer.Typer()
now = datetime.now()
console = Console()


@app.command()
def hello(name: str) -> None:
    print(f"[bold red]Hello[/bold red], [blue]{name}[/blue]!")
    print(data)


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


@app.command()
def table():
    table = Table("Name", "Item")
    table.add_row("Rick", "Portal Gun")
    table.add_row("Morty", "Plumbus")
    console.print(table)


if __name__ == "__main__":
    app()
