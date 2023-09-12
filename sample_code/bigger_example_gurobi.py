from gurobipy import *

# Warehouse demand in thousands of units
demand = [20,30,30,45]

# Plant capacity in thousands of units
capacity = [35,40,50]


# Transportation costs per thousand units
transCosts = [[6,9,10,8],[9,5,16,14],[12,7,13,9]]

starbases = ['Farpoint','Yorktown','Earhart']
colonies = ['Triacus','New_Berlin','Strnad','Vega'] 

# Model
m = Model("facility")

# add decision variables
x = m.addVars(colonies,starbases,vtype=GRB.INTEGER,name='x')

# add constraints

m.addConstrs(
    sum(x[i,j] for i in colonies) <=  capacity[index]
    for index,j in enumerate(starbases)
)

m.addConstrs(
    sum(x[i,j] for j in starbases) >=  demand[index]
    for index,i in enumerate(colonies)
)

# set objective function
m.setObjective(
    sum(
        x[i,j]*transCosts[index_j][index_i]
        for index_i,i in enumerate(colonies)
        for index_j,j in enumerate(starbases)

    )
)

m.optimize()

