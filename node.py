class Node:
    """
    *********
    | 0 1 2 |
    | 3 4 5 |
    | 6 7 8 |
    *********
    """

    def __init__(self, state, parent=None, action="initial", col=3):
        self.state = state
        self.index = state.find("0")
        self.parent = parent
        self.action = action
        self.col = col
        if parent is None:
            self.depth = 0
        else:
            self.depth = self.parent.depth + 1

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
                self.children.append(Node(state=new_state, parent=self, action="up"))
            else:
                return None

    def move_down(self):
        index = self.index + self.col  # index + 3 < length => check if there is space to move down
        if index < len(self.state):
            new_state = self.new_state(index)
            if new_state != self.state:
                self.children.append(Node(new_state, parent=self, action="down"))
            else:
                return None

    def move_left(self):
        index = self.index - 1
        if self.index % self.col > 0:  # index % 3 < 2 => check if there is space to move left
            new_state = self.new_state(index)
            if new_state != self.state:
                self.children.append(Node(new_state, parent=self, action="left"))
            else:
                return None

    def move_right(self):
        index = self.index + 1
        if self.index % self.col < self.col - 1:  # index % 3 < 0 => check if there is space to move right
            new_state = self.new_state(index)
            if new_state != self.state:
                self.children.append(Node(new_state, parent=self, action="right"))
            else:
                return None

    def new_state(self, index):
        state = swap(self.state, self.index, index)
        return state

    def expand(self):
        self.move_left()
        self.move_right()
        self.move_up()
        self.move_down()
        return self.children

    def get_state(self):
        return self.state

    def get_children(self):
        return self.children

    def print_state(self):
        print(self.state[0:self.col])
        print(self.state[self.col:self.col + self.col])
        print(self.state[self.col + self.col:len(self.state)])
        print("-------------------------")

    def get_list_to_root(self):
        temp = self
        lst = [temp]
        while temp.parent is not None:
            temp = temp.parent
            lst.append(temp)
        return lst[::-1]


def swap(s, i, j):
    lst = list(s)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)