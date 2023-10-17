from gurobipy import *

def main():
    # Create a new model
    m = Model("Investment")

    # Define decision variables
    x = {}
    y = {}
    investments = ["A", "B", "C", "D", "E"]
    for investment in investments:
        x[investment] = m.addVar(vtype=GRB.CONTINUOUS, name=f"x_{investment}")
        y[investment] = m.addVar(vtype=GRB.BINARY, name=f"y_{investment}")

    # Set the objective function
    c1 = x["A"] * (1 + 4.5 / 100) ** 9
    c2 = x["B"] * (1 + 5.4 / 100) ** 15
    c3 = x["C"] * (1 + 5.1 / 100) ** 4 - 0.3 * x["C"] * (1 + 5.1 / 100) ** 4
    c4 = x["D"] * (1 + 4.4 / 100) ** 3 - 0.3 * x["D"] * (1 + 4.4 / 100) ** 3
    c5 = x["E"] * (1 + 46.1 / 100) ** 2
    m.setObjective(c1 + c2 + c3 + c4 + c5, GRB.MAXIMIZE)

    # Add constraints
    m.addConstr(quicksum(x[inv] for inv in investments) <= 1e9)
    m.addConstr(quicksum(x[inv] for inv in ["B", "C", "D"]) >= 0.4 * 1e9)
    m.addConstr(9 * x["A"] + 15 * x["B"] + 4 * x["C"] + 3 * x["D"] + 2 * x["E"] <= 5 * quicksum(x[inv] for inv in investments))
    m.addConstr(2 * x["A"] + 3 * x["B"] + x["C"] + 4 * x["D"] + 5 * x["E"] <= 1.5 * quicksum(x[inv] for inv in investments))
    m.addConstr(y["C"] + y["D"] <= 1)
    M = 1e9
    m.addConstr(x["C"] <= M * y["C"])
    m.addConstr(x["D"] <= M * y["D"])
    m.addConstr(x["E"] <= M * y["E"])
    m.addConstr(x["A"] >= 1e6 * y["E"])

    # Optimize the model
    m.optimize()

    # Display results
    for investment in investments:
        print(f"Investment in {investment}: {x[investment].x}")

if __name__ == "__main__":
    main()
