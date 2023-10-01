from z3 import *
from shop_floor_layout import *

def IntNot(x:Int) -> Int:
    return (1 - x)

def pathCheck(node:Int, edge_list:list, n:int) -> Bool:
    # here, n is number of edges active at a time. 
    # n = 2 if there exist seperate entry and exit edges to and from node
    # n = 1 if there is same edge for entry and exit to and from node
    return n*IntNot(node) + sum(edge_list) == n

def get_keys_from_value(d, val):
    return [k for k, v in d.items() if v == val]

edge_weights = {"edge_4W_4":21, "edge_4_1N":45, "edge_1N_6W":18, "edge_6W_6":28, 
                "edge_5NW_5N":21, "edge_5N_1W":25, "edge_1W_1":20, "edge_1_1E":18, "edge_1E_DN":28, 
                "edge_W_5W":7, "edge_5W_5":21, "edge_5_5E":25, "edge_1S_3N":18, "edge_3N_3NE":28, "edge_3NE_D":8, 
                "edge_BN_5S":21, "edge_2_2E":20, "edge_3_3E":28, 
                "edge_B_BE":21, "edge_BE_2S":25, "edge_2S_3S":38, "edge_3S_3SE":28, 
                
                "edge_4W_5NW":19, "edge_5NW_5W":17, "edge_5W_BN":17, "edge_BN_B":17, 
                "edge_5N_5":17, "edge_5S_BE":17, 
                "edge_1W_5E":17, "edge_5E_2":17, "edge_2_2S":17, 
                "edge_1N_1":19, "edge_1_1S":17, "edge_1S_2E":17, 
                "edge_6W_1E":19, "edge_1E_3N":17, "edge_3N_3":17, "edge_3_3S":17, 
                "edge_DN_3NE":17, "edge_3NE_3E":17, "edge_3E_3SE":17,}

# create new model
m = Optimize()

# add decision variables for nodes and edges
node_vars = {node:Int(node) for node in node_names}
edge_vars = {edge:Int(edge) for edge in edge_names}

# treat all decision variables related to node and edges as boolean
for node in node_names:
    m.add(node_vars[node] >= 0)
    m.add(node_vars[node] <= 1)

for edge in edge_names:
    m.add(edge_vars[edge] >= 0)
    m.add(edge_vars[edge] <= 1)


# add constraints
start = "node5"
end = "node3"

for name, node in nodes.items():
    # get all edges connected to the node
    node_edges = shop_floor.get_edges_for(node)
    
    # get the name of the edges -- silly and heavy operation :(
    node_edges_names = []
    for edge in node_edges:
        names = get_keys_from_value(edges, edge)
        node_edges_names += [name for name in names]

    # get booleans related to these respective edges
    node_edges = [edge_vars[name] for name in node_edges_names]
    
    # For both source and destination nodes, only one of the neighboring edges will be part of the path.
    if (name == start) or (name == end):
        m.add(sum(node_edges) == 1)
        continue

    # All other nodes (except the source and destination nodes) will either be (i) part of the path or (ii) not part of the path.
    if len(node_edges) >= 2:
        m.add(pathCheck(node_vars[node.name], node_edges, 2))
    else:
        m.add(pathCheck(node_vars[node.name], node_edges, 1))

# set objective function
obj = Int('obj')
m.add(obj > 0)
m.add(obj == sum([edge_weights[edge]*edge_vars[edge] for edge in edges]))

m.minimize(obj)

# solve the model
m.check()
print(m.model())

