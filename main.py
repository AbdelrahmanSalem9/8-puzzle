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
    manhattan_sum = 0
    for s in state:
        current_index = state.find(s)
        goal_index = goal.find(s)
        manhattan_sum = manhattan_sum + abs((current_index % 3) - (goal_index % 3)) + abs(
            (current_index // 3) - (goal_index // 3))
    return manhattan_sum


def euclidean_distance(state):
    goal = "012345678"
    euclidean_sum = 0
    for s in state:
        current_index = state.find(s)
        goal_index = goal.find(s)
        euclidean_sum = euclidean_sum + sqrt(
            ((current_index % 3) - (goal_index % 3)) ** 2 + ((current_index // 3) - (goal_index // 3)) ** 2)
    return euclidean_sum


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
    frontier = heapdict()  # optimized priority queue using hashing
    frontier[initial_state] = euclidean_distance(initial_state)

    explored = set()
    parent_map = {}

    while len(frontier) > 0:
        prev_cost = frontier.peekitem()[1] - euclidean_distance(
            frontier.peekitem()[0])  # to get the cost of the parent node
        state = frontier.popitem()[0]
        explored.add(state)

        if state == "012345678":
            return find_path(parent_map, initial_state)

        for child in generate_children(state):
            if child not in frontier and child not in explored:
                parent_map[child] = state
                frontier[child] = euclidean_distance(child) + prev_cost + 1  # f(n) = h(n) + c(n)
            elif child in frontier:
                if frontier[child] > euclidean_distance(child):
                    frontier[child] = euclidean_distance(child)

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

    test_games = ["013425786", "125340678", "312045678", "182043765", "812045673"]  # Solvable initial states
    test_unsolvable = "812043765"
    game = test_games[1]
    if check_solvable(game):
        solution = a_star_md(game)
        print_path(solution)
    else:
        print("Not Solvable")
