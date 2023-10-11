from kruskals import kruskals_no_sort,kruskals, cost
from approximate import KMB_3 
from numpy.random import random
from copy import deepcopy, copy 
from prune import prune
import argparse
from read_input import read_input
from  edge_reweighting import reweight
import random

def MH_step(edges0: list, c0: int, parentVertices: int, rVertices: list, p: float): 
    def P(x): 
        return x 
    edges1 = deepcopy(edges0) 
    for i in range(len(edges1)-1): 
        swp = random() 
        if swp < p: 
             tmp = copy(edges1[i])   
             edges1[i] = copy(edges1[i+1])
             edges1[i+1] = tmp
   

    mst1 = kruskals_no_sort(edges1,parentVertices)
    mst1 = prune(mst1, rVertices)
    c1 = cost(mst1) 
    accept = min(1,P(c0)/P(c1))  
    u = random()
    if u < accept:
        return edges1,c1 
    return edges0,c0 

def MH(iters: int, edges: list, parentVertices: int, rVertices: list): 
    edges = KMB_3(edges, parentVertices, rVertices)
    edges.sort(key = lambda e: e.weight)
    mst0 = kruskals_no_sort(edges, parentVertices)
    mst0 = prune(mst0, rVertices) 
    c = cost(mst0)
    min_edges = edges 
    min_cost = c 
    for i in range(iters): 
        edges,c = MH_step(edges,c,parentVertices, rVertices, .95 - (.9)*i/iters)
        if c < min_cost: 
            min_cost = c
            min_edges = deepcopy(edges)
    mst = kruskals_no_sort(min_edges,parentVertices)
    mst = prune(mst, rVertices)
    return mst

def patrick_KMB(iters: int, edges: list, n: int, req_verts: list, p : int):
    total_edges = deepcopy(edges) 
    edges = KMB_3(edges, n, req_verts)
    mst0 = kruskals(edges, n)
    mst0 = prune(mst0, req_verts) 
    c = cost(mst0)
    min_mst = mst0 
    min_cost = c 
    for i in range(iters): 
        num_take = random.randint(1,max(len(total_edges)*p//100,1))
        new_edges = [random.choice(total_edges) for _ in range(num_take)]
        edges = min_mst+new_edges
        mst = kruskals(edges, n)
        mst = prune(mst, req_verts) 
        c = cost(mst)
        if c <= min_cost: 
            min_cost = c
            min_mst = deepcopy(mst) 
    return min_mst



    


def main():
    """ 
    Takes a graph from an input file and outputs the result of our modified kruskal's algorithm. 
    """
    parser = argparse.ArgumentParser(
                    prog="Modified Kruskals", 
                    description="Runs our modified kruskals on the input file and writes the result to an output file") 
    parser.add_argument('input') 
    parser.add_argument('output') 
    parser.add_argument('-i', '--iters', type=int, required = True)
    parser.add_argument('-p', '--percent', type=int,default = 10, required = False)
    args = parser.parse_args() 

    parentVertices, edgesArray, numOfRvertices,rVertices = read_input(args.input)
    #mst = reweight(edgesArray, parentVertices, rVertices,args.iters)
    cst = cost(mst) 
    print(cst)

    with open(args.output, 'w') as fileOut: 
        fileOut.write(str(cst)+'\n')
        fileOut.write(str(len(mst))+'\n') 
        for edge in mst: 
            fileOut.write(f"{edge.u} {edge.v}\n")  

main()


    


