import numpy as np
import read_pgn
import coordinates as coord

file = 'Carlsen.pgn'

white_moves, black_moves = read_pgn.read_pgn(file)

w_data = np.zeros((32, len(white_moves)), 'float32')
b_data = np.zeros((32, len(black_moves)), 'float32')

wm = []
bm = []

for move in white_moves:
    wm.append(coord.SAD_to_move(move))

for move in black_moves:
    bm.append(coord.SAD_to_move(move))

j = 0
for m in wm:
    for i in range(8):
        if m[0] == i * coord.RANK:
            b_data[0, j] = 1
        elif m[0] == coord.FILE + i * coord.RANK:
            b_data[1, j] = 1
        elif m[0] == 2 * coord.FILE + i * coord.RANK:
            b_data[2, j] = 1
        elif m[0] == 3 * coord.FILE + i * coord.RANK:
            b_data[3, j] = 1
        elif m[0] == 4 * coord.FILE + i * coord.RANK:
            b_data[4, j] = 1
        elif m[0] == 5 * coord.FILE + i * coord.RANK:
            b_data[5, j] = 1
        elif m[0] == 6 * coord.FILE + i * coord.RANK:
            b_data[6, j] = 1
        elif m[0] == 7 * coord.FILE + i * coord.RANK:
            b_data[7, j] = 1

        if m[1] == i * coord.RANK:
            b_data[16, j] = 1
        elif m[1] == coord.FILE + i * coord.RANK:
            b_data[7, j] = 1
        elif m[1] == 2 * coord.FILE + i * coord.RANK:
            b_data[18, j] = 1
        elif m[1] == 3 * coord.FILE + i * coord.RANK:
            b_data[19, j] = 1
        elif m[1] == 4 * coord.FILE + i * coord.RANK:
            b_data[20, j] = 1
        elif m[1] == 5 * coord.FILE + i * coord.RANK:
            b_data[21, j] = 1
        elif m[1] == 6 * coord.FILE + i * coord.RANK:
            b_data[22, j] = 1
        elif m[1] == 7 * coord.FILE + i * coord.RANK:
            b_data[23, j] = 1

    if coord.a1 <= m[0] <= coord.h1:
        b_data[8, j] = 1
    elif coord.a2 <= m[0] <= coord.h2:
        b_data[9, j] = 1
    elif coord.a3 <= m[0] <= coord.h3:
        b_data[10, j] = 1
    elif coord.a4 <= m[0] <= coord.h4:
        b_data[11, j] = 1
    elif coord.a5 <= m[0] <= coord.h5:
        b_data[12, j] = 1
    elif coord.a6 <= m[0] <= coord.h6:
        b_data[13, j] = 1
    elif coord.a7 <= m[0] <= coord.h7:
        b_data[14, j] = 1
    elif coord.a8 <= m[0] <= coord.h8:
        b_data[15, j] = 1

    if coord.a1 <= m[1] <= coord.h1:
        b_data[24, j] = 1
    elif coord.a2 <= m[1] <= coord.h2:
        b_data[25, j] = 1
    elif coord.a3 <= m[1] <= coord.h3:
        b_data[26, j] = 1
    elif coord.a4 <= m[1] <= coord.h4:
        b_data[27, j] = 1
    elif coord.a5 <= m[1] <= coord.h5:
        b_data[28, j] = 1
    elif coord.a6 <= m[1] <= coord.h6:
        b_data[29, j] = 1
    elif coord.a7 <= m[1] <= coord.h7:
        b_data[30, j] = 1
    elif coord.a8 <= m[1] <= coord.h8:
        b_data[31, j] = 1

for m in bm:
    for i in range(8):
        if m[0] == i * coord.RANK:
            w_data[0, j] = 1
        elif m[0] == coord.FILE + i * coord.RANK:
            w_data[1, j] = 1
        elif m[0] == 2 * coord.FILE + i * coord.RANK:
            w_data[2, j] = 1
        elif m[0] == 3 * coord.FILE + i * coord.RANK:
            w_data[3, j] = 1
        elif m[0] == 4 * coord.FILE + i * coord.RANK:
            w_data[4, j] = 1
        elif m[0] == 5 * coord.FILE + i * coord.RANK:
            w_data[5, j] = 1
        elif m[0] == 6 * coord.FILE + i * coord.RANK:
            w_data[6, j] = 1
        elif m[0] == 7 * coord.FILE + i * coord.RANK:
            w_data[7, j] = 1

        if m[1] == i * coord.RANK:
            w_data[16, j] = 1
        elif m[1] == coord.FILE + i * coord.RANK:
            w_data[7, j] = 1
        elif m[1] == 2 * coord.FILE + i * coord.RANK:
            w_data[18, j] = 1
        elif m[1] == 3 * coord.FILE + i * coord.RANK:
            w_data[19, j] = 1
        elif m[1] == 4 * coord.FILE + i * coord.RANK:
            w_data[20, j] = 1
        elif m[1] == 5 * coord.FILE + i * coord.RANK:
            w_data[21, j] = 1
        elif m[1] == 6 * coord.FILE + i * coord.RANK:
            w_data[22, j] = 1
        elif m[1] == 7 * coord.FILE + i * coord.RANK:
            w_data[23, j] = 1

    if coord.a1 <= m[0] <= coord.h1:
        w_data[8, j] = 1
    elif coord.a2 <= m[0] <= coord.h2:
        w_data[9, j] = 1
    elif coord.a3 <= m[0] <= coord.h3:
        w_data[10, j] = 1
    elif coord.a4 <= m[0] <= coord.h4:
        w_data[11, j] = 1
    elif coord.a5 <= m[0] <= coord.h5:
        w_data[12, j] = 1
    elif coord.a6 <= m[0] <= coord.h6:
        w_data[13, j] = 1
    elif coord.a7 <= m[0] <= coord.h7:
        w_data[14, j] = 1
    elif coord.a8 <= m[0] <= coord.h8:
        w_data[15, j] = 1

    if coord.a1 <= m[1] <= coord.h1:
        w_data[24, j] = 1
    elif coord.a2 <= m[1] <= coord.h2:
        w_data[25, j] = 1
    elif coord.a3 <= m[1] <= coord.h3:
        w_data[26, j] = 1
    elif coord.a4 <= m[1] <= coord.h4:
        w_data[27, j] = 1
    elif coord.a5 <= m[1] <= coord.h5:
        w_data[28, j] = 1
    elif coord.a6 <= m[1] <= coord.h6:
        w_data[29, j] = 1
    elif coord.a7 <= m[1] <= coord.h7:
        w_data[30, j] = 1
    elif coord.a8 <= m[1] <= coord.h8:
        w_data[31, j] = 1
