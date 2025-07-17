"""
 ____ ____ ____ ____ ____ ____ ____ ____
|_56_|_57_|_58_|_59_|_60_|_61_|_62_|_63_|
|_48_|_49_|_50_|_51_|_52_|_53_|_54_|_55_|
|_40_|_41_|_42_|_43_|_44_|_45_|_46_|_47_|
|_32_|_33_|_34_|_35_|_36_|_37_|_38_|_39_|
|_24_|_25_|_26_|_27_|_28_|_29_|_30_|_31_|
|_16_|_17_|_18_|_19_|_20__|_21_|_22_|_23_|
|_08_|_09_|_10_|_11_|_12_|_13_|_14_|_15_|
|_00_|_01_|_02_|_03_|_04_|_05_|_06_|_07_|

"""

RANK = 8
FILE = 1

a1 = 0 * FILE + 0 * RANK
b1 = 1 * FILE + 0 * RANK
c1 = 2 * FILE + 0 * RANK
d1 = 3 * FILE + 0 * RANK
e1 = 4 * FILE + 0 * RANK
f1 = 5 * FILE + 0 * RANK
g1 = 6 * FILE + 0 * RANK
h1 = 7 * FILE + 0 * RANK
a2 = 0 * FILE + 1 * RANK
b2 = 1 * FILE + 1 * RANK
c2 = 2 * FILE + 1 * RANK
d2 = 3 * FILE + 1 * RANK
e2 = 4 * FILE + 1 * RANK
f2 = 5 * FILE + 1 * RANK
g2 = 6 * FILE + 1 * RANK
h2 = 7 * FILE + 1 * RANK
a3 = 0 * FILE + 2 * RANK
b3 = 1 * FILE + 2 * RANK
c3 = 2 * FILE + 2 * RANK
d3 = 3 * FILE + 2 * RANK
e3 = 4 * FILE + 2 * RANK
f3 = 5 * FILE + 2 * RANK
g3 = 6 * FILE + 2 * RANK
h3 = 7 * FILE + 2 * RANK
a4 = 0 * FILE + 3 * RANK
b4 = 1 * FILE + 3 * RANK
c4 = 2 * FILE + 3 * RANK
d4 = 3 * FILE + 3 * RANK
e4 = 4 * FILE + 3 * RANK
f4 = 5 * FILE + 3 * RANK
g4 = 6 * FILE + 3 * RANK
h4 = 7 * FILE + 3 * RANK
a5 = 0 * FILE + 4 * RANK
b5 = 1 * FILE + 4 * RANK
c5 = 2 * FILE + 4 * RANK
d5 = 3 * FILE + 4 * RANK
e5 = 4 * FILE + 4 * RANK
f5 = 5 * FILE + 4 * RANK
g5 = 6 * FILE + 4 * RANK
h5 = 7 * FILE + 4 * RANK
a6 = 0 * FILE + 5 * RANK
b6 = 1 * FILE + 5 * RANK
c6 = 2 * FILE + 5 * RANK
d6 = 3 * FILE + 5 * RANK
e6 = 4 * FILE + 5 * RANK
f6 = 5 * FILE + 5 * RANK
g6 = 6 * FILE + 5 * RANK
h6 = 7 * FILE + 5 * RANK
a7 = 0 * FILE + 6 * RANK
b7 = 1 * FILE + 6 * RANK
c7 = 2 * FILE + 6 * RANK
d7 = 3 * FILE + 6 * RANK
e7 = 4 * FILE + 6 * RANK
f7 = 5 * FILE + 6 * RANK
g7 = 6 * FILE + 6 * RANK
h7 = 7 * FILE + 6 * RANK
a8 = 0 * FILE + 7 * RANK
b8 = 1 * FILE + 7 * RANK
c8 = 2 * FILE + 7 * RANK
d8 = 3 * FILE + 7 * RANK
e8 = 4 * FILE + 7 * RANK
f8 = 5 * FILE + 7 * RANK
g8 = 6 * FILE + 7 * RANK
h8 = 7 * FILE + 7 * RANK

def string_to_sqr(_input):
    if "+" in _input or "#" in _input:
        if "=" in _input:
            sqr = _input[-5] + _input[-4]
        elif "O-O-O" in _input:
            sqr = _input[0] + _input[1] + _input[2] + _input[3] + _input[4]
        elif "O-O" in _input:
            sqr = _input[0] + _input[1] + _input[2]
        else:
            sqr = _input[-3] + _input[-2]
    else:
        if "=" in _input:
            sqr = _input[-4] + _input[-3]
        elif "O-O-O" in _input:
            sqr = _input[0] + _input[1] + _input[2] + _input[3] + _input[4]
        elif "O-O" in _input:
            sqr = _input[0] + _input[1] + _input[2]
        else:
            sqr = _input[-2] + _input[-1]

    match sqr:
        case "a1":
            return a1
        case "a2":
            return a2
        case "a3":
            return a3
        case "a4":
            return a4
        case "a5":
            return a5
        case "a6":
            return a6
        case "a7":
            return a7
        case "a8":
            return a8
        case "b1":
            return b1
        case "b2":
            return b2
        case "b3":
            return b3
        case "b4":
            return b4
        case "b5":
            return b5
        case "b6":
            return b6
        case "b7":
            return b7
        case "b8":
            return b8
        case "c1":
            return c1
        case "c2":
            return c2
        case "c3":
            return c3
        case "c4":
            return c4
        case "c5":
            return c5
        case "c6":
            return c6
        case "c7":
            return c7
        case "c8":
            return c8
        case "d1":
            return d1
        case "d2":
            return d2
        case "d3":
            return d3
        case "d4":
            return d4
        case "d5":
            return d5
        case "d6":
            return d6
        case "d7":
            return d7
        case "d8":
            return d8
        case "e1":
            return e1
        case "e2":
            return e2
        case "e3":
            return e3
        case "e4":
            return e4
        case "e5":
            return e5
        case "e6":
            return e6
        case "e7":
            return e7
        case "e8":
            return e8
        case "f1":
            return f1
        case "f2":
            return f2
        case "f3":
            return f3
        case "f4":
            return f4
        case "f5":
            return f5
        case "f6":
            return f6
        case "f7":
            return f7
        case "f8":
            return f8
        case "g1":
            return g1
        case "g2":
            return g2
        case "g3":
            return g3
        case "g4":
            return g4
        case "g5":
            return g5
        case "g6":
            return g6
        case "g7":
            return g7
        case "g8":
            return g8
        case "h1":
            return h1
        case "h2":
            return h2
        case "h3":
            return h3
        case "h4":
            return h4
        case "h5":
            return h5
        case "h6":
            return h6
        case "h7":
            return h7
        case "h8":
            return h8
        case "O-O":
            return "castle short"
        case "O-O-O":
            return "castle long"
        case _:
            return "not a square"

def SAD_to_move(_input):
    piece_type = 0
    move = (0,0)

    if (_input[0] != "N" and _input[0] != "B" and _input[0] != "R" and _input[0] != "Q"
          and _input[0] != "K" and _input[0] != "O"):
        piece_type = 10
    elif "K" in _input or "O" in _input:
        piece_type = 15
    elif "N" in _input:
        piece_type = 12
    elif "B" in _input:
        piece_type = 13
    elif "R" in _input:
        piece_type = 11
    elif "Q" in _input:
        piece_type = 14

    move = string_to_sqr(_input)

    rest = ""

    if "=" in _input:
        if "+" in _input or "#" in _input:
            for i in range(len(_input)):
                if i == 0:
                    continue
                if i == len(_input) - 4:
                    continue
                if i == len(_input) - 5:
                    continue
                else:
                    rest += _input[i]
        else:
            for i in range(len(_input)):
                if i == 0:
                    continue
                if i == len(_input) - 3:
                    continue
                if i == len(_input) - 4:
                    continue
                else:
                    rest += _input[i]
    elif "x" in _input and _input[0].islower() and ("+" in _input or "#" in _input):
        for i in range(len(_input)):
            if i == len(_input) - 2:
                continue
            if i == len(_input) - 3:
                continue
            else:
                rest += _input[i]
    elif "x" in _input and _input[0].islower():
        for i in range(len(_input)):
            if i == len(_input) - 1:
                continue
            if i == len(_input) - 2:
                continue
            else:
                rest += _input[i]
    elif "+" in _input or "#" in _input:
        for i in range(len(_input)):
            if i == 0:
                continue
            if i == len(_input) - 2:
                continue
            if i == len(_input) - 3:
                continue
            else:
                rest += _input[i]
    else:
        for i in range(len(_input)):
            if i == 0:
                continue
            if i == len(_input)-1:
                continue
            if i == len(_input)-2:
                continue
            else:
                rest += _input[i]

    return piece_type, move, rest

def get_file_index(_input):
    file_indexes = []

    for i in range(RANK):
        if "a" in _input:
            file_indexes.append(0 + i * RANK)
        elif "b" in _input:
            file_indexes.append(1 + i * RANK)
        elif "c" in _input:
            file_indexes.append(2 + i * RANK)
        elif "d" in _input:
            file_indexes.append(3 + i * RANK)
        elif "e" in _input:
            file_indexes.append(4 + i * RANK)
        elif "f" in _input:
            file_indexes.append(5 + i * RANK)
        elif "g" in _input:
            file_indexes.append(6 + i * RANK)
        elif "h" in _input:
            file_indexes.append(7 + i * RANK)

    return file_indexes

def get_rank_index(_input):
    rank_indexes = []

    for i in range(RANK):
        if "1" in _input:
            rank_indexes.append(i + 0 * RANK)
        elif "2" in _input:
            rank_indexes.append(i + 1 * RANK)
        elif "3" in _input:
            rank_indexes.append(i + 2 * RANK)
        elif "4" in _input:
            rank_indexes.append(i + 3 * RANK)
        elif "5" in _input:
            rank_indexes.append(i + 4 * RANK)
        elif "6" in _input:
            rank_indexes.append(i + 5 * RANK)
        elif "7" in _input:
            rank_indexes.append(i + 6 * RANK)
        elif "8" in _input:
            rank_indexes.append(i + 7 * RANK)

    return rank_indexes

def print_state(state):
    for i in range(8,0,-1):
        contents = []
        print(" ___ ___ ___ ___ ___ ___ ___ ___")
        for j in range(1,9,1):
            if state[8*i-j,1] == 10 or state[8*i-j,1] == 0:
                match state[8*i-j,0]:
                    case 0:
                        contents.append(" ")
                    case 10:
                        contents.append("p")
                    case 11:
                        contents.append("r")
                    case 12:
                        contents.append("n")
                    case 13:
                        contents.append("b")
                    case 14:
                        contents.append("q")
                    case 15:
                        contents.append("k")
            elif state[8*i-j,1] == 11 or state[8*i-j,1] == 0:
                match state[8*i-j,0]:
                    case 0:
                        contents.append(" ")
                    case 10:
                        contents.append("P")
                    case 11:
                        contents.append("R")
                    case 12:
                        contents.append("N")
                    case 13:
                        contents.append("B")
                    case 14:
                        contents.append("Q")
                    case 15:
                        contents.append("K")
        print("| " + contents[7] + " | " + contents[6] + " | " + contents[5] + " | " + contents[4] + " | " + contents[3] + " | "
              + contents[2] + " | " + contents[1] + " | " + contents[0] + " |")
    print(" ___ ___ ___ ___ ___ ___ ___ ___")
