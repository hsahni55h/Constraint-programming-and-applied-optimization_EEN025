from z3 import *

# Warehouse demand in thousands of units
demand = [20,30,30,45]

# Plant capacity in thousands of units
capacity = [35,40,50]


# Transportation costs per thousand units
transCosts = [[6,9,10,8],[9,5,16,14],[12,7,13,9]]

starbases = ['Farpoint','Yorktown','Earhart']
colonies = ['Triacus','New_Berlin','Strnad','Vega'] 

# in z3 it is not possible to name variables using strings so we might as well just
# define some variables to enumerate starbases and colonies
num_star = len(starbases)
num_col = len(colonies)

# Model
s = Optimize()

# add decision variables
x = [[Int('x_%s_%s' % (i+1,j+1)) for j in range(num_col)] for i in range(num_star)]
Z = Int('Z')

#restrict the variables domain first (if required by the problem)
domain = [
    x[i][j] >= 0 for i in range(num_star) for j in range(num_col)
    ]

# add constraints
capacity_constraint = [
    Sum([x[i][j] for j in range(num_col)]) <=  capacity[i] 
    for i in range(num_star)
]

demand_constraint = [
    Sum([x[i][j] for i in range(num_star)]) >=  demand[j] 
    for j in range(num_col)
]

# set objective function
objective =[
    Z == Sum([
        x[i][j]*transCosts[i][j] 
        for i in range(num_star) 
        for j in range(num_col)
    ])
]

# add constraint sets to the model
s.add(domain + capacity_constraint + demand_constraint + objective)

s.minimize(Z)

s.check()

print(int(str(s.model()[Z])))

