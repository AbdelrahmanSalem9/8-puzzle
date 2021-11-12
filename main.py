from math import sqrt
import collections
import heapdict as heapdict

import algorithm as algo
import node


# from heapdict import heapdict


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


if __name__ == '__main__':
    solver = algo
    print("welcome to 8_puzzle solver")

    while True:

        while True:  # do while to check if correct
            initial_state = input("insert initial state: ")
            freq = collections.Counter(initial_state)
            if len(initial_state) == len(freq) == 9 and initial_state.isdecimal():
                break
            print("wrong initial state")
        print("algorithms\n"
              "-----------\n"
              "[1] BFS\n"
              "[2] DFS\n"
              "[3] A*\n")
        switch = int(input("=>"))

        if not solver.is_solvable(initial_state):
            print(initial_state + " Cannot be solved")
            continue
        root = node.Node(initial_state)

        if switch == 1:
            root = solver.BFS(root)
        elif switch == 2:
            root = solver.DFS(root)
        elif switch == 3:
            input("choose heuristic:\n"
                  "-----------------\n"
                  "[1] Manhattan\n"
                  "[2] Euclidean\n")

        for child in root.get_list_to_root():
            child.print_state()
