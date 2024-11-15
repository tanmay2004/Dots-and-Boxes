from model import DotsAndBoxes
from policies import *
import time

policies = {0: humanPolicy, +1: minimaxPolicy}
game = DotsAndBoxes(N=2, M=2)
state = game.startState()

while not game.isEnd(state):
    print('='*20)
    print("Player 0 score:", state[3])
    print("Player 1 score:", state[4])
    print(f"\nPlayer {state[0]}'s turn!\n")
    game.printGameState(state)
    player = game.player(state)
    policy = policies[player]
    action = policy(game, state)
    state = game.succ(state, action)
    time.sleep(1)

print('='*20)
print("GAME OVER!\n")
print("Player 0 score:", state[3])
print("Player 1 score:", state[4], "\n")
game.printGameState(state)

print("\nUtility = {}".format(game.utility(state)))
