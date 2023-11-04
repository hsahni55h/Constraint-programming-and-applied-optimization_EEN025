from z3 import *

# Parameters
tws = 3  # Number of towers
ds = 3   # Number of disks
ts = 1   # Initial time step

# Create a Z3 solver
s = Solver()

# Temporary variable (not used)
temp = Int('temp')
s.add(temp == 1, temp == 2)

# Initialize on_test to store the state of towers
on_test = [[[False for _ in range(128)] for _ in range(tws)] for _ in range(ds)]

# Iterate until a solution is found
while s.check() == unsat:
    ts = ts + 1  # Increment time step
    s.reset()    # Reset the solver for new constraints

    # Define Boolean variables and arrays
    on = [[[Bool('on_%s_%s_%s' % (i, j, k)) for k in range(ts)] for j in range(tws)] for i in range(ds)]
    obj = [[Bool('obj_%s_%s' % (i, j)) for j in range(ts)] for i in range(ds)]
    start = [[Bool('start_%s_%s' % (i, j)) for j in range(ts)] for i in range(tws)]
    to = [[Bool('to_%s_%s' % (i, j)) for j in range(ts)] for i in range(tws)]

    # Constraints
    # Precondition I
    Con1 = [Implies(And(on[d][tw][t], Or([on[d2][tw][t] for d2 in range(d)])),
                    Not(obj[d][t]))
            for d in range(ds)
            for tw in range(tws)
            for t in range(ts)]

    # Precondition II
    Con2 = [Implies(And(on[d][tw][t], Or([on[d2][tw2][t] for d2 in range(d)])),
                    Not(And(obj[d][t], to[tw2][t])))
            for d in range(ds)
            for tw in range(tws)
            for tw2 in range(tws) if tw2 != tw
            for t in range(ts)]

    # Uniqueness of start variable
    Con3 = [Implies(And(on[d][tw][t], obj[d][t]),
                    And(start[tw][t], And([Not(start[tw2][t]) for tw2 in range(tws) if tw2 != tw])))
            for d in range(ds)
            for tw in range(tws)
            for t in range(ts)]

    # Uniqueness of To variable
    Con4 = [to[tw][t] ==
            And([Not(to[tw2][t]) for tw2 in range(tws) if tw2 != tw])
            for tw in range(tws)
            for t in range(ts)]

    # Uniqueness of Obj variable
    Con5 = [obj[d][t] == And([Not(obj[d2][t]) for d2 in range(ds) if d2 != d])
            for d in range(ds)
            for t in range(ts)]

    # Non-moving disks
    Con6 = [Implies(And(Not(obj[d][t]), on[d][tw][t]),
                    And(on[d][tw][t + 1], And([Not(on[d][tw2][t + 1]) for tw2 in range(tws) if tw2 != tw])))
            for d in range(ds)
            for tw in range(tws)
            for t in range(ts - 1)]

    # Distinct Start/To
    Con7 = [Implies(start[tw][t], Not(to[tw][t]))
            for tw in range(tws)
            for t in range(ts)]

    # Update
    Con8 = [Implies(And(obj[d][t], And(start[tw][t], to[tw2][t])),
                    And(on[d][tw2][t + 1], And([Not(on[d][tw3][t + 1]) for tw3 in range(tws) if tw3 != tw2])))
            for d in range(ds)
            for t in range(ts - 1)
            for tw in range(tws)
            for tw2 in range(tws) if tw2 != tw]

    # Initial/Final State
    Con9 = [And(on[d][0][0], on[d][tws - 1][ts - 1])
            for d in range(ds)]

    # Add all constraints to the solver
    s.add(Con1 + Con2 + Con3 + Con4 + Con5 + Con6 + Con7 + Con8 + Con9)

print(s.check())
if s.check() == sat:
    print('Minimum time steps needed to solve is', ts - 1)
    m = s.model()

    # Determine the actual number of time steps
    actual_ts = ts

    # Print the solution for the Tower of Hanoi with 3 discs
    print("Solution for the Tower of Hanoi with 3 discs:")
    for t in range(actual_ts):
        print(f"Time step {t}:")
        for tw in range(tws):
            print(f"Tower {tw}: [", end=" ")
            for d in range(ds):
                on_test[d][tw][t] = m[on[d][tw][t]]
                if on_test[d][tw][t]:
                    print(f"Disk {d}", end=" ")
            print("]")
else:
    print('No solution found.')
