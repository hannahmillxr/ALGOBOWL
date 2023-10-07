import networkx as nx
import random
import matplotlib.pyplot as plt


def make_input_parameterized(max_nodes: int, max_edges: int):
    G = nx.Graph()

    wt_range = range(1,50)

    # add max number of nodes
    G.add_nodes_from(range(1,max_nodes + 1))

    # build spanning tree
    for i in range(2,max_nodes + 1):
        if(i == 2):
            G.add_edge(i, 1, weight = random.choice(wt_range))
        else:
            G.add_edge(i, random.choice(range(1, i-1)), weight = random.choice(wt_range))

    # add other random edges
    for i in range(0, random.choice(range(1, max_edges))):
        G.add_edge(random.choice(range(1, max_nodes)), random.choice(range(1, max_nodes)), weight = random.choice(wt_range))

    required_nodes = set()
    for i in range(0, random.choice(range(1, max_nodes))):
        required_nodes.add(random.choice(range(1, max_nodes)))

    return G,required_nodes



def make_input():
    G = nx.Graph()
    graph_file = "custom_input.txt"

    wt_range = range(1,50)
    max_nodes = 1000
    max_edges = 100000

    # add max number of nodes
    G.add_nodes_from(range(1,max_nodes + 1))

    # build spanning tree
    for i in range(2,max_nodes + 1):
        if(i == 2):
            G.add_edge(i, 1, weight = random.choice(wt_range))
        else:
            G.add_edge(i, random.choice(range(1, i-1)), weight = random.choice(wt_range))

    # add other random edges
    for i in range(0, random.choice(range(1, max_edges))):
        G.add_edge(random.choice(range(1, max_nodes)), random.choice(range(1, max_nodes)), weight = random.choice(wt_range))

    required_nodes = set()
    for i in range(0, random.choice(range(1, max_nodes))):
        required_nodes.add(random.choice(range(1, max_nodes)))

    # write graph to file
    nx.write_weighted_edgelist(G, graph_file)

    header = f'{max_nodes} {G.number_of_edges()} {len(required_nodes)}\n'
    header += ' '.join(map(str, required_nodes)) + '\n'

    # append metadata to start of file
    with open(graph_file, 'r+') as f:
        old_content = f.read()
        f.seek(0)
        f.write(header + old_content)
