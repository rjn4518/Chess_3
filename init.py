import numpy as np
import king
import rook
import coordinates as coord


def init():
    turn = 1

    """
    state[x][0] = previous state
    state[x][1] = current state

    a1 = state[0][x] ... h1 = state[7][x]
    a2 = state[8][x] ... h2 = state[15][x]
    a3 = state[16][x] ... h3 = state[23][x]
    a4 = state[24][x] ... h4 = state[31][x]
    a5 = state[32][x] ... h5 = state[39][x]
    a6 = state[40][x] ... h6 = state[47][x]
    a7 = state[48][x] ... h7 = state[55][x]
    a8 = state[56][x] ... h8 = state[63][x]

    state[x][y] = [piece, color]

    piece code:
        pawn = 10
        rook = 11
        knight = 12
        bishop = 13
        queen = 14
        king = 15
    color code:
        white = 10
        black = 11

    """
    state = np.zeros((2, 64, 2))
    # print(state)

    for i in range(64):
        if i == 0 or i == 7:
            state[1, i, :] = [11, 10]
        elif i == 1 or i == 6:
            state[1, i, :] = [12, 10]
        elif i == 2 or i == 5:
            state[1, i, :] = [13, 10]
        elif i == 3:
            state[1, i, :] = [14, 10]
        elif i == 4:
            state[1, i, :] = [15, 10]
        elif 8 <= i <= 15:
            state[1, i, :] = [10, 10]
        elif 48 <= i <= 55:
            state[1, i, :] = [10, 11]
        elif i == 56 or i == 63:
            state[1, i, :] = [11, 11]
        elif i == 57 or i == 62:
            state[1, i, :] = [12, 11]
        elif i == 58 or i == 61:
            state[1, i, :] = [13, 11]
        elif i == 59:
            state[1, i, :] = [14, 11]
        elif i == 60:
            state[1, i, :] = [15, 11]

    # coord.print_state(state[1, :, :])

    w_rooks = [rook.Rook(), rook.Rook()]
    b_rooks = [rook.Rook(), rook.Rook()]

    w_king = king.King()
    b_king = king.King()

    return [turn, state, w_rooks, b_rooks, w_king, b_king]
