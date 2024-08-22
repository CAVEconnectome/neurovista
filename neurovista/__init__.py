"""Top-level package for neurovista."""

from .utils import (
    bounds_to_box,
    center_camera,
    set_up_camera,
    to_line_polydata,
    to_mesh_polydata,
)

__all__ = [
    "set_up_camera",
    "to_line_polydata",
    "to_mesh_polydata",
    "center_camera",
    "bounds_to_box",
]
