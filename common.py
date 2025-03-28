board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

# Создаём доску
def print_board(board):
    for i in range(len(board)):
        pipe = "|".join(board[i])
        print(pipe)
        if i < len(board) - 1:
            print("-----")

def check_row_win(row):
    if row[0] == row[1] == row[2]:
        return row[0]

def check_col_win(col,board):
    if board[0][col] == board[1][col] == board[2][col]:
        return board[0][col]

def check_diagonal_win(board):
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

def check_draw(board):
    for row in board:
        for cell in row:
            if cell not in ["X", "O"]:
                return False
    return True
    # TODO напиши сам - должно возвращать True если доска заполненна и никто не выиграл
    #  или (за дополнительный респект) если остался всего один ход который не приведет к победе

# Проверка на победу
def check_win(board, player):
    for row in board:
        if check_row_win(row):
            return player
    for col in range(3):
        if check_col_win(col, board):
            return player
    if check_diagonal_win(board):
        return player