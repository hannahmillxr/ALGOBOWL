from kruskals import cost
from rkruskals import rkruskals_no_sort
from numpy.random import random
from copy import deepcopy, copy 
from prune import prune
import argparse
from read_input import read_input
from numpy import exp

def MH_step(edges0: list, temp: float, c0: int, parentVertices: list, rVertices: list, p: float, mst0 :list): 
    def P(x): 
        return exp(x/temp) 
    edges1 = deepcopy(edges0) 
    for i in range(len(edges1)-1): 
        swp = random() 
        if swp < p: 
             tmp = copy(edges1[i])   
             edges1[i] = copy(edges1[i+1])
             edges1[i+1] = tmp
   

    mst1 = rkruskals_no_sort(edges1,parentVertices, rVertices)
    mst1 = prune(mst1, rVertices)
    c1 = cost(mst1) 
    accept = min(1,P(c0)/P(c1))  
    u = random()
    if u < accept:
        return mst1,edges1,c1 
    return mst0,edges0,c0 

def MH(iters: int, edges: list, parentVertices: list, rVertices: list): 
    rSet = set(rVertices) 
    def inR(v):
        if v in rSet: 
            return 0.5
        return 0
    edges.sort(key = lambda e: e.weight - inR(e.u) - inR(e.v))
    mst0 = rkruskals_no_sort(edges, parentVertices, rVertices)
    mst0 = prune(mst0, rVertices) 
    mst = deepcopy(mst0) 
    c = cost(mst0)
    temp = c
    min_mst = deepcopy(mst0) 
    min_edges = edges 
    min_cost = c 
    for i in range(iters): 
        mst,edges,c = MH_step(edges,temp, c,parentVertices, rVertices, .95 - (.9)*i/(iters-1),mst)
        if c < min_cost: 
            min_cost = c
            min_edges = deepcopy(edges)
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
    args = parser.parse_args() 

    parentVertices, edgesArray, numOfRvertices,rVertices = read_input(args.input)
    mst = MH(args.iters, edgesArray, parentVertices, rVertices) 
    cst = cost(mst) 
    print(cst)

    with open(args.output, 'w') as fileOut: 
        fileOut.write(str(cst)+'\n')
        fileOut.write(str(len(mst))+'\n') 
        for edge in mst: 
            fileOut.write(f"{edge.u} {edge.v}\n")  

main()


    


