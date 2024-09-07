import typer
import os
import json

from rich import print
from rich.console import Console
from rich.table import Table

app = typer.Typer()
TASK_FILE = "tasks.json"
console = Console()


if not os.path.exists(TASK_FILE) or os.path.getsize(TASK_FILE) == 0:
    with open(TASK_FILE, "w") as file:
        json.dump([], file)


@app.command()
def add(task: str) -> None:
    with open(TASK_FILE, "r") as file:
        data = json.load(file)

    data.append(task)
    
    with open(TASK_FILE, "w") as file:
        json.dump(data, file, indent=4)

    print("[bold red]Task has been added.[/bold red]")
    print(f"[yellow]TASK:[/yellow] [blue]{task}[/blue]")


@app.command()
def tasks() -> None:
    table = Table("Tasks")

    with open(TASK_FILE, "r") as file:
        data = json.load(file)

    for task in data:
        table.add_row(task)

    console.print(table)


if __name__ == "__main__":
    app()
