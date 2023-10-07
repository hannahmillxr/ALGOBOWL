from kruskals import kruskals, Edge, cost
from prune import prune
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

    with open(args.input, 'r') as fileIn:
        data1 = fileIn.readline()
        line = data1.split()
        intLine = [int (i) for i in line]
        parentVertices = intLine[0]
        edges = intLine[1]
        numOfRVertices = intLine[2]

        #second line
        data2 = fileIn.readline()
        line2 = data2.split()
        rVertices = [int (i) for i in line2]

        #list of all possible edges
        edgesArray = []
        for i in range(edges):
            data3 = fileIn.readline()
            line3 = data3.split()
            edgesArray.append(Edge(int(line3[0]),int(line3[1]), int(line3[2])))

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
