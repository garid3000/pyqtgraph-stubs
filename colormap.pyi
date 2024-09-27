from _typeshed import Incomplete

__all__ = ['ColorMap']

class ColorMap:
    """
    ColorMap(pos, color, mapping=ColorMap.CLIP)

    ColorMap stores a mapping of specific data values to colors, for example:

        | 0.0 → black
        | 0.2 → red
        | 0.6 → yellow
        | 1.0 → white

    The colors for intermediate values are determined by interpolating between
    the two nearest colors in RGB color space.

    A ColorMap object provides access to the interpolated colors by indexing with a float value:
    ``cm[0.5]`` returns a QColor corresponding to the center of ColorMap `cm`.
    """
    CLIP: int
    REPEAT: int
    MIRROR: int
    DIVERGING: int
    BYTE: int
    FLOAT: int
    QCOLOR: int
    enumMap: Incomplete
    name: Incomplete
    pos: Incomplete
    color: Incomplete
    mapping_mode: Incomplete
    stopsCache: Incomplete
    def __init__(self, pos, color, mapping=..., mode: Incomplete | None = None, linearize: bool = False, name: str = '') -> None:
        """
        __init__(pos, color, mapping=ColorMap.CLIP)
        
        Parameters
        ----------
        pos: array_like of float, optional
            Assigned positions of specified colors. `None` sets equal spacing.
            Values need to be in range 0.0-1.0.
        color: array_like of color_like
            List of colors, interpreted via :func:`mkColor() <pyqtgraph.mkColor>`.
        mapping: str or int, optional
            Controls how values outside the 0 to 1 range are mapped to colors.
            See :func:`setMappingMode() <ColorMap.setMappingMode>` for details. 
            
            The default of `ColorMap.CLIP` continues to show
            the colors assigned to 0 and 1 for all values below or above this range, respectively.
        """
    def setMappingMode(self, mapping) -> None:
        """
        Sets the way that values outside of the range 0 to 1 are mapped to colors.

        Parameters
        ----------
        mapping: int or str
            Sets mapping mode to

            - `ColorMap.CLIP` or 'clip': Values are clipped to the range 0 to 1. ColorMap defaults to this.
            - `ColorMap.REPEAT` or 'repeat': Colors repeat cyclically, i.e. range 1 to 2 repeats the colors for 0 to 1.
            - `ColorMap.MIRROR` or 'mirror': The range 0 to -1 uses same colors (in reverse order) as 0 to 1.
            - `ColorMap.DIVERGING` or 'diverging': Colors are mapped to -1 to 1 such that the central value appears at 0.
        """
    def __getitem__(self, key):
        """ Convenient shorthand access to palette colors """
    def linearize(self) -> None:
        """
        Adjusts the positions assigned to color stops to approximately equalize the perceived color difference
        for a fixed step.
        """
    def reverse(self) -> None:
        """
        Reverses the color map, so that the color assigned to a value of 1 now appears at 0 and vice versa.
        This is convenient to adjust imported color maps.
        """
    def getSubset(self, start, span):
        """
        Returns a new ColorMap object that extracts the subset specified by 'start' and 'length' 
        to the full 0.0 to 1.0 range. A negative length results in a color map that is reversed 
        relative to the original.
        
        Parameters
        ----------
        start : float
                Starting value that defines the 0.0 value of the new color map.
                Possible value between 0.0 to 1.0
        span  : float
                Span of the extracted region. The original color map will be 
                treated as cyclical if the extracted interval exceeds the 
                0.0 to 1.0 range.  Possible values between -1.0 to 1.0.
        """
    def map(self, data, mode=...):
        """
        map(data, mode=ColorMap.BYTE)

        Returns an array of colors corresponding to a single value or an array of values.
        Data must be either a scalar position or an array (any shape) of positions.

        Parameters
        ----------
        data: float or array_like of float
            Scalar value(s) to be mapped to colors

        mode: str or int, optional
            Determines return format:

              - `ColorMap.BYTE` or 'byte': Colors are returned as 0-255 unsigned bytes. (default)
              - `ColorMap.FLOAT` or 'float': Colors are returned as 0.0-1.0 floats.
              - `ColorMap.QCOLOR` or 'qcolor': Colors are returned as QColor objects.

        Returns
        -------
        np.ndarray of {``ColorMap.BYTE``, ``ColorMap.FLOAT``, QColor}
            for `ColorMap.BYTE` or `ColorMap.FLOAT`:

            RGB values for each `data` value, arranged in the same shape as `data`.
        list of QColor
            for `ColorMap.QCOLOR`:

            Colors for each `data` value as QColor objects.
        """
    def mapToQColor(self, data):
        """Convenience function; see :func:`map() <pyqtgraph.ColorMap.map>`."""
    def mapToByte(self, data):
        """Convenience function; see :func:`map() <pyqtgraph.ColorMap.map>`."""
    def mapToFloat(self, data):
        """Convenience function; see :func:`map() <pyqtgraph.ColorMap.map>`."""
    def getByIndex(self, idx):
        """Retrieve a QColor by the index of the stop it is assigned to."""
    def getGradient(self, p1: Incomplete | None = None, p2: Incomplete | None = None):
        """
        Returns a QtGui.QLinearGradient corresponding to this ColorMap.
        The span and orientation is given by two points in plot coordinates.

        When no parameters are given for `p1` and `p2`, the gradient is mapped to the
        `y` coordinates 0 to 1, unless the color map is defined for a more limited range.
        
        This is a somewhat expensive operation, and it is recommended to store and reuse the returned
        gradient instead of repeatedly regenerating it.

        Parameters
        ----------
        p1: QtCore.QPointF, optional
            Starting point (value 0) of the gradient. Default value is QPointF(0., 0.)
        p2: QtCore.QPointF, optional
            End point (value 1) of the gradient. Default parameter `dy` is the span of ``max(pos) - min(pos)``
            over which the color map is defined, typically `dy=1`.  Default is QPointF(dy, 0.)
        """
    def getBrush(self, span=(0.0, 1.0), orientation: str = 'vertical'):
        """
        Returns a QBrush painting with the color map applied over the selected span of plot values.
        When the mapping mode is set to `ColorMap.MIRROR`, the selected span includes the color map twice,
        first in reversed order and then normal.
        
        It is recommended to store and reuse this gradient brush instead of regenerating it repeatedly.

        Parameters
        ----------
        span : tuple of float, optional
            Span of data values covered by the gradient:

              - Color map value 0.0 will appear at `min`,
              - Color map value 1.0 will appear at `max`.
            
            Default value is (0., 1.)

        orientation : str, default 'vertical'
            Orientation of the gradient:

              - 'vertical': `span` corresponds to the `y` coordinate.
              - 'horizontal': `span` corresponds to the `x` coordinate.
        """
    def getPen(self, span=(0.0, 1.0), orientation: str = 'vertical', width: float = 1.0):
        """
        Returns a QPen that draws according to the color map based on vertical or horizontal position.
        
        It is recommended to store and reuse this gradient pen instead of regenerating it repeatedly.


        Parameters
        ----------
        span : tuple of float
            Span of the data values covered by the gradient:

              - Color map value 0.0 will appear at `min`.
              - Color map value 1.0 will appear at `max`.

            Default is (0., 1.)
        orientation : str, default 'vertical'
            Orientation of the gradient:

              - 'vertical' creates a vertical gradient, where `span` corresponds to the `y` coordinate.
              - 'horizontal' creates a horizontal gradient, where `span` corresponds to the `x` coordinate.

        width : int or float
            Width of the pen in pixels on screen.
        """
    def getColors(self, mode=...):
        """
        Returns a list of the colors associated with the stops of the color map.
        
        The parameter `mode` can be one of
            - `ColorMap.BYTE` or 'byte' to return colors as RGBA tuples in byte format (0 to 255)
            - `ColorMap.FLOAT` or 'float' to return colors as RGBA tuples in float format (0.0 to 1.0)
            - `ColorMap.QCOLOR` or 'qcolor' to return a list of QColors
            
        The default is byte format.
        """
    def getStops(self, mode=...):
        """
        Returns a tuple (stops, colors) containing a list of all stops (ranging 0.0 to 1.0)
        and a list of the associated colors.
        
        The parameter `mode` can be one of
            - `ColorMap.BYTE` or 'byte' to return colors as RGBA tuples in byte format (0 to 255)
            - `ColorMap.FLOAT` or 'float' to return colors as RGBA tuples in float format (0.0 to 1.0)
            - `ColorMap.QCOLOR` or 'qcolor' to return a list of QColors

        The default is byte format.
        """
    def getLookupTable(self, start: float = 0.0, stop: float = 1.0, nPts: int = 512, alpha: Incomplete | None = None, mode=...):
        """
        getLookupTable(start=0.0, stop=1.0, nPts=512, alpha=None, mode=ColorMap.BYTE)

        Returns an equally-spaced lookup table of RGB(A) values created
        by interpolating the specified color stops.

        Parameters
        ----------
        start:  float, default=0.0
            The starting value in the lookup table
        stop: float, default=1.0
            The final value in the lookup table
        nPts: int, default=512
            The number of points in the returned lookup table.
        alpha: bool, optional
            Specifies whether or not alpha values are included in the table.
            If alpha is None, it will be automatically determined.
        mode: int or str, default='byte'
            Determines return type as described in :func:`map() <pyqtgraph.ColorMap.map>`, can be
            either `ColorMap.BYTE` (0 to 255), `ColorMap.FLOAT` (0.0 to 1.0) or `ColorMap.QColor`.

        Returns
        -------
        np.ndarray of {``ColorMap.BYTE``, ``ColorMap.FLOAT``}
            for `ColorMap.BYTE` or `ColorMap.FLOAT`:

            RGB values for each `data` value, arranged in the same shape as `data`.
            If alpha values are included the array has shape (`nPts`, 4), otherwise (`nPts`, 3).
    
        list of QColor
            for `ColorMap.QCOLOR`:

            Colors for each `data` value as QColor objects.
        """
    def usesAlpha(self):
        """Returns `True` if any stops have assigned colors with alpha < 255."""
    def isMapTrivial(self):
        """
        Returns `True` if the gradient has exactly two stops in it: Black at 0.0 and white at 1.0.
        """
    def __eq__(self, other): ...
