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
def add() -> None:
    while True:
        task: str = input("Task: ")

        if len(task) <= 3:
            print("Your task must be more than 3 letters.")
            continue

        break

    with open(TASK_FILE, "r") as file:
        data = json.load(file)

    data.append(task)

    with open(TASK_FILE, "w") as file:
        json.dump(data, file, indent=4)

    print("[bold red]Task has been added.[/bold red]")
    print(f"[yellow]TASK:[/yellow] [blue]{task}[/blue]")


@app.command()
def tasks() -> None:
    table = Table("No.", "Tasks")

    with open(TASK_FILE, "r") as file:
        data = json.load(file)

    for index, task in enumerate(data, start=1):
        table.add_row(str(index), task)

    console.print(table)


@app.command()
def remove(index: int) -> None:
    with open(TASK_FILE, "r") as file:
        data = json.load(file)

    try:
        task = data[index - 1]
    except IndexError:
        task = None

    if not task:
        print("[red]No task found.[/red]\nUse `tasks` command to see the list.")
        return
    
    data.remove(task)

    with open(TASK_FILE, "w") as file:
        json.dump(data, file, indent=4)

    print("[blue]Task has been removed.[/blue]")


if __name__ == "__main__":
    app()
