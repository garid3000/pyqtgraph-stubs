from .GLMeshItem import GLMeshItem
from _typeshed import Incomplete

__all__ = ['GLBarGraphItem']

class GLBarGraphItem(GLMeshItem):
    def __init__(self, pos, size, parentItem: Incomplete | None = None) -> None:
        """
        pos is (...,3) array of the bar positions (the corner of each bar)
        size is (...,3) array of the sizes of each bar
        """
