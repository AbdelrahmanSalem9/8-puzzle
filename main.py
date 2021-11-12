import time
from collections import deque
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
def print_path(game, cost, nodes_explored, depth, time_taken):
    game = game[::-1]  # reverse the path
    for state in game:
        for i in range(9):
            if i == 2 or i == 5 or i == 8:
                print(state[i] + " ")
            else:
                print(state[i], end=" ")
        print("---------------------------------------------")
    print("Cost = " + str(cost))
    print("Depth = " + str(depth))
    print("Nodes Explored = " + str(nodes_explored))
    print("Running Time = " + str(time_taken))
    # print("Cost = "+str(cost) + "  Nodes Explored = "+str(nodes_explored))


# backtracking the path from the goal state to the initial state
def find_path(parent_map, initial_state, nodes_explored, depth, time_taken):
    current_state = "012345678"  # to get the parent of the goal state
    path = [current_state]
    cost = 0
    while current_state != initial_state:
        path.append(parent_map[current_state])
        current_state = parent_map.get(current_state)
        cost += 1
    # return path
    print_path(path, cost, nodes_explored, depth, time_taken)


def bfs(initial_state):
    start_time = time.time()
    frontier = [initial_state]
    explore = set()
    parent_map = {}
    frontier_state = {initial_state: True}
    depth_map = {initial_state: 0}
    max_depth = 0
    while len(frontier) != 0:
        state = frontier.pop(0)
        explore.add(state)
        frontier_state.pop(state)

        if state == "012345678":
            return find_path(parent_map, initial_state, len(explore), max_depth, time.time() - start_time)

        else:

            for child in generate_children(state):
                if child not in frontier_state and child not in explore:
                    parent_map[child] = state
                    frontier_state[child] = True
                    frontier.append(child)
                    depth_map[child] = depth_map[state] + 1
                    if depth_map[child] > max_depth:
                        max_depth = depth_map[child]

    return []


def dfs(initial_state):
    start_time = time.time()
    frontier = deque()
    frontier.append(initial_state)
    frontier_state = {initial_state: True}
    explore = set()
    parent_map = {}
    depth_map = {initial_state: 0}
    max_depth = 0
    while len(frontier) != 0:
        state = frontier.pop()  # Stack behaviour
        frontier_state.pop(state)
        explore.add(state)

        if state == "012345678":
            return find_path(parent_map, initial_state, len(explore), max_depth, time.time() - start_time)
        else:
            for child in reversed(generate_children(state)):
                if child not in frontier_state and child not in explore:
                    parent_map[child] = state
                    frontier_state[child] = True
                    frontier.append(child)
                    depth_map[child] = depth_map[state] + 1
                    if depth_map[child] > max_depth:
                        max_depth = depth_map[child]

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
    start_time = time.time()

    frontier = heapdict()
    frontier[initial_state] = get_state_manhattan_distance(initial_state)
    explored = set()
    parent_map = {}
    depth_map = {initial_state: 0}
    max_depth = 0
    while len(frontier) > 0:
        prev_cost = frontier.peekitem()[1] - get_state_manhattan_distance(frontier.peekitem()[0])
        state = frontier.popitem()[0]
        explored.add(state)

        if state == "012345678":
            return find_path(parent_map, initial_state, len(explored), max_depth, time.time() - start_time)

        for child in generate_children(state):
            if child not in frontier and child not in explored:
                parent_map[child] = state
                frontier[child] = get_state_manhattan_distance(child) + prev_cost + 1

                depth_map[child] = depth_map[state] + 1
                if depth_map[child] > max_depth:
                    max_depth = depth_map[child]

            elif child in frontier:
                if frontier[child] > get_state_manhattan_distance(child):
                    frontier[child] = get_state_manhattan_distance(child)

    return []


def a_star_ed(initial_state):
    start_time = time.time()
    frontier = heapdict()  # optimized priority queue using hashing
    frontier[initial_state] = euclidean_distance(initial_state)
    explored = set()
    parent_map = {}

    depth_map = {initial_state: 0}
    max_depth = 0

    while len(frontier) > 0:
        prev_cost = frontier.peekitem()[1] - euclidean_distance(
            frontier.peekitem()[0])  # to get the cost of the parent node
        state = frontier.popitem()[0]
        explored.add(state)

        if state == "012345678":
            return find_path(parent_map, initial_state, len(explored), max_depth, time.time() - start_time)

        for child in generate_children(state):
            if child not in frontier and child not in explored:
                parent_map[child] = state
                frontier[child] = euclidean_distance(child) + prev_cost + 1  # f(n) = h(n) + c(n)

                depth_map[child] = depth_map[state] + 1
                if depth_map[child] > max_depth:
                    max_depth = depth_map[child]

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

    # test_games = ["013425786", "125340678", "312045678", "182043765", "812045673",
    #               "312045678", "012345678"]  # Solvable initial states
    # test_unsolvable = "812043765"
    # game = test_games[0]

    initial_state = input("Enter initial state : ")
    print("1-BFS    2-DFS   3-A*(manhattan)     4-A*(Euclidean)")
    alg = int(input("Choose Algorithm to solve : : "))
    if check_solvable(initial_state):
        if alg == 1:
            bfs(initial_state)
        elif alg == 2:
            dfs(initial_state)
        elif alg == 3:
            a_star_md(initial_state)
        elif alg == 4:
            a_star_ed(initial_state)
    else:
        print("Not Solvable")
