from .GraphicsObject import GraphicsObject
from _typeshed import Incomplete

__all__ = ['PColorMeshItem']

class QuadInstances:
    nrows: int
    ncols: int
    pointsarray: Incomplete
    def __init__(self) -> None: ...
    polys: Incomplete
    def resize(self, nrows, ncols) -> None: ...
    def ndarray(self): ...
    def instances(self): ...

class PColorMeshItem(GraphicsObject):
    """
    **Bases:** :class:`GraphicsObject <pyqtgraph.GraphicsObject>`
    """
    sigLevelsChanged: Incomplete
    qpicture: Incomplete
    x: Incomplete
    y: Incomplete
    z: Incomplete
    edgecolors: Incomplete
    antialiasing: Incomplete
    levels: Incomplete
    cmap: Incomplete
    lut_qcolor: Incomplete
    quads: Incomplete
    def __init__(self, *args, **kwargs) -> None:
        '''
        Create a pseudocolor plot with convex polygons.

        Call signature:

        ``PColorMeshItem([x, y,] z, **kwargs)``

        x and y can be used to specify the corners of the quadrilaterals.
        z must be used to specified to color of the quadrilaterals.

        Parameters
        ----------
        x, y : np.ndarray, optional, default None
            2D array containing the coordinates of the polygons
        z : np.ndarray
            2D array containing the value which will be mapped into the polygons
            colors.
            If x and y is None, the polygons will be displaced on a grid
            otherwise x and y will be used as polygons vertices coordinates as::

                (x[i+1, j], y[i+1, j])           (x[i+1, j+1], y[i+1, j+1])
                                    +---------+
                                    | z[i, j] |
                                    +---------+
                    (x[i, j], y[i, j])           (x[i, j+1], y[i, j+1])

            "ASCII from: <https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.pcolormesh.html>".
        colorMap : pyqtgraph.ColorMap
            Colormap used to map the z value to colors.
            default ``pyqtgraph.colormap.get(\'viridis\')``
        levels: tuple, optional, default None
            Sets the minimum and maximum values to be represented by the colormap (min, max). 
            Values outside this range will be clipped to the colors representing min or max.
            ``None`` disables the limits, meaning that the colormap will autoscale 
            the next time ``setData()`` is called with new data.
        enableAutoLevels: bool, optional, default True
            Causes the colormap levels to autoscale whenever ``setData()`` is called. 
            It is possible to override this value on a per-change-basis by using the
            ``autoLevels`` keyword argument when calling ``setData()``.
            If ``enableAutoLevels==False`` and ``levels==None``, autoscaling will be 
            performed once when the first z data is supplied. 
        edgecolors : dict, optional
            The color of the edges of the polygons.
            Default None means no edges.
            Only cosmetic pens are supported.
            The dict may contains any arguments accepted by :func:`mkColor() <pyqtgraph.mkColor>`.
            Example: ``mkPen(color=\'w\', width=2)``
        antialiasing : bool, default False
            Whether to draw edgelines with antialiasing.
            Note that if edgecolors is None, antialiasing is always False.
        '''
    def setData(self, *args, **kwargs) -> None:
        '''
        Set the data to be drawn.

        Parameters
        ----------
        x, y : np.ndarray, optional, default None
            2D array containing the coordinates of the polygons
        z : np.ndarray
            2D array containing the value which will be mapped into the polygons
            colors.
            If x and y is None, the polygons will be displaced on a grid
            otherwise x and y will be used as polygons vertices coordinates as::
                
                (x[i+1, j], y[i+1, j])           (x[i+1, j+1], y[i+1, j+1])
                                    +---------+
                                    | z[i, j] |
                                    +---------+
                    (x[i, j], y[i, j])           (x[i, j+1], y[i, j+1])

            "ASCII from: <https://matplotlib.org/3.2.1/api/_as_gen/
                         matplotlib.pyplot.pcolormesh.html>".
        autoLevels: bool, optional
            If set, overrides the value of ``enableAutoLevels``
        '''
    def setLevels(self, levels, update: bool = True) -> None:
        """
        Sets color-scaling levels for the mesh. 
        
        Parameters
        ----------
            levels: tuple
                ``(low, high)`` 
                sets the range for which values can be represented in the colormap.
            update: bool, optional
                Controls if mesh immediately updates to reflect the new color levels.
        """
    def getLevels(self):
        """
        Returns a tuple containing the current level settings. See :func:`~setLevels`.
        The format is ``(low, high)``.
        """
    def setLookupTable(self, lut, update: bool = True) -> None: ...
    def getColorMap(self): ...
    def setColorMap(self, cmap) -> None: ...
    def enableAutoLevels(self) -> None: ...
    def disableAutoLevels(self) -> None: ...
    def paint(self, p, *args) -> None: ...
    def width(self): ...
    def height(self): ...
    def dataBounds(self, ax, frac: float = 1.0, orthoRange: Incomplete | None = None): ...
    def pixelPadding(self): ...
    def boundingRect(self): ...
