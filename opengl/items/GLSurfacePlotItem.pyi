from OpenGL.GL import *
from .GLMeshItem import GLMeshItem
from _typeshed import Incomplete

__all__ = ['GLSurfacePlotItem']

class GLSurfacePlotItem(GLMeshItem):
    """
    **Bases:** :class:`GLMeshItem <pyqtgraph.opengl.GLMeshItem>`
    
    Displays a surface plot on a regular x,y grid
    """
    def __init__(self, x: Incomplete | None = None, y: Incomplete | None = None, z: Incomplete | None = None, colors: Incomplete | None = None, parentItem: Incomplete | None = None, **kwds) -> None:
        """
        The x, y, z, and colors arguments are passed to setData().
        All other keyword arguments are passed to GLMeshItem.__init__().
        """
    def setData(self, x: Incomplete | None = None, y: Incomplete | None = None, z: Incomplete | None = None, colors: Incomplete | None = None) -> None:
        """
        Update the data in this surface plot. 
        
        ==============  =====================================================================
        **Arguments:**
        x,y             1D arrays of values specifying the x,y positions of vertexes in the
                        grid. If these are omitted, then the values will be assumed to be
                        integers.
        z               2D array of height values for each grid vertex.
        colors          (width, height, 4) array of vertex colors.
        ==============  =====================================================================
        
        All arguments are optional.
        
        Note that if vertex positions are updated, the normal vectors for each triangle must 
        be recomputed. This is somewhat expensive if the surface was initialized with smooth=False
        and very expensive if smooth=True. For faster performance, initialize with 
        computeNormals=False and use per-vertex colors or a normal-independent shader program.
        """
    def generateFaces(self) -> None: ...
