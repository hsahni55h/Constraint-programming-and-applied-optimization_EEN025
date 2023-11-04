from z3 import *


def sort_bricks_case1(n_bricks, n_slots, init, goal):
    ts = 1

    # Create model
    s = Solver()
    solved = False

    while not solved:
        s.reset()

        bricks = range(n_bricks)
        slots = range(n_slots)
        timesteps = range(ts)

        # Decision variables
        on = [[[Bool('on_%s_%s_%s' % (i, j, k)) for k in timesteps] for j in slots] for i in bricks]
        obj = [[Bool('obj_%s_%s' % (i, j)) for j in timesteps] for i in bricks]
        to = [[Bool('to_%s_%s' % (i, j)) for j in timesteps] for i in slots]
        start = [[Bool('start_%s_%s' % (i, j)) for j in timesteps] for i in slots]

        # Constraints
        # Uniqueness of start variable
        Con1 = [Implies(And(on[b][s][t], obj[b][t]),
                        And(start[s][t], And([Not(start[s2][t]) for s2 in slots if s2 != s])))
                for b in bricks
                for s in slots
                for t in timesteps]

        # print(Con3)

        # Uniqueness of To variable
        Con2 = [to[s][t] ==
                And([Not(to[s2][t]) for s2 in slots if s2 != s])
                for s in slots
                for t in timesteps]

        # print(Con4)

        # Uniqueness of Obj variable
        Con3 = [obj[b][t] == And([Not(obj[b2][t]) for b2 in bricks if b2 != b])
                for b in bricks
                for t in timesteps]

        # print(Con5)

        # Non-moving disks
        Con4 = [Implies(And(Not(obj[b][t]), on[b][s][t]),
                        And(on[b][s][t + 1], And([Not(on[b][s2][t + 1]) for s2 in slots if s2 != s])))
                for b in bricks
                for s in slots
                for t in range(ts - 1)]

        # print(Con6)

        # Distinct Start/ To
        Con5 = [Implies(start[s][t], Not(to[s][t]))
                for s in slots
                for t in timesteps]

        # print(Con7)

        # Update
        Con6 = [Implies(And(obj[b][t], And(start[s][t], to[s2][t])),
                        And(on[b][s2][t + 1], And([Not(on[b][s3][t + 1]) for s3 in slots if s3 != s2])))
                for b in bricks
                for t in range(ts - 1)
                for s in slots
                for s2 in slots if s2 != s]

        # print(Con8)

        # Initial/ Final State
        Con7 = [And(on[b][init[b] - 1][0], on[b][goal[b] - 1][ts - 1])
                for b in bricks]

        # Con8 = [And(on[b][init[b] - 1][0])
        #         for b in bricks]

        s.add(Con1 + Con2 + Con3 + Con4 + Con5 + Con6 + Con7)

        if s.check() == sat:
            solved = True
            m = s.model()
            # Print statements to check for 3 discs scenario
            # on_test = [[[i for i in range(ts1)] for j in range(slots)] for k in range(bricks)]
            print("Current position:")
            for t in timesteps:
                for s in slots:
                    for b in bricks:
                        # on_test[b][s][t] = m[on[b][s][t]]
                        print(m[on[b][s][t]], end=" ")
                    print("Slot")
                print("Time step - %s" % t)

            # print(m[on[0][0][0]])
        else:
            ts = ts + 1

    return [ts - 1, m]


# Parameters
bricks = 3
slots = 5
init = [1, 2, 3]
goal = [4, 5, 1]

[ts1, m1] = sort_bricks_case1(bricks, slots, init, goal)
print('Time steps needed to sort bricks in case 1 is {}'.format(ts1))
