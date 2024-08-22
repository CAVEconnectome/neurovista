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


def center_camera(
    plotter: pv.Plotter,
    center: np.ndarray,
    distance: float,
    up: Literal["x", "y", "z", "-x", "-y", "-z"] = "-y",
    elevation: Union[float, int] = 25,
):
    plotter.camera_position = "zx"
    plotter.camera.focal_point = center
    plotter.camera.position = center + np.array([0, 0, distance])
    plotter.camera.up = UP_MAP[up]
    plotter.camera.elevation = elevation


def _edges_to_lines(nodes, edges):
    iloc_map = dict(zip(nodes.index.values, range(len(nodes))))
    iloc_edges = edges[["source", "target"]].applymap(lambda x: iloc_map[x])

    lines = np.empty((len(edges), 3), dtype=int)
    lines[:, 0] = 2
    lines[:, 1:3] = iloc_edges[["source", "target"]].values

    return lines


def to_line_polydata(
    nodes: np.ndarray,
    edges: np.ndarray,
):
    points = nodes.astype(float)

    lines = np.hstack([np.full((len(edges), 1), 2), edges])

    poly = pv.PolyData(points, lines=lines)
    return poly


def to_mesh_polydata(
    nodes: np.ndarray,
    faces: np.ndarray,
):
    points = nodes.astype(float)

    faces = np.hstack([np.full((len(faces), 1), 3), faces])

    poly = pv.PolyData(points, faces=faces)

    return poly


def bounds_to_box(bounds: np.ndarray, **kwargs):
    assert bounds.shape == (2, 3)
    # pyvista expects  (xMin, xMax, yMin, yMax, zMin, zMax)
    box = np.array(
        [
            bounds[0, 0],
            bounds[1, 0],
            bounds[0, 1],
            bounds[1, 1],
            bounds[0, 2],
            bounds[1, 2],
        ]
    )
    return pv.Box(box, **kwargs)
