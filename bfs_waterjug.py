from collections import deque

# Function to perform BFS and find the solution
def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    visited = set()
    queue = deque()

    # Each state is represented as (jug1, jug2)
    queue.append([(0, 0)])  # start with both jugs empty

    while queue:
        path = queue.popleft()
        current = path[-1]

        # If target is found in any jug
        if current[0] == target or current[1] == target:
            print("Steps to reach the target:")
            for step in path:
                print(step)
            return

        if current in visited:
            continue

        visited.add(current)

        jug1, jug2 = current
        possible_states = []

        # Fill jug1
        possible_states.append((jug1_capacity, jug2))
        # Fill jug2
        possible_states.append((jug1, jug2_capacity))
        # Empty jug1
        possible_states.append((0, jug2))
        # Empty jug2
        possible_states.append((jug1, 0))
        # Pour jug1 -> jug2
        pour = min(jug1, jug2_capacity - jug2)
        possible_states.append((jug1 - pour, jug2 + pour))
        # Pour jug2 -> jug1
        pour = min(jug2, jug1_capacity - jug1)
        possible_states.append((jug1 + pour, jug2 - pour))

        for state in possible_states:
            if state not in visited:
                queue.append(path + [state])

    print("No solution found.")

# Example usage
jug1_capacity = 4
jug2_capacity = 3
target = 2

water_jug_bfs(jug1_capacity, jug2_capacity, target)
