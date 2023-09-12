from z3 import *

# create new model
s= Optimize()

#add decision varibles
x,y,z = Ints('x y z')
obj = Int('obj')
b = Bool('b')

# s.add(x<100,y<100,z<100,)

s.add(obj == x + y + z)
s.add(If(b,x>10,x<10))
s.add(Implies(y>10,z<0))

s.maximize(obj)
s.check()
print(s.model())
