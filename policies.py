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

def getHashableFromState(state):
    return (
        state[0], 
        tuple(tuple(edge) for edge in state[1]), 
        tuple(tuple(edge) for edge in state[2]), 
        state[3], 
        state[4]
    )

memo = {}

def minimaxPolicy(game, state):
    def recurse(state):
        hashable = getHashableFromState(state)

        # Check if already calculated
        if hashable in memo:
            return memo[hashable]

        # Return (utility of that state, action that achieves that utility)
        if game.isEnd(state):
            result = (game.utility(state), None)
        else:
            # List of (utility of succ, action leading to that succ)
            candidates = [
                (recurse(game.succ(state, action))[0], action)
                for action in game.actions(state)
            ]

            player = game.player(state)

            if player == 0:
                result = max(candidates)
            elif player == 1:
                result = min(candidates)
        
        memo[hashable] = result
        return result

    state_copy = deepcopy(state)
    utility, action = recurse(state_copy)
    print('minimaxPolicy: action {} with utility {}'.format(action, utility))
    return action