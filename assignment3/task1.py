from z3 import *

# Define parameters
n = 3  # Number of disks
m = 3  # Number of towers
t = Int('t')  # Number of steps to minimize

# Define variables to represent the state of the towers
towers = [[Int(f'd_{i}_{j}') for j in range(m)] for i in range(n)]

# Define initial and final states
initial_state = [list(range(n, 0, -1))] + [[] for _ in range(m - 1)]
final_state = [[] for _ in range(m - 1)] + [list(range(n, 0, -1))]

# Create a Z3 solver
solver = Solver()

# Encode Tower of Hanoi rules as constraints
for i in range(n):
    for j in range(m):
        # A disk can only be on top of a bigger disk (if present) on another tower
        if i < n - 1:
            for k in range(j + 1, m):
                solver.add(Implies(towers[i][j] != 0, And(towers[i][k] == 0, towers[i][j] < towers[i + 1][j]))
        # No disk can be placed on top of a smaller one
        if j < m - 1:
            for k in range(i + 1, n):
                solver.add(Implies(And(towers[i][j] != 0, towers[i][k] != 0), towers[i][j] < towers[i][k]))

# Set up the optimization objective
moves = Sum([If(towers[i][j] != final_state[i][j], 1, 0) for i in range(n) for j in range(m)])
solver.add(t == moves)

# Check if the problem is solvable
if solver.check() == sat:
    model = solver.model()
    num_steps = model[t].as_long()
    print(f"Minimum number of steps: {num_steps}")
    # Extract the sequence of moves to achieve the solution
    for i in range(n):
        for j in range(m):
            if model[towers[i][j]].as_long() != final_state[i][j]:
                disk = model[towers[i][j]].as_long()
                src_tower = j
                dest_tower = final_state[i].index(disk)
                print(f"Move disk {disk} from tower {src_tower} to tower {dest_tower}")
else:
    print("No solution found")
