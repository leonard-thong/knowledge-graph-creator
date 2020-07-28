from knoledge_graph_creation.create_graph_1 import G
from import_libraries import nx, plt

plt.figure(figsize=(12, 12))

pos = nx.spring_layout(G)
nx.draw(G, with_labels=True, node_color='skyblue', edge_cmap=plt.cm.Blues, pos=pos)
plt.show()
