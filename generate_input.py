from make_input import make_input_parameterized
import argparse
import networkx as nx

def main():
    parser = argparse.ArgumentParser(prog = "Input generator", 
                                    description="Given a number of nodes and edges, generates a random graph with a random number of r vertices") 

    
    parser.add_argument("num_nodes",type=int)
    parser.add_argument("num_edges",type=int)
    parser.add_argument("output", type=str) 

    args = parser.parse_args()

    G, required_nodes = make_input_parameterized(args.num_nodes, args.num_edges)

    graph_file = args.output
    # write graph to file
    nx.write_weighted_edgelist(G, graph_file)

    header = f'{G.number_of_nodes()} {G.number_of_edges()} {len(required_nodes)}\n'
    header += ' '.join(map(str, required_nodes)) + '\n'

    # append metadata to start of file
    with open(graph_file, 'r+') as f:
        old_content = f.read()
        f.seek(0)
        f.write(header + old_content)

main()
