from OpenGL.GL import *
from ..GLGraphicsItem import GLGraphicsItem
from _typeshed import Incomplete

__all__ = ['GLMeshItem']

class GLMeshItem(GLGraphicsItem):
    """
    **Bases:** :class:`GLGraphicsItem <pyqtgraph.opengl.GLGraphicsItem.GLGraphicsItem>`
    
    Displays a 3D triangle mesh. 
    """
    opts: Incomplete
    vertexes: Incomplete
    normals: Incomplete
    colors: Incomplete
    faces: Incomplete
    def __init__(self, parentItem: Incomplete | None = None, **kwds) -> None:
        """
        ============== =====================================================
        **Arguments:**
        meshdata       MeshData object from which to determine geometry for 
                       this item.
        color          Default face color used if no vertex or face colors 
                       are specified.
        edgeColor      Default edge color to use if no edge colors are
                       specified in the mesh data.
        drawEdges      If True, a wireframe mesh will be drawn. 
                       (default=False)
        drawFaces      If True, mesh faces are drawn. (default=True)
        shader         Name of shader program to use when drawing faces.
                       (None for no shader)
        smooth         If True, normal vectors are computed for each vertex
                       and interpolated within each face.
        computeNormals If False, then computation of normal vectors is 
                       disabled. This can provide a performance boost for 
                       meshes that do not make use of normals.
        ============== =====================================================
        """
    def setShader(self, shader) -> None:
        """Set the shader used when rendering faces in the mesh. (see the GL shaders example)"""
    def shader(self): ...
    def setColor(self, c) -> None:
        """Set the default color to use when no vertex or face colors are specified."""
    def setMeshData(self, **kwds) -> None:
        """
        Set mesh data for this item. This can be invoked two ways:
        
        1. Specify *meshdata* argument with a new MeshData object
        2. Specify keyword arguments to be passed to MeshData(..) to create a new instance.
        """
    edges: Incomplete
    edgeColors: Incomplete
    def meshDataChanged(self) -> None:
        """
        This method must be called to inform the item that the MeshData object
        has been altered.
        """
    edgeVerts: Incomplete
    def parseMeshData(self) -> None: ...
    def paint(self) -> None: ...
