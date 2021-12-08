from typing import Optional

import importlib_metadata as metadata
import typer

app = typer.Typer(help="Inventopy")

def version_callback(value: bool):
    if value:
        typer.echo(f"Version: {metadata.version('inventopy')}")
        raise typer.Exit(0)


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None, "--version", callback=version_callback, is_eager=True
    ),
):  # pylint: disable=unused-argument
    pass


if __name__ == "__main__":
    app()
