
def read_tuple(ss: str) -> tuple: 
    u,v,w = map(int,ss.split()) 
    return (u,v,w) 

def main(): 
    n,m,r = map(int, input().split()) 
    rs = map(int, input().split())
    edges = [read_tuple(input()) for _ in range(m)]
    print("graph G{")
    for node in rs: 
        print(f"{node} [color = blue]")
    for edge in edges:
        u,v,w = edge 
        print(f"{u} -- {v}[label = {w}]") 
    print("}")

if __name__ == "__main__": 
    main()
