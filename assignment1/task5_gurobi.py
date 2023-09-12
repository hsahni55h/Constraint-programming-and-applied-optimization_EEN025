from gurobipy import *

# create new model
m = Model('model')

# add integer decision variables
a = m.addVar(vtype=GRB.CONTINUOUS, name='a', lb=0.0, ub=1.0)
b = m.addVar(vtype=GRB.CONTINUOUS, name='b', lb=0.0, ub=1.0)
c = m.addVar(vtype=GRB.CONTINUOUS, name='c', lb=0.0, ub=1.0)
d = m.addVar(vtype=GRB.CONTINUOUS, name='d', lb=0.0, ub=1.0)
e = m.addVar(vtype=GRB.CONTINUOUS, name='e', lb=0.0, ub=1.0)

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
r_a = (1 + p_a * i_a / 12.0)
r_b = (1 + p_b * i_b / 12.0)
r_c = (1 + p_c * i_c * 0.7 / 12.0)
r_d = (1 + p_d * i_d * 0.7 / 12.0)
r_e = (1 + p_e * i_e / 12.0)

# set objective function
m.setObjective(r_a*a + r_b*b + r_c*c + r_d*d + r_e*e, GRB.MAXIMIZE)

# add constraints
c1 = m.addConstr(b + c + d >= 0.4)
c2 = m.addConstr(2*a + 3*b + c + 4*d + 5*e <= 7.5)          # 1.5 * 5 = 7.5
c3 = m.addConstr(9*a + 15*b + 4*c + 3*d + 2*e <= 300)       # 5 yr * 12 month/yr * 5 = 300

# c4 = m.addConstr()
# c5 = m.addConstr(a >= (1.0/1000.0)+0.0001)  # 0.0001 is added to introduce equality sign
c6 = m.addConstr(a + b + c + d + e == 1.0)

# solve the model
m.optimize()

vars = m.getVars()
for var in vars:
    # print(f"{var.VarName}: {var.X}")
    print(var)
