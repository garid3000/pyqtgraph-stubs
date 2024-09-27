from ..Qt import QtGui as QtGui
from _typeshed import Incomplete

class MeshData:
    """
    Class for storing and operating on 3D mesh data. May contain:
    
      - list of vertex locations
      - list of edges
      - list of triangles
      - colors per vertex, edge, or tri
      - normals per vertex or tri
    
    This class handles conversion between the standard [list of vertexes, list of faces]
    format (suitable for use with glDrawElements) and 'indexed' [list of vertexes] format
    (suitable for use with glDrawArrays). It will automatically compute face normal
    vectors as well as averaged vertex normal vectors. 
    
    The class attempts to be as efficient as possible in caching conversion results and
    avoiding unnecessary conversions.
    """
    def __init__(self, vertexes: Incomplete | None = None, faces: Incomplete | None = None, edges: Incomplete | None = None, vertexColors: Incomplete | None = None, faceColors: Incomplete | None = None) -> None:
        """
        ==============  =====================================================
        **Arguments:**
        vertexes        (Nv, 3) array of vertex coordinates.
                        If faces is not specified, then this will instead be
                        interpreted as (Nf, 3, 3) array of coordinates.
        faces           (Nf, 3) array of indexes into the vertex array.
        edges           [not available yet]
        vertexColors    (Nv, 4) array of vertex colors.
                        If faces is not specified, then this will instead be
                        interpreted as (Nf, 3, 4) array of colors.
        faceColors      (Nf, 4) array of face colors.
        ==============  =====================================================
        
        All arguments are optional.
        """
    def faces(self):
        """Return an array (Nf, 3) of vertex indexes, three per triangular face in the mesh.
        
        If faces have not been computed for this mesh, the function returns None.
        """
    def edges(self):
        """Return an array (Nf, 3) of vertex indexes, two per edge in the mesh."""
    def setFaces(self, faces) -> None:
        """Set the (Nf, 3) array of faces. Each rown in the array contains
        three indexes into the vertex array, specifying the three corners 
        of a triangular face."""
    def vertexes(self, indexed: Incomplete | None = None):
        """Return an array (N,3) of the positions of vertexes in the mesh. 
        By default, each unique vertex appears only once in the array.
        If indexed is 'faces', then the array will instead contain three vertexes
        per face in the mesh (and a single vertex may appear more than once in the array)."""
    def setVertexes(self, verts: Incomplete | None = None, indexed: Incomplete | None = None, resetNormals: bool = True) -> None:
        """
        Set the array (Nv, 3) of vertex coordinates.
        If indexed=='faces', then the data must have shape (Nf, 3, 3) and is
        assumed to be already indexed as a list of faces.
        This will cause any pre-existing normal vectors to be cleared
        unless resetNormals=False.
        """
    def resetNormals(self) -> None: ...
    def hasFaceIndexedData(self):
        """Return True if this object already has vertex positions indexed by face"""
    def hasEdgeIndexedData(self): ...
    def hasVertexColor(self):
        """Return True if this data set has vertex color information"""
    def hasFaceColor(self):
        """Return True if this data set has face color information"""
    def faceNormals(self, indexed: Incomplete | None = None):
        """
        Return an array (Nf, 3) of normal vectors for each face.
        If indexed='faces', then instead return an indexed array
        (Nf, 3, 3)  (this is just the same array with each vector
        copied three times).
        """
    def vertexNormals(self, indexed: Incomplete | None = None):
        """
        Return an array of normal vectors.
        By default, the array will be (N, 3) with one entry per unique vertex in the mesh.
        If indexed is 'faces', then the array will contain three normal vectors per face
        (and some vertexes may be repeated).
        """
    def vertexColors(self, indexed: Incomplete | None = None):
        """
        Return an array (Nv, 4) of vertex colors.
        If indexed=='faces', then instead return an indexed array
        (Nf, 3, 4). 
        """
    def setVertexColors(self, colors, indexed: Incomplete | None = None) -> None:
        """
        Set the vertex color array (Nv, 4).
        If indexed=='faces', then the array will be interpreted
        as indexed and should have shape (Nf, 3, 4)
        """
    def faceColors(self, indexed: Incomplete | None = None):
        """
        Return an array (Nf, 4) of face colors.
        If indexed=='faces', then instead return an indexed array
        (Nf, 3, 4)  (note this is just the same array with each color
        repeated three times). 
        """
    def setFaceColors(self, colors, indexed: Incomplete | None = None) -> None:
        """
        Set the face color array (Nf, 4).
        If indexed=='faces', then the array will be interpreted
        as indexed and should have shape (Nf, 3, 4)
        """
    def faceCount(self):
        """
        Return the number of faces in the mesh.
        """
    def edgeColors(self): ...
    def vertexFaces(self):
        """
        Return list mapping each vertex index to a list of face indexes that use the vertex.
        """
    def save(self):
        """Serialize this mesh to a string appropriate for disk storage"""
    def restore(self, state) -> None:
        """Restore the state of a mesh previously saved using save()"""
    @staticmethod
    def sphere(rows, cols, radius: float = 1.0, offset: bool = True):
        """
        Return a MeshData instance with vertexes and faces computed
        for a spherical surface.
        """
    @staticmethod
    def cylinder(rows, cols, radius=[1.0, 1.0], length: float = 1.0, offset: bool = False):
        """
        Return a MeshData instance with vertexes and faces computed
        for a cylindrical surface.
        The cylinder may be tapered with different radii at each end (truncated cone)
        """
