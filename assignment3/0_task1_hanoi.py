from z3 import *

def tower_of_hanoi(ds, tws, ts):
    solver = Solver()
    
    # Define variables to represent the state of the towers.
    # tower[i][j][s] = True means there's a disk j on tower i at time-step s.
    tower = [[[Bool(f'tower_{i}_{j}_{s}') for s in range(ts)] for j in range(ds)] for i in range(tws)]
    
    # Initial configuration: All disks are on tower 0 at time-step 0.
    for j in range(ds):
        solver.add(tower[0][j][0] == True)

    # Constraint 1: If a disk is on a tower and a smaller disk is on the same tower, it cannot be moved.
    for s in range(ts - 1):
        for i in range(tws):
            for j in range(ds):
                smaller_disks = [tower[i][k][s] for k in range(j)]
                solver.add(Implies(tower[i][j][s], Not(Or(smaller_disks))))

    # Constraint 2: If we are to move a disk onto a tower with a smaller disk, it's not possible.
    for s in range(ts - 1):
        for i in range(tws):
            for j in range(ds):
                smaller_disks = [tower[i][k][s] for k in range(j)]
                solver.add(Implies(tower[i][j][s + 1], Not(Or(smaller_disks))))

    # Constraint 3: Uniqueness of 'from' variable.
    for s in range(ts):
        for j in range(ds):
            for i in range(tws):
                other_towers = [tower[k][j][s] for k in range(tws) if k != i]
                solver.add(Implies(tower[i][j][s], Not(Or(other_towers))))

    # Constraint 4: Uniqueness of 'to' variable.
    for s in range(ts):
        to_vars = [Or([tower[i][j][s] for i in range(tws)]) for j in range(ds)]
        for j in range(ds):
            solver.add(Implies(to_vars[j], And([tower[i][j][s] for i in range(tws)])))

    # Constraint 5: Uniqueness of 'obj' variable.
    for s in range(ts):
        obj_vars = [Or([tower[i][j][s] for i in range(tws)]) for j in range(ds)]
        for j in range(ds):
            solver.add(Implies(obj_vars[j], And([tower[i][j][s] for i in range(tws)])))

    # Constraint 6: Non-moving disks stay on the same tower.
    for s in range(ts - 1):
        for i in range(tws):
            for j in range(ds):
                solver.add(Implies(Not(tower[i][j][s]), tower[i][j][s + 1]))

    # Constraint 7: Distinct 'from' and 'to' variables.
    for s in range(ts - 1):
        for i in range(tws):
            for j in range(ds):
                for k in range(tws):
                    if i != k:
                        solver.add(Implies(And(tower[i][j][s], tower[i][j][s + 1]), Not(tower[k][j][s + 1])))

    # Constraint 8: Update state when moving a disk.
    for s in range(ts - 1):
        for i in range(tws):
            for j in range(ds):
                other_towers = [tower[k][j][s + 1] for k in range(tws) if k != i]
                solver.add(Implies(tower[i][j][s], Not(Or(other_towers))))

    # Constraint 9: Initial state.
    for j in range(ds):
        solver.add(tower[0][j][0] == True)
    
    # Constraint 10: Final state.
    for j in range(ds):
        solver.add(tower[tws - 1][j][ts - 1] == True)
    
	# Constraint 11: Ensure the Tower of Hanoi is solved within the maximum number of steps.
    solver.add(sum(tower[0][j][ts - 1] for j in range(ds)) == ds)

    if solver.check() == sat:
        return "Solvable"
    else:
        return "Unsolvable"

# Example usage:
number_of_disks = 3
number_of_towers = 3
max_number_of_steps = 7

print(tower_of_hanoi(number_of_disks, number_of_towers, max_number_of_steps))
