import networkx as nx
from kruskals import Edge

def prune(mst: list,rVertices: list): 
    G2 = nx.Graph()
    for edge in mst:
        G2.add_edge(edge.u, edge.v, weight=edge.weight)

    while True:
        remove_nodes = [] 
        for v in G2.nodes():
            if G2.degree[v] == 1 and v not in rVertices:
                remove_nodes.append(v) 
        for node in remove_nodes:
            G2.remove_node(node)
        if not remove_nodes:
            break

    res = []
    for edge in G2.edges.data(): 
        res.append(Edge(edge[0],edge[1], edge[2]['weight']))
    return res
        
               
