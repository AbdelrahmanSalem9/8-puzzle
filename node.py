class Node:
    """
    *********
    | 0 1 2 |
    | 3 4 5 |
    | 6 7 8 |
    *********
    """

    def __init__(self, state, index, action = "initial_state", parent=None, col=3):
        self.state = state
        self.index = index
        self.parent = parent
        self.action = action
        self.col = col
        if parent is None:
            self.depth = 0
        else:
            self.depth = parent.depth + 1

        # Children
        self.children = []

    def is_goal(self, goal=None):
        if goal is None:
            goal = "012345678"
        if self.state == goal:
            return True
        else:
            return False

    #   Create children Nodes
    def move_up(self):
        index = self.index - self.col  # index - 3 < 0 => check if there is space to move up
        if index > 0:
            new_state = self.new_state(index)
            if new_state != self.state:
                self.children.append(Node(new_state, index, "up",self))
            else:
                return None

    def move_down(self):
        index = self.index + self.col  # index + 3 < length => check if there is space to move down
        if index < len(self.state):
            new_state = self.new_state(index)
            if new_state != self.state:
                self.children.append(Node(new_state, index, "down",self))
            else:
                return None
                
    def move_left(self):
        index = self.index - 1
        if self.index % self.col > 0:  # index % 3 < 2 => check if there is space to move left
            new_state = self.new_state(index)
            if new_state != self.state:
                self.children.append(Node(new_state, index, "left",self))
            else:
                return None

    def move_right(self):
        index = self.index + 1
        if self.index % self.col < self.col - 1:  # index % 3 < 0 => check if there is space to move right
            new_state = self.new_state(index)
            if new_state != self.state:
                self.children.append(Node(new_state, index, "right",self))
            else:
                return None

    def new_state(self, index):
        state = swap(self.state, self.index, index)
        return state

    def expand(self):
        self.expand_left()
        self.expand_right()
        self.expand_up()
        self.expand_down()
        return self.children

    def get_state(self):
        return self.state
    
    def get_children(self):
        return self.children
        
    def print_state(self):
        print(self.state[0:self.col])
        print(self.state[self.col :self.col + self.col])
        print(self.state[self.col + self.col :len(self.state)])

    def get_list_to_root(self, solutin_node):
        temp = solutin_node
        lst = [temp]
        while temp.parent is not None:
            temp = temp.parent
            lst.append(temp)
        return lst

def swap(s, i, j):
    lst = list(s)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)