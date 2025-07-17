import coordinates as coord

class King():
    def __init__(self):
        self.castled = False
        self.check = False

    def get_moves(self, state, index):
        moves = []

        moves.append(index + coord.FILE)
        moves.append(index - coord.RANK)
        moves.append(index + coord.RANK)
        moves.append(index - coord.FILE)

        moves.append(index + coord.FILE + coord.RANK)
        moves.append(index + coord.FILE - coord.RANK)
        moves.append(index - coord.FILE + coord.RANK)
        moves.append(index - coord.FILE - coord.RANK)

        moves.append(index + 2 * coord.FILE)
        moves.append(index - 2 * coord.FILE)

        moves = self.check_rules(moves, state, index)

        return moves

    def check_rules(self, moves, state, index):
        delete = []

        castle_short, castle_long = self.check_castle(state, index)

        right = index + coord.FILE
        left = index - coord.FILE

        if not castle_short:
            moves.remove(index + 2 * coord.FILE)

        if not castle_long:
            moves.remove(index - 2 * coord.FILE)

        for i in range(coord.RANK):
            if index == coord.a1 + i * coord.RANK:
                delete.append(index - coord.FILE)
                delete.append(index - coord.FILE + coord.RANK)
                delete.append(index - coord.FILE - coord.RANK)
            elif index == coord.h1 + i * coord.RANK:
                delete.append(index + coord.FILE)
                delete.append(index + coord.FILE + coord.RANK)
                delete.append(index + coord.FILE - coord.RANK)

        for move in moves:
            if move < coord.a1 or move > coord.h8:
                delete.append(move)
                continue

            if state[1, move, 0] != 0:
                if state[1, move, 1] != state[1, index, 1]:
                    continue
                else:
                    delete.append(move)

        for dell in delete:
            try:
                moves.remove(dell)
            except ValueError:
                continue

        return moves

    def check_castle(self, state, index):
        castle_short = False
        castle_long = False

        if self.castled:
            return False, False

        sqr_r_1 = index + coord.FILE
        sqr_r_2 = index + 2 * coord.FILE

        sqr_l_1 = index - coord.FILE
        sqr_l_2 = index - 2 * coord.FILE
        sqr_l_3 = index - 3 * coord.FILE

        if not state[1,sqr_r_1,0] and not state[1,sqr_r_2,0]:
            castle_short = True
        if not state[1,sqr_l_1,0] and not state[1,sqr_l_2,0] and not state[1,sqr_l_3,0]:
            castle_long = True

        return castle_short, castle_long
