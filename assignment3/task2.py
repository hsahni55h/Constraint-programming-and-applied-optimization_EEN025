from z3 import *

def sort_bricks_case1(n_bricks, n_slots, init, goal):
    ts = 1

    while True:
        s = Solver()
        bricks = range(n_bricks)
        slots = range(n_slots)
        timesteps = range(ts)

        on = [[[Bool(f'on_{b}_{s}_{t}') for t in timesteps] for s in slots] for b in bricks]
        obj = [[Bool(f'obj_{b}_{t}') for t in timesteps] for b in bricks]
        to = [[Bool(f'to_{s}_{t}') for t in timesteps] for s in slots]
        start = [[Bool(f'start_{s}_{t}') for t in timesteps] for s in slots]

        Con1 = [Implies(And(on[b][s][t], obj[b][t]),
                        And(start[s][t], And([Not(start[s2][t]) for s2 in slots if s2 != s])))
                for b in bricks
                for s in slots
                for t in timesteps]

        Con2 = [to[s][t] ==
                And([Not(to[s2][t]) for s2 in slots if s2 != s])
                for s in slots
                for t in timesteps]

        Con3 = [obj[b][t] == And([Not(obj[b2][t]) for b2 in bricks if b2 != b])
                for b in bricks
                for t in timesteps]

        Con4 = [Implies(And(Not(obj[b][t]), on[b][s][t]),
                        And(on[b][s][t + 1], And([Not(on[b][s2][t + 1]) for s2 in slots if s2 != s])))
                for b in bricks
                for s in slots
                for t in range(ts - 1)]

        Con5 = [Implies(start[s][t], Not(to[s][t]))
                for s in slots
                for t in timesteps]

        Con6 = [Implies(And(obj[b][t], And(start[s][t], to[s2][t])),
                        And(on[b][s2][t + 1], And([Not(on[b][s3][t + 1]) for s3 in slots if s3 != s2])))
                for b in bricks
                for t in range(ts - 1)
                for s in slots
                for s2 in slots if s2 != s]

        Con7 = [And(on[b][init[b] - 1][0], on[b][goal[b] - 1][ts - 1])
                for b in bricks]

        s.add(Con1 + Con2 + Con3 + Con4 + Con5 + Con6 + Con7)

        if s.check() == sat:
            m = s.model()
            print("Current position:")
            for t in timesteps:
                for s in slots:
                    for b in bricks:
                        print(m[on[b][s][t]], end=" ")
                    print("Slot")
                print("Time step - %s" % t)
            break
        else:
            ts += 1

    return [ts - 1, m]

# Parameters
bricks = 3
slots = 5
init = [1, 2, 3]
goal = [4, 5, 1]

[ts1, m1] = sort_bricks_case1(bricks, slots, init, goal)
print('Time steps needed to sort bricks in case 1 is {}'.format(ts1))
