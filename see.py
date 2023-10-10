import argparse
from visualize import read_tuple

def read_two_tuple(ss: str) -> tuple: 
    u,v = map(int, ss.split()) 
    return (u,v) 

def sort_tuple(uv: tuple) -> tuple: 
    u,v = uv
    if v < u:
        return (v,u) 
    return (u,v) 

def print_graph(edges, mst_edges, rs): 
    def color(edge): 
        u,v,w = edge 
        if (u,v) in mst_edges: 
            return "blue" 
        return "black" 

    print("graph G{") 
    for r in rs: 
        print(f"{r} [color = blue]")
    for edge in edges: 
        u,v,w = edge 
        print(f"{u}--{v} [label = {w}, color = {color(edge)}]")
    print("}") 


def main():
    parser = argparse.ArgumentParser(
                    prog="Maps our output on top of the input", 
                    description="Maps out output on top of the input") 
    parser.add_argument('input') 
    parser.add_argument('output') 
    args = parser.parse_args() 

    with open(args.input, 'r') as inputFile: 
        n,m,r = map(int, inputFile.readline().split()) 
        rs = map(int, inputFile.readline().split()) 
        edges = [read_tuple(inputFile.readline()) for _ in range(m)] 

    with open(args.output, 'r') as outputFile: 
        w = map(int, outputFile.readline().split()) 
        m = map(int, outputFile.readline().split())
        m = list(m)[0]
        w = list(w)[0]
        mst_edges = set([sort_tuple(read_two_tuple(outputFile.readline())) for _ in range(m)])

    
    for edge in edges: 
        u,v,w = edge 
        u,v = sort_tuple((u,v)) 
        edge = (u,v,w) 

    print_graph(edges,mst_edges,rs)

   
main()
