from gurobipy import *

# Create a new model
m = Model('CarProduction')

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

profit = [p - c for p, c in zip(price, total_production_cost)]

net_income = [p * (1 - (t / 100)) for p, t in zip(profit, tax)]

# Add integer decision variables for production quantities
x = {}
for i, plant in enumerate(plants):
    for j, model in enumerate(models):
        x[(i, j)] = m.addVar(vtype=GRB.INTEGER, name=f'x_{i}_{j}')

# Set the objective function
m.setObjective(quicksum(net_income[j] * x[(i, j)] for i in range(len(plants)) for j in range(len(models))), GRB.MAXIMIZE)

# Add constraints
c1 = m.addConstr(quicksum(x[(i, 0)] for i in range(len(plants))) <= 300000)  # Total production capacity constraint
c2 = m.addConstr(x[(0, 0)] >= 120000)  # Production constraint for Panda in Mirafiori
c3 = m.addConstr(x[(1, 1)] >= 100000)  # Production constraint for 500 in Tychy
c4 = m.addConstr(x[(2, 2)] >= 80000)   # Production constraint for Musa in Melfi
c5 = m.addConstr(x[(3, 3)] >= 15000)   # Production constraint for Giulia in Cassino

# Solve the model
m.optimize()

# Print the results
if m.status == GRB.OPTIMAL:
    for i, plant in enumerate(plants):
        for j, model in enumerate(models):
            print(f"{model} produced in {plant}: {x[(i, j)].X}")
