from gurobipy import *

# create new model
m = Model('model')

# add decision variables
x = m.addVar(vtype = GRB.BINARY, name = 'x')
y = m.addVar(vtype = GRB.BINARY, name = 'y')
z = m.addVar(vtype = GRB.BINARY, name = 'z')

# set objective function
m.setObjective(x + y + 2*z, GRB.MAXIMIZE)

# add constraints
c1 = m.addConstr(x + 2*y + 3*z <= 4)
c2 = m.addConstr(x + y >= 1)

# solve the model
m.optimize()

vars = m.getVars()
for i in vars:
    print(i)
