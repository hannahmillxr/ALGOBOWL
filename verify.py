import networkx as nx
import argparse
from read_input import read_input
from kruskals import Edge

#verification 
def subgraph(mst: list, parentEdgesArray:list):
    parentEdges_noweights = set((Edge(edge.u,edge.v,-1) for edge in parentEdgesArray))
    for i in mst:
        if i not in parentEdgesArray:
            return False
    return True

#is_tree will test for cycles and connectivity
def connected(mst: list):
    Graph = nx.DiGraph()
    for edge in mst:
        Graph.add_edge(edge.u, edge.v)
    if (nx.is_tree(Graph)==False):
            return False    
    return True

def has_required_vertices(mst: list, required_vertices: list):
    found_verts: set = set()
    for e in mst:
        if e.v in required_vertices:
            found_verts.add(e.v)
        if e.u in required_vertices:
            found_verts.add(e.u)

    print("Found vertices: ", found_verts)
    print("Required vertices: ", required_vertices)
    return len(found_verts) == len(required_vertices)

def cost_of_graph(mst: list, parentEdges: list):
    #setup dictionary 
    parent_dict = {Edge(edge.u,edge.v,-1): edge for edge in parentEdges}
    cost = 0
    for edge in mst:
        cost += parent_dict[edge].weight
    return cost

def verify(mst: list, parentEdgesArray: list, required_vertices: list, weight: int):
    if (not subgraph(mst, parentEdgesArray)):
        print("MST is not a subgraph of the parent graph")
    elif cost_of_graph(mst, parentEdgesArray) != weight: 
        print(f"Supplied weight of {weight} does not equal {cost_of_grapg(mst,parentEdgesArray)}")
    elif (not connected(mst)):
        print("MST is not connected")
    elif (not has_required_vertices(mst, required_vertices)):
        print("MST does not contain all required vertices")
    else:
        print("MST is complete, is a subgraph of parent, supplies the correct weight and contains all required vertices")

def parseUnweightedEdge(st: str):
    u,v = map(int,st.split())
    return Edge(u,v,-1) # just assign a weight of -1 for an unweighted edge
    

def main(): 
    """ 
    Assumes input and output are formatted according to the AlgoBowl doc.
    """
    parser = argparse.ArgumentParser(prog = "Verify",
                                    description = "Verifies an output file represents a valid graph") 

    parser.add_argument("input") 
    parser.add_argument("output") 

    args = parser.parse_args() 

    parentVertices, inputEdges, numOfRVertices, rVertices = read_input(args.input) 
    with open(args.output, 'r') as inputFile: 
        weight   = int(inputFile.readline()) #grab weight
        numEdges = int(inputFile.readline()) #grab number of Edges

        edges = [parseUnweightedEdge(inputFile.readline()) for _ in range(numEdges)] 

    verify(edges,inputEdges,rVertices, weight)

main()
