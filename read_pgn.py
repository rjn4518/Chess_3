from pathlib import Path
import chess.pgn

directory = Path.cwd()

pgn_dir = directory / 'training_data' / 'Carlsen.pgn'

print(pgn_dir)

pgn = open(pgn_dir)

games = []

for i in range(2):
    games.append(chess.pgn.read_game(pgn))
    if games[i] == None:
        games.remove(None)
        break

white_moves = []
black_moves = []

for g in range(len(games)):
    white_moves.append([])
    black_moves.append([])
    board = games[g].board()
    count = 0
    for move in games[g].mainline_moves():
        _move = board.san(move)
        if count % 2 == 0:
            white_moves[g].append(_move)
        else:
            black_moves[g].append(_move)
        board.push(move)
        count = count + 1

print(white_moves)
print(black_moves)

