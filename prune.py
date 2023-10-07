import networkx as nx

def prune(mst: list,rVertices: list): 
    def _prune(mst: list, v: int):
        for edge in mst:
            if edge.v == v or edge.u == v:
                mst.remove(edge)
        return mst

    continue_pruning = True

    while(continue_pruning):
        mst_size = len(mst)

        G2 = nx.Graph()
        for edge in mst:
            G2.add_edge(edge.u, edge.v)

        for v in G2.nodes():
            if G2.degree[v] == 1 and v not in rVertices:
                mst = _prune(mst, v)

        if mst_size == len(mst):
            continue_pruning = False
