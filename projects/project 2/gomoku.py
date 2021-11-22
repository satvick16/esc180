"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Oct. 30, 2021
"""


def is_empty(board):
    for row in board:
        for elem in row:
            if elem != " ":
                return False

    return True


def is_bounded(board, y_end, x_end, length, d_y, d_x):
    curr_player = board[y_end][x_end]

    x_min, y_min = 0, 0
    x_max, y_max = len(board[0]) - 1, len(board) - 1
    x_start, y_start = None, None
    left, right = False, False

    if d_y == 0:
        x_start = x_end - length + 1
        y_start = y_end

        if x_start - 1 >= x_min and board[y_start][x_start-1] in [" ", curr_player]:
            left = True
        if x_end + 1 <= x_max and board[y_end][x_end+1] in [" ", curr_player]:
            right = True
    else:
        y_start = y_end - length + 1

        if d_x == 0:
            x_start = x_end

            if y_start - 1 >= y_min and board[y_start-1][x_start] in [" ", curr_player]:
                left = True
            if y_end + 1 <= y_max and board[y_end+1][x_end] in [" ", curr_player]:
                right = True
        elif d_x == 1:
            x_start = x_end - length + 1

            if x_start - 1 >= x_min and y_start - 1 >= y_min and board[y_start-1][x_start-1] in [" ", curr_player]:
                left = True
            if x_end + 1 <= x_max and y_end + 1 <= y_max and board[y_end+1][x_end+1] in [" ", curr_player]:
                right = True
        else:
            x_start = x_end + length - 1

            if x_start + 1 <= x_max and y_start + 1 <= y_max and board[y_start+1][x_start+1] in [" ", curr_player]:
                right = True
            if x_end - 1 >= x_min and y_end + 1 <= y_max and board[y_end+1][x_end-1] in [" ", curr_player]:
                left = True

    if left and right:
        return "OPEN"
    elif not left and not right:
        return "CLOSED"
    else:
        return "SEMIOPEN"


def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    if col == "b":
        nc = "w"
    else:
        nc = "b"

    x = x_start
    y = y_start

    row = ""

    while y < len(board) and x < len(board[0]) and y >= 0 and x >= 0:
        row += board[y][x]
        x += d_x
        y += d_y

    open_seq_count, semi_open_seq_count = 0, 0

    for i in range(len(row) - (length+1)):
        if row[i:i+length+2] == " " + col*length + " ":
            open_seq_count += 1
        if row[i:i+length+2] == nc + col*length + " ":
            semi_open_seq_count += 1
        if row[i:i+length+2] == " " + col*length + nc:
            semi_open_seq_count += 1

    if row[:length+1] == col*length + " ":
        semi_open_seq_count += 1
    if row[len(row)-length-1:] == " " + col*length:
        semi_open_seq_count += 1

    # print(row, open_seq_count, semi_open_seq_count)

    return open_seq_count, semi_open_seq_count


def detect_rows(board, col, length):
    open_seq_count, semi_open_seq_count = 0, 0

    for i in range(len(board)):
        op, se = detect_row(board, col, i, 0, length, 0, 1)
        open_seq_count += op
        semi_open_seq_count += se

        op, se = detect_row(board, col, 0, i, length, 1, 0)
        open_seq_count += op
        semi_open_seq_count += se

    for i in range(len(board[0])-length+1):
        op, se = detect_row(board, col, 0, i, length, 1, 1)
        open_seq_count += op
        semi_open_seq_count += se

        op, se = detect_row(board, col, 0, len(board[0])-1-i, length, 1, -1)
        open_seq_count += op
        semi_open_seq_count += se

        # print(f"\\ (0, {i})")
        # print(f"/ (0, {len(board[0])-1-i})")

        if i != 0:
            op, se = detect_row(board, col, i, 0, length, 1, 1)
            open_seq_count += op
            semi_open_seq_count += se

            op, se = detect_row(board, col, i, len(board[0])-1, length, 1, -1)
            open_seq_count += op
            semi_open_seq_count += se

            # print(f"\\ ({i}, 0)")
            # print(f"/ ({i}, {len(board[0])-1})")

    return open_seq_count, semi_open_seq_count


def search_max(board):
    move_y, move_x = None, None
    best = -99999999

    board_copy = []

    for row in board:
        board_copy.append(row[:])

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == " ":
                board_copy[i][j] = "b"

                if score(board_copy) > best:
                    move_y, move_x = i, j
                    best = score(board_copy)

                board_copy[i][j] = " "

    return move_y, move_x


def score(board):
    MAX_SCORE = 100000

    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}

    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)

    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE

    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE

    return (-10000 * (open_w[4] + semi_open_w[4]) +
            500 * open_b[4] +
            50 * semi_open_b[4] +
            -100 * open_w[3] +
            -30 * semi_open_w[3] +
            50 * open_b[3] +
            10 * semi_open_b[3] +
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])


def detect_win(board, col, y_start, x_start, length, d_y, d_x):
    if col == "b":
        nc = "w"
    else:
        nc = "b"

    x = x_start
    y = y_start

    row = ""

    while y < len(board) and x < len(board[0]) and y >= 0 and x >= 0:
        row += board[y][x]
        x += d_x
        y += d_y

    open_seq_count, semi_open_seq_count, closed_seq_count = 0, 0, 0

    for i in range(len(row) - (length+1)):
        if row[i:i+length+2] == " " + col*length + " ":
            open_seq_count += 1
        if row[i:i+length+2] == nc + col*length + " ":
            semi_open_seq_count += 1
        if row[i:i+length+2] == " " + col*length + nc:
            semi_open_seq_count += 1
        if row[i:i+length+2] == nc + col*length + nc:
            closed_seq_count += 1

    if row == col*length:
        closed_seq_count += 1

    left = row[:length+1]
    right = row[len(row)-length-1:]

    if left == col*length + nc:
        closed_seq_count += 1
    if right == nc + col*length:
        closed_seq_count += 1

    if left == col*length + " ":
        semi_open_seq_count += 1
    if right == " " + col*length:
        semi_open_seq_count += 1

    # print(row, open_seq_count, semi_open_seq_count)

    return open_seq_count, semi_open_seq_count, closed_seq_count


def detect_wins(board, col, length):
    open_seq_count, semi_open_seq_count, closed_seq_count = 0, 0, 0

    for i in range(len(board)):
        op, se, cl = detect_win(board, col, i, 0, length, 0, 1)
        open_seq_count += op
        semi_open_seq_count += se
        closed_seq_count += cl

        op, se, cl = detect_win(board, col, 0, i, length, 1, 0)
        open_seq_count += op
        semi_open_seq_count += se
        closed_seq_count += cl

    for i in range(len(board[0])-length+1):
        op, se, cl = detect_win(board, col, 0, i, length, 1, 1)
        open_seq_count += op
        semi_open_seq_count += se
        closed_seq_count += cl

        op, se, cl = detect_win(
            board, col, 0, len(board[0])-1-i, length, 1, -1)
        open_seq_count += op
        semi_open_seq_count += se
        closed_seq_count += cl

        # print(f"\\ (0, {i})")
        # print(f"/ (0, {len(board[0])-1-i})")

        if i != 0:
            op, se, cl = detect_win(board, col, i, 0, length, 1, 1)
            open_seq_count += op
            semi_open_seq_count += se
            closed_seq_count += cl

            op, se, cl = detect_win(
                board, col, i, len(board[0])-1, length, 1, -1)
            open_seq_count += op
            semi_open_seq_count += se
            closed_seq_count += cl

            # print(f"\\ ({i}, 0)")
            # print(f"/ ({i}, {len(board[0])-1})")

    return open_seq_count, semi_open_seq_count, closed_seq_count


def is_win(board):
    is_full = True
    break_now = False

    for row in board:
        if break_now:
            break
        for item in row:
            if break_now:
                break

            if item == " ":
                is_full = False
                break_now = True

    if is_full:
        return "Draw"

    # TODO check for wins
    op, se, cl = detect_wins(board, "b", 5)

    if op or se or cl:
        return "Black won"

    op, se, cl = detect_wins(board, "w", 5)

    if op or se or cl:
        return "White won"

    return "Continue playing"


def print_board(board):

    s = "*"
    for i in range(len(board[0])-1):
        s += str(i % 10) + "|"
    s += str((len(board[0])-1) % 10)
    s += "*\n"

    for i in range(len(board)):
        s += str(i % 10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1])

        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"

    print(s)


def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board


def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i)
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))


def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])

    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)

        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res

        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res


def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x


def test_is_empty():
    board = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")


def test_is_bounded():
    board = make_empty_board(8)
    x = 5
    y = 1
    d_x = 0
    d_y = 1
    length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5
    y = 1
    d_x = 0
    d_y = 1
    length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0, x, length, d_y, d_x) == (1, 0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")


def test_detect_rows():
    board = make_empty_board(8)
    x = 5
    y = 1
    d_x = 0
    d_y = 1
    length = 3
    col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col, length) == (1, 0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")


def test_search_max():
    board = make_empty_board(8)
    x = 5
    y = 0
    d_x = 0
    d_y = 1
    length = 4
    col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6
    y = 0
    d_x = 0
    d_y = 1
    length = 4
    col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4, 6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")


def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()


def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5
    x = 2
    d_x = 0
    d_y = 1
    length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)

    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0

    y = 3
    x = 5
    d_x = -1
    d_y = 1
    length = 2

    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)

    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #

    y = 5
    x = 3
    d_x = -1
    d_y = 1
    length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)

    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #
    #
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0


if __name__ == '__main__':
    play_gomoku(8)
    # some_tests()
    # easy_testset_for_main_functions()
