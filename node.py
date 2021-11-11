class Node:
    """
    *********
    | 0 1 2 |
    | 3 4 5 |
    | 6 7 8 |
    *********
    """

    def __init__(self, state, index, parent=None, col=3):
        self.state = state
        self.index = index
        self.parent = parent
        self.col = col
        if parent is None:
            self.depth = 0
        else:
            self.depth = parent.depth + 1

        # Children
        self.children = []

    def isGoalState(self, goal=None):
        if goal is None:
            goal = "012345678"
        if self.state == goal:
            return True
        else:
            return False

    #   Create children Nodes
    def moveUp(self):
        index = self.index - self.col  # index - 3 < 0 => check if there is space to move up
        if index > 0:
            newState = self.newState(index)
            if newState != self.state:
                self.children.append(Node(newState, index, self))
            else:
                return None

    def moveDown(self):
        index = self.index + self.col  # index + 3 < length => check if there is space to move down
        if index < len(self.state):
            newState = self.newState(index)
            if newState != self.state:
                self.children.append(Node(newState, index, self))
            else:
                return None
                
    def moveLeft(self):
        index = self.index - 1
        if self.index % self.col > 0:  # index % 3 < 2 => check if there is space to move left
            newState = self.newState(index)
            if newState != self.state:
                self.children.append(Node(newState, index, self))
            else:
                return None

    def moveRight(self):
        index = self.index + 1
        if self.index % self.col < self.col - 1:  # index % 3 < 0 => check if there is space to move right
            newState = self.newState(index)
            if newState != self.state:
                self.children.append(Node(newState, index, self))
            else:
                return None

    def newState(self, index):
        state = swap(self.state, self.index, index)
        return state

    def move(self):
        self.moveLeft()
        self.moveRight()
        self.moveUp()
        self.moveDown()

    def getState(self):
        return self.state
    
    def getChildren(self):
        return self.children
        
    def printState(self):
        print(self.state[0:self.col])
        print(self.state[self.col :self.col + self.col])
        print(self.state[self.col + self.col :len(self.state)])

def swap(s, i, j):
    lst = list(s)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)