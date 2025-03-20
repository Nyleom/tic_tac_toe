from mock_boards import *
from common import *


# на настоящей работе такая функция будет предоставленна тестинг фреймворком но для иллюстрации поинта
# сделаем простенькую версию сами
def assert_equal(a, b, explanation):
    if a == b :
        print(f"Test PASSED for: {explanation}.")
    else :
        raise Exception(f"Test FAILED for: {explanation}.")


def test_check_win():
    # сначала проверили что настоящие победы оно действительно детектит (true positive)
    # и не выдает как за невыигранные (false negative)
    test1 = check_win(board_with_horizonal_x_win, "X")
    assert_equal(test1, "X", "checking for horizontal win")

    test2 = check_win(board_with_vertical_x_win, "X")
    assert_equal(test2, "X", "checking for vertical_win")

    test3 = check_win(board_with_diagonal_x_win, "X")
    assert_equal(test3, "X", "checking for diagonal_win")


    # потом проверили что оно не выдает победу неверно (false positive)
    # и выдает победу неверно (true negative)
    test4 = check_win(board_with_draw, "X")
    assert_equal(test4, None, "checking that not a win is in fact not a win 1")

    test4 = check_win(board_with_unachievable_win, "X")
    assert_equal(test4, None, "checking that not a win is in fact not a win 2: the test strikes back")

    test4 = check_win(random_unfinished_game_1, "X")
    assert_equal(test4, None, "checking that not a win is in fact not a win 3: testing happily ever after")

    test4 = check_win(random_unfinished_game_2, "X")
    assert_equal(test4, None, "checking that not a win is in fact not a win 4: and the leathery wand")

    return True


def test_check_draw():
    # TODO когда допишешь check_draw() можно раскомментить и должно работать

    # проверяем что победы это не ничья
    # test1 = check_draw(board_with_horizonal_x_win, False)
    # assert_equal(test1, False, "checking that horizontal win is not a draw")
    #
    # test2 = check_draw(board_with_vertical_x_win, False)
    # assert_equal(test2, False, "checking that vertical win is not a draw")
    #
    # test3 = check_draw(check_diagonal_win(), False)
    # assert_equal(test3, False, "checking that diagonal win is not a draw")
    #
    # # проверяем что посреди игры это еще не ничья
    # test4 = check_draw(random_unfinished_game_1, False)
    # assert_equal(test4, False, "checking that if there are moves to be made that might result in a victory is not a draw")
    #
    # test5 = check_draw(random_unfinished_game_2, False)
    # assert_equal(test5, False, "checking that if there are moves to be made that might result in a victory is not a draw 2: тестовая братва")
    #
    # # проверяем что ничья это ничья
    # test6 = check_draw(board_with_draw(), True)
    # assert_equal(test6, False, "checking that the filled board that doesn't have a win is indeed a draw")
    #
    # # проверяем что если остался всего один ход и он не приведет к победе то это тоже ничья (опционально)
    # test7 = check_draw(board_with_unachievable_win(), True)
    # assert_equal(test7, False, "checking that there is only one move left to make that will not result in a victory IS a draw")

    return True

