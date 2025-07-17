import coordinates as coord

def get_moves(state, index):
    moves = []

    moves.append(index + coord.FILE + 2 * coord.RANK)
    moves.append(index + coord.FILE - 2 * coord.RANK)
    moves.append(index - coord.FILE + 2 * coord.RANK)
    moves.append(index - coord.FILE - 2 * coord.RANK)
    moves.append(index + 2 * coord.FILE + coord.RANK)
    moves.append(index + 2 * coord.FILE - coord.RANK)
    moves.append(index - 2 * coord.FILE + coord.RANK)
    moves.append(index - 2 * coord.FILE - coord.RANK)

    moves = check_rules(moves, state, index)

    return moves

def check_rules(moves, state, index):
    delete = []

    for i in range(coord.RANK):
        if index == coord.g1 + i * coord.RANK:
            delete.append(index + 2 * coord.FILE + coord.RANK)
            delete.append(index + 2 * coord.FILE - coord.RANK)
        elif index == coord.h1 + i * coord.RANK:
            delete.append(index + coord.FILE + coord.RANK)
            delete.append(index + coord.FILE - coord.RANK)

    for move in moves:
        if move < coord.a1 or move > coord.h8:
            delete.append(move)
        elif state[1,move,1] == state[1,index,1]:
            delete.append(move)

    for dell in delete:
        try:
            moves.remove(dell)
        except ValueError:
            continue

    return moves
