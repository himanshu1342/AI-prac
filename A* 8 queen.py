import heapq

# Goal state
GOAL_STATE = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

# Heuristic: Manhattan Distance
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                target_x = (value - 1) // 3
                target_y = (value - 1) % 3
                distance += abs(i - target_x) + abs(j - target_y)
    return distance

# Convert state to tuple (hashable for visited set)
def state_to_tuple(state):
    return tuple(tuple(row) for row in state)

# Find position of blank (0)
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate all valid moves from current state
def get_neighbors(state):
    x, y = find_blank(state)
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in state]
            # Swap blank with the neighbor
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append(new_state)

    return neighbors

# A* Search Algorithm
def solve_puzzle(start_state):
    visited = set()
    heap = []

    # (total_cost, cost_so_far, state, path)
    heapq.heappush(heap, (manhattan_distance(start_state), 0, start_state, []))

    while heap:
        total_cost, cost_so_far, current_state, path = heapq.heappop(heap)

        state_tuple = state_to_tuple(current_state)
        if state_tuple in visited:
            continue

        visited.add(state_tuple)
        path = path + [current_state]

        if current_state == GOAL_STATE:
            print("Solution found in", cost_so_far, "moves:")
            for step in path:
                for row in step:
                    print(row)
                print("------")
            return

        for neighbor in get_neighbors(current_state):
            if state_to_tuple(neighbor) not in visited:
                g = cost_so_far + 1
                h = manhattan_distance(neighbor)
                f = g + h
                heapq.heappush(heap, (f, g, neighbor, path))

    print("No solution found.")

# Example usage
initial_state = [[1, 2, 3],
                 [4, 0, 6],
                 [7, 5, 8]]

solve_puzzle(initial_state)
