from knoledge_graph_creation.extract_nodes import kg_df
from import_libraries import nx

# create a directed-graph from a dataframe
G = nx.from_pandas_edgelist(kg_df, "source", "target", edge_attr=True, create_using=nx.MultiDiGraph())
