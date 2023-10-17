from gurobipy import *

# create new model
m = Model('model')

# add integer decision variables
x1 = m.addVar(vtype=GRB.CONTINUOUS, name='x1')
x2 = m.addVar(vtype=GRB.CONTINUOUS, name='x2')
x3 = m.addVar(vtype=GRB.CONTINUOUS, name='x3')
x4 = m.addVar(vtype=GRB.CONTINUOUS, name='x4')
x5 = m.addVar(vtype=GRB.CONTINUOUS, name='x5')

C = m.addVar(vtype=GRB.BINARY, name='C')
D = m.addVar(vtype=GRB.BINARY, name='D')
E = m.addVar(vtype=GRB.BINARY, name='E')

r_a = x1 * (pow(1 + 4.5 / 100, 9))
r_b = x2 * (pow(1 + 5.4 / 100, 15))
r_c = x3 * (pow(1 + 5.1 / 100, 4)) - 0.3 * (x3 * (pow(1 + 5.1 / 100, 4)))
r_d = x4 * (pow(1 + 4.4 / 100, 3)) - 0.3 * (x4 * (pow(1 + 4.4 / 100, 3)))
r_e = x5 * (pow(1 + 46.1 / 100, 2))

M = 1e9
M1 = 1.1e9

# set objective function
m.setObjective(r_a + r_b + r_c + r_d + r_e, GRB.MAXIMIZE)

# add constraints
m.addConstr(x1 + x2 + x3 + x4 + x5 <= 1000000000.0)
m.addConstr(x2 + x3 + x4 >= 40/100 * 1000000000.0)
m.addConstr(9 * x1 + 15 * x2 + 4 * x3 + 3 * x4 + 2 * x5 <= 5 * (x1 + x2 + x3 + x4 + x5))
m.addConstr(2 * x1 + 3 * x2 + x3 + 4 * x4 + 5 * x5 <= 1.5 * (x1 + x2 + x3 + x4 + x5))

m.addConstr(C + D <= 1)
m.addConstr(x3 <= M * C)
m.addConstr(x4 <= M * D)
m.addConstr(x5 <= M * E)
m.addConstr(x1 >= 1e6 * E)

# solve the model
m.optimize()
print("investment in A:", x1.x)
print("investment in B:", x2.x)
print("investment in C:", x3.x)
print("investment in D:", x4.x)
print("investment in E:", x5.x)
