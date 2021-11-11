from math import sqrt
import queue
class Algorithms:

    def find_path(parent_map, initial_state):
        current_state = "012345678"  # to get the parent of the goal state
        path = [current_state]
        while current_state != initial_state:
            path.append(parent_map[current_state])
            current_state = parent_map.get(current_state)
        return path

    # TODO: Search algorithms BFS, DFS ,A*
    def BFS(node):
        frontier = queue.Queue()
        frontier.put(node)

        frontier_state = set()
        frontier_state.add(node.get_state())

        explored = set()

        while not frontier.empty():
            current = frontier.get()
            explored.add(current.get_state())

            if current.is_goal():
                return current
            else:
                for child in current.expand():
                    if child.get_state() not in explored and child.get_state() not in frontier_state:
                        frontier.put(child)
                        frontier_state.add(child.get_state())
        return None

    def DFS(node):
        frontier = queue.LifoQueue()
        frontier.put(node)
        
        frontier_state = set()
        frontier_state.add(node.get_state())

        explored = set()
        while not frontier.empty():
            current = frontier.get()
            explored.add(current.get_state())

            if current.is_goal():
                return current
            else:
                for child in current.expand():
                    if child.get_state() not in explored and child.get_state() not in frontier_state:
                        frontier.put(child)
                        frontier_state.add(child.get_state())
        return None

    def print_path(game):  # reverse the path
        for state in game:
            for i in range(9):
                if i == 2 or i == 5 or i == 8:
                    print(state[i] + " ")
                else:
                    print(state[i], end=" ")
            print("---------------------------------------------")


    def a_star_ed(node):
        frontier = heapdict()
        frontier[node.get_state()] = Algorithms.euclidesDistance(node)

        explored = set()
        parent_map = {}

        while len(frontier) > 0:
            prev_cost = frontier.peekitem()[1] - Algorithms.euclidesDistance(frontier.peekitem()[0])
            state = frontier.popitem()[0]
            explored.add(state)

            if state == "012345678":
                return Algorithms.find_path(parent_map, node.get_state())
            
            node.expand()
            for child in node.get_children(state):
                if child.get_state() not in frontier and child.get_state() not in explored:
                    parent_map[child.state] = state
                    frontier[child.get_state()] = Algorithms.euclidesDistance(child) + prev_cost + 1
                elif child in frontier:
                    if frontier[child] > Algorithms.euclidesDistance(child):
                        frontier[child] = Algorithms.euclidesDistance(child)

        return []


    def is_solvable(state):
        inv_count = 0
        empty_value = 0
        for i in range(0, 9):
            for j in range(i + 1, 9):
                if int(state[j]) != empty_value and int(state[i]) != empty_value and int(state[i]) > int(state[j]):
                    inv_count += 1
        if inv_count % 2 == 0:
            return True
        return False
    """
    Heuristic functions
    => Manhattan Distance
    => Euclides Distance
    """
    def manhattan_distance(self, state, goal="012345678", col = 3):
        h = 0
        for c in state:
            index = state.find(c)
            target = goal.find(c)
            x_index = index % col
            y_index = index // col
            x_target = target % col
            y_target = target // col
            h = h + abs(x_index - x_target) + ( y_index - y_target)
        return h

    def euclides_distance(self, state, goal="012345678", col=3):
        h = 0
        for c in state:
            index = state.find(c)
            target = goal.find(c)
            x_index = index % col
            y_index = index // col
            x_target = target % col
            y_target = target // col
            h = h + sqrt( (x_index - x_target)**2 + ( y_index - y_target) ** 2)
        return h