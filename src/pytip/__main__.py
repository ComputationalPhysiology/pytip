from pathlib import Path
import random
from rich.console import Console
from rich.pretty import pprint
from typing import Optional
import typer


from .tips import names, get_tips


def main(
    list_tips: bool = typer.Option(False, help="List all available tips"),
    history: Optional[Path] = typer.Option(
        None,
        help="Provide a path to a history file so that previously used tips will not be used",
    ),
):

    if list_tips:

        pprint(list(names), expand_all=True)
        raise typer.Exit()

    console = Console()
    data = get_tips()

    key = random.choice(list(iter(data.keys())))
    console.print(data[key])


if __name__ == "__main__":
    typer.run(main)
