import santa


def o_will_lose(board):
    '''Return True iff O starts and loses with perfect play'''
    if santa.x_won(invert_board(board)):
        return False
    if santa.x_won(board):
        return True

    if is_full(board):
        return False

    # for every placement of O on the board,
    # w_will_win(board with the placement) is True
    # => o_will_lose is False

    # if there is a placement such that x_will_win(board with placement)
    # is False, then we need to return False

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                if not x_will_win(board):
                    return False

    return True


def x_will_win(board):
    '''Return True iff X starts andd wins with perfect play'''
    # if there is a placement of X such that o_will_lose(board with placement) is True, return True
    # if for no placement of X o_will_lose(board with placement) is True return False

    if santa.x_won(invert_board(board)):
        return True
    if santa.x_won(board):
        return False

    if is_full(board):
        return False

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                if o_will_lose(board):
                    return True

    return True
