import typer

from tensortrans import __version__

app = typer.Typer()


@app.command()
def version() -> None:
    typer.echo(f"TensorTrans version {__version__}")


@app.command()
def tf2pytorch(
    input_file: str = typer.Argument(..., help="Input file or dir path"),
    output_file: str = typer.Argument(..., help="output file or dir path"),
) -> None:
    typer.echo(f"Converting fro TensorFlow2 to Pytorch: {input_file} -> {output_file}")
