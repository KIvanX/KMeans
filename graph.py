import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

nodes = [1, 2, 3, 4, 5, 6, 7]
edges = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 5), (5, 5), (1, 7), (4, 6)]

# добавляем информацию в объект графа
G.add_nodes_from(nodes)
G.add_edges_from(edges)

T = nx.minimum_spanning_tree(G)
sorted(T.edges(data=True))

# рисуем граф и отображаем его
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()

nx.draw(T, with_labels=True, font_weight='bold')
plt.show()
