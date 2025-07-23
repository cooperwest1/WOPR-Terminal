import time
from rich.console import Console

console = Console()

def start_game():
    console.print("[bold red]GLOBAL THERMONUCLEAR WAR SIMULATION INITIATED[/bold red]")
    time.sleep(1)
    regions = ["USA", "SOVIET UNION", "CHINA", "FRANCE", "UNITED KINGDOM", "NORTH KOREA", "ISRAEL", "IRAN"]
    
    console.print("\nSelect target region:")
    for i, region in enumerate(regions, start=1):
        console.print(f"{i}. {region}")

    try:
        choice = int(console.input("\n> "))
        if 1 <= choice <= len(regions):
            selected = regions[choice - 1]
            simulate_strike(selected)
        else:
            console.print("[red]Invalid region selection[/red]")
    except ValueError:
        console.print("[red]Invalid input[/red]")

def simulate_strike(region):
    console.print(f"\n[bold yellow]Target Locked: {region}[/bold yellow]")
    time.sleep(1)
    console.print("Launching missiles...")
    for i in range(3):
        time.sleep(1)
        console.print(f"Missile {i+1} launched...")
    console.print(f"\n[bold red]{region} has been obliterated.[/bold red]")
    console.print("[green]Would you like to play a game?[/green]")
