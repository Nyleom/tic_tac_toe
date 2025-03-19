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



def check_col_win(col):
    if board[0][col] == board[1][col] == board[2][col]:
        return board[0][col]

def check_diagonal_win(board):
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

# Проверка на победу
def check_win(board):
    for row in board:
        if check_row_win(row):
            return player
    for col in range(3):
        if check_col_win(col):
            return player
    if check_diagonal_win(board):
        return player


player_is_cross = True



while True:
    print_board(board)
    player = "X" #if player_is_cross else "O"
    if player_is_cross:
        player = "X"
    else:
        player = "O"
    while True:
        try:
            players_move = int(input(f"Игрок {player}, введите номер клетки (1-9): "))
            if players_move < 1 or players_move > 9:
                print("Введите от 1 до 9!")
                continue
            row = (players_move - 1) // 3
            col = (players_move - 1) % 3
            if board[row][col] not in ["X", "O"]:
                board[row][col] = player
                break
            else:
                print("Клетка занята, выберите другую!")
        except ValueError:
            print("Введите число!")


    winner = check_win(board)
    # Показать победителя
    if winner:
        print_board(board)
        print(f"Игрок {winner} победил!")
        break
    # Проверка на ничью
    if all(cell in ["X", "O"] for row in board for cell in row):
        print_board(board)
        print("Ничья")
        break


    player_is_cross = not player_is_cross


