#Tic Tac Toe Game In Python

board = [" " for i in range(9)]

def display_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner (player):
    win_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in win_positions:
        if board[a] == board[b] == board[c] == player:
            return True

    return False

def play_game():
    player = "X"

    while True:
        display_board()

        try:
            position = int(input(
                f"Player (player), enter position (1-9):"
            )) - 1
        except ValueError:
            print("please enter a number from 1 to 9.")
            continue

        if position < 0 or position > 8:
            print("Invalid position! Choose from 1 to 9.")

        if board[position] != " ":
            print("Position already occupied! Try again.")

        board[position] = player

        if check_winner(player):
            display_board()
            print(f"player (player) wins!")
            break

        if " " not in board:
            display_board()
            print("The game is a draw!")
            break

        player = "Q" if player == "X" else "X"

play_game()
