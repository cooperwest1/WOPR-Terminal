
from rich.console import Console
from rich.prompt import Prompt
import time

console = Console()

def main_menu():
    console.print("[bold green]\nWOPR MAIN MENU[/bold green]")
    console.print("1. LOGON")
    console.print("2. HELP GAMES")
    console.print("3. LIST GAMES")
    console.print("4. GLOBAL THERMONUCLEAR WAR\n")

    choice = Prompt.ask("Select an option")
    if choice == "1":
        console.print("LOGON not implemented yet.")
    elif choice == "2":
        console.print("HELP GAMES not implemented yet.")
    elif choice == "3":
    from games.tictactoe import start_game
    start_game()
    elif choice == "4":
        from games.global_thermonuclear_war import start_game
        start_game()
    else:
        console.print("[red]Invalid option[/red]")

if __name__ == "__main__":
    main_menu()
