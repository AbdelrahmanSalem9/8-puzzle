from math import sqrt
from heapdict import heapdict


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


def get_state_manhattan_distance(state):
    goal = "012345678"
    sum = 0
    for s in state:
        sindex = state.find(s)
        gindex = goal.find(s)
        xs = sindex % 3
        ys = int(sindex / 3)
        xg = gindex % 3
        yg = int(gindex / 3)
        sum = sum + abs(xs - xg) + abs(ys - yg)
    return sum


def euclidesDistance(state, col=3):
    h = 0
    for c in state:
        index = state.find(c)
        target = int(c)
        x_index = index % col
        y_index = index // col
        x_target = target % col
        y_target = target // col
        h = h + sqrt((x_index - x_target) ** 2 + (y_index - y_target) ** 2)
    return h


def a_star_md(initial_state):
    frontier = heapdict()
    frontier[initial_state] = get_state_manhattan_distance(initial_state)

    explored = set()
    parent_map = {}

    while len(frontier) > 0:
        prev_cost = frontier.peekitem()[1] - get_state_manhattan_distance(frontier.peekitem()[0])
        state = frontier.popitem()[0]
        explored.add(state)

        if state == "012345678":
            return find_path(parent_map, initial_state)

        for child in generate_children(state):
            if child not in frontier and child not in explored:
                parent_map[child] = state
                frontier[child] = get_state_manhattan_distance(child) + prev_cost + 1
            elif child in frontier:
                if frontier[child] > get_state_manhattan_distance(child):
                    frontier[child] = get_state_manhattan_distance(child)

    return []


def a_star_ed(initial_state):
    frontier = heapdict()
    frontier[initial_state] = euclidesDistance(initial_state)

    explored = set()
    parent_map = {}

    while len(frontier) > 0:
        prev_cost = frontier.peekitem()[1] - euclidesDistance(frontier.peekitem()[0])
        state = frontier.popitem()[0]
        explored.add(state)

        if state == "012345678":
            return find_path(parent_map, initial_state)

        for child in generate_children(state):
            if child not in frontier and child not in explored:
                parent_map[child] = state
                frontier[child] = euclidesDistance(child) + prev_cost + 1
            elif child in frontier:
                if frontier[child] > euclidesDistance(child):
                    frontier[child] = euclidesDistance(child)

    return []


def check_solvable(state):
    inv_count = 0
    empty_value = 0
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if int(state[j]) != empty_value and int(state[i]) != empty_value and int(state[i]) > int(state[j]):
                inv_count += 1
    if inv_count % 2 == 0:
        return True
    return False


if __name__ == '__main__':
    # easy solvable games
    # game1 = bfs("125340678")
    #     game2 = bfs("102345678")
    # game3 = bfs("312045678")
    # game4 = a_star_md("812045673")
    # print_path(game4)=
    # print("h = "+str(get_state_manhattan_distance("102345678")))
    # initial_state = input("Enter Initial State : ")
    #
    #
    # print("Choose Algorithm to solve ")
    # print("1 - BFS    2 - DFS     3 - A*(Manhattan distance) ")
    # alg = input("Enter your choice : ")
    # if not check_solvable(initial_state):
    #     print("Not Solvable")
    #     exit(0)
    #
    # if alg == 1:
    #     game = bfs(initial_state)
    # elif alg == 2:
    #     game = dfs(initial_state)
    # elif alg == 3:
    #     game = a_star_md(initial_state)

    game = a_star_ed("182043765")
    # game2 = a_star_ed("013425786")

    print_path(game)
