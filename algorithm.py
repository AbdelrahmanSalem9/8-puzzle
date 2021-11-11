from math import sqrt
class Algorithms:

    def find_path(parent_map, initial_state):
        current_state = "012345678"  # to get the parent of the goal state
        path = [current_state]
        while current_state != initial_state:
            path.append(parent_map[current_state])
            current_state = parent_map.get(current_state)
        return path

    # TODO: Search algorithms BFS, DFS ,A*
    def bfs(node):
        frontier = [node.getState()]
        explore = set()
        parent_map = {}
        while len(frontier) != 0:
            state = frontier.pop(0)
            explore.add(state)

            if state == "012345678":
                return Algorithms.find_path(parent_map, node.getState())

            else:
                node.move()
                for child in node.getChildren():
                    if child.getState() not in frontier and child.getState() not in explore:
                        parent_map[child.getState()] = state
                        frontier.append(child.getState())
        return []


    def dfs_recursive(node, initial_state ,visited=None ,goal="012345678"):
        if visited is None:
            visited = set()
        visited.add(node.getState())
        node.move()
        for child in node.getChildren():
            if node.isGoalState(goal):
                break

            if child.getState() not in visited and not node.isGoalState():
                return Algorithms.dfs_recursive(child, initial_state, visited)
        return child


    def print_path(game):  # reverse the path
        for state in game:
            for i in range(9):
                if i == 2 or i == 5 or i == 8:
                    print(state[i] + " ")
                else:
                    print(state[i], end=" ")
            print("---------------------------------------------")


    def dfs(self, node):
        pass

    def a_star(self, node):
        pass
    """
    Heuristic functions
    => Manhattan Distance
    => Euclides Distance
    """
    def manhattanDistance(self, state, col = 3):
        h = 0
        for c in state:
            index = state.find(c)
            target = int(c)
            x_index = index % col
            y_index = index // col
            x_target = target % col
            y_target = target // col
            h = h + abs(x_index - x_target) + ( y_index - y_target)

        return h
    def euclidesDistance(self, state, col=3):
        h = 0
        for c in state:
            index = state.find(c)
            target = int(c)
            x_index = index % col
            y_index = index // col
            x_target = target % col
            y_target = target // col
            h = h + sqrt( (x_index - x_target)**2 + ( y_index - y_target) )
        return h
