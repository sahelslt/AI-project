import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, move=None, depth=0, cost=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost
    
    def __lt__(self, other):
        return (self.depth + self.cost) < (other.depth + other.cost)

class PuzzleSolver:
    def __init__(self, initial_state):
        self.initial_state = initial_state

    def solve(self):
        goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
        h = self.heuristic(self.initial_state, goal_state)
        root = PuzzleNode(state=self.initial_state, cost=h)
        heap = []
        heapq.heappush(heap, root)
        max_iterations = 10000  
        iterations = 0

        while heap and iterations < max_iterations:
            iterations += 1
            node = heapq.heappop(heap)
            print(f"Cost  {iterations}: {node.cost}") 
            if node.state == goal_state:
                return self.trace_path(node)
            
            z_i = node.state.index(0)
            x, y = divmod(z_i, 3)

            for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_x, new_y = x + move[0], y + move[1]
                if 0 <= new_x < 3 and 0 <= new_y < 3:
                    new_z_i = new_x * 3 + new_y
                    new_state = node.state[:]
                    new_state[z_i], new_state[new_z_i] = new_state[new_z_i], new_state[z_i]
                    h = self.heuristic(new_state, goal_state)
                    new_node = PuzzleNode(state=new_state, parent=node, move=(x, y), depth=node.depth + 1, cost=h)
                    heapq.heappush(heap, new_node)
        
        return None

    def trace_path(self, node):
        path = []
        while node:
            path.append(node.state)
            node = node.parent
        return path[::-1]

    def heuristic(self, state, goal_state):
        h = 0
        for i in range(1, 9):
            if state.index(i) != goal_state.index(i):
                h += 1
        return h

# Example
initial_state = [0, 2, 3, 1, 6, 4, 8, 7, 5]
solver = PuzzleSolver(initial_state)
solution_path = solver.solve()
if solution_path is None:
    print("No solution found.")
else:
    for state in solution_path:
        print(state[0:3])
        print(state[3:6])
        print(state[6:9])
        print()
