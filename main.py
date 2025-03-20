from common import print_board, board, check_win
from test_tic_tac_toe import test_check_win


def main():
    print("Начинаем игру!")
    player = "X"

    while True:
        print_board(board)
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

        winner = check_win(board, player)
        # Показать победителя
        if winner:
            print_board(board)
            print(f"Игрок {winner} победил!")
            break
        # Проверка на ничью - TODO заменить на check_draw()
        if all(cell in ["X", "O"] for row in board for cell in row):
            print_board(board)
            print("Ничья")
            break

        # flipping the player at the end of a loop iteration
        if player == "X":
            player = "O"
        else:
            player = "X"

if __name__ == '__main__':
    # прогоняем тесты прежде чем начинать играть

    test_check_win()
    # test_check_draw()  <- TODO раскомменть как напишешь check_draw()

    print('\n' * 5)

    # убедились что тесты работают теперь запускаем цикл
    main()