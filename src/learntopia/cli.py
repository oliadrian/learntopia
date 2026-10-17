import importlib.metadata as mtd
from typing import Annotated

import typer

__version__ = mtd.version("learntopia")

app = typer.Typer()


def version_callback(value: bool) -> None:
    if value:
        typer.echo(f"Learntopia CLI Version: {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Annotated[
        bool,
        typer.Option(
            "--version",
            callback=version_callback,
            is_eager=True,
            help="Show the version and exit.",
        ),
    ] = False,
) -> None:
    """Learntopia: a study planner that replans for you."""
