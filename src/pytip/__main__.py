import random
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.table import Table

from .tips import get_tips


def main(
    list_tips: bool = typer.Option(False, help="List all available tips"),
    history: Optional[Path] = typer.Option(
        None,
        help="Provide a path to a history file so that previously used tips will not be used",
    ),
):
    console = Console()
    data = get_tips()

    if list_tips:

        table = Table(title="Tips and tricks")
        table.add_column("Name")
        table.add_column("Description")
        table.add_column("Keywords")

        for k, v in data.items():
            table.add_row(
                v.metadata["name"],
                v.metadata["description"],
                v.metadata["keywords"],
            )

        console.print(table)
        raise typer.Exit()

    key = random.choice(list(iter(data.keys())))
    console.print(data[key].text)


if __name__ == "__main__":
    typer.run(main)
