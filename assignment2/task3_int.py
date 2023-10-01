from z3 import *

def IntNot(x:Int):
    return (1 - x)

# create new model
m = Optimize()

# add decision variables for nodes
node4W = Int("node4W")
node4 = Int("node4")
node1N = Int("node1N")
node6W = Int("node6W")
node6 = Int("node6")

node5NW = Int("node5NW")
node5N = Int("node5N")
node1W = Int("node1W")
node1 = Int("node1")
node1E = Int("node1E")
nodeDN = Int("nodeDN")

nodeW = Int("nodeW")
node5W = Int("node5W")
node5 = Int("node5")
node5E = Int("node5E")
node1S = Int("node1S")
node3N = Int("node3N")
node3NE = Int("node3NE")
nodeD = Int("nodeD")

nodeBN = Int("nodeBN")
node5S = Int("node5S")
node2 = Int("node2")
node2E = Int("node2E")
node3 = Int("node3")
node3E = Int("node3E")

nodeB = Int("nodeB")
nodeBE = Int("nodeBE")
node2S = Int("node2S")
node3S = Int("node3S")
node3SE = Int("node3SE")

# add decision variables for edges
edge_4W_4 = Int("edge_4W_4")
edge_4_1N = Int("edge_4_1N")
edge_1N_6W = Int("edge_1N_6W")
edge_6W_6 = Int("edge_6W_6")
edge_5NW_5N = Int("edge_5NW_5N")
edge_5N_1W = Int("edge_5N_1W")
edge_1W_1 = Int("edge_1W_1")
edge_1_1E = Int("edge_1_1E")
edge_1E_DN = Int("edge_1E_DN")
edge_W_5W = Int("edge_W_5W")
edge_5W_5 = Int("edge_5W_5")
edge_5_5E = Int("edge_5_5E")
edge_1S_3N = Int("edge_1S_3N")
edge_3N_3NE = Int("edge_3N_3NE")
edge_3NE_D = Int("edge_3NE_D")
edge_BN_5S = Int("edge_BN_5S")
edge_2_2E = Int("edge_2_2E")
edge_3_3E = Int("edge_3_3E")
edge_B_BE = Int("edge_B_BE")
edge_BE_2S = Int("edge_BE_2S")
edge_2S_3S = Int("edge_2S_3S")
edge_3S_3SE = Int("edge_3S_3SE")
edge_4W_5NW = Int("edge_4W_5NW")
edge_1N_1 = Int("edge_1N_1")
edge_6W_1E = Int("edge_6W_1E")
edge_5NW_5W = Int("edge_5NW_5W")
edge_5N_5 = Int("edge_5N_5")
edge_1W_5E = Int("edge_1W_5E")
edge_1_1S = Int("edge_1_1S")
edge_1E_3N = Int("edge_1E_3N")
edge_DN_3NE = Int("edge_DN_3NE")
edge_5W_BN = Int("edge_5W_BN")
edge_5E_2 = Int("edge_5E_2")
edge_1S_2E = Int("edge_1S_2E")
edge_3N_3 = Int("edge_3N_3")
edge_3NE_3E = Int("edge_3NE_3E")
edge_BN_B = Int("edge_BN_B")
edge_5S_BE = Int("edge_5S_BE")
edge_2_2S = Int("edge_2_2S")
edge_3_3S = Int("edge_3_3S")
edge_3E_3SE = Int("edge_3E_3SE")

obj = Int('obj')

# add constraints

# treat all decision variables related to node and edges as boolean
m.add(
    node4W >= 0, node4W <= 1,
    node4 >= 0, node4 <= 1,
    node1N >= 0, node1N <= 1,
    node6W >= 0, node6W <= 1,
    node6 >= 0, node6 <= 1,
    node5NW >= 0, node5NW <= 1,
    node5N >= 0, node5N <= 1,
    node1W >= 0, node1W <= 1,
    node1 >= 0, node1 <= 1,
    node1E >= 0, node1E <= 1,
    nodeDN >= 0, nodeDN <= 1,
    nodeW >= 0, nodeW <= 1,
    node5W >= 0, node5W <= 1,
    node5 >= 0, node5 <= 1,
    node5E >= 0, node5E <= 1,
    node1S >= 0, node1S <= 1,
    node3N >= 0, node3N <= 1,
    node3NE >= 0, node3NE <= 1,
    nodeD >= 0, nodeD <= 1,
    nodeBN >= 0, nodeBN <= 1,
    node5S >= 0, node5S <= 1,
    node2 >= 0, node2 <= 1,
    node2E >= 0, node2E <= 1,
    node3 >= 0, node3 <= 1,
    node3E >= 0, node3E <= 1,
    nodeB >= 0, nodeB <= 1,
    nodeBE >= 0, nodeBE <= 1,
    node2S >= 0, node2S <= 1,
    node3S >= 0, node3S <= 1,
    node3SE >= 0, node3SE <= 1,
    edge_4W_4 >= 0, edge_4W_4 <= 1,
    edge_4_1N >= 0, edge_4_1N <= 1,
    edge_1N_6W >= 0, edge_1N_6W <= 1,
    edge_6W_6 >= 0, edge_6W_6 <= 1,
    edge_5NW_5N >= 0, edge_5NW_5N <= 1,
    edge_5N_1W >= 0, edge_5N_1W <= 1,
    edge_1W_1 >= 0, edge_1W_1 <= 1,
    edge_1_1E >= 0, edge_1_1E <= 1,
    edge_1E_DN >= 0, edge_1E_DN <= 1,
    edge_W_5W >= 0, edge_W_5W <= 1,
    edge_5W_5 >= 0, edge_5W_5 <= 1,
    edge_5_5E >= 0, edge_5_5E <= 1,
    edge_1S_3N >= 0, edge_1S_3N <= 1,
    edge_3N_3NE >= 0, edge_3N_3NE <= 1,
    edge_3NE_D >= 0, edge_3NE_D <= 1,
    edge_BN_5S >= 0, edge_BN_5S <= 1,
    edge_2_2E >= 0, edge_2_2E <= 1,
    edge_3_3E >= 0, edge_3_3E <= 1,
    edge_B_BE >= 0, edge_B_BE <= 1,
    edge_BE_2S >= 0, edge_BE_2S <= 1,
    edge_2S_3S >= 0, edge_2S_3S <= 1,
    edge_3S_3SE >= 0, edge_3S_3SE <= 1,
    edge_4W_5NW >= 0, edge_4W_5NW <= 1,
    edge_1N_1 >= 0, edge_1N_1 <= 1,
    edge_6W_1E >= 0, edge_6W_1E <= 1,
    edge_5NW_5W >= 0, edge_5NW_5W <= 1,
    edge_5N_5 >= 0, edge_5N_5 <= 1,
    edge_1W_5E >= 0, edge_1W_5E <= 1,
    edge_1_1S >= 0, edge_1_1S <= 1,
    edge_1E_3N >= 0, edge_1E_3N <= 1,
    edge_DN_3NE >= 0, edge_DN_3NE <= 1,
    edge_5W_BN >= 0, edge_5W_BN <= 1,
    edge_5E_2 >= 0, edge_5E_2 <= 1,
    edge_1S_2E >= 0, edge_1S_2E <= 1,
    edge_3N_3 >= 0, edge_3N_3 <= 1,
    edge_3NE_3E >= 0, edge_3NE_3E <= 1,
    edge_BN_B >= 0, edge_BN_B <= 1,
    edge_5S_BE >= 0, edge_5S_BE <= 1,
    edge_2_2S >= 0, edge_2_2S <= 1,
    edge_3_3S >= 0, edge_3_3S <= 1,
    edge_3E_3SE >= 0, edge_3E_3SE <= 1)

# m.add(x + 2*y + 3*z <= 4)
# m.add(x + y >= 1)
# m.add(x<=1,y<=1,z<=1)


# For both source and destination nodes, only one of the neighboring edges will be part of the path.
m.add(edge_5W_5 + edge_5_5E + edge_5N_5 == 1)
m.add(edge_3N_3 + edge_3_3S + edge_3_3E == 1)

# TODO: All other nodes (except the source and destination nodes) will either be (i) part of the path or (ii) not part of the path. 
def pathCheck(node:Int, edge_list:list) -> Int:
    return 2*IntNot(node) + sum(edge_list)

m.add(pathCheck(node5W, [edge_5NW_5W, edge_W_5W, edge_5W_5, edge_5W_BN]) == 2)
m.add(pathCheck(node5NW, [edge_5NW_5W, edge_5NW_5N, edge_4W_5NW]) == 2)
m.add(pathCheck(node4W, [edge_4W_5NW, edge_4W_4]) == 2)
m.add(pathCheck(node4, [edge_4W_4, edge_4_1N]) == 2)
m.add(pathCheck(node1N, [edge_4_1N, edge_1N_1, edge_1N_6W]) == 2)
m.add(pathCheck(node6W, [edge_1N_6W, edge_6W_6, edge_6W_1E]) == 2)
m.add(pathCheck(node1E, [edge_6W_1E, edge_1_1E, edge_1E_3N, edge_1E_DN]) == 2)
m.add(pathCheck(nodeDN, [edge_1E_DN, edge_DN_3NE]) == 2)
m.add(pathCheck(node3NE, [edge_DN_3NE, edge_3NE_D, edge_3NE_3E, edge_3N_3NE]) == 2)
m.add(pathCheck(node3N, [edge_3N_3NE, edge_1E_3N, edge_1S_3N, edge_3N_3]) == 2)
m.add(pathCheck(node3, [edge_3N_3, edge_3_3E, edge_3_3S]) == 2)
m.add(pathCheck(node3E, [edge_3_3E, edge_3NE_3E, edge_3E_3SE]) == 2)
m.add(pathCheck(node3SE, [edge_3E_3SE, edge_3S_3SE]) == 2)
m.add(pathCheck(node3S, [edge_3_3S, edge_3S_3SE, edge_2S_3S]) == 2)
m.add(pathCheck(node2S, [edge_2_2S, edge_2S_3S, edge_BE_2S]) == 2)
m.add(pathCheck(nodeBE, [edge_5S_BE, edge_BE_2S, edge_B_BE]) == 2)
m.add(pathCheck(nodeB, [edge_B_BE, edge_BN_B]) == 2)
m.add(pathCheck(nodeBN, [edge_BN_B, edge_5W_BN, edge_BN_5S]) == 2)
m.add(pathCheck(node5S, [edge_BN_5S, edge_5S_BE]) == 2)
m.add(pathCheck(node5, [edge_5W_5, edge_5N_5, edge_5_5E]) == 2)
m.add(pathCheck(node5N, [edge_5N_5, edge_5NW_5N, edge_5N_1W]) == 2)
m.add(pathCheck(node1W, [edge_5N_1W, edge_1W_1, edge_1W_5E]) == 2)
m.add(pathCheck(node1, [edge_1W_1, edge_1N_1, edge_1_1E, edge_1_1S]) == 2)
m.add(pathCheck(node1S, [edge_1_1S, edge_1S_3N, edge_1S_2E]) == 2)
m.add(pathCheck(node2E, [edge_1S_2E, edge_2_2E]) == 2)
m.add(pathCheck(node2, [edge_2_2E, edge_2_2S, edge_5E_2]) == 2)
m.add(pathCheck(node5E, [edge_5E_2, edge_5_5E, edge_1W_5E]) == 2)

# boundary line cases
m.add(IntNot(node6) + edge_6W_6 == 1)
m.add(IntNot(nodeD) + edge_3NE_D == 1)
m.add(IntNot(nodeW) + edge_W_5W == 1)

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

