"""List command group - list local data files."""

import os
from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table

from .utils import find_files_by_schema

app = typer.Typer(help="List data files in directory")
console = Console()


@app.command("providers")
def list_providers(
    data_dir: Path | None = typer.Argument(
        None,
        help="Directory containing provider files (default: ./data or UNITYSVC_DATA_DIR env var)",
    ),
):
    """List all provider files found in the data directory."""
    # Set data directory
    if data_dir is None:
        data_dir_str = os.getenv("UNITYSVC_DATA_DIR")
        if data_dir_str:
            data_dir = Path(data_dir_str)
        else:
            data_dir = Path.cwd() / "data"

    if not data_dir.is_absolute():
        data_dir = Path.cwd() / data_dir

    if not data_dir.exists():
        console.print(f"[red]✗[/red] Data directory not found: {data_dir}", style="bold red")
        raise typer.Exit(code=1)

    console.print(f"[blue]Searching for providers in:[/blue] {data_dir}\n")

    # Find provider files by schema
    provider_files = find_files_by_schema(data_dir, "provider_v1")

    if not provider_files:
        console.print("[yellow]No provider files found.[/yellow]")
        return

    # Create table
    table = Table(title="Provider Files", show_lines=True)
    table.add_column("File", style="cyan")
    table.add_column("Name", style="green")
    table.add_column("Display Name", style="blue")

    for file_path, _file_format, data in sorted(provider_files, key=lambda x: x[0]):
        table.add_row(
            str(file_path.relative_to(data_dir)),
            data.get("name", "N/A"),
            data.get("display_name", "N/A"),
        )

    console.print(table)
    console.print(f"\n[green]Total:[/green] {len(provider_files)} provider file(s)")


@app.command("sellers")
def list_sellers(
    data_dir: Path | None = typer.Argument(
        None,
        help="Directory containing seller files (default: ./data or UNITYSVC_DATA_DIR env var)",
    ),
):
    """List all seller files found in the data directory."""
    # Set data directory
    if data_dir is None:
        data_dir_str = os.getenv("UNITYSVC_DATA_DIR")
        if data_dir_str:
            data_dir = Path(data_dir_str)
        else:
            data_dir = Path.cwd() / "data"

    if not data_dir.is_absolute():
        data_dir = Path.cwd() / data_dir

    if not data_dir.exists():
        console.print(f"[red]✗[/red] Data directory not found: {data_dir}", style="bold red")
        raise typer.Exit(code=1)

    console.print(f"[blue]Searching for sellers in:[/blue] {data_dir}\n")

    # Find seller files by schema
    seller_files = find_files_by_schema(data_dir, "seller_v1")

    if not seller_files:
        console.print("[yellow]No seller files found.[/yellow]")
        return

    # Create table
    table = Table(title="Seller Files", show_lines=True)
    table.add_column("File", style="cyan")
    table.add_column("Name", style="green")
    table.add_column("Display Name", style="blue")

    for file_path, _file_format, data in sorted(seller_files, key=lambda x: x[0]):
        table.add_row(
            str(file_path.relative_to(data_dir)),
            data.get("name", "N/A"),
            data.get("display_name", "N/A"),
        )

    console.print(table)
    console.print(f"\n[green]Total:[/green] {len(seller_files)} seller file(s)")


@app.command("offerings")
def list_offerings(
    data_dir: Path | None = typer.Argument(
        None,
        help="Directory containing service files (default: ./data or UNITYSVC_DATA_DIR env var)",
    ),
):
    """List all service offering files found in the data directory."""
    # Set data directory
    if data_dir is None:
        data_dir_str = os.getenv("UNITYSVC_DATA_DIR")
        if data_dir_str:
            data_dir = Path(data_dir_str)
        else:
            data_dir = Path.cwd() / "data"

    if not data_dir.is_absolute():
        data_dir = Path.cwd() / data_dir

    if not data_dir.exists():
        console.print(f"[red]✗[/red] Data directory not found: {data_dir}", style="bold red")
        raise typer.Exit(code=1)

    console.print(f"[blue]Searching for service offerings in:[/blue] {data_dir}\n")

    # Find service files by schema
    service_files = find_files_by_schema(data_dir, "service_v1")

    if not service_files:
        console.print("[yellow]No service offering files found.[/yellow]")
        return

    # Create table
    table = Table(title="Service Offering Files", show_lines=True)
    table.add_column("File", style="cyan")
    table.add_column("Name", style="green")
    table.add_column("Display Name", style="blue")
    table.add_column("Status", style="magenta")

    for file_path, _file_format, data in sorted(service_files, key=lambda x: x[0]):
        table.add_row(
            str(file_path.relative_to(data_dir)),
            data.get("name", "N/A"),
            data.get("display_name", "N/A"),
            data.get("upstream_status", "N/A"),
        )

    console.print(table)
    console.print(f"\n[green]Total:[/green] {len(service_files)} service offering file(s)")


@app.command("listings")
def list_listings(
    data_dir: Path | None = typer.Argument(
        None,
        help="Directory containing listing files (default: ./data or UNITYSVC_DATA_DIR env var)",
    ),
):
    """List all service listing files found in the data directory."""
    # Set data directory
    if data_dir is None:
        data_dir_str = os.getenv("UNITYSVC_DATA_DIR")
        if data_dir_str:
            data_dir = Path(data_dir_str)
        else:
            data_dir = Path.cwd() / "data"

    if not data_dir.is_absolute():
        data_dir = Path.cwd() / data_dir

    if not data_dir.exists():
        console.print(f"[red]✗[/red] Data directory not found: {data_dir}", style="bold red")
        raise typer.Exit(code=1)

    console.print(f"[blue]Searching for service listings in:[/blue] {data_dir}\n")

    # Find listing files by schema
    listing_files = find_files_by_schema(data_dir, "listing_v1")

    if not listing_files:
        console.print("[yellow]No service listing files found.[/yellow]")
        return

    # Create table
    table = Table(title="Service Listing Files", show_lines=True)
    table.add_column("File", style="cyan")
    table.add_column("Seller", style="green")
    table.add_column("Status", style="magenta")

    for file_path, _file_format, data in sorted(listing_files, key=lambda x: x[0]):
        table.add_row(
            str(file_path.relative_to(data_dir)),
            data.get("seller_name", "N/A"),
            data.get("listing_status", "N/A"),
        )

    console.print(table)
    console.print(f"\n[green]Total:[/green] {len(listing_files)} service listing file(s)")
