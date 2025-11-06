import numpy as np

board = np.array(['-'] * 9).reshape(3, 3)
x = "X"
o = "O"

def check_rows(symbol):
    for r in range(3):
        count = 0
        for c in range(3):
            if board[r][c] == symbol:
                count += 1
        if count == 3:
            print(f"{symbol} won")
            return True
    return False

def check_cols(symbol):
    for r in range(3):
        count = 0
        for c in range(3):
            if board[r][c] == symbol:
                count += 1
        if count == 3:
            print(f"{symbol} won")
            return True
    return False

def check_diagonals(symbol):
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] == symbol:
        print(f"{symbol} won")
        return True
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] == symbol:
        print(f"{symbol} won")
        return True
    return False

def won(symbol):
    return check_rows(symbol) or check_cols(symbol) or check_diagonals(symbol)

def place(symbol):
    print(board)
    while True:
        row = int(input('Enter row: 1 / 2 / 3: '))
        col = int(input('Enter col: 1 / 2 / 3: '))
        if row > 0 and row < 4 and col > 0 and col < 4 and board[row - 1][col - 1] == '-':
            break
        else:
            print('Invalid Input. Please enter again')
    board[row - 1][col - 1] = symbol


def play():
    for turn in range(9):
        if turn % 2 == 0:
            print('X turn')
            place(x)
            if won(x):
                break
        else:
            print('O turn')
            place(o)
            if won(o):
                break
    if not won(x) and not won(o):
        print('Draw')

play()

