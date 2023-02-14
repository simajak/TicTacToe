divider = "=" * 42

print("Welcome to Tic Tac Toe")
print(divider)
print("GAME RULES: \n"
      "Each player can place one mark (or stone) \n"
      "per turn on the 3x3 grid. \n"
      "The WINNER is who succeeds in placing \n"
      "three of their marks in a \n"
      "* horizontal, \n"
      "* vertical or \n"
      "* diagonal row.")
print(divider)
print("Let's start the game!")

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
curr_player = "X"
winner = None
game_running = True

# Herní plán
def print_board(board):
    def print_board(board):
        print(board[0] + " | " + board[1] + " | " + board[2])
        print("---------")
        print(board[3] + " | " + board[4] + " | " + board[5])
        print("---------")
        print(board[6] + " | " + board[7] + " | " + board[8])
    print_board(board)

# Hráč hraje
def player_input(board):
    inp = int(input(f"Player {curr_player} | Please enter your move number: "))
    if inp >= 1 and inp <=9 and board[inp - 1] == "-":
        board[inp - 1] = curr_player
    else:
        print("Player already placed mark in that spot!")


# Kontrola, zda vyhrál

# horizontálně
def check_horizont(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

# vertikálně
def check_vertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

# diagonálně
def check_diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

# Výhra
def check_if_win(board):
    if check_diagonal(board) or check_vertical(board) or check_horizont(board):
        print_board(board)
        print(f" Congratulations, the player {winner} WON!")
        print(divider)
        game_running = False

# Remíza
def check_if_tie(board):
    if "-" not in board:
        print_board(board)
        print("It's a Tie!")
        game_running = False

# Výměna hráčů

while game_running:
    print_board(board)
    player_input(board)
    check_if_win(board)
    check_if_tie(board)