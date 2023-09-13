from gurobipy import *

# create new model
m = Model('model')

# add integer decision variables

# export tax
E = 0.0025          

#Price
S = [[86, 92, 100, 0],        
     [106, 136, 150, 427], 
     [150, 170, 0, 550], 
     [112, 150, 170, 500]]

# Tax
T = [[0.3, 0.15, 0.2, 0.3], 
     [0.3, 0.15, 0.2, 0.3], 
     [0.3+E, 0.15+E, 0.2+E, 0.3+E], 
     [0.3, 0.15, 0.2, 0.3]]

# material cost
M = [0.57, 0.60, 0.55, 0.45]  

# salary
P = [20, 11, 20, 26]     

# delivery cost
D = [[0.8, 0, 12, 0], 
     [0, 1, 0, 0], 
     [3.5, 2.8, 0, 5], 
     [2, 1.6, 2.2, 2.5]]

# manhour
H = [40, 45, 38, 100] 

# demand
q_min = [[75, 20, 10, 0], 
         [35, 40, 80, 8], 
         [40, 50, 0, 3], 
         [2, 5, 1, 1]]


q = [[0, 0, 0, 0], 
     [0, 0, 0, 0], 
     [0, 0, 0, 0], 
     [0, 0, 0, 0]]


C = [[0, 0, 0, 0], 
     [0, 0, 0, 0], 
     [0, 0, 0, 0], 
     [0, 0, 0, 0]]


constraint = [[0, 0, 0, 0], 
     [0, 0, 0, 0], 
     [0, 0, 0, 0], 
     [0, 0, 0, 0]]
z = 0
C_sum = 0

for n in range(4):
    for v in range(4):
        q[n][v] = m.addVar(vtype=GRB.INTEGER, name=f'q{n+1}{v+1}', lb = q_min[n][v])
        C[n][v] = (M[v] + (P[v] / 160) * H[n] + D[n][v]) * q[n][v]
        z += (S[n][v] - C[n][v])*(1 - T[n][v])
        
        C_sum += C[n][v]

# set objective function
m.setObjective(z, GRB.MAXIMIZE)

# add constraints
constraint[n][v] = m.addConstr(C_sum <= 4*1000*1000)

# solve the model
m.optimize()

vars = m.getVars()
for var in vars:
    print(f"{var.VarName}: {var.X}")
