from rich.prompt import Prompt
from rich.console import Console
import os

from games.tictactoe import start_game as tictactoe_game
from games.global_thermonuclear_war import start_game as gtw_game

console = Console()

def main_menu():
    while True:
        console.print("[bold green]\nWOPR MAIN MENU[/bold green]")
        console.print("1. LOGON")
        console.print("2. HELP GAMES")
        console.print("3. LIST GAMES")
        console.print("4. GLOBAL THERMONUCLEAR WAR")
        console.print("5. EXIT\n")

        choice = Prompt.ask("Select an option")

        if choice == "1":
            console.print("LOGON not implemented yet.")
        elif choice == "2":
            console.print("HELP GAMES not implemented yet.")
        elif choice == "3": os.system("clear")
            console.print("Available Games:\n- Tic Tac Toe\n- Global Thermonuclear War")
        elif choice == "4": os.system("clear")
            gtw_game()
        elif choice == "5":
            console.print("Exiting WOPR Terminal.")
            break
        elif choice == "tic tac toe" or choice == "tictactoe":
            tictactoe_game()
        else:
            console.print("[red]Invalid option[/red]")

if __name__ == "__main__":
    main_menu()
