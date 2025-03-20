# X has won in the first row
board_with_horizonal_x_win = [
    ["X", "X", "X"],
    ["4", "O", "6"],
    ["7", "8", "O"]
]

board_with_vertical_x_win = [
    ["X", "2", "O"],
    ["X", "O", "6"],
    ["X", "8", "9"]
]

# X has won in the left up to right down diagonal
board_with_diagonal_x_win = [
    ["X", "O", "O"],
    ["4", "X", "6"],
    ["7", "8", "X"]
]

# the entire board is filled - no turns left to make
board_with_draw = [
    ["O", "X", "O"],
    ["O", "X", "X"],
    ["X", "O", "X"]
]

# there's only one possible turn left and it will not result in victory
board_with_unachievable_win = [
    ["O", "X", "O"],
    ["O", "X", "X"],
    ["X", "8", "X"]
]

# random half played out game
random_unfinished_game_1 = [
    ["X", "2", "X"],
    ["X", "O", "O"],
    ["O", "8", "9"]
]

# another random half played out game
random_unfinished_game_2 = [
    ["X", "O", "O"],
    ["X", "O", "6"],
    ["7", "X", "X"]
]
