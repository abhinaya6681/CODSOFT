import math

# Initialize the board
board = [' ' for _ in range(9)]

def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def is_winner(brd, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    return any(all(brd[i] == player for i in condition) for condition in win_conditions)

def is_draw(brd):
    return ' ' not in brd

def minimax(brd, depth, is_maximizing):
    if is_winner(brd, 'O'):
        return 1
    elif is_winner(brd, 'X'):
        return -1
    elif is_draw(brd):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = 'O'
                score = minimax(brd, depth + 1, False)
                brd[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = 'X'
                score = minimax(brd, depth + 1, True)
                brd[i] = ' '
                best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'O'

def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("Cell already taken.")
        except (IndexError, ValueError):
            print("Invalid input. Please enter a number from 1 to 9.")

def main():
    print("Welcome to Tic-Tac-Toe!")
    print_board()
    
    while True:
        player_move()
        print_board()
        if is_winner(board, 'X'):
            print("You win!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

        print("AI's move:")
        ai_move()
        print_board()
        if is_winner(board, 'O'):
            print("AI wins!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
