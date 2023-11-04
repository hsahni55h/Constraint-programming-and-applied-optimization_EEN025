from z3 import *
import time

# Parameters
tws = 3
ds = 3
# includes the initial time in which all discs are in the first tower
ts = 1
# 3 discs - 8 time steps
# 4 discs - 16 ts
# 5 discs - 32 ts
# 6 discs - 64 ts
# 7 discs - 128 ts
# Alternative 7 discs in 127 time steps

# Create model
s = Solver()

temp = Int('temp')

s.add(temp == 1, temp == 2)

while s.check() == unsat:
    ts = ts + 1

    s.reset()

    on = [[[Bool('on_%s_%s_%s' % (i, j, k)) for k in range(ts)] for j in range(tws)] for i in range(ds)]
    # pp(on)
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

    # print(Con1)

    # Precondition II
    Con2 = [Implies(And(on[d][tw][t], Or([on[d2][tw2][t] for d2 in range(d)])),
                    Not(And(obj[d][t], to[tw2][t])))
            for d in range(ds)
            for tw in range(tws)
            for tw2 in range(tws) if tw2 != tw
            for t in range(ts)]

    # print(Con2)

    # Uniqueness of start variable
    Con3 = [Implies(And(on[d][tw][t], obj[d][t]),
                    And(start[tw][t], And([Not(start[tw2][t]) for tw2 in range(tws) if tw2 != tw])))
            for d in range(ds)
            for tw in range(tws)
            for t in range(ts)]

    # print(Con3)

    # Uniqueness of To variable
    Con4 = [to[tw][t] ==
            And([Not(to[tw2][t]) for tw2 in range(tws) if tw2 != tw])
            for tw in range(tws)
            for t in range(ts)]

    # print(Con4)

    # Uniqueness of Obj variable
    Con5 = [obj[d][t] == And([Not(obj[d2][t]) for d2 in range(ds) if d2 != d])
            for d in range(ds)
            for t in range(ts)]

    # print(Con5)

    # Non-moving disks
    Con6 = [Implies(And(Not(obj[d][t]), on[d][tw][t]),
                    And(on[d][tw][t + 1], And([Not(on[d][tw2][t + 1]) for tw2 in range(tws) if tw2 != tw])))
            for d in range(ds)
            for tw in range(tws)
            for t in range(ts - 1)]

    # print(Con6)

    # Distinct Start/ To
    Con7 = [Implies(start[tw][t], Not(to[tw][t]))
            for tw in range(tws)
            for t in range(ts)]

    # print(Con7)

    # Update
    Con8 = [Implies(And(obj[d][t], And(start[tw][t], to[tw2][t])),
                    And(on[d][tw2][t + 1], And([Not(on[d][tw3][t + 1]) for tw3 in range(tws) if tw3 != tw2])))
            for d in range(ds)
            for t in range(ts - 1)
            for tw in range(tws)
            for tw2 in range(tws) if tw2 != tw]

    # print(Con8)

    # Initial/ Final State
    Con9 = [And(on[d][0][0], on[d][tws - 1][ts - 1])
            for d in range(ds)]

    # print(Con9)

    s.add(Con1 + Con2 + Con3 + Con4 + Con5 + Con6 + Con7 + Con8 + Con9)
    # start_time = time.time()
    print(ts-1)
    # end_time = time.time()
    # duration = end_time - start_time

print(s.check())
print('Minimum time steps needed to solve is', ts-1)
m = s.model()
# Print statements to check for 3 discs scenario
on_test = [[[i for i in range(ts)] for j in range(tws)] for k in range(ds)]
print("Current position:")
for t in range(ts):
    for tw in range(tws):
        for d in range(ds):
            on_test[d][tw][t] = m[on[d][tw][t]]
            print(on_test[d][tw][t], end=" ")
        print("Tower")
    print("Time step - %s" % t)
#
# print("Moving")
# obj_result = [[i for i in range(ts)] for j in range(ds)]
# for d in range(ds):
#     for t in range(ts):
#         obj_result[d][t] = m[obj[d][t]]
#         print(obj_result[d][t], end=" ")
#     print("Disc")
#
# print("Starting from")
# start_result = [[i for i in range(ts)] for j in range(tws)]
# for tw in range(tws):
#     for t in range(ts):
#         start_result[tw][t] = m[start[tw][t]]
#         print(start_result[tw][t], end=" ")
#     print('Tower')
#
# print("Going to")
# to_result = [[i for i in range(ts)] for j in range(tws)]
# for tw in range(tws):
#     for t in range(ts):
#         to_result[tw][t] = m[to[tw][t]]
#         print(to_result[tw][t], end=" ")
#     print('Tower')
#
# print(on_test)
