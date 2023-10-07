from kruskals import Edge

def read_input(filename: str): 
    with open(filename, 'r') as fileIn:
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
    return parentVertices,edgesArray,numOfRVertices,rVertices

