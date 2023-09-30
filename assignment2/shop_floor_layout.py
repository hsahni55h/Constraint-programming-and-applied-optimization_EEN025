from Graph import Node, Edge, Graph


# Define nodes and edges - all x and y distances are from point O
node4W = Node("4W", {"x":7, "y":70})
node4 = Node("4", {"x":28, "y":70})
node1N = Node("1N", {"x":73, "y":70})
node6W = Node("6W", {"x":91, "y":70})
node6 = Node("6", {"x":119, "y":70})

node5NW = Node("5NW", {"x":7, "y":51})
node5N = Node("5N", {"x":28, "y":51})
node1W = Node("1W", {"x":53, "y":51})
node1 = Node("1", {"x":73, "y":51})
node1E = Node("1E", {"x":91, "y":51})
nodeDN = Node("DN", {"x":119, "y":51})

nodeW = Node("W", {"x":0, "y":34})
node5W = Node("5W", {"x":7, "y":34})
node5 = Node("5", {"x":28, "y":34})
node5E = Node("5E", {"x":53, "y":34})
node1S = Node("1S", {"x":73, "y":34})
node3N = Node("3N", {"x":91, "y":34})
node3NE = Node("3NE", {"x":119, "y":34})
nodeD = Node("D", {"x":127, "y":34})

nodeBN = Node("BN", {"x":7, "y":17})
node5S = Node("5S", {"x":28, "y":17})
node2 = Node("2", {"x":53, "y":17})
node2E = Node("2E", {"x":73, "y":17})
node3 = Node("3", {"x":91, "y":17})
node3E = Node("3E", {"x":119, "y":17})

nodeB = Node("B", {"x":7, "y":0})
nodeBE = Node("BE", {"x":28, "y":0})
node2S = Node("2S", {"x":53, "y":0})
node3S = Node("3S", {"x":91, "y":0})
node3SE = Node("3SE", {"x":119, "y":0})

machine_node = [node1, node2, node3, node4, node5, node6]

nodes = [
    node4W, node4, node1N, node6W, node6,
    node5NW, node5N, node1W, node1, node1E, nodeDN, 
    nodeW, node5W, node5, node5E, node1S, node3N, node3NE, nodeD,
    nodeBN, node5S, node2, node2E, node3, node3E,
    nodeB, nodeBE, node2S, node3S, node3SE,
    ]

edges = [
    Edge(node4W, node4, 21), Edge(node4, node1N, 45), Edge(node1N, node6W, 18), Edge(node6W, node6, 28),
    Edge(node5NW, node5N, 21), Edge(node5N, node1W, 25), Edge(node1W, node1, 20), Edge(node1, node1E, 18), Edge(node1E, nodeDN, 28),
    Edge(nodeW, node5W, 7), Edge(node5W, node5, 21), Edge(node5, node5E, 25), Edge(node1S, node3N, 18), Edge(node3N, node3NE, 28), Edge(node3NE, nodeD, 8),
    Edge(nodeBN, node5S, 21), Edge(node2, node2E, 20), Edge(node3, node3E, 28), 
    Edge(nodeB, nodeBE, 21), Edge(nodeBE, node2S, 25), Edge(node2S, node3S, 38), Edge(node3S, node3SE, 28), 
    
    Edge(node4W, node5NW, 19), Edge(node1N, node1, 19), Edge(node6W, node1E, 19), 
    Edge(node5NW, node5W, 17), Edge(node5N, node5, 17), Edge(node1W, node5E, 17), Edge(node1, node1S, 17), Edge(node1E, node3N, 17), Edge(nodeDN, node3NE, 17), 
    Edge(node5W, nodeBN, 17), Edge(node5E, node2, 17), Edge(node1S, node2E, 17), Edge(node3N, node3, 17), Edge(node3NE, node3E, 17), 
    Edge(nodeBN, nodeB, 17), Edge(node5S, nodeBE, 17), Edge(node2, node2S, 17), Edge(node3, node3S, 17), Edge(node3E, node3SE, 17)
    ]

shop_floor = Graph(nodes, edges)
