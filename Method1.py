import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

G = nx.MultiGraph()

G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")

G.add_edge("A", "C")
G.add_edge("A", "C")
G.add_edge("A", "B")
G.add_edge("A", "B")
G.add_edge("A", "D")
G.add_edge("B", "D")
G.add_edge("D", "C")

print("number of edges", G.number_of_edges())
print("number of nodes", G.number_of_nodes())

list(G.degree(["A", "B", "C", "D"]))


def eulerpath(G):
    odd = 0
    a = list(G.degree(G.nodes()))
    for i in a:
        if (i[1] % 2) != 0:
            odd += 1
    if odd > 2:
        print("Not an Euler path:", odd, "vertices with odd degree")
    else:
        print("There is a possible Euler path")


# Visualize the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=500, node_color="lightblue", font_size=12, font_weight="bold")
plt.title("Graph")
plt.show()

# Check for Euler path
eulerpath(G)
