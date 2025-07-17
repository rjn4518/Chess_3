import coordinates as coord

def get_moves(state, index):
    moves = []
    moves_up = []
    moves_down = []
    moves_right = []
    moves_left = []

    moves_up_right = []
    moves_up_left = []
    moves_down_right = []
    moves_down_left = []

    for i in range(1,9):
        moves_right.append(index + i * coord.FILE)
        moves_up.append(index + i * coord.RANK)
        moves_down.append(index - i * coord.RANK)
        moves_left.append(index - i * coord.FILE)
        moves_down_right.append(index + i * coord.FILE - i * coord.RANK)
        moves_up_right.append(index + i * coord.FILE + i * coord.RANK)
        moves_down_left.append(index - i * coord.FILE - i * coord.RANK)
        moves_up_left.append(index - i * coord.FILE + i * coord.RANK)

    moves.append(moves_right)
    moves.append(moves_left)
    moves.append(moves_up)
    moves.append(moves_down)

    moves.append(moves_up_right)
    moves.append(moves_up_left)
    moves.append(moves_down_right)
    moves.append(moves_down_left)

    moves = check_rules(moves, state, index)

    return moves

def check_rules(moves, state, index):
    delete = []
    in_the_way = False

    moves_right = moves[0]
    moves_left = moves[1]
    moves_up = moves[2]
    moves_down = moves[3]

    moves_up_right = moves[4]
    moves_up_left = moves[5]
    moves_down_right = moves[6]
    moves_down_left = moves[7]

    for move in moves_right:
        for i in range(coord.RANK):
            if index == 7 * coord.FILE + i * coord.RANK:
                in_the_way = True
                break

        if move < coord.a1 or move > coord.h8:
            delete.append(move)
            continue

        if in_the_way:
            delete.append(move)
            continue

        if state[1,move,0] != 0:
            if state[1,move,1] != state[1,index,1]:
                    in_the_way = True
            else:
                    delete.append(move)
                    in_the_way = True

        for i in range(coord.RANK):
            if move == 7 * coord.FILE + i * coord.RANK:
                in_the_way = True
                break


    for dell in delete:
        try:
            moves_right.remove(dell)
        except ValueError:
            continue

    delete = []
    in_the_way = False

    for move in moves_left:
        for i in range(coord.RANK):
            if index == i * coord.RANK:
                in_the_way = True
                break

        if move < coord.a1 or move > coord.h8:
            delete.append(move)
            continue

        if in_the_way:
            delete.append(move)
            continue

        if state[1, move, 0] != 0:
            if state[1, move, 1] != state[1, index, 1]:
                in_the_way = True
            else:
                delete.append(move)
                in_the_way = True

        for i in range(coord.RANK):
            if move == i * coord.RANK:
                in_the_way = True
                break

    for dell in delete:
        try:
            moves_left.remove(dell)
        except ValueError:
            continue

    delete = []
    in_the_way = False

    for move in moves_up:
        if move < coord.a1 or move > coord.h8:
            delete.append(move)
            continue

        if in_the_way:
            delete.append(move)
            continue

        if state[1, move, 0] != 0:
            if state[1, move, 1] != state[1, index, 1]:
                in_the_way = True
            else:
                delete.append(move)
                in_the_way = True

    for dell in delete:
        try:
            moves_up.remove(dell)
        except ValueError:
            continue

    delete = []
    in_the_way = False

    for move in moves_down:
        if move < coord.a1 or move > coord.h8:
            delete.append(move)
            continue

        if in_the_way:
            delete.append(move)
            continue

        if state[1, move, 0] != 0:
            if state[1, move, 1] != state[1, index, 1]:
                in_the_way = True
            else:
                delete.append(move)
                in_the_way = True

    for dell in delete:
        try:
            moves_down.remove(dell)
        except ValueError:
            continue

    delete = []
    in_the_way = False

    for move in moves_up_right:
        for i in range(coord.RANK):
            if index == 7 * coord.FILE + i * coord.RANK:
                in_the_way = True
                break

        if move < coord.a1 or move > coord.h8:
            delete.append(move)
            continue

        if in_the_way:
            delete.append(move)
            continue

        if state[1,move,0] != 0:
            if state[1,move,1] != state[1,index,1]:
                    in_the_way = True
            else:
                    delete.append(move)
                    in_the_way = True

        for i in range(coord.RANK):
            if move == 7 * coord.FILE + i * coord.RANK:
                in_the_way = True
                break


    for dell in delete:
        try:
            moves_up_right.remove(dell)
        except ValueError:
            continue

    delete = []
    in_the_way = False

    for move in moves_up_left:
        for i in range(coord.RANK):
            if index == i * coord.RANK:
                in_the_way = True
                break

        if move < coord.a1 or move > coord.h8:
            delete.append(move)
            continue

        if in_the_way:
            delete.append(move)
            continue

        if state[1, move, 0] != 0:
            if state[1, move, 1] != state[1, index, 1]:
                in_the_way = True
            else:
                delete.append(move)
                in_the_way = True

        for i in range(coord.RANK):
            if move == i * coord.RANK:
                in_the_way = True
                break

    for dell in delete:
        try:
            moves_up_left.remove(dell)
        except ValueError:
            continue

    delete = []
    in_the_way = False

    for move in moves_down_right:
        for i in range(coord.RANK):
            if index == 7 * coord.FILE + i * coord.RANK:
                in_the_way = True
                break

        if move < coord.a1 or move > coord.h8:
            delete.append(move)
            continue

        if in_the_way:
            delete.append(move)
            continue

        if state[1, move, 0] != 0:
            if state[1, move, 1] != state[1, index, 1]:
                in_the_way = True
            else:
                delete.append(move)
                in_the_way = True

        for i in range(coord.RANK):
            if move == 7 * coord.FILE + i * coord.RANK:
                in_the_way = True
                break

    for dell in delete:
        try:
            moves_down_right.remove(dell)
        except ValueError:
            continue

    delete = []
    in_the_way = False

    for move in moves_down_left:
        for i in range(coord.RANK):
            if index == i * coord.RANK:
                in_the_way = True
                break

        if move < coord.a1 or move > coord.h8:
            delete.append(move)
            continue

        if in_the_way:
            delete.append(move)
            continue

        if state[1, move, 0] != 0:
            if state[1, move, 1] != state[1, index, 1]:
                in_the_way = True
            else:
                delete.append(move)
                in_the_way = True

        for i in range(coord.RANK):
            if move == i * coord.RANK:
                in_the_way = True
                break

    for dell in delete:
        try:
            moves_down_left.remove(dell)
        except ValueError:
            continue

    moves = []

    for move in moves_right:
        moves.append(move)
    for move in moves_left:
        moves.append(move)
    for move in moves_up:
        moves.append(move)
    for move in moves_down:
        moves.append(move)

    for move in moves_up_right:
        moves.append(move)
    for move in moves_up_left:
        moves.append(move)
    for move in moves_down_right:
        moves.append(move)
    for move in moves_down_left:
        moves.append(move)

    return moves
