def water_jug_dfs(jug1_capacity, jug2_capacity, target):
    visited = set()
    solution_found = False

    def dfs(jug1, jug2, path):
        nonlocal solution_found

        if (jug1, jug2) in visited or solution_found:
            return

        visited.add((jug1, jug2))
        path.append((jug1, jug2))

        # Goal check
        if jug1 == target or jug2 == target:
            print("Steps to reach the target:")
            for step in path:
                print(step)
            solution_found = True
            return

        # Possible next moves
        possible_states = [
            (jug1_capacity, jug2),       # Fill Jug1
            (jug1, jug2_capacity),       # Fill Jug2
            (0, jug2),                   # Empty Jug1
            (jug1, 0),                   # Empty Jug2
            # Pour Jug1 -> Jug2
            (jug1 - min(jug1, jug2_capacity - jug2), jug2 + min(jug1, jug2_capacity - jug2)),
            # Pour Jug2 -> Jug1
            (jug1 + min(jug2, jug1_capacity - jug1), jug2 - min(jug2, jug1_capacity - jug1)),
        ]

        for state in possible_states:
            dfs(state[0], state[1], path.copy())

    dfs(0, 0, [])

    if not solution_found:
        print("No solution found.")

# Example usage
jug1_capacity = 4
jug2_capacity = 3
target = 2

water_jug_dfs(jug1_capacity, jug2_capacity, target)
