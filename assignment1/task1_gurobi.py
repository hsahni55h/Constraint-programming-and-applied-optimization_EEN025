from gurobipy import *

# x = Panda (Mirafori)
# y = 500 (Tychy)
# z = Musa (Melfi)
# w = Giulia (cassino)


# Create a new model
m = Model('model')

plants = ['Mirafiori', 'Tychy', 'Melfi', 'Cassino']
models = ['Panda', '500', 'Musa', 'Giulia']

tax = [30, 15, 20, 30]
price = [106000, 136000, 150000, 427000]
material_cost_percentage = [57, 60, 55, 45]
monthly_salary = [20000, 11000, 20000, 26000]
manhour = [40, 45, 38, 100]

# Calculating the material cost
material_cost = [round(p * (m / 100), 2) for p, m in zip(price, material_cost_percentage)]

# Calculating the manhour cost of production
manhour_cost = [(s / 160) * m for s, m in zip(monthly_salary, manhour)]

# Calculating the total production cost
total_production_cost = [m + h for m, h in zip(material_cost, manhour_cost)]

# Calculating the profit
profit = [p - c for p, c in zip(price, total_production_cost)]

# Calculating the net income
net_income = [p * (1 - (t / 100)) for p, t in zip(profit, tax)]
# print(net_income)

# add integer decision variables
x = m.addVar(vtype=GRB.INTEGER, name='x')
y = m.addVar(vtype=GRB.INTEGER, name='y')
z = m.addVar(vtype=GRB.INTEGER, name='z')
w = m.addVar(vtype=GRB.INTEGER, name='w')


# set objective function
m.setObjective(net_income[0]*x + net_income[1]*y + net_income[2]*z + net_income[3]*w, GRB.MAXIMIZE)

# add constraints
c1 = m.addConstr(x + z <= 300000)

c2 = m.addConstr(x >= 120000)
c3 = m.addConstr(y >= 100000)
c4 = m.addConstr(z >= 80000)
c5 = m.addConstr(w >= 15000)
c6 = m.addConstr(total_production_cost[0]*x + total_production_cost[1]*y + total_production_cost[2]*z + total_production_cost[3]*w <= 40000000000)

# solve the model
m.optimize()

# Check if the optimization was successful
if m.status == GRB.OPTIMAL:
    vars = m.getVars()
    for var in vars:
        print(f"{var.VarName}: {var.X}")
else:
    print("Optimization was not successful. Gurobi status:", m.status)




