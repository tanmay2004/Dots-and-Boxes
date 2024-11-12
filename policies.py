import random, time
from copy import deepcopy

def humanPolicy(game, state):
    actions = game.actions(state)

    while True:
        action = input("\nInput action: ")
        action = tuple(map(int, action.split()))

        if action in actions:
            return action
        else:
            print("Invalid move, try again!")

def randomPolicy(game, state):
    actions = game.actions(state)
    return random.choice(actions)

def minimaxPolicy(game, state):
    def recurse(state):
        # Return (utility of that state, action that achieves that utility)
        if game.isEnd(state):
            return (game.utility(state), None)
        # List of (utility of succ, action leading to that succ)
        candidates = [
            (recurse(game.succ(state, action))[0], action)
            for action in game.actions(state)
        ]
        player = game.player(state)

        if player == 0:
            return max(candidates)
        elif player == 1:
            return min(candidates)

    state_copy = deepcopy(state)
    utility, action = recurse(state_copy)
    print('minimaxPolicy: state {} => action {} with utility {}'.format(state, action, utility))
    return action