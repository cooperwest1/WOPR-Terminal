def start_game():
    board = [" " for _ in range(9)]

    def print_board():
        print("\n")
        print(f"{board[0]} | {board[1]} | {board[2]}")
        print("--+---+--")
        print(f"{board[3]} | {board[4]} | {board[5]}")
        print("--+---+--")
        print(f"{board[6]} | {board[7]} | {board[8]}")
        print("\n")

    def check_win(player):
        wins = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in wins:
            if all(board[i] == player for i in combo):
                return True
        return False

    def check_draw():
        return " " not in board

    current_player = "X"
    while True:
        print_board()
        move = input(f"Player {current_player}, enter your move (1-9): ")
        if not move.isdigit() or int(move) not in range(1, 10):
            print("Invalid input. Try again.")
            continue
        move = int(move) - 1
        if board[move] != " ":
            print("Spot already taken. Try again.")
            continue
        board[move] = current_player
        if check_win(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break
        if check_draw():
            print_board()
            print("It's a draw!")
            break
        current_player = "O" if current_player == "X" else "X"
