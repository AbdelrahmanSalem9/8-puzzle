# move action function to swap between two tiles
def swap(s, i, j):
    lst = list(s)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)


def generate_children(state):
    state = str(state)
    children = []

    # Create children Nodes
    # Get index of empty tile
    index = state.index("0")

    # Check Move up
    if index > 2:
        children.append(swap(state, index, index - 3))

    # Check Move down
    if index < 6:
        children.append((swap(state, index, index + 3)))

    # Check Left move
    if index % 3 > 0:
        children.append(swap(state, index, index - 1))

    # Check Right move
    if index % 3 < 2:
        children.append(swap(state, index, index + 1))

    return children


# printing the state in 3x3 board
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
    frontier = [initial_state]
    explore = set()
    parent_map = {}
    while len(frontier) != 0:
        state = frontier.pop(0)
        explore.add(state)

        if state == "012345678":
            return find_path(parent_map, initial_state)

        else:
            for child in generate_children(state):
                if child not in frontier and child not in explore:
                    parent_map[child] = state
                    frontier.append(child)
    return []


# backtracking the path from the goal state to the initial state
def find_path(parent_map, initial_state):
    current_state = "012345678"  # to get the parent of the goal state
    path = [current_state]
    while current_state != initial_state:
        path.append(parent_map[current_state])
        current_state = parent_map.get(current_state)
    return path


def dfs(initial_state):
    frontier = [initial_state]
    explore = set()
    parent_map = {}
    while len(frontier) != 0:
        state = frontier.pop()  # Stack behaviour
        explore.add(state)

        if state == "012345678":
            return find_path(parent_map, initial_state)

        else:
            for child in generate_children(state):
                if child not in frontier and child not in explore:
                    parent_map[child] = state
                    frontier.append(child)
    return []


# easy solvable games
game1 = bfs("125340678")
game2 = bfs("102345678")
game3 = bfs("312045678")
game4 = bfs("312645708")

print_path(game1)
