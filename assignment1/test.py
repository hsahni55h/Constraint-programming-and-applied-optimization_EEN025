
from gurobipy import *
m = Model("Investment")
xA  = m.addVar(vtype=GRB.CONTINUOUS, name ="x_A")
xB  = m.addVar(vtype=GRB.CONTINUOUS, name ="x_B")
xC  = m.addVar(vtype=GRB.CONTINUOUS, name ="x_C")
xD  = m.addVar(vtype=GRB.CONTINUOUS, name ="x_D")
xE  = m.addVar(vtype=GRB.CONTINUOUS, name ="x_E")
y_C = m.addVar(vtype=GRB.BINARY, name="y_C")
y_D = m.addVar(vtype=GRB.BINARY, name="y_D")
y_E = m.addVar(vtype=GRB.BINARY, name="y_E")
c1 = xA * (pow(1 + 4.5 / 100, 9))
c2 = xB * (pow(1 + 5.4 / 100, 15))
c3 = xC * (pow(1 + 5.1 / 100, 4)) - 0.3 * (xC * (pow(1 + 5.1 / 100, 4)))
c4 = xD * (pow(1 + 4.4 / 100, 3)) - 0.3 * (xD * (pow(1 + 4.4 / 100, 3)))
c5 = xE * (pow(1 + 46.1 / 100, 2))
M = 1e9
M1 = 1.1e9
m.setObjective(c1 + c2 + c3 + c4 + c5, GRB.MAXIMIZE)
m.addConstr(xA + xB + xC + xD + xE <= 1000000000.0)
m.addConstr(xB + xC + xD >= 40/100 * 1000000000.0)
m.addConstr(9*xA+15*xB+4*xC+3*xD+2*xE <= 5*(xA+xB+xC+xD+xE))
m.addConstr(2 * xA + 3 * xB + xC + 4 * xD + 5 * xE <= 1.5 * (xA + xB + xC + xD + xE))
m.addConstr(y_C + y_D <= 1)
m.addConstr(xC <= M * y_C)
m.addConstr(xD <= M * y_D)
m.addConstr(xE <= M * y_E)
m.addConstr(xA >= 1e6 * y_E)




m.optimize()
print("investment in A:", xA.x)
print("investment in B:", xB.x)
print("investment in C:", xC.x)
print("investment in D:", xD.x)
print("investment in E:", xE.x)