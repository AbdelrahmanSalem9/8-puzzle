
def swap(s, i, j):
    lst = list(s)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)

def generate_childs(state):

    state = str(state)
    index = state.index("0")
    childs = []

    #ay haga
    # if index == 0:
    #     childs.append(swap(state, index, 1))
    #     childs.append(swap(state, index, 3))
    # elif index == 1:
    #     childs.append(swap(state, index, 0))
    #     childs.append(swap(state, index, 2))
    #     childs.append(swap(state, index, 4))
    # elif index == 2:
    #     childs.append(swap(state, index, 1))
    #     childs.append(swap(state, index, 5))
    # elif index == 3:
    #     childs.append(swap(state, index, 0))
    #     childs.append(swap(state, index, 4))
    #     childs.append(swap(state, index, 6))
    # elif index == 4:
    #     childs.append(swap(state, index, 1))
    #     childs.append(swap(state, index, 3))
    #     childs.append(swap(state, index, 5))
    #     childs.append(swap(state, index, 7))
    # elif index == 5:
    #     childs.append(swap(state, index, 2))
    #     childs.append(swap(state, index, 4))
    #     childs.append(swap(state, index, 8))
    # elif index == 6:
    #     childs.append(swap(state, index, 3))
    #     childs.append(swap(state, index, 7))
    # elif index == 7:
    #     childs.append(swap(state, index, 4))
    #     childs.append(swap(state, index, 6))
    #     childs.append(swap(state, index, 8))
    # elif index == 8:
    #     childs.append(swap(state, index, 5))
    #     childs.append(swap(state, index, 7))
    #   Create children Nodes
    # def moveUp():
    index = state.index("0")  # index - 3 < 0 => check if there is space to move up
    if index > 2:
        childs.append(swap(state, index, index-3))


    index = state.index("0")  # index + 3 < length => check if there is space to move down
    if index < 6:
         childs.append((swap(state, index, index+3)))


    index = state.index("0") - 1
    if state.index("0") % 3 > 0:  # index % 3 < 2 => check if there is space to move left
            # self.left = Node(self.newState(index), self.index - 1, self.parent)
        childs.append(swap(state,state.index("0"),index))


    index = state.index("0") + 1
    if state.index("0") % 3 < 3 - 1:  # index % 3 < 0 => check if there is space to move right
        childs.append(swap(state,state.index("0"),index))

    return childs

def print_path(game):
    game = game[::-1]  # reverse the path
    for state in game:
        for i in range(9):
            if i == 2 or i == 5 or i == 8:
                print(state[i] + " ")
            else:
                print(state[i], end=" ")
        print("---------------------------------------------")

def bfs(initial_state):

    frontier = [];
    frontier.append(initial_state)
    explore = set()
    parent_map ={}
    while len(frontier) != 0:
        state = frontier.pop(0)
        explore.add(state)

        if state == "012345678":
            return find_path(parent_map, initial_state)

        else:
            for child in generate_childs(state):
                if child not in frontier and child not in explore:
                    parent_map[child] = state
                    frontier.append(child)
    return []


def find_path(parent_map,initial_state):
    current_state = "012345678"        #34an ageeb awl state abl el goal bta3y
    path =[current_state]
    while current_state != initial_state:
        path.append(parent_map[current_state])
        current_state = parent_map.get(current_state)
    return path

def dfs(initial_state):

    frontier = [];
    frontier.append(initial_state)
    explore = set()
    parent_map ={}
    while len(frontier) != 0:
        state = frontier.pop()
        explore.add(state)

        if state == "012345678":
            return find_path(parent_map, initial_state)

        else:
            for child in generate_childs(state):
                if child not in frontier and child not in explore:
                    parent_map[child] = state
                    frontier.append(child)
    return []


game1=bfs("125340678")
game2=dfs("102345678")
game3=bfs("312045678")
game4=dfs("312645708")
# game4=bfs("632105478")
print_path(game2)
