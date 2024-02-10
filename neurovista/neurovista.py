import pyvista as pv
from networkframe import NetworkFrame

from .utils import _edges_to_lines


def to_points_poly(points):
    pass


def to_line_poly(points, lines):
    pass


def to_mesh_poly(points, faces):
    pass


def networkframe_to_points_poly(networkframe: NetworkFrame):
    points = networkframe.nodes[["x", "y", "z"]].values.astype(float)
    poly = pv.PolyData(points)
    return poly


def networkframe_to_line_poly(networkframe: NetworkFrame):
    nodes = networkframe.nodes
    edges = networkframe.edges

    points = nodes[["x", "y", "z"]].values.astype(float)
    lines = _edges_to_lines(nodes, edges)

    poly = pv.PolyData(points, lines=lines)
    return poly
