from kruskals import kruskals, Edge, cost
from prune import prune
from read_input import read_input 
import argparse 


def main():
    """ 
    Takes a graph from an input file and outputs the result of our modified kruskal's algorithm. 
    """
    parser = argparse.ArgumentParser(
                    prog="Modified Kruskals", 
                    description="Runs our modified kruskals on the input file and writes the result to an output file") 
    parser.add_argument('input') 
    parser.add_argument('output') 
    args = parser.parse_args() 
    parentVertices, edgesArray, numOfRvertices,rVertices = read_input(args.input)


    mst = kruskals(edgesArray, parentVertices) 
    prune(mst, rVertices)
    cst = cost(mst) 
    print(cst) 


    with open(args.output, 'w') as fileOut: 
        fileOut.write(str(cst)+'\n')
        fileOut.write(str(len(mst))+'\n') 
        for edge in mst: 
            fileOut.write(f"{edge.u} {edge.v}\n")  

main()
