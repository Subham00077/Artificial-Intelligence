import math

def print_board(board):
    
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):

    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_full(board):

    return all(board[row][col] != " " for row in range(3) for col in range(3))

def minimax(board, is_maximizing):

    winner = check_winner(board)
    if winner == "X":
        return -1
    elif winner == "O":
        return 1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "O"
                    score = minimax(board, False)
                    board[row][col] = " "
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "X"
                    score = minimax(board, True)
                    board[row][col] = " "
                    best_score = min(best_score, score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "O"
                score = minimax(board, False)
                board[row][col] = " "
                if score > best_score:
                    best_score = score
                    move = (row, col)
    return move

def main():

    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Player move
        while True:
            try:
                player_move = int(input("Enter your move (1-9): ")) - 1
                row, col = divmod(player_move, 3)
                if board[row][col] == " ":
                    board[row][col] = "X"
                    break
                else:
                    print("Cell already taken! Try again.")
            except (ValueError, IndexError):
                print("Invalid input! Please enter a number between 1 and 9.")

        print_board(board)

        if check_winner(board) == "X":
            print("Congratulations! You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        # AI move
        print("AI's turn...")
        ai_move = best_move(board)
        if ai_move:
            board[ai_move[0]][ai_move[1]] = "O"

        print_board(board)

        if check_winner(board) == "O":
            print("AI wins! Better luck next time.")
            break
        if is_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
