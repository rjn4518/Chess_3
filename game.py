import sys
from unittest import case
import init
import pawn
import knight
import bishop
import rook
import queen
import test as t
import nn_blind_sup
import coordinates as coord

CHECKMATE = False
STALEMATE = False
COUNT = 0
MAX_COUNT = 100

def update_state(state, before, after, e_p, e_p_sqr):

    index_before = before[1]
    state[index_before,:] = [0,0]
    index_after = after[1]
    state[index_after,:] = [after[0], after[2]]

    if e_p:
        state[e_p_sqr,:] = [0,0]

    #print(state)

    return state

def promote(command):
    if "=N" in command:
        return 12
    elif "=B" in command:
        return 13
    elif "=R" in command:
        return 11
    elif "=Q" in command:
        return 14

def check_check(state, w_king, b_king, index, moves, color, check_mate):
    check = False
    delete = []
    hypothetical_state = state.copy()

    hypothetical_state[0,:,:] = hypothetical_state[1,:,:]

    piece_type = hypothetical_state[1,index,0]
    #print(color)

    not_color = 0
    if color == 10:
        not_color = 11
    elif color == 11:
        not_color = 10

    king_sqr = 100

    for i in range(64):
        if state[1,i,0] == 15 and state[1,i,1] == color:
            king_sqr = i
            break

    hypothetical_moves = []
    for j in range(64):
        if hypothetical_state[1, j, 1] == not_color:
            if hypothetical_state[1, j, 0] == 10:
                temp1, temp2 = pawn.get_moves(hypothetical_state, j)
                for t in temp1:
                    hypothetical_moves.append(t)
            elif hypothetical_state[1, j, 0] == 11:
                temp1 = rook.get_moves(hypothetical_state, j)
                for t in temp1:
                    hypothetical_moves.append(t)
            elif hypothetical_state[1, j, 0] == 12:
                temp1 = knight.get_moves(hypothetical_state, j)
                for t in temp1:
                    hypothetical_moves.append(t)
            elif hypothetical_state[1, j, 0] == 13:
                temp1 = bishop.get_moves(hypothetical_state, j)
                for t in temp1:
                    hypothetical_moves.append(t)
            elif hypothetical_state[1, j, 0] == 14:
                temp1 = queen.get_moves(hypothetical_state, j)
                for t in temp1:
                    hypothetical_moves.append(t)

    for hm in hypothetical_moves:
        if hm == king_sqr:
            check = True
            break

    before = (piece_type, index)

    match hypothetical_state[1,index,1]:
        case 10:
            match check_mate:
                case True:
                    king_moves = []

                    temp0 = b_king.get_moves(hypothetical_state, king_sqr)

                    for t in temp0:
                        king_moves.append(t)

                    #print("km",  king_moves)

                    for km in king_moves:
                        #print("km", km)
                        before = (hypothetical_state[1, king_sqr, 0], king_sqr)
                        after = (hypothetical_state[1, king_sqr, 0], km, hypothetical_state[1, king_sqr, 1])
                        hypothetical_state[1, :, :] = update_state(hypothetical_state[1, :, :], before, after,
                                                                   False, (0, 0))
                        hypothetical_moves = []
                        for j in range(64):
                            if hypothetical_state[1, j, 1] == 10:
                                if hypothetical_state[1, j, 0] == 10:
                                    temp1, temp2 = pawn.get_moves(hypothetical_state, j)
                                    for t in temp1:
                                        hypothetical_moves.append(t)
                                elif hypothetical_state[1, j, 0] == 11:
                                    temp1 = rook.get_moves(hypothetical_state, j)
                                    for t in temp1:
                                        hypothetical_moves.append(t)
                                elif hypothetical_state[1, j, 0] == 12:
                                    temp1 = knight.get_moves(hypothetical_state, j)
                                    for t in temp1:
                                        hypothetical_moves.append(t)
                                elif hypothetical_state[1, j, 0] == 13:
                                    temp1 = bishop.get_moves(hypothetical_state, j)
                                    for t in temp1:
                                        hypothetical_moves.append(t)
                                elif hypothetical_state[1, j, 0] == 14:
                                    temp1 = queen.get_moves(hypothetical_state, j)
                                    for t in temp1:
                                        hypothetical_moves.append(t)
                                elif hypothetical_state[1, j, 0] == 15:
                                    temp1 = w_king.get_moves(hypothetical_state, j)
                                    #print("temp", temp1)
                                    for t in temp1:
                                        hypothetical_moves.append(t)

                        hypothetical_state[1, :, :] = hypothetical_state[0, :, :]

                        #print("hm",  hypothetical_moves)

                        for h_m in hypothetical_moves:
                            if h_m == km:
                                delete.append(km)

                        #print(km)
                    #print(delete)

                    for dell in delete:
                        try:
                            king_moves.remove(dell)
                        except ValueError:
                            continue

                    for r in king_moves:
                        moves.append(r)

                    #print("moves",  moves)

                    if len(moves):
                        return len(moves), check

                    delete = []
                    for i in range(64):
                        temp = []
                        if hypothetical_state[1, i, 1] == 11:
                            if hypothetical_state[1, i, 0] == 10:
                                temp1, temp2 = pawn.get_moves(hypothetical_state, i)
                                #print(temp1)
                                for t in temp1:
                                    temp.append(t)
                            elif hypothetical_state[1, i, 0] == 11:
                                temp1 = rook.get_moves(hypothetical_state, i)
                                for t in temp1:
                                    temp.append(t)
                            elif hypothetical_state[1, i, 0] == 12:
                                temp1 = knight.get_moves(hypothetical_state, i)
                                for t in temp1:
                                    temp.append(t)
                            elif hypothetical_state[1, i, 0] == 13:
                                temp1 = bishop.get_moves(hypothetical_state, i)
                                for t in temp1:
                                    temp.append(t)
                            elif hypothetical_state[1, i, 0] == 14:
                                temp1 = queen.get_moves(hypothetical_state, i)
                                for t in temp1:
                                    temp.append(t)

                            #print("temp", temp)

                            for m in temp:
                                before = (hypothetical_state[1, i, 0], i)
                                after = (hypothetical_state[1, i, 0], m, hypothetical_state[1, i, 1])
                                hypothetical_state[1, :, :] = update_state(hypothetical_state[1, :, :], before, after,
                                                                           False, (0, 0))
                                hypothetical_moves = []
                                for j in range(64):
                                    if hypothetical_state[1, j, 1] == 10:
                                        if hypothetical_state[1, j, 0] == 10:
                                            temp1, temp2 = pawn.get_moves(hypothetical_state, j)
                                            for t in temp1:
                                                hypothetical_moves.append(t)
                                        elif hypothetical_state[1, j, 0] == 11:
                                            temp1 = rook.get_moves(hypothetical_state, j)
                                            for t in temp1:
                                                hypothetical_moves.append(t)
                                        elif hypothetical_state[1, j, 0] == 12:
                                            temp1 = knight.get_moves(hypothetical_state, j)
                                            for t in temp1:
                                                hypothetical_moves.append(t)
                                        elif hypothetical_state[1, j, 0] == 13:
                                            temp1 = bishop.get_moves(hypothetical_state, j)
                                            for t in temp1:
                                                hypothetical_moves.append(t)
                                        elif hypothetical_state[1, j, 0] == 14:
                                            temp1 = queen.get_moves(hypothetical_state, j)
                                            for t in temp1:
                                                hypothetical_moves.append(t)
                                        elif hypothetical_state[1, j, 0] == 15:
                                            temp1 = w_king.get_moves(hypothetical_state, j)
                                            for t in temp1:
                                                hypothetical_moves.append(t)

                                hypothetical_state[1, :, :] = hypothetical_state[0, :, :]

                                #print(king_sqr)

                                #print("hm", hypothetical_moves)
                                #print(temp)
                                for h_m in hypothetical_moves:
                                    if h_m == king_sqr:
                                        delete.append(m)

                            #print("delete", delete)
                            for dell in delete:
                                try:
                                    temp.remove(dell)
                                except ValueError:
                                    continue

                            for t in temp:
                                moves.append(t)

                            #print("moves", moves)

                            if len(moves):
                                return len(moves), check

                    # print(len(moves), check)

                    return len(moves), check

                case False:
                    #print("moves", moves)
                    for m in moves:
                        after = (piece_type, m, color)
                        hypothetical_state[1, :, :] = update_state(hypothetical_state[1, :, :], before, after,
                                                                   False, (0, 0))
                        hypothetical_moves = []
                        for i in range(64):
                            if hypothetical_state[1, i, 1] == 11:
                                if hypothetical_state[1, i, 0] == 10:
                                    temp1, temp2 = pawn.get_moves(hypothetical_state, i)
                                    #print("temp1", temp1)
                                    for t in temp1:
                                        hypothetical_moves.append(t)
                                elif hypothetical_state[1, i, 0] == 11:
                                    temp1 = rook.get_moves(hypothetical_state, i)
                                    #print("temp1", temp1)
                                    for t in temp1:
                                        hypothetical_moves.append(t)
                                elif hypothetical_state[1, i, 0] == 12:
                                    temp1 = knight.get_moves(hypothetical_state, i)
                                    for t in temp1:
                                        hypothetical_moves.append(t)
                                elif hypothetical_state[1, i, 0] == 13:
                                    temp1 = bishop.get_moves(hypothetical_state, i)
                                    for t in temp1:
                                        hypothetical_moves.append(t)
                                elif hypothetical_state[1, i, 0] == 14:
                                    temp1 = queen.get_moves(hypothetical_state, i)
                                    for t in temp1:
                                        hypothetical_moves.append(t)
                                elif hypothetical_state[1, i, 0] == 15:
                                    temp1 = b_king.get_moves(hypothetical_state, i)
                                    for t in temp1:
                                        hypothetical_moves.append(t)

                        hypothetical_state[1, :, :] = hypothetical_state[0, :, :]

                        #print(hypothetical_moves)
                        #print(moves)
                        for h_m in hypothetical_moves:
                            if piece_type == 15:
                                if h_m == m:
                                    delete.append(m)
                            else:
                                if h_m == king_sqr:
                                    delete.append(m)
        case 11:
            match check_mate:
                case True:
                    king_moves = []

                    temp0 = w_king.get_moves(hypothetical_state, king_sqr)

                    for t in temp0:
                        king_moves.append(t)

                    # print("km",  king_moves)

                    for km in king_moves:
                        # print("km", km)
                        before = (hypothetical_state[1, king_sqr, 0], king_sqr)
                        after = (hypothetical_state[1, king_sqr, 0], km, hypothetical_state[1, king_sqr, 1])
                        hypothetical_state[1, :, :] = update_state(hypothetical_state[1, :, :], before, after,
                                                                   False, (0, 0))
                        hypothetical_moves = []
                        for j in range(64):
                            if hypothetical_state[1, j, 1] == 11:
                                if hypothetical_state[1, j, 0] == 10:
                                    temp1, temp2 = pawn.get_moves(hypothetical_state, j)
                                    for t in temp1:
                                        hypothetical_moves.append(t)
                                elif hypothetical_state[1, j, 0] == 11:
                                    temp1 = rook.get_moves(hypothetical_state, j)
                                    for t in temp1:
                                        hypothetical_moves.append(t)
                                elif hypothetical_state[1, j, 0] == 12:
                                    temp1 = knight.get_moves(hypothetical_state, j)
                                    for t in temp1:
                                        hypothetical_moves.append(t)
                                elif hypothetical_state[1, j, 0] == 13:
                                    temp1 = bishop.get_moves(hypothetical_state, j)
                                    for t in temp1:
                                        hypothetical_moves.append(t)
                                elif hypothetical_state[1, j, 0] == 14:
                                    temp1 = queen.get_moves(hypothetical_state, j)
                                    for t in temp1:
                                        hypothetical_moves.append(t)
                                elif hypothetical_state[1, j, 0] == 15:
                                    temp1 = b_king.get_moves(hypothetical_state, j)
                                    # print("temp", temp1)
                                    for t in temp1:
                                        hypothetical_moves.append(t)

                        hypothetical_state[1, :, :] = hypothetical_state[0, :, :]

                        # print("hm",  hypothetical_moves)

                        for h_m in hypothetical_moves:
                            if h_m == km:
                                delete.append(km)

                        # print(km)
                    # print(delete)

                    for dell in delete:
                        try:
                            king_moves.remove(dell)
                        except ValueError:
                            continue

                    for r in king_moves:
                        moves.append(r)

                    # print("moves",  moves)

                    if len(moves):
                        return len(moves), check

                    delete = []
                    for i in range(64):
                        temp = []
                        if hypothetical_state[1, i, 1] == 10:
                            if hypothetical_state[1, i, 0] == 10:
                                temp1, temp2 = pawn.get_moves(hypothetical_state, i)
                                # print(temp1)
                                for t in temp1:
                                    temp.append(t)
                            elif hypothetical_state[1, i, 0] == 11:
                                temp1 = rook.get_moves(hypothetical_state, i)
                                for t in temp1:
                                    temp.append(t)
                            elif hypothetical_state[1, i, 0] == 12:
                                temp1 = knight.get_moves(hypothetical_state, i)
                                for t in temp1:
                                    temp.append(t)
                            elif hypothetical_state[1, i, 0] == 13:
                                temp1 = bishop.get_moves(hypothetical_state, i)
                                for t in temp1:
                                    temp.append(t)
                            elif hypothetical_state[1, i, 0] == 14:
                                temp1 = queen.get_moves(hypothetical_state, i)
                                for t in temp1:
                                    temp.append(t)

                            # print("temp", temp)

                            for m in temp:
                                before = (hypothetical_state[1, i, 0], i)
                                after = (hypothetical_state[1, i, 0], m, hypothetical_state[1, i, 1])
                                hypothetical_state[1, :, :] = update_state(hypothetical_state[1, :, :], before, after,
                                                                           False, (0, 0))
                                hypothetical_moves = []
                                for j in range(64):
                                    if hypothetical_state[1, j, 1] == 11:
                                        if hypothetical_state[1, j, 0] == 10:
                                            temp1, temp2 = pawn.get_moves(hypothetical_state, j)
                                            for t in temp1:
                                                hypothetical_moves.append(t)
                                        elif hypothetical_state[1, j, 0] == 11:
                                            temp1 = rook.get_moves(hypothetical_state, j)
                                            for t in temp1:
                                                hypothetical_moves.append(t)
                                        elif hypothetical_state[1, j, 0] == 12:
                                            temp1 = knight.get_moves(hypothetical_state, j)
                                            for t in temp1:
                                                hypothetical_moves.append(t)
                                        elif hypothetical_state[1, j, 0] == 13:
                                            temp1 = bishop.get_moves(hypothetical_state, j)
                                            for t in temp1:
                                                hypothetical_moves.append(t)
                                        elif hypothetical_state[1, j, 0] == 14:
                                            temp1 = queen.get_moves(hypothetical_state, j)
                                            for t in temp1:
                                                hypothetical_moves.append(t)
                                        elif hypothetical_state[1, j, 0] == 15:
                                            temp1 = b_king.get_moves(hypothetical_state, j)
                                            for t in temp1:
                                                hypothetical_moves.append(t)

                                hypothetical_state[1, :, :] = hypothetical_state[0, :, :]

                                # print(king_sqr)

                                # print("hm", hypothetical_moves)
                                # print(temp)
                                for h_m in hypothetical_moves:
                                    if h_m == king_sqr:
                                        delete.append(m)

                            # print("delete", delete)
                            for dell in delete:
                                try:
                                    temp.remove(dell)
                                except ValueError:
                                    continue

                            for t in temp:
                                moves.append(t)

                            # print("moves", moves)

                            if len(moves):
                                return len(moves), check

                    # print(len(moves), check)

                    return len(moves), check

                case False:
                    for m in moves:
                        after = (piece_type, m, color)
                        hypothetical_state[1, :, :] = update_state(hypothetical_state[1, :, :], before, after,
                                                                   False, (0, 0))
                        hypothetical_moves = []
                        for i in range(64):
                            if hypothetical_state[1, i, 1] == 10:
                                if hypothetical_state[1, i, 0] == 10:
                                    temp1, temp2 = pawn.get_moves(hypothetical_state, i)
                                    #print(temp1)
                                    for t in temp1:
                                        hypothetical_moves.append(t)
                                elif hypothetical_state[1, i, 0] == 11:
                                    temp1 = rook.get_moves(hypothetical_state, i)
                                    #print(temp1)
                                    for t in temp1:
                                            hypothetical_moves.append(t)
                                elif hypothetical_state[1, i, 0] == 12:
                                    temp1 = knight.get_moves(hypothetical_state, i)
                                    #print(temp1)
                                    for t in temp1:
                                        hypothetical_moves.append(t)
                                elif hypothetical_state[1, i, 0] == 13:
                                    temp1 = bishop.get_moves(hypothetical_state, i)
                                    #print(temp1)
                                    for t in temp1:
                                        hypothetical_moves.append(t)
                                elif hypothetical_state[1, i, 0] == 14:
                                    temp1 = queen.get_moves(hypothetical_state, i)
                                    #print(temp1)
                                    for t in temp1:
                                        hypothetical_moves.append(t)
                                elif hypothetical_state[1, i, 0] == 15:
                                    temp1 = w_king.get_moves(hypothetical_state, i)
                                    for t in temp1:
                                        hypothetical_moves.append(t)

                        hypothetical_state[1, :, :] = hypothetical_state[0, :, :]

                        for h_m in hypothetical_moves:
                            if piece_type == 15:
                                if h_m == m:
                                    delete.append(m)
                            else:
                                if h_m == king_sqr:
                                    delete.append(m)

    #if len(delete) > 0:
        #print("delete", delete)
        #print("check")

    return delete

def game(test):
    global CHECKMATE
    global STALEMATE
    global COUNT
    global MAX_COUNT

    [turn, state, w_rooks, b_rooks, w_king, b_king] = init.init()

    moved = False

    while not CHECKMATE and not STALEMATE:

        if test == True:
            _input = t.test(turn-1)
        else:
            _input = input()

        if _input == "z":
            break

        piece_type, move, rest = coord.SAD_to_move(_input)
        file_indexes = coord.get_file_index(rest)
        rank_indexes = coord.get_rank_index(rest)

        nn_blind_sup.nn((piece_type, move))

        #print(piece_type, move, rest)

        if turn % 2 == 0:
            for s in range(64):
                if state[1, s, 1] == 11:
                    if piece_type == 10 == state[1,s,0]:
                        if "x" in rest:
                            if s in file_indexes:
                                if move == s - coord.RANK + coord.FILE:
                                    legal_moves, e_p = pawn.get_moves(state, s)
                                    delete = check_check(state, w_king, b_king, s, legal_moves, state[1,s,1],False)

                                    print(legal_moves)
                                    print(delete)

                                    for dell in delete:
                                        try:
                                            legal_moves.remove(dell)
                                        except ValueError:
                                            continue

                                    for m in legal_moves:
                                        if m == move:
                                            before = (10, s)
                                            if coord.a1 <= move <= coord.h1:
                                                new_piece = promote(rest)
                                                after = (new_piece, m, 11)
                                            else:
                                                after = (10, m, 11)
                                            state[0, :, :] = state[1, :, :]
                                            if e_p:
                                                e_p_sqr = move + coord.RANK
                                                state[1, :, :] = update_state(state[1, :, :], before, after,
                                                                              e_p, e_p_sqr)
                                            else:
                                                state[1, :, :] = update_state(state[1, :, :], before, after,
                                                                              False, (0, 0))

                                            l_m, check = check_check(state, w_king, b_king, m, [], 10, True)

                                            if not l_m:
                                                if check:
                                                    CHECKMATE = True
                                                elif not check:
                                                    STALEMATE = True

                                            COUNT = 0
                                            turn = turn + 1
                                            moved = True
                                            break
                                elif move == s - coord.RANK - coord.FILE:
                                    legal_moves, e_p = pawn.get_moves(state, s)
                                    delete = check_check(state, w_king, b_king, s, legal_moves, state[1,s,1], False)

                                    for dell in delete:
                                        try:
                                            legal_moves.remove(dell)
                                        except ValueError:
                                            continue

                                    for m in legal_moves:
                                        if m == move:
                                            before = (10, s)
                                            if coord.a1 <= move <= coord.h1:
                                                new_piece = promote(rest)
                                                after = (new_piece, m, 11)
                                            else:
                                                after = (10, m, 11)
                                            state[0, :, :] = state[1, :, :]
                                            if e_p:
                                                e_p_sqr = move + coord.RANK
                                                state[1, :, :] = update_state(state[1, :, :], before, after,
                                                                              e_p, e_p_sqr)
                                            else:
                                                state[1, :, :] = update_state(state[1, :, :], before, after,
                                                                          False, (0, 0))

                                            l_m, check = check_check(state, w_king, b_king, m, [], 10, True)

                                            if not l_m:
                                                if check:
                                                    CHECKMATE = True
                                                elif not check:
                                                    STALEMATE = True

                                            COUNT = 0
                                            turn = turn + 1
                                            moved = True
                                            break
                        else:
                            if move == s - coord.RANK or move == s - 2 * coord.RANK:
                                legal_moves, e_p = pawn.get_moves(state, s)
                                delete = check_check(state, w_king, b_king, s, legal_moves, state[1,s,1], False)

                                for dell in delete:
                                    try:
                                        legal_moves.remove(dell)
                                    except ValueError:
                                        continue

                                for m in legal_moves:
                                    if m == move:
                                        before = (10, s)
                                        if coord.a1 <= move <= coord.h1:
                                            new_piece = promote(rest)
                                            after = (new_piece, m, 11)
                                        else:
                                            after = (10, m, 11)
                                        state[0, :, :] = state[1, :, :]
                                        state[1, :, :] = update_state(state[1, :, :], before, after,
                                                                      False, (0, 0))

                                        l_m, check = check_check(state, w_king, b_king, m, [], 10, True)

                                        if not l_m:
                                            if check:
                                                CHECKMATE = True
                                            elif not check:
                                                STALEMATE = True

                                        COUNT = 0
                                        turn = turn + 1
                                        moved = True
                                        break
                    elif piece_type == 15 == state[1,s,0]:
                        legal_moves = b_king.get_moves(state, s)
                        delete = check_check(state, w_king, b_king, s, legal_moves, state[1,s,1], False)

                        #print(legal_moves)
                        #print(delete)

                        for dell in delete:
                            try:
                                legal_moves.remove(dell)
                            except ValueError:
                                continue

                        for m in legal_moves:
                            if (move == "castle short" and m == s + 2 * coord.FILE and not b_rooks[1].moved
                                    and s + coord.FILE in legal_moves):
                                before = (piece_type, s)
                                after = (piece_type, m, 11)
                                state[0, :, :] = state[1, :, :]
                                state[1, :, :] = update_state(state[1, :, :], before, after,
                                                              False, (0, 0))
                                before = (11, coord.h8)
                                after = (11, coord.f8, 11)
                                state[1, :, :] = update_state(state[1, :, :], before, after,
                                                              False, (0, 0))
                                b_king.castled = True

                                l_m, check = check_check(state, w_king, b_king, m, [], 10, True)

                                if not l_m:
                                    if check:
                                        CHECKMATE = True
                                    elif not check:
                                        STALEMATE = True

                                COUNT = COUNT + 1
                                turn = turn + 1
                                moved = True
                                break
                            elif (move == "castle long" and m == s - 2 * coord.FILE and not b_rooks[0].moved
                                  and s - coord.FILE in legal_moves):
                                before = (piece_type, s)
                                after = (piece_type, m, 11)
                                state[0, :, :] = state[1, :, :]
                                state[1, :, :] = update_state(state[1, :, :], before, after,
                                                              False, (0, 0))
                                before = (11, coord.a8)
                                after = (11, coord.d8, 11)
                                state[1, :, :] = update_state(state[1, :, :], before, after,
                                                              False, (0, 0))
                                b_king.castled = True

                                l_m, check = check_check(state, w_king, b_king, m, [], 10,  True)

                                COUNT = COUNT + 1
                                turn = turn + 1
                                moved = True
                                break
                            elif m == move:
                                before = (piece_type, s)
                                after = (piece_type, m, 11)
                                state[0, :, :] = state[1, :, :]
                                state[1, :, :] = update_state(state[1, :, :], before, after,
                                                              False, (0, 0))
                                b_king.castled = True

                                if state[0, m, 0] == 0:
                                    COUNT = COUNT + 1
                                else:
                                    COUNT = 0

                                l_m, check = check_check(state, w_king, b_king, m, [], 10,  True)

                                if not l_m:
                                    if check:
                                        CHECKMATE = True
                                    elif not check:
                                        STALEMATE = True

                                turn = turn + 1
                                moved = True
                                break
                    else:
                        legal_moves = []
                        delete = []
                        if piece_type == 11 == state[1,s,0]:
                            legal_moves = rook.get_moves(state, s)
                            delete = check_check(state, w_king, b_king, s, legal_moves, state[1,s,1], False)
                        elif piece_type == 12 == state[1,s,0]:
                            legal_moves = knight.get_moves(state, s)
                            delete = check_check(state, w_king, b_king, s, legal_moves, state[1,s,1], False)
                        elif piece_type == 13 == state[1, s, 0]:
                            legal_moves = bishop.get_moves(state, s)
                            delete = check_check(state, w_king, b_king, s, legal_moves, state[1,s,1], False)
                        elif piece_type == 14 == state[1, s, 0]:
                            legal_moves = queen.get_moves(state, s)
                            delete = check_check(state, w_king, b_king, s, legal_moves, state[1,s,1], False)

                        #print(legal_moves)
                        #print(delete)

                        for dell in delete:
                            try:
                                legal_moves.remove(dell)
                            except ValueError:
                                continue

                        for m in legal_moves:
                            if rest == "" or rest == "x" or rest == "x+" or rest == "x#" or rest == "+" or rest == "#":
                                if m == move:
                                    before = (piece_type, s)
                                    after = (piece_type, m, 11)
                                    state[0, :, :] = state[1, :, :]
                                    state[1, :, :] = update_state(state[1, :, :], before, after,
                                                              False, (0,0))

                                    l_m, check = check_check(state, w_king, b_king, m, [], 10, True)

                                    if not l_m:
                                        if check:
                                            CHECKMATE = True
                                        elif not check:
                                            STALEMATE = True

                                    if piece_type == 11:
                                        if s == coord.a1:
                                            b_rooks[0].moved = True
                                        elif s == coord.h1:
                                            b_rooks[1].moved = True

                                    if state[0, m, 0] == 0:
                                        COUNT = COUNT + 1
                                    else:
                                        COUNT = 0

                                    turn = turn + 1
                                    moved = True
                                    break
                            else:
                                if s in file_indexes:
                                    if m == move:
                                        before = (piece_type, s)
                                        after = (piece_type, m, 11)
                                        state[0, :, :] = state[1, :, :]
                                        state[1, :, :] = update_state(state[1, :, :], before, after,
                                                                      False, (0, 0))

                                        l_m, check = check_check(state, w_king, b_king, m, [], 10, True)

                                        if not l_m:
                                            if check:
                                                CHECKMATE = True
                                            elif not check:
                                                STALEMATE = True

                                        if piece_type == 11:
                                            if s == coord.a1:
                                                b_rooks[0].moved = True
                                            elif s == coord.h1:
                                                b_rooks[1].moved = True

                                        if state[0, m, 0] == 0:
                                            COUNT = COUNT + 1
                                        else:
                                            COUNT = 0

                                        turn = turn + 1
                                        moved = True
                                        break
                                elif s in rank_indexes:
                                    if m == move:
                                        before = (piece_type, s)
                                        after = (piece_type, m, 11)
                                        state[0, :, :] = state[1, :, :]
                                        state[1, :, :] = update_state(state[1, :, :], before, after,
                                                                      False, (0, 0))

                                        l_m, check = check_check(state, w_king, b_king, m, [], 10, True)

                                        if not l_m:
                                            if check:
                                                CHECKMATE = True
                                            elif not check:
                                                STALEMATE = True

                                        if piece_type == 11:
                                            if s == coord.a1:
                                                b_rooks[0].moved = True
                                            elif s == coord.h1:
                                                b_rooks[1].moved = True

                                        if state[0, m, 0] == 0:
                                            COUNT = COUNT + 1
                                        else:
                                            COUNT = 0

                                        turn = turn + 1
                                        moved = True
                                        break
                if moved:
                    moved = False
                    break
        else:
            for s in range(64):
                if state[1, s, 1] == 10:
                    if piece_type == 10 == state[1,s,0]:
                        if "x" in rest:
                            if s in file_indexes:
                                if move == s + coord.RANK + coord.FILE:
                                    legal_moves, e_p = pawn.get_moves(state, s)
                                    delete = check_check(state, w_king, b_king, s, legal_moves, state[1,s,1],  False)

                                    for dell in delete:
                                        try:
                                            legal_moves.remove(dell)
                                        except ValueError:
                                            continue

                                    for m in legal_moves:
                                        if m == move:
                                            before = (10, s)
                                            if coord.a8 <= move <= coord.h8:
                                                new_piece = promote(rest)
                                                after = (new_piece, m, 10)
                                            else:
                                                after = (10, m, 10)
                                            state[0, :, :] = state[1, :, :]
                                            if e_p:
                                                e_p_sqr = move - coord.RANK
                                                state[1, :, :] = update_state(state[1, :, :], before, after,
                                                                              e_p, e_p_sqr)
                                            else:
                                                state[1, :, :] = update_state(state[1, :, :], before, after,
                                                                              False, (0, 0))

                                            l_m, check = check_check(state, w_king, b_king, m, [], 11, True)

                                            if not l_m:
                                                if check:
                                                    CHECKMATE = True
                                                elif not check:
                                                    STALEMATE = True

                                            COUNT = 0
                                            turn = turn + 1
                                            moved = True
                                            break
                                elif move == s + coord.RANK - coord.FILE:
                                    legal_moves, e_p = pawn.get_moves(state, s)
                                    delete = check_check(state, w_king, b_king, s, legal_moves, state[1,s,1], False)

                                    for dell in delete:
                                        try:
                                            legal_moves.remove(dell)
                                        except ValueError:
                                            continue

                                    #print(legal_moves)
                                    for m in legal_moves:
                                        if m == move:
                                            before = (10, s)
                                            if coord.a8 <= move <= coord.h8:
                                                new_piece = promote(rest)
                                                after = (new_piece, m, 10)
                                            else:
                                                after = (10, m, 10)
                                            state[0, :, :] = state[1, :, :]
                                            if e_p:
                                                e_p_sqr = move - coord.RANK
                                                state[1, :, :] = update_state(state[1, :, :], before, after,
                                                                              e_p, e_p_sqr)
                                            else:
                                                state[1, :, :] = update_state(state[1, :, :], before, after,
                                                                              False, (0, 0))

                                            l_m, check = check_check(state, w_king, b_king, m, [], 11, True)

                                            if not l_m:
                                                if check:
                                                    CHECKMATE = True
                                                elif not check:
                                                    STALEMATE = True

                                            COUNT = 0
                                            turn = turn + 1
                                            moved = True
                                            break
                        else:
                            if move == s + coord.RANK or move == s + 2 * coord.RANK:
                                legal_moves, e_p = pawn.get_moves(state, s)
                                delete = check_check(state, w_king, b_king, s, legal_moves, state[1,s,1], False)

                                for dell in delete:
                                    try:
                                        legal_moves.remove(dell)
                                    except ValueError:
                                        continue

                                for m in legal_moves:
                                    if m == move:
                                        before = (10, s)
                                        if coord.a8 <= move <= coord.h8:
                                            new_piece = promote(rest)
                                            after = (new_piece, m, 10)
                                        else:
                                            after = (10, m, 10)
                                        state[0, :, :] = state[1, :, :]
                                        state[1, :, :] = update_state(state[1, :, :], before, after,
                                                                      False, (0, 0))

                                        l_m, check = check_check(state, w_king, b_king, m, [], 11, True)

                                        if not l_m:
                                            if check:
                                                CHECKMATE = True
                                            elif not check:
                                                STALEMATE = True

                                        COUNT = 0
                                        turn = turn + 1
                                        moved = True
                                        break
                    elif piece_type == 15 == state[1, s, 0]:
                        legal_moves = w_king.get_moves(state, s)
                        delete = check_check(state, w_king, b_king, s, legal_moves, state[1,s,1], False)

                        print(legal_moves)
                        print(delete)

                        for dell in delete:
                            try:
                                legal_moves.remove(dell)
                            except ValueError:
                                continue

                        print(legal_moves)

                        for m in legal_moves:
                            if (move == "castle short" and m == s + 2 * coord.FILE and not w_rooks[1].moved
                                    and s + coord.FILE in legal_moves):
                                before = (piece_type, s)
                                after = (piece_type, m, 10)
                                state[0, :, :] = state[1, :, :]
                                state[1, :, :] = update_state(state[1, :, :], before, after,
                                                              False, (0, 0))
                                before = (11, coord.h1)
                                after = (11, coord.f1, 10)
                                state[1, :, :] = update_state(state[1, :, :], before, after,
                                                              False, (0, 0))
                                w_king.castled = True

                                l_m, check = check_check(state, w_king, b_king, m, [], 11, True)

                                if not l_m:
                                    if check:
                                        CHECKMATE = True
                                    elif not check:
                                        STALEMATE = True

                                COUNT = COUNT + 1
                                turn = turn + 1
                                moved = True
                                break
                            elif (move == "castle long" and m == s - 2 * coord.FILE and not w_rooks[0].moved
                                  and s - coord.FILE in legal_moves):
                                before = (piece_type, s)
                                after = (piece_type, m, 10)
                                state[0, :, :] = state[1, :, :]
                                state[1, :, :] = update_state(state[1, :, :], before, after,
                                                              False, (0, 0))
                                before = (11, coord.a1)
                                after = (11, coord.d1, 10)
                                state[1, :, :] = update_state(state[1, :, :], before, after,
                                                              False, (0, 0))

                                w_king.castled = True

                                lm, check = check_check(state, w_king, b_king, m, [], 11, True)

                                if not l_m:
                                    if check:
                                        CHECKMATE = True
                                    elif not check:
                                        STALEMATE = True

                                COUNT = COUNT + 1
                                turn = turn + 1
                                moved = True
                                break
                            elif m == move:
                                before = (piece_type, s)
                                after = (piece_type, m, 10)
                                state[0, :, :] = state[1, :, :]
                                state[1, :, :] = update_state(state[1, :, :], before, after,
                                                              False, (0, 0))
                                w_king.castled = True

                                l_m, check = check_check(state, w_king, b_king, m, [], 11, True)

                                if not l_m:
                                    if check:
                                        CHECKMATE = True
                                    elif not check:
                                        STALEMATE = True

                                if state[0, m, 0] == 0:
                                    COUNT = COUNT + 1
                                else:
                                    COUNT = 0

                                turn = turn + 1
                                moved = True
                                break
                    else:
                        legal_moves = []
                        delete = []
                        if piece_type == 11 == state[1, s, 0]:
                            legal_moves = rook.get_moves(state, s)
                            delete = check_check(state, w_king, b_king, s, legal_moves, state[1, s, 1], False)
                        elif piece_type == 12 == state[1, s, 0]:
                            legal_moves = knight.get_moves(state, s)
                            delete = check_check(state, w_king, b_king, s, legal_moves, state[1, s, 1], False)
                        elif piece_type == 13 == state[1, s, 0]:
                            legal_moves = bishop.get_moves(state, s)
                            delete = check_check(state, w_king, b_king, s, legal_moves, state[1, s, 1], False)
                        elif piece_type == 14 == state[1, s, 0]:
                            legal_moves = queen.get_moves(state, s)
                            delete = check_check(state, w_king, b_king, s, legal_moves, state[1, s, 1], False)

                        for dell in delete:
                            try:
                                legal_moves.remove(dell)
                            except ValueError:
                                continue

                        for m in legal_moves:
                            if rest == "" or rest == "x" or rest == "x+" or rest == "x#" or rest == "+" or rest == "#":
                                if m == move:
                                    before = (piece_type, s)
                                    after = (piece_type, m, 10)
                                    state[0, :, :] = state[1, :, :]
                                    state[1, :, :] = update_state(state[1, :, :], before, after,
                                                                  False, (0, 0))

                                    l_m, check = check_check(state, w_king, b_king, m, [], 11, True)

                                    if not l_m:
                                        if check:
                                            CHECKMATE = True
                                        elif not check:
                                            STALEMATE = True

                                    if piece_type == 11:
                                        if s == coord.a1:
                                            w_rooks[0].moved = True
                                        elif s == coord.h1:
                                            w_rooks[1].moved = True

                                    if state[0, m, 0] == 0:
                                        COUNT = COUNT + 1
                                    else:
                                        COUNT = 0

                                    turn = turn + 1
                                    moved = True
                                    break
                            else:
                                if s in file_indexes:
                                    if m == move:
                                        before = (piece_type, s)
                                        after = (piece_type, m, 10)
                                        state[0, :, :] = state[1, :, :]
                                        state[1, :, :] = update_state(state[1, :, :], before, after,
                                                                      False, (0, 0))

                                        l_m, check = check_check(state, w_king, b_king, m, [], 11, True)

                                        if not l_m:
                                            if check:
                                                CHECKMATE = True
                                            elif not check:
                                                STALEMATE = True

                                        if piece_type == 11:
                                            if s == coord.a1:
                                                w_rooks[0].moved = True
                                            elif s == coord.h1:
                                                w_rooks[1].moved = True

                                        if state[0, m, 0] == 0:
                                            COUNT = COUNT + 1
                                        else:
                                            COUNT = 0

                                        turn = turn + 1
                                        moved = True
                                        break
                                elif s in rank_indexes:
                                    if m == move:
                                        before = (piece_type, s)
                                        after = (piece_type, m, 10)
                                        state[0, :, :] = state[1, :, :]
                                        state[1, :, :] = update_state(state[1, :, :], before, after,
                                                                      False, (0, 0))

                                        l_m, check = check_check(state, w_king, b_king, m, [], 11, True)

                                        if not l_m:
                                            if check:
                                                CHECKMATE = True
                                            elif not check:
                                                STALEMATE = True

                                        if piece_type == 11:
                                            if s == coord.a1:
                                                w_rooks[0].moved = True
                                            elif s == coord.h1:
                                                w_rooks[1].moved = True

                                        if state[0, m, 0] == 0:
                                            COUNT = COUNT + 1
                                        else:
                                            COUNT = 0

                                        turn = turn + 1
                                        moved = True
                                        break
                    if moved:
                        moved = False
                        break

        if COUNT >= MAX_COUNT:
            STALEMATE = True

        coord.print_state(state[1, :, :])

        if CHECKMATE:
            if turn % 2 == 0:
                print("White wins (1,0)")
            else:
                print("Black wins (0,1)")
        if STALEMATE:
            print("Draw (1/2,1/2)")