class Edge():
    def __init__(self,u: int, v: int, weight: int) -> None:
        self.u = u 
        self.v = v
        self.weight = weight

class DSU(): 
    def __init__(self, num_verts: int): 
        self.parent = [i for i in range(num_verts+1)]
        self.height = [1 for i in range(num_verts+1)]
    
    def find(self, x : int) -> int: 
        if x == self.parent[x]: 
            return x 
        self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x]

    def union(self,x: int, y: int) -> bool: 
        x = self.find(x) #replace with set id 
        y = self.find(y) 
        if x == y: 
            return False #not part of different components
        if self.height[x] > self.height[y]: 
            self.parent[y] = x 
        elif self.height[x] == self.height[y]: 
            self.parent[y] = x 
            self.height[x]+=1 
        else: 
            self.parent[x] = y 
        return True #part of different components 


def kruskals(edges: list, num_verts: int) -> list:
    dsu = DSU(num_verts) 
    edges.sort(key = lambda edge: edge.weight)
    mst = []
    num_edges  = 0
    index = 0   
    while index < len(edges) and num_edges < num_verts-1: 
        if dsu.union(edges[index].u, edges[index].v):
            mst.append(edges[index]) 
            num_edges+=1 
        index+=1 
    return mst

def cost(edgeList: list) -> int: 
    return sum([e.weight for e in edgeList])
