from gurobipy import *

# create new model
m = Model('model')

# add integer decision variables
a = m.addVar(vtype=GRB.INTEGER, name='a', lb=0)
b = m.addVar(vtype=GRB.INTEGER, name='b', lb=0)
c = m.addVar(vtype=GRB.INTEGER, name='c', lb=0)
d = m.addVar(vtype=GRB.INTEGER, name='d', lb=0)
e = m.addVar(vtype=GRB.INTEGER, name='e', lb=0)
f = m.addVar(vtype=GRB.INTEGER, name='f', lb=0)
u = m.addVar(vtype=GRB.INTEGER, name='u', lb=0)
v = m.addVar(vtype=GRB.INTEGER, name='v', lb=0)
w = m.addVar(vtype=GRB.INTEGER, name='w', lb=0)
x = m.addVar(vtype=GRB.INTEGER, name='x', lb=0)
y = m.addVar(vtype=GRB.INTEGER, name='y', lb=0)
z = m.addVar(vtype=GRB.INTEGER, name='z', lb=0)

# set objective function
m.setObjective(10*a + 15*b + 5*c + 15*d + 10*e + 5*f + 20*u + 5*v + 10*w + 10*x + 15*y + 20*z, GRB.MAXIMIZE)

# add constraints
c1 = m.addConstr(a + b + c <= 100)
c2 = m.addConstr(d + e + f <= 150)
c3 = m.addConstr(u + v + w <= 80)
c4 = m.addConstr(x + y + z <= 200)
c5 = m.addConstr(10*a + 15*d + 20*u + 10*x >= 0)
c6 = m.addConstr(15*b + 10*e + 5*v + 15*y >= 0)
c7 = m.addConstr(5*c + 5*f + 10*w + 20*z >= 0)

c8 = m.addConstr(10*a + 15*d + 20*u + 10*x - 15*b - 10*e - 5*v - 15*y == 0)
c9 = m.addConstr(10*a + 15*d + 20*u + 10*x - 5*c - 5*f - 10*w - 20*z == 0)

# Additional constraints for a >= 0, b >= 0, c >= 0, etc.
# c10 = m.addConstr(a >= 0)
# c11 = m.addConstr(b >= 0)
# c12 = m.addConstr(c >= 0)
# c13 = m.addConstr(d >= 0)
# c14 = m.addConstr(e >= 0)
# c15 = m.addConstr(f >= 0)
# c16 = m.addConstr(u >= 0)
# c17 = m.addConstr(v >= 0)
# c18 = m.addConstr(w >= 0)
# c19 = m.addConstr(x >= 0)
# c20 = m.addConstr(y >= 0)
# c21 = m.addConstr(z >= 0)

# solve the model
m.optimize()

vars = m.getVars()
for var in vars:
    print(f"{var.VarName}: {var.X}")
