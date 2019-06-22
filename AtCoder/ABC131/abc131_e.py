n,k = map(int, input().split())

import networkx as nx

G = nx.Graph()

for i in range(1,n):
    G.add_node(i)
    for j in range(k):
        G.add_weighted_edges_from(i,j,1)

