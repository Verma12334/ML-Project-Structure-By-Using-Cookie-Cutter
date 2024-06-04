"""Console script for ml_basic_practice."""
import ml_basic_practice

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for ml_basic_practice."""
    console.print("Replace this message by putting your code into "
               "ml_basic_practice.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
