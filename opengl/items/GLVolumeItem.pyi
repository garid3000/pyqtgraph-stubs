from OpenGL.GL import *
from ..GLGraphicsItem import GLGraphicsItem
from _typeshed import Incomplete

__all__ = ['GLVolumeItem']

class GLVolumeItem(GLGraphicsItem):
    """
    **Bases:** :class:`GLGraphicsItem <pyqtgraph.opengl.GLGraphicsItem.GLGraphicsItem>`
    
    Displays volumetric data. 
    """
    sliceDensity: Incomplete
    smooth: Incomplete
    data: Incomplete
    texture: Incomplete
    def __init__(self, data, sliceDensity: int = 1, smooth: bool = True, glOptions: str = 'translucent', parentItem: Incomplete | None = None) -> None:
        """
        ==============  =======================================================================================
        **Arguments:**
        data            Volume data to be rendered. *Must* be 4D numpy array (x, y, z, RGBA) with dtype=ubyte.
        sliceDensity    Density of slices to render through the volume. A value of 1 means one slice per voxel.
        smooth          (bool) If True, the volume slices are rendered with linear interpolation 
        ==============  =======================================================================================
        """
    def setData(self, data) -> None: ...
    def paint(self) -> None: ...
    def drawVolume(self, ax, d) -> None: ...
