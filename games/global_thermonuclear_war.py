from rich.console import Console
import time
import random

console = Console()

def start_game():
    console.print("[bold red]\nInitializing Global Thermonuclear War Simulation...[/bold red]")
    time.sleep(1.5)

    countries = ["USA", "USSR", "China", "France", "UK"]
    targets = ["military base", "missile silo", "airfield", "submarine fleet", "command center"]
    
    selected_enemy = random.choice([c for c in countries if c != "USA"])
    console.print(f"\nEnemy Identified: [bold yellow]{selected_enemy}[/bold yellow]")
    time.sleep(1.2)

    console.print("\nPreparing first strike options...")
    time.sleep(1.2)

    for i in range(1, 4):
        target = random.choice(targets)
        location = f"Sector {random.randint(1, 99)}"
        console.print(f"[cyan]Option {i}: Launch at {target} in {location}[/cyan]")
        time.sleep(0.8)

    console.print("\n[bold green]Launch Option Selected...[/bold green]")
    time.sleep(1)
    console.print("[red]Launching missiles...[/red]")
    for i in range(5):
        console.print(f"[yellow]>> Missile {i+1} en route...[/yellow]")
        time.sleep(0.6)

    console.print("\n[bold red]Impact detected.[/bold red] Damage assessment underway...")
    time.sleep(1.5)

    casualties = random.randint(1_000_000, 200_000_000)
    console.print(f"[bold red]Estimated casualties: {casualties:,}[/bold red]")
    time.sleep(2)

    console.print("\n[green]Simulation complete. Returning to main menu...[/green]")
    time.sleep(2)
