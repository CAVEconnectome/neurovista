import pandas as pd
from navis import TreeNeuron
from networkframe import NetworkFrame


def treeneuron_to_networkframe(treeneuron: TreeNeuron):
    nodes = treeneuron.nodes.set_index("node_id")
    edges = treeneuron.edges
    edges = pd.DataFrame(edges, columns=["source", "target"])
    return NetworkFrame(nodes, edges)
