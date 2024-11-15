from copy import deepcopy

# The agent is player 0 and the opponent is player 1
# State is stored as a tuple so that it is immutable

class DotsAndBoxes(object):
    def __init__(self, N, M):
        self.N = N # number of rows
        self.M = M # number of columns
        self.num_boxes = self.N * self.M
        self.horizontal = [[0 for _ in range(M)] for _ in range(N+1)]
        self.vertical = [[0 for _ in range(M+1)] for _ in range(N)]

    # state = (player, horizontal edges, vertical edges, player0 score, player1 score)

    def startState(self):
        return (0, self.horizontal, self.vertical, 0, 0)

    def isEnd(self, state):
        # can be redefined to be max(state[3], state[4]) > num_boxes // 2
        return state[3]+state[4] == self.num_boxes

    def utility(self, state):
        return state[3] - state[4]

    def actions(self, state):
        horizontal = state[1]
        vertical = state[2]
        actions = []

        for i in range(self.N+1):
            for j in range(self.M):
                if horizontal[i][j] == 0:
                    actions.append((i, j, 0))
        
        for i in range(self.N):
            for j in range(self.M+1):
                if vertical[i][j] == 0:
                    actions.append((i, j, 1))
        
        return actions

    def player(self, state):
        return state[0]

    def succ(self, state, action):
        player = state[0]
        horizontal = deepcopy(state[1])
        vertical = deepcopy(state[2])
        
        if action[2] == 0:
            horizontal[action[0]][action[1]] = 1
        elif action[2] == 1:
            vertical[action[0]][action[1]] = 1
        
        num_added = self.calcNumRects(horizontal, vertical) - (state[3]+state[4])

        if num_added > 0:
            if player == 0:
                new_0 = state[3] + num_added
                new_1 = state[4]
            elif player == 1:
                new_0 = state[3]
                new_1 = state[4] + num_added
            
            return (player, horizontal, vertical, new_0, new_1)
        
        return (int(not player), horizontal, vertical, state[3], state[4])

    def calcNumRects(self, horizontal, vertical):
        count = 0

        for i in range(self.N):
            for j in range(self.M):
                if horizontal[i][j] and horizontal[i+1][j] and vertical[i][j] and vertical[i][j+1]:
                    count += 1
        
        return count

    def printGameState(self, state):
        horizontal, vertical = state[1], state[2]

        for i in range(self.N+1):
            for j in range(self.M+1):
                print("*", end='')

                if j < self.M:
                    if horizontal[i][j]:
                        print("----", end='')
                    else:
                        print("    ", end='')

            print()

            if i < self.N:
                curr = ""

                for k in range(self.M+1):
                    if vertical[i][k]:
                        curr += "|"
                    else:
                        curr += " "
                    
                    curr += "    "
                
                print(curr)
                print(curr)
