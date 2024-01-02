from math import prod

import networkx as nx

all_wires = []
with open('d25_input', 'r') as f:
    for line in f:
        line = line.strip()
        from_comp = line.split(':')[0]
        to_comp = line.split(':')[1].split()
        for comp in to_comp:
            all_wires.append((from_comp, comp))
print(all_wires)

G = nx.Graph()
G.add_edges_from(all_wires)
cut_edges = nx.minimum_edge_cut(G)
print(cut_edges)
G.remove_edges_from(cut_edges)

groups = list(nx.connected_components(G))
print('part1: ', prod(len(i) for i in groups))