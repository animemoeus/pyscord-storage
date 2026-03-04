import typer

from ._sync import upload_from_file, upload_from_url

app = typer.Typer()


@app.command()
def file(path: str = typer.Argument(..., help="Path to local file to upload")):
    """Upload a local file to Discord storage."""
    result = upload_from_file(path)
    _print_result(result)


@app.command()
def url(file_url: str = typer.Argument(..., help="Remote URL to upload")):
    """Upload a remote URL to Discord storage."""
    result = upload_from_url(file_url)
    _print_result(result)


def _print_result(result):
    data = result.get("data")
    status = result.get("status")

    if status == 200 and isinstance(data, dict) and "x_url" in data:
        typer.echo(data["x_url"])
    else:
        if isinstance(data, dict):
            typer.echo(data.get("message") or data.get("error") or str(data), err=True)
        else:
            typer.echo(str(data), err=True)
        raise typer.Exit(1)


def main():
    app()
