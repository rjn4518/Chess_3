import coordinates as coord

def get_moves(state, index):
    moves = []

    if state[1,index,1] == 11:
        if coord.a7 <= index <= coord.h7:
            moves.append(index - coord.RANK)
            moves.append(index - 2 * coord.RANK)
            moves.append(index - coord.RANK + coord.FILE)
            moves.append(index - coord.RANK - coord.FILE)
        else:
            moves.append(index - coord.RANK)
            moves.append(index - coord.RANK + coord.FILE)
            moves.append(index - coord.RANK - coord.FILE)
    else:
        if coord.a2 <= index <= coord.h2:
            moves.append(index + coord.RANK)
            moves.append(index + 2 * coord.RANK)
            moves.append(index + coord.RANK + coord.FILE)
            moves.append(index + coord.RANK - coord.FILE)
        else:
            moves.append(index + coord.RANK)
            moves.append(index + coord.RANK + coord.FILE)
            moves.append(index + coord.RANK - coord.FILE)

    moves, e_p = check_rules(moves, state, index)

    return moves, e_p

def check_rules(moves, state, index):
    delete = []

    e_p = check_en_passant(state, index)

    for i in range(coord.RANK):
        if index == coord.a1 + i * coord.RANK:
            delete.append(index + coord.RANK - coord.FILE)
            delete.append(index - coord.RANK - coord.FILE)
        elif index == coord.h1 + i * coord.RANK:
            delete.append(index + coord.RANK + coord.FILE)
            delete.append(index - coord.RANK + coord.FILE)

    for move in moves:
        if state[1, move, 0] != 0:
            if (move == index + coord.RANK or move == index - coord.RANK
                    or move == index - 2 * coord.RANK or move == index + 2 * coord.RANK):
                delete.append(move)
            elif state[1, move, 1] == state[1, index, 1]:
                delete.append(move)
        elif (state[1, move, 0] == 0 and
              (move == index + coord.RANK + coord.FILE or move == index + coord.RANK - coord.FILE
               or move == index - coord.RANK + coord.FILE or move == index - coord.RANK - coord.FILE)):
            if e_p:
                continue
            delete.append(move)

    for dell in delete:
        try:
            moves.remove(dell)
        except ValueError:
            continue

    return moves, e_p

def check_en_passant(state, index):
    e_p = False

    if not coord.a4 <= index <= coord.h5:
        return e_p

    adj_index_r = index + coord.FILE
    adj_index_l = index - coord.FILE

    if adj_index_r != "not a square":
        # if there is an adjacent pawn of the opposite color to the right
        if state[1, adj_index_r, 0] == 10 and state[1, adj_index_r, 1] != state[1, index, 1]:
            # find squares 2 squares away from adjacent pawn
            adj_r_up = adj_index_r + 2 * coord.RANK
            adj_r_down = adj_index_r - 2 * coord.RANK

            if adj_r_up != "not a square":
                if state[0, adj_r_up, 0] == 10 and state[0, adj_r_up, 1] != state[1, index, 1]:
                    e_p = True
                elif state[0, adj_r_down, 0] == 10 and state[0, adj_r_down, 1] != state[1, index, 1]:
                    e_p = True

    if adj_index_l != "not a square":
        if state[1, adj_index_l, 0] == 10 and state[1, adj_index_l, 1] != state[1, index, 1]:
            adj_l_up = adj_index_l + 2 * coord.RANK
            adj_l_down = adj_index_l - 2 * coord.RANK

            if adj_l_up != "not a square":
                if state[0, adj_l_up, 0] == 10 and state[0, adj_l_up, 1] != state[1, index, 1]:
                    e_p = True
                elif state[0, adj_l_down, 0] == 10 and state[0, adj_l_down, 1] != state[1, index, 1]:
                    e_p = True

    return e_p
