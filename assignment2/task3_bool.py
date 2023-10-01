from z3 import *

# create new model
m = Optimize()

# add decision variables for nodes
node4W = Bool("node4W")
node4 = Bool("node4")
node1N = Bool("node1N")
node6W = Bool("node6W")
node6 = Bool("node6")

node5NW = Bool("node5NW")
node5N = Bool("node5N")
node1W = Bool("node1W")
node1 = Bool("node1")
node1E = Bool("node1E")
nodeDN = Bool("nodeDN")

nodeW = Bool("nodeW")
node5W = Bool("node5W")
node5 = Bool("node5")
node5E = Bool("node5E")
node1S = Bool("node1S")
node3N = Bool("node3N")
node3NE = Bool("node3NE")
nodeD = Bool("nodeD")

nodeBN = Bool("nodeBN")
node5S = Bool("node5S")
node2 = Bool("node2")
node2E = Bool("node2E")
node3 = Bool("node3")
node3E = Bool("node3E")

nodeB = Bool("nodeB")
nodeBE = Bool("nodeBE")
node2S = Bool("node2S")
node3S = Bool("node3S")
node3SE = Bool("node3SE")

# add decision variables for edges
edge_4W_4 = Bool("edge_4W_4")
edge_4_1N = Bool("edge_4_1N")
edge_1N_6W = Bool("edge_1N_6W")
edge_6W_6 = Bool("edge_6W_6")
edge_5NW_5N = Bool("edge_5NW_5N")
edge_5N_1W = Bool("edge_5N_1W")
edge_1W_1 = Bool("edge_1W_1")
edge_1_1E = Bool("edge_1_1E")
edge_1E_DN = Bool("edge_1E_DN")
edge_W_5W = Bool("edge_W_5W")
edge_5W_5 = Bool("edge_5W_5")
edge_5_5E = Bool("edge_5_5E")
edge_1S_3N = Bool("edge_1S_3N")
edge_3N_3NE = Bool("edge_3N_3NE")
edge_3NE_D = Bool("edge_3NE_D")
edge_BN_5S = Bool("edge_BN_5S")
edge_2_2E = Bool("edge_2_2E")
edge_3_3E = Bool("edge_3_3E")
edge_B_BE = Bool("edge_B_BE")
edge_BE_2S = Bool("edge_BE_2S")
edge_2S_3S = Bool("edge_2S_3S")
edge_3S_3SE = Bool("edge_3S_3SE")
edge_4W_5NW = Bool("edge_4W_5NW")
edge_1N_1 = Bool("edge_1N_1")
edge_6W_1E = Bool("edge_6W_1E")
edge_5NW_5W = Bool("edge_5NW_5W")
edge_5N_5 = Bool("edge_5N_5")
edge_1W_5E = Bool("edge_1W_5E")
edge_1_1S = Bool("edge_1_1S")
edge_1E_3N = Bool("edge_1E_3N")
edge_DN_3NE = Bool("edge_DN_3NE")
edge_5W_BN = Bool("edge_5W_BN")
edge_5E_2 = Bool("edge_5E_2")
edge_1S_2E = Bool("edge_1S_2E")
edge_3N_3 = Bool("edge_3N_3")
edge_3NE_3E = Bool("edge_3NE_3E")
edge_BN_B = Bool("edge_BN_B")
edge_5S_BE = Bool("edge_5S_BE")
edge_2_2S = Bool("edge_2_2S")
edge_3_3S = Bool("edge_3_3S")
edge_3E_3SE = Bool("edge_3E_3SE")

obj = Int('obj')

# add constraints

# For both source and destination nodes, only one of the neighboring edges will be part of the path.
m.add(PbEq(((edge_5W_5, 1), (edge_5_5E, 1), (edge_5N_5, 1)), 1))
m.add(PbEq(((edge_5W_5, 1), (edge_5_5E, 1), (edge_5N_5, 1)), 1))
m.add(PbEq(((edge_3N_3, 1), (edge_3_3S, 1), (edge_3_3E, 1)), 1))

# TODO: All other nodes (except the source and destination nodes) will either be (i) part of the path or (ii) not part of the path. 
def pathCheck(node:Bool, edge_list:list) -> Bool:
    return Or(And(node, PbEq(edge_list, 2)), And(Not(node), PbEq(edge_list, 0)))

# Or(And(node5W, PbEq([edge_5NW_5W, edge_W_5W, edge_5W_5, edge_5W_BN], 2)), And(Not(node5W), PbEq([edge_5NW_5W, edge_W_5W, edge_5W_5, edge_5W_BN], 0)))

m.add(pathCheck(node5W, ((edge_5NW_5W, 1), (edge_W_5W, 1), (edge_5W_5, 1), (edge_5W_BN, 1)) ))
m.add(pathCheck(node5NW, ((edge_5NW_5W, 1), (edge_5NW_5N, 1), (edge_4W_5NW, 1)) ))
m.add(pathCheck(node4W, ((edge_4W_5NW, 1), (edge_4W_4, 1)) ))
m.add(pathCheck(node4, ((edge_4W_4, 1), (edge_4_1N, 1)) ))
m.add(pathCheck(node1N, ((edge_4_1N, 1), (edge_1N_1, 1), (edge_1N_6W, 1)) ))
m.add(pathCheck(node6W, ((edge_1N_6W, 1), (edge_6W_6, 1), (edge_6W_1E, 1)) ))
m.add(pathCheck(node1E, ((edge_6W_1E, 1), (edge_1_1E, 1), (edge_1E_3N, 1), (edge_1E_DN, 1)) ))
m.add(pathCheck(nodeDN, ((edge_1E_DN, 1), (edge_DN_3NE, 1)) ))
m.add(pathCheck(node3NE, ((edge_DN_3NE, 1), (edge_3NE_D, 1), (edge_3NE_3E, 1), (edge_3N_3NE, 1)) ))
m.add(pathCheck(node3N, ((edge_3N_3NE, 1), (edge_1E_3N, 1), (edge_1S_3N, 1), (edge_3N_3, 1)) ))
m.add(pathCheck(node3, ((edge_3N_3, 1), (edge_3_3E, 1), (edge_3_3S, 1)) ))
m.add(pathCheck(node3E, ((edge_3_3E, 1), (edge_3NE_3E, 1), (edge_3E_3SE, 1)) ))
m.add(pathCheck(node3SE, ((edge_3E_3SE, 1), (edge_3S_3SE, 1)) ))
m.add(pathCheck(node3S, ((edge_3_3S, 1), (edge_3S_3SE, 1), (edge_2S_3S, 1)) ))
m.add(pathCheck(node2S, ((edge_2_2S, 1), (edge_2S_3S, 1), (edge_BE_2S, 1)) ))
m.add(pathCheck(nodeBE, ((edge_5S_BE, 1), (edge_BE_2S, 1), (edge_B_BE, 1)) ))
m.add(pathCheck(nodeB, ((edge_B_BE, 1), (edge_BN_B, 1)) ))
m.add(pathCheck(nodeBN, ((edge_BN_B, 1), (edge_5W_BN, 1), (edge_BN_5S, 1)) ))
m.add(pathCheck(node5S, ((edge_BN_5S, 1), (edge_5S_BE, 1)) ))
m.add(pathCheck(node5, ((edge_5W_5, 1), (edge_5N_5, 1), (edge_5_5E, 1)) ))
m.add(pathCheck(node5N, ((edge_5N_5, 1), (edge_5NW_5N, 1), (edge_5N_1W, 1)) ))
m.add(pathCheck(node1W, ((edge_5N_1W, 1), (edge_1W_1, 1), (edge_1W_5E, 1)) ))
m.add(pathCheck(node1, ((edge_1W_1, 1), (edge_1N_1, 1), (edge_1_1E, 1), (edge_1_1S, 1)) ))
m.add(pathCheck(node1S, ((edge_1_1S, 1), (edge_1S_3N, 1), (edge_1S_2E, 1)) ))
m.add(pathCheck(node2E, ((edge_1S_2E, 1), (edge_2_2E, 1)) ))
m.add(pathCheck(node2, ((edge_2_2E, 1), (edge_2_2S, 1), (edge_5E_2, 1)) ))
m.add(pathCheck(node5E, ((edge_5E_2, 1), (edge_5_5E, 1), (edge_1W_5E, 1)) ))

# boundary line cases
m.add(Or(And(node6, edge_6W_6), And(Not(node6), Not(edge_6W_6))))
m.add(Or(And(nodeD, edge_3NE_D), And(Not(nodeD), Not(edge_3NE_D))))
m.add(Or(And(nodeW, edge_W_5W), And(Not(nodeW), Not(edge_W_5W))))

# set objective function
m.add(obj > 0)
m.add(obj == 
      (edge_4W_4 * 21) + (edge_4_1N * 45) + (edge_1N_6W * 18) + (edge_6W_6 * 28) + (edge_5NW_5N * 21) + (edge_5N_1W * 25) + 
      (edge_1W_1 * 20) + (edge_1_1E * 18) + (edge_1E_DN * 28) + (edge_W_5W * 7) + (edge_5W_5 * 21) + (edge_5_5E * 25) + 
      (edge_1S_3N * 18) + (edge_3N_3NE * 28) + (edge_3NE_D * 8) + (edge_BN_5S * 21) + (edge_2_2E * 20) + (edge_3_3E * 28) + 
      (edge_B_BE * 21) + (edge_BE_2S * 25) + (edge_2S_3S * 38) + (edge_3S_3SE * 28) + (edge_4W_5NW * 19) + (edge_1N_1 * 19) + 
      (edge_6W_1E * 19) + (edge_5NW_5W * 17) + (edge_5N_5 * 17) + (edge_1W_5E * 17) + (edge_1_1S * 17) + (edge_1E_3N * 17) + 
      (edge_DN_3NE * 17) + (edge_5W_BN * 17) + (edge_5E_2 * 17) + (edge_1S_2E * 17) + (edge_3N_3 * 17) + (edge_3NE_3E * 17) + 
      (edge_BN_B * 17) + (edge_5S_BE * 17) + (edge_2_2S * 17) + (edge_3_3S * 17) + (edge_3E_3SE * 17))

m.minimize(obj)

# solve the model
m.check()
print(m.model())

