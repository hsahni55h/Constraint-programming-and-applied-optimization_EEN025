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

# constants - interest rate per annum
i_a = 0.045
i_b = 0.054
i_c = 0.051
i_d = 0.044
i_e = 0.061

# constants - period (in months)
p_a = 9.0
p_b = 15.0
p_c = 4.0
p_d = 3.0
p_e = 2.0

# constants - revenue
r_a = x1 * (pow(1 + i_a, p_a))
r_b = x2 * (pow(1 +  i_b, p_b))
r_c = x3 * (pow(1 +  i_c, p_c)) - 0.3 * (x3 * (pow(1 + i_c, p_c)))
r_d = x4 * (pow(1 +  i_d, p_d)) - 0.3 * (x4 * (pow(1 + i_d, p_d)))
r_e = x5 * (pow(1 +  i_e, p_e))

M = 1e9
M1 = 1.1e9

# set objective function
m.setObjective(r_a + r_b + r_c + r_d + r_e, GRB.MAXIMIZE)

# add constraints
m.addConstr(x1 + x2 + x3 + x4 + x5 <= 1000000000.0)
m.addConstr(x2 + x3 + x4 >= 40/100 * 1000000000.0)
m.addConstr(9*x1+15*x2+4*x3+3*x4+2*x5 <= 5*(x1+x2+x3+x4+x5))
m.addConstr(2 * x1 + 3 * x2 + x3 + 4 * x4 + 5 * x5 <= 1.5 * (x1 + x2 + x3 + x4 + x4))

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
