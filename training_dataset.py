import numpy as np
import read_pgn
import init
import game as g
import coordinates as coord

file = 'Carlsen.pgn'

games = read_pgn.read_pgn(file)
#print(games)

temp_examples = []
temp_labels = []

for game in games:
    # print(game)
    [turn, state, w_rooks, b_rooks, w_king, b_king] = init.init()
    last_state = state
    temp = np.zeros((len(game) + 1, 64, 2))
    temp[0, :, :] = state[1, :, :]
    temp_examples.append(temp[0, :, :])
    for m in game:
        print(m)
        new_state = g.game(m, turn, last_state, w_rooks, b_rooks, w_king, b_king)
        temp[turn, :, :] = new_state[1, :, :]
        if turn % 2 == 0:
            temp_labels.append(temp[turn, :, :])
        else:
            temp_examples.append(temp[turn, :, :])
        last_state = new_state
        """
        if count == 0:
            train_labels = g.game(m, turn, state, w_rooks, b_rooks, w_king, b_king)
            o = 1
        elif count % 2 == 0:
            temp = g.game(m, turn, state, w_rooks, b_rooks, w_king, b_king)
            train_labels = np.vstack([train_labels, temp])
        elif count % 2 != 0:
            temp = g.game(m, turn, state, w_rooks, b_rooks, w_king, b_king)
            print(temp)
            train_examples = np.vstack([train_examples, temp])
        """
        turn = turn + 1

train_examples = np.array(temp_examples)
train_labels = np.array(temp_labels)

# print(temp[23, 15, 0])
print(train_examples.shape)
print(train_labels.shape)


