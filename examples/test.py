# %%
import navis

nl = navis.example_neurons()

# %%
import pandas as pd

neuron = nl[0]
nodes = neuron.nodes.set_index("node_id")
points = nodes[["x", "y", "z"]].values.astype(float)
edges = neuron.edges
edges = pd.DataFrame(edges, columns=["source", "target"])

from neurovista.navis import treeneuron_to_networkframe

networkframe = treeneuron_to_networkframe(neuron)

# %%
import pyvista as pv

pv.set_jupyter_backend("client")
plotter = pv.Plotter()
line_poly = pv.PolyData(points, lines=lines)
plotter.add_mesh(line_poly, color="black")
plotter.show()
