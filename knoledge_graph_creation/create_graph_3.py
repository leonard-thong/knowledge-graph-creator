from knoledge_graph_creation.extract_nodes import kg_df
from import_libraries import nx, plt

G = nx.from_pandas_edgelist(kg_df[kg_df['edge'] == "composed by"], "source", "target",
                            edge_attr=True, create_using=nx.MultiDiGraph())

plt.figure(figsize=(12, 12))
pos = nx.spring_layout(G, k=0.5)  # k regulates the distance between nodes
nx.draw(G, with_labels=True, node_color='skyblue', node_size=1500, edge_cmap=plt.cm.Blues, pos=pos)
plt.show()
