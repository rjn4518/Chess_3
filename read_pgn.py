from pathlib import Path
import chess.pgn


def read_pgn(file):
    directory = Path.cwd()

    pgn_dir = directory / 'training_data' / file

    # print(pgn_dir)

    pgn = open(pgn_dir)

    games = []

    for i in range(10000):
        games.append(chess.pgn.read_game(pgn))
        if games[i] is None:
            games.remove(None)
            break

    #print(len(games))

    # white_moves = []
    # black_moves = []

    moves = []

    for g in range(len(games)):
        # white_moves.append([])
        # black_moves.append([])
        moves.append([])
        #print(moves)
        board = games[g].board()
        count = 0
        for move in games[g].mainline_moves():
            #print(move)
            _move = board.san(move)
            #print(_move)
            moves[g].append(_move)
            """
            if count % 2 == 0:
                white_moves[g].append(_move)
            else:
                black_moves[g].append(_move)
            """
            board.push(move)
            count = count + 1

    # return white_moves, black_moves
    return moves
