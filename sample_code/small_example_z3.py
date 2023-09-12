from z3 import *

# create new model
s = Optimize()

# add decision variables
x = Int('x')
y = Int('y')
z = Int('z')

obj = Int('obj')

# add constraints
s.add(x + 2*y + 3*z <= 4)
s.add(x + y >= 1)

s.add(x<=1,y<=1,z<=1)

# set objective function
s.add(obj == x + y + 2*z)

s.maximize(obj)

# solve the model
s.check()
print(s.model())

