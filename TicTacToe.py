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

# Kontrola, zda vyhrál

# Výměna hráčů

# Kontrola, zda vyhrál

