from z3 import *
# We know each queen must be in a different row.
# So, we represent each queen by a single integer: the column position
board_size = 8

Q = [ Int('Q_%i' % (i + 1)) for i in range(board_size) ]

# Each queen is in a column {1, ... 8 }
val_c = [ And(1 <= Q[i], Q[i] <= 8) for i in range(board_size) ]

# At most one queen per column
col_c = [ Distinct(Q) ]

# Diagonal constraint
diag_c = [ 
              And(Q[i] - Q[j] != i - j, Q[i] - Q[j] != j - i)
           for i in range(board_size) for j in range(i) if i!=j ]

solve(val_c + col_c + diag_c)