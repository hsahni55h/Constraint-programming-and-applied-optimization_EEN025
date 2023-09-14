from gurobipy import *

# create new model
m = Model('model')

# add integer decision variables
x1 = m.addVar(vtype=GRB.CONTINUOUS, name='x1', lb=0.0, ub=1.0)
x2 = m.addVar(vtype=GRB.CONTINUOUS, name='x2', lb=0.0, ub=1.0)
x3 = m.addVar(vtype=GRB.CONTINUOUS, name='x3', lb=0.0, ub=1.0)
x4 = m.addVar(vtype=GRB.CONTINUOUS, name='x4', lb=0.0, ub=1.0)
x5 = m.addVar(vtype=GRB.CONTINUOUS, name='x5', lb=0.0, ub=1.0)

# A = m.addVar(vtype=GRB.INTEGER, name='A', lb=0, ub=1)
C = m.addVar(vtype=GRB.INTEGER, name='C', lb=0, ub=1)
D = m.addVar(vtype=GRB.INTEGER, name='D', lb=0, ub=1)
E = m.addVar(vtype=GRB.INTEGER, name='E', lb=0, ub=1)

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
m.setObjective(r_a*x1 + r_b*x2 + r_c*x3*C + r_d*x4*D + r_e*x5*E, GRB.MAXIMIZE)

# add constraints
c1 = m.addConstr(x2 + x3 + x4 >= 0.4)
c2 = m.addConstr(2*x1 + 3*x2 + x3 + 4*x4 + 5*x5 <= 7.5)          # 1.5 * 5 = 7.5
c3 = m.addConstr(9*x1 + 15*x2 + 4*x3 + 3*x4 + 2*x5 <= 300)       # 5 yr * 12 month/yr * 5 = 300

c4 = m.addConstr(C + D <= 1)                            # mutual exclusion between C and D
c5 = m.addConstr(1.0 + (x1 - (1.0/1000.0)) >= 1.0*E)    # if investment in A > 1 million (out of 1 billion) then you may (or even may not) invest in E, but its possible to invest in E if required
c6 = m.addConstr(x1 + x2 + x2 + x4 + x5 == 1.0)         # sum of all percentages must equal  to 100% i.e 1.0

# solve the model
m.optimize()

vars = m.getVars()
for var in vars:
    print(f"{var.VarName}: {var.X}")
    # print(var)
