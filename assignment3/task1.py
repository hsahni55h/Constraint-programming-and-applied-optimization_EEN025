from z3 import *

# Define parameters
n = 3  # Number of disks
m = 3  # Number of towers

# Create a Z3 solver
solver = Solver()

# Define variables to represent the state of the towers
towers = [[Int(f'd_{i}_{j}') for j in range(m)] for i in range(n)]

# Define variables to represent actions (moving disks)
actions = [Int(f'a_{i}_{j}_{k}') for i in range(n) for j in range(m) for k in range(m)]

# Encode Tower of Hanoi rules as constraints
for i in range(n):
    for j in range(m):
        # A disk can only be on top of a bigger disk (if present) on another tower
        if i < n - 1:
            for k in range(j + 1, m):
                solver.add(Implies(towers[i][j] != 0, And(towers[i][k] == 0, towers[i][j] < towers[i + 1][j])))
        # No disk can be placed on top of a smaller one
        if j < m - 1:
            for k in range(i + 1, n):
                solver.add(Implies(And(towers[i][j] != 0, towers[i][k] != 0), towers[i][j] < towers[i][k]))

# Define the initial state
initial_state = [Int(f'initial_state_{i}') for i in range(m)]
for i in range(m):
    solver.add(initial_state[i] == 0)  # All towers are initially empty
solver.add(towers[0] == [initial_state[i] for i in range(m)])  # Set the initial state

# Define the final state
final_state = [Int(f'final_state_{i}') for i in range(m)]
for i in range(m):
    solver.add(final_state[i] == n - 1)  # All disks are in the final tower
solver.add(towers[n - 1] == [final_state[i] for i in range(m)])  # Set the final state

# Define constraints for actions
for i in range(n):
    for j in range(m):
        for k in range(m):
            # An action is valid if and only if it corresponds to moving a disk
            solver.add(actions[i * m * m + j * m + k] ==
                       If(Or(towers[i][j] == 0, And(towers[i][j] != 0, towers[i][k] == 0, towers[i][j] < towers[i][k])),
                          1, 0))

# Set up the optimization objective
num_disks_not_in_final_state = Sum([If(towers[i][j] != final_state[j], 1, 0) for i in range(n) for j in range(m)])
solver.add(num_disks_not_in_final_state == 0)  # All disks should be in the final state

# Ensure that only one action is taken at each time step
for i in range(n):
    solver.add(Sum([actions[i * m * m + j * m + k] for j in range(m) for k in range(m)]) == 1)

# Check if the problem is solvable
if solver.check() == sat:
    model = solver.model()
    print("Solution found:")
    for i in range(n):
        for j in range(m):
            print(f"Disk {i + 1} on tower {j + 1}: {model[towers[i][j]]}")
else:
    print("No solution found")
