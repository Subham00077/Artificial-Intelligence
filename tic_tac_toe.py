 # Tic-Tac-Toe Game def print_board(board): for row in board: print(" | ".join(row)) 
print("-" * 5) 
 
 
def check_winner(board, player): 
# Check rows, columns, and diagonals for a win 
 for i in range(3): 
 if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]): 
return True 
return (board[0][0] == board[1][1] == board[2][2] == player) or (board[0][2] == 
board[1][1] == board[2][0] == player) 
 
 
def is_draw(board): 
return all([cell != " " for row in board for cell in row]) 
 
 
def tic_tac_toe_pvp(): board = [[" " for _ in range(3)] for _ in range(3)] players = ["X", "O"] 
current_player = 0 
 
 
while True: 
print_board(board) print(f"Player {players[current_player]}'s turn.") 
try: 
row, col = map(int, input("Enter row and column (1-3) separated by space: ").split()) 
row, col = row - 1, col - 1 # Convert to zero-index if board[row][col] == " ": 
board[row][col] = players[current_player] if check_winner(board, players[current_player]): print_board(board) print(f"Player {players[current_player]} wins!") break if is_draw(board): print_board(board) 
print("It's a draw!") 
break current_player = 1 - current_player 
else: 
print("Cell already taken. Try again.") except (ValueError, IndexError): 
print("Invalid input. Try again.") 
 
 
# Run the player vs player game 
tic_tac_toe_pvp() 
 
Player vs Computer:- 
import random 
 
 
# Tic-Tac-Toe Game: Man vs Computer def print_board(board): for row in board: print(" | ".join(row)) print("-" * 5) 
 
def check_winner(board, player): 
for i in range(3): 
if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]): 
return True 
return (board[0][0] == board[1][1] == board[2][2] == player) or (board[0][2] == board[1][1] 
== board[2][0] == player) 
 
 
def is_draw(board): 
return all([cell != " " for row in board for cell in row]) 
 
 
def computer_move(board): 
empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "] 
return random.choice(empty_cells) 
 
def tic_tac_toe_vs_computer(): 
board = [[" " for _ in range(3)] for _ in range(3)] player = "X" 
computer = "O" 
 
 
while True: 
print_board(board) 
 
# Player's turn print("Your turn.") 
try: 
row, col = map(int, input("Enter row and column (1-3) separated by space: ").split()) row, col = row - 1, col - 1 if board[row][col] == " ": board[row][col] = player 
if check_winner(board, player): 
print_board(board) print("You win!") break if is_draw(board): print_board(board) 
print("It's a draw!") 
break 
 
# Computer's turn row, col = computer_move(board) board[row][col] = computer 
print(f"Computer places 'O' at ({row + 1}, {col + 1})") if check_winner(board, computer): 
print_board(board) print("Computer wins!") break if is_draw(board): print_board(board) 
print("It's a draw!") 
break 
else: 
print("Cell already taken. Try again.") except (ValueError, IndexError): 
print("Invalid input. Try again.") 
 
