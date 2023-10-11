from kruskals import kruskals,Edge
from prune import prune



def all_pairs_shortest_path(edges, n, req_verts):
    INF = 10**9

    adj_list = [[] for _ in range(n+1)]
    for edge in edges: 
        adj_list[edge.u].append(Edge(edge.u,edge.v,edge.weight))
        adj_list[edge.v].append(Edge(edge.v, edge.u, edge.weight))

    dist = {} 
    for r in req_verts:
        for i in range(1,n+1):
            dist[(r,i)] = INF

    parent = {}
    for r in req_verts: 
        for i in range(1,n+1):
            parent[(r,i)] = -1

    for r in req_verts: 
        d = [INF for _ in range(n+1)] 
        p = [(-1, -1) for _ in range(n+1)] 
        visited = [False for _ in range(n+1)] 
        d[r] = 0
        cur = r
        for _ in range(n):  
            visited[cur] = True
            for edge in adj_list[cur]: 
                if d[cur] + edge.weight < d[edge.v]: 
                    d[edge.v] = d[cur] +edge.weight 
                    p[edge.v] = (cur,edge.weight) 

            min_dist = INF 
            for i in range(1,n+1): 
                if not visited[i] and d[i] < min_dist: 
                    cur = i 
                    min_dist = d[i]

        for i in range(1,n+1): 
            parent[(r,i)] = p[i] 

        for i in range(1,n+1): 
            dist[(r,i)] = d[i] 

    return dist, parent 

def KMB(edges,n, req_verts): 

    #Step 1: 
    dist, parent = all_pairs_shortest_path(edges, n ,req_verts) 

    rmapping = {}
    irmapping = {}
    ct = 0 
    for i in req_verts: 
        ct+=1
        rmapping[i] = ct
        irmapping[ct] = i 

    edges1 = []
    for r0 in req_verts: 
        for r1 in req_verts: 
            if r0!=r1: 
                edges1.append(Edge(rmapping[r0],rmapping[r1],dist[(r0,r1)]))

    
    #Step 2: 
    mst1 = kruskals(edges1,len(req_verts))

    mst1 = [Edge(irmapping[edge.u], irmapping[edge.v], edge.weight) for edge in mst1] 

    #Step 3: 
    s_edges= []
    for edge in mst1: 
        cur = edge.u 
        while cur!=edge.v:
            u, weight = parent[(edge.v,cur)] 
            s_edges.append(Edge(cur,u,weight)) 
            cur = u 

    #Step 4
    s_mst = kruskals(s_edges, n) 

    #Step 5 
    s_mst = prune(s_mst, req_verts) 

    return s_mst

def KMB_3(edges,n, req_verts): 

    #Step 1: 
    dist, parent = all_pairs_shortest_path(edges, n ,req_verts) 

    rmapping = {}
    irmapping = {}
    ct = 0 
    for i in req_verts: 
        ct+=1
        rmapping[i] = ct
        irmapping[ct] = i 

    edges1 = []
    for r0 in req_verts: 
        for r1 in req_verts: 
            if r0!=r1: 
                edges1.append(Edge(rmapping[r0],rmapping[r1],dist[(r0,r1)]))

    
    #Step 2: 
    mst1 = kruskals(edges1,len(req_verts))

    mst1 = [Edge(irmapping[edge.u], irmapping[edge.v], edge.weight) for edge in mst1] 

    #Step 3: 
    s_edges= []
    for edge in mst1: 
        cur = edge.u 
        while cur!=edge.v:
            u, weight = parent[(edge.v,cur)] 
            s_edges.append(Edge(cur,u,weight)) 
            cur = u 

    return s_edges

