from typing import Literal, Union

import numpy as np
import pyvista as pv

UP_MAP = {
    "x": (1, 0, 0),
    "y": (0, 1, 0),
    "z": (0, 0, 1),
    "-x": (-1, 0, 0),
    "-y": (0, -1, 0),
    "-z": (0, 0, -1),
}


def set_up_camera(
    plotter: pv.Plotter,
    neuron,
    setback: Union[float, int] = -2_000_000,
    elevation: Union[float, int] = 25,
    up: Literal["x", "y", "z", "-x", "-y", "-z"] = "-y",
):
    nuc_loc = neuron.nodes.loc[neuron.nucleus_id, ["x", "y", "z"]].values
    plotter.camera_position = "zx"
    plotter.camera.focal_point = nuc_loc
    plotter.camera.position = nuc_loc + np.array([0, 0, setback])
    plotter.camera.up = UP_MAP[up]
    plotter.camera.elevation = elevation


def _edges_to_lines(nodes, edges):
    iloc_map = dict(zip(nodes.index.values, range(len(nodes))))
    iloc_edges = edges[["source", "target"]].applymap(lambda x: iloc_map[x])

    lines = np.empty((len(edges), 3), dtype=int)
    lines[:, 0] = 2
    lines[:, 1:3] = iloc_edges[["source", "target"]].values

    return lines
