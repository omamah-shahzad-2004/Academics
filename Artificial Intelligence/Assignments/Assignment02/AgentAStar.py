from queue import PriorityQueue

class Agent(object):
    def SearchSolution(self, state):
        return []

class AgentAStar(Agent):
    def _init_(self):
        pass

    def heuristic_func(self, curr_pos, goal):
        return abs(goal[0] - curr_pos[0]) + abs(goal[1] - curr_pos[1])

    def neighbors(self, position, state):
        x, y = position
        directions = [
            (0, 1),
            (0, -1), 
            (1, 0), 
            (-1, 0)]
        neighbors = []
        for dir_x, dir_y in directions:
            new_x, new_y = x + dir_x, y + dir_y
            if (new_x >= 0 and new_y >= 0 and new_x < state.maze.WIDTH and new_y < state.maze.HEIGHT):
                neighbors.append((new_x, new_y))
        return neighbors

    def SearchSolution(self, state):
        FoodX = state.FoodPosition.X
        FoodY = state.FoodPosition.Y
        
        HeadX = state.snake.HeadPosition.X #L
        HeadY = state.snake.HeadPosition.Y #T
		
        plan = []

        start = (HeadX, HeadY)
        goal = (FoodX, FoodY)

        frontier = PriorityQueue()
        frontier.put((0, start))
        parent = {}
        parent[start] = None
        cost_so_far = {}
        cost_so_far[start] = 0

        while not frontier.empty():
            _, node = frontier.get()
            if node == goal:
                break
            for neighbor in self.neighbors(node, state):
                x, y = node
                cost = cost_so_far[node] + 1
                if (neighbor not in cost_so_far or cost < cost_so_far[neighbor]) and state.maze.MAP[y][x] != -1:
                    cost_so_far[neighbor] = cost
                    estimated_cost = cost + self.heuristic_func(neighbor, goal)
                    frontier.put((estimated_cost, neighbor))
                    parent[neighbor] = node

        path = []
        curr = goal
        while curr != start:
            path.append(curr)
            curr = parent[curr]
        path.append(start)
        path.reverse()

        for i in range(1, len(path)):
            DR = path[i][0] - path[i-1][0]
            DC = path[i][1] - path[i-1][1]
            if DR == 1:
                plan.append(3)  # Right
            elif DR == -1:
                plan.append(9)  # Left
            elif DC == 1:
                plan.append(6)  # Down
            elif DC == -1:
                plan.append(0)  # Up

        return plan

def showAgent():
    print("A Snake Solver By Omamah")