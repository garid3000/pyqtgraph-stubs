# from .Qt import QtCore, QtGui
from .Qt import  QtCore, QtGui
import numpy as np
from numpy.typing import NDArray


from _typeshed import Incomplete

__all__ = ['siScale', 'siFormat', 'siParse', 'siEval', 'siApply', 'Color', 'mkColor', 'mkBrush', 'mkPen', 'hsvColor', 'CIELabColor', 'colorCIELab', 'colorDistance', 'colorTuple', 'colorStr', 'intColor', 'glColor', 'makeArrowPath', 'eq', 'affineSliceCoords', 'affineSlice', 'interweaveArrays', 'interpolateArray', 'subArray', 'transformToArray', 'transformCoordinates', 'solve3DTransform', 'solveBilinearTransform', 'clip_scalar', 'clip_array', 'rescaleData', 'applyLookupTable', 'makeRGBA', 'makeARGB', 'makeQImage', 'imageToArray', 'colorToAlpha', 'gaussianFilter', 'downsample', 'arrayToQPath', 'isocurve', 'traceImage', 'isosurface', 'invertQTransform', 'pseudoScatter', 'toposort', 'disconnect', 'SignalBlock']

def siScale(x, minVal: float = 1e-25, allowUnicode: bool = True):
    """
    Return the recommended scale factor and SI prefix string for x.

    Example::

        siScale(0.0001)   # returns (1e6, 'μ')
        # This indicates that the number 0.0001 is best represented as 0.0001 * 1e6 = 100 μUnits
    """
def siFormat(x, precision: int = 3, suffix: str = '', space: bool = True, error: Incomplete | None = None, minVal: float = 1e-25, allowUnicode: bool = True):
    '''
    Return the number x formatted in engineering notation with SI prefix.

    Example::
        siFormat(0.0001, suffix=\'V\')  # returns "100 μV"
    '''
def siParse(s, regex=..., suffix: Incomplete | None = None):
    '''Convert a value written in SI notation to a tuple (number, si_prefix, suffix).

    Example::

        siParse(\'100 µV")  # returns (\'100\', \'µ\', \'V\')

    Note that in the above example, the µ symbol is the "micro sign" (UTF-8
    0xC2B5), as opposed to the Greek letter mu (UTF-8 0xCEBC).

    Parameters
    ----------
    s : str
        The string to parse.
    regex : re.Pattern, optional
        Compiled regular expression object for parsing. The default is a
        general-purpose regex for parsing floating point expressions,
        potentially containing an SI prefix and a suffix.
    suffix : str, optional
        Suffix to check for in ``s``. The default (None) indicates there may or
        may not be a suffix contained in the string and it is returned if
        found. An empty string ``""`` is handled differently: if the string
        contains a suffix, it is discarded. This enables interpreting
        characters following the numerical value as an SI prefix.
    '''
def siEval(s, typ=..., regex=..., suffix: Incomplete | None = None):
    '''
    Convert a value written in SI notation to its equivalent prefixless value.

    Example::

        siEval("100 μV")  # returns 0.0001
    '''
def siApply(val, siprefix):
    """
    """

class Color(QtGui.QColor):
    def __init__(self, *args) -> None: ...
    def glColor(self):
        """Return (r,g,b,a) normalized for use in opengl"""
    def __getitem__(self, ind): ...

def mkColor(*args):
    '''
    Convenience function for constructing QColor from a variety of argument
    types. Accepted arguments are:

    ================ ================================================
     \'c\'             one of: r, g, b, c, m, y, k, w or an SVG color keyword
     R, G, B, [A]    integers 0-255
     (R, G, B, [A])  tuple of integers 0-255
     float           greyscale, 0.0-1.0
     int             see :func:`intColor() <pyqtgraph.intColor>`
     (int, hues)     see :func:`intColor() <pyqtgraph.intColor>`
     "#RGB"
     "#RGBA"
     "#RRGGBB"
     "#RRGGBBAA"
     QColor          QColor instance; makes a copy.
    ================ ================================================
    '''
def mkBrush(*args, **kwds) -> QtGui.QBrush:
    """
    | Convenience function for constructing Brush.
    | This function always constructs a solid brush and accepts the same arguments as :func:`mkColor() <pyqtgraph.mkColor>`
    | Calling mkBrush(None) returns an invisible brush.
    """
def mkPen(*args: str|float|QtCore.Qt.PenStyle, **kargs: str|float|QtCore.Qt.PenStyle) -> QtGui.QPen:
    '''
    Convenience function for constructing QPen.

    Examples::

        mkPen(color)
        mkPen(color, width=2)
        mkPen(cosmetic=False, width=4.5, color=\'r\')
        mkPen({\'color\': "#FF0", width: 2})
        mkPen(None)   # (no pen)

    In these examples, *color* may be replaced with any arguments accepted by :func:`mkColor() <pyqtgraph.mkColor>`    '''
def hsvColor(hue, sat: float = 1.0, val: float = 1.0, alpha: float = 1.0):
    """Generate a QColor from HSVa values. (all arguments are float 0.0-1.0)"""
def CIELabColor(L, a, b, alpha: float = 1.0):
    '''
    Generates as QColor from CIE L*a*b* values.

    Parameters
    ----------
        L: float
            Lightness value ranging from 0 to 100
        a, b: float
            (green/red) and (blue/yellow) coordinates, typically -127 to +127.
        alpha: float, optional
            Opacity, ranging from 0 to 1

    Notes
    -----
    The CIE L*a*b* color space parametrizes color in terms of a luminance `L`
    and the `a` and `b` coordinates that locate the hue in terms of
    a "green to red" and a "blue to yellow" axis.

    These coordinates seek to parametrize human color preception in such a way
    that the Euclidean distance between the coordinates of two colors represents
    the visual difference between these colors. In particular, the difference

    ΔE = sqrt( (L1-L2)² + (a1-a2)² + (b1-b2)² ) = 2.3

    is considered the smallest "just noticeable difference" between colors.

    This simple equation represents the CIE76 standard. Later standards CIE94
    and CIE2000 refine the difference calculation ΔE, while maintaining the
    L*a*b* coordinates.

    Alternative (and arguably more accurate) methods exist to quantify color
    difference, but the CIELab color space remains a convenient approximation.

    Under a known illumination, assumed to be white standard illuminant D65
    here, a CIELab color induces a response in the human eye
    that is described by the tristimulus value XYZ. Once this is known, an
    sRGB color can be calculated to induce the same response.

    More information and underlying mathematics can be found in e.g.
    "CIELab Color Space" by Gernot Hoffmann, available at
    http://docs-hoffmann.de/cielab03022003.pdf .

    Also see :func:`colorDistance() <pyqtgraph.colorDistance>`.
    '''
def colorCIELab(qcol):
    """
    Describes a QColor by an array of CIE L*a*b* values.
    Also see :func:`CIELabColor() <pyqtgraph.CIELabColor>` .

    Parameters
    ----------
    qcol: QColor
        QColor to be converted

    Returns
    -------
    np.ndarray
        Color coordinates `[L, a, b]`.
    """
def colorDistance(colors, metric: str = 'CIE76'):
    '''
    Returns the perceptual distances between a sequence of QColors.
    See :func:`CIELabColor() <pyqtgraph.CIELabColor>` for more information.

    Parameters
    ----------
        colors: list of QColor
            Two or more colors to calculate the distances between.
        metric: str, optional
            Metric used to determined the difference. Only \'CIE76\' is supported at this time,
            where a distance of 2.3 is considered a "just noticeable difference".
            The default may change as more metrics become available.

    Returns
    -------
    List
        The `N-1` sequential distances between `N` colors.
    '''
def colorTuple(c):
    """Return a tuple (R,G,B,A) from a QColor"""
def colorStr(c):
    """Generate a hex string code from a QColor"""
def intColor(index, hues: int = 9, values: int = 1, maxValue: int = 255, minValue: int = 150, maxHue: int = 360, minHue: int = 0, sat: int = 255, alpha: int = 255):
    """
    Creates a QColor from a single index. Useful for stepping through a predefined list of colors.

    The argument *index* determines which color from the set will be returned. All other arguments determine what the set of predefined colors will be

    Colors are chosen by cycling across hues while varying the value (brightness).
    By default, this selects from a list of 9 hues."""
def glColor(*args, **kargs):
    """
    Convert a color to OpenGL color format (r,g,b,a) floats 0.0-1.0
    Accepts same arguments as :func:`mkColor <pyqtgraph.mkColor>`.
    """
def makeArrowPath(headLen: int = 20, headWidth: Incomplete | None = None, tipAngle: int = 20, tailLen: int = 20, tailWidth: int = 3, baseAngle: int = 0):
    """
    Construct a path outlining an arrow with the given dimensions.
    The arrow points in the -x direction with tip positioned at 0,0.
    If *headWidth* is supplied, it overrides *tipAngle* (in degrees).
    If *tailLen* is None, no tail will be drawn.
    """
def eq(a, b):
    """The great missing equivalence function: Guaranteed evaluation to a single bool value.

    This function has some important differences from the == operator:

    1. Returns True if a IS b, even if a==b still evaluates to False.
    2. While a is b will catch the case with np.nan values, special handling is done for distinct
       float('nan') instances using math.isnan.
    3. Tests for equivalence using ==, but silently ignores some common exceptions that can occur
       (AtrtibuteError, ValueError).
    4. When comparing arrays, returns False if the array shapes are not the same.
    5. When comparing arrays of the same shape, returns True only if all elements are equal (whereas
       the == operator would return a boolean array).
    6. Collections (dict, list, etc.) must have the same type to be considered equal. One
       consequence is that comparing a dict to an OrderedDict will always return False.
    """
def affineSliceCoords(shape, origin, vectors, axes):
    """Return the array of coordinates used to sample data arrays in affineSlice().
    """
def affineSlice(data: NDArray[np.uint8, np.int64, np.float64], shape: tuple[int | float, ...] | list[int | float], origin: tuple[int |float, ...] | list[int |float], vectors: tuple[tuple[int | float, ...], ...], axes:tuple[int, ...] | list[int], order: int = 1, returnCoords: bool = False, **kargs):
    """
    Take a slice of any orientation through an array. This is useful for extracting sections of multi-dimensional arrays
    such as MRI images for viewing as 1D or 2D data.

    The slicing axes are aribtrary; they do not need to be orthogonal to the original data or even to each other. It is
    possible to use this function to extract arbitrary linear, rectangular, or parallelepiped shapes from within larger
    datasets. The original data is interpolated onto a new array of coordinates using either interpolateArray if order<2
    or scipy.ndimage.map_coordinates otherwise.

    For a graphical interface to this function, see :func:`ROI.getArrayRegion <pyqtgraph.ROI.getArrayRegion>`

    ==============  ====================================================================================================
    **Arguments:**
    *data*          (ndarray) the original dataset
    *shape*         the shape of the slice to take (Note the return value may have more dimensions than len(shape))
    *origin*        the location in the original dataset that will become the origin of the sliced data.
    *vectors*       list of unit vectors which point in the direction of the slice axes. Each vector must have the same
                    length as *axes*. If the vectors are not unit length, the result will be scaled relative to the
                    original data. If the vectors are not orthogonal, the result will be sheared relative to the
                    original data.
    *axes*          The axes in the original dataset which correspond to the slice *vectors*
    *order*         The order of spline interpolation. Default is 1 (linear). See scipy.ndimage.map_coordinates
                    for more information.
    *returnCoords*  If True, return a tuple (result, coords) where coords is the array of coordinates used to select
                    values from the original dataset.
    *All extra keyword arguments are passed to scipy.ndimage.map_coordinates.*
    --------------------------------------------------------------------------------------------------------------------
    ==============  ====================================================================================================

    Note the following must be true:

        | len(shape) == len(vectors)
        | len(origin) == len(axes) == len(vectors[i])

    Example: start with a 4D fMRI data set, take a diagonal-planar slice out of the last 3 axes

        * data = array with dims (time, x, y, z) = (100, 40, 40, 40)
        * The plane to pull out is perpendicular to the vector (x,y,z) = (1,1,1)
        * The origin of the slice will be at (x,y,z) = (40, 0, 0)
        * We will slice a 20x20 plane from each timepoint, giving a final shape (100, 20, 20)

    The call for this example would look like::

        affineSlice(data, shape=(20,20), origin=(40,0,0), vectors=((-1, 1, 0), (-1, 0, 1)), axes=(1,2,3))

    """
def interweaveArrays(*args):
    """
    Parameters
    ----------

    args : numpy.ndarray
           series of 1D numpy arrays of the same length and dtype

    Returns
    -------
    numpy.ndarray
        A numpy array with all the input numpy arrays interwoven

    Examples
    --------

    >>> result = interweaveArrays(numpy.ndarray([0, 2, 4]), numpy.ndarray([1, 3, 5]))
    >>> result
    array([0, 1, 2, 3, 4, 5])
    """
def interpolateArray(data, x, default: float = 0.0, order: int = 1):
    """
    N-dimensional interpolation similar to scipy.ndimage.map_coordinates.

    This function returns linearly-interpolated values sampled from a regular
    grid of data. It differs from `ndimage.map_coordinates` by allowing broadcasting
    within the input array.

    ==============  ===========================================================================================
    **Arguments:**
    *data*          Array of any shape containing the values to be interpolated.
    *x*             Array with (shape[-1] <= data.ndim) containing the locations within *data* to interpolate.
                    (note: the axes for this argument are transposed relative to the same argument for
                    `ndimage.map_coordinates`).
    *default*       Value to return for locations in *x* that are outside the bounds of *data*.
    *order*         Order of interpolation: 0=nearest, 1=linear.
    ==============  ===========================================================================================

    Returns array of shape (x.shape[:-1] + data.shape[x.shape[-1]:])

    For example, assume we have the following 2D image data::

        >>> data = np.array([[1,   2,   4  ],
                             [10,  20,  40 ],
                             [100, 200, 400]])

    To compute a single interpolated point from this data::

        >>> x = np.array([(0.5, 0.5)])
        >>> interpolateArray(data, x)
        array([ 8.25])

    To compute a 1D list of interpolated locations::

        >>> x = np.array([(0.5, 0.5),
                          (1.0, 1.0),
                          (1.0, 2.0),
                          (1.5, 0.0)])
        >>> interpolateArray(data, x)
        array([  8.25,  20.  ,  40.  ,  55.  ])

    To compute a 2D array of interpolated locations::

        >>> x = np.array([[(0.5, 0.5), (1.0, 2.0)],
                          [(1.0, 1.0), (1.5, 0.0)]])
        >>> interpolateArray(data, x)
        array([[  8.25,  40.  ],
               [ 20.  ,  55.  ]])

    ..and so on. The *x* argument may have any shape as long as
    ```x.shape[-1] <= data.ndim```. In the case that
    ```x.shape[-1] < data.ndim```, then the remaining axes are simply
    broadcasted as usual. For example, we can interpolate one location
    from an entire row of the data::

        >>> x = np.array([[0.5]])
        >>> interpolateArray(data, x)
        array([[  5.5,  11. ,  22. ]])

    This is useful for interpolating from arrays of colors, vertexes, etc.
    """
def subArray(data, offset, shape, stride):
    """
    Unpack a sub-array from *data* using the specified offset, shape, and stride.

    Note that *stride* is specified in array elements, not bytes.
    For example, we have a 2x3 array packed in a 1D array as follows::

        data = [_, _, 00, 01, 02, _, 10, 11, 12, _]

    Then we can unpack the sub-array with this call::

        subArray(data, offset=2, shape=(2, 3), stride=(4, 1))

    ..which returns::

        [[00, 01, 02],
         [10, 11, 12]]

    This function operates only on the first axis of *data*. So changing
    the input in the example above to have shape (10, 7) would cause the
    output to have shape (2, 3, 7).
    """
def transformToArray(tr):
    """
    Given a QTransform, return a 3x3 numpy array.
    Given a QMatrix4x4, return a 4x4 numpy array.

    Example: map an array of x,y coordinates through a transform::

        ## coordinates to map are (1,5), (2,6), (3,7), and (4,8)
        coords = np.array([[1,2,3,4], [5,6,7,8], [1,1,1,1]])  # the extra '1' coordinate is needed for translation to work

        ## Make an example transform
        tr = QtGui.QTransform()
        tr.translate(3,4)
        tr.scale(2, 0.1)

        ## convert to array
        m = pg.transformToArray()[:2]  # ignore the perspective portion of the transformation

        ## map coordinates through transform
        mapped = np.dot(m, coords)
    """
def transformCoordinates(tr, coords, transpose: bool = False):
    """
    Map a set of 2D or 3D coordinates through a QTransform or QMatrix4x4.
    The shape of coords must be (2,...) or (3,...)
    The mapping will _ignore_ any perspective transformations.

    For coordinate arrays with ndim=2, this is basically equivalent to matrix multiplication.
    Most arrays, however, prefer to put the coordinate axis at the end (eg. shape=(...,3)). To
    allow this, use transpose=True.

    """
def solve3DTransform(points1, points2):
    """
    Find a 3D transformation matrix that maps points1 onto points2.
    Points must be specified as either lists of 4 Vectors or
    (4, 3) arrays.
    """
def solveBilinearTransform(points1, points2):
    """
    Find a bilinear transformation matrix (2x4) that maps points1 onto points2.
    Points must be specified as a list of 4 Vector, Point, QPointF, etc.

    To use this matrix to map a point [x,y]::

        mapped = np.dot(matrix, [x*y, x, y, 1])
    """
def clip_scalar(val, vmin, vmax):
    """ convenience function to avoid using np.clip for scalar values """
def clip_array(arr, vmin, vmax, out: Incomplete | None = None): ...

clip_array: Incomplete

def rescaleData(data, scale, offset, dtype: Incomplete | None = None, clip: Incomplete | None = None):
    """Return data rescaled and optionally cast to a new dtype.

    The scaling operation is::

        data => (data-offset) * scale
    """
def applyLookupTable(data, lut):
    """
    Uses values in *data* as indexes to select values from *lut*.
    The returned data has shape data.shape + lut.shape[1:]

    Note: color gradient lookup tables can be generated using GradientWidget.

    Parameters
    ----------
    data : np.ndarray
    lut : np.ndarray
        Either cupy or numpy arrays are accepted, though this function has only
        consistently behaved correctly on windows with cuda toolkit version >= 11.1.
    """
def makeRGBA(*args, **kwds):
    """Equivalent to makeARGB(..., useRGBA=True)"""
def makeARGB(data, lut: Incomplete | None = None, levels: Incomplete | None = None, scale: Incomplete | None = None, useRGBA: bool = False, maskNans: bool = True, output: Incomplete | None = None):
    """
    Convert an array of values into an ARGB array suitable for building QImages,
    OpenGL textures, etc.

    Returns the ARGB array (unsigned byte) and a boolean indicating whether
    there is alpha channel data. This is a two stage process:

        1) Rescale the data based on the values in the *levels* argument (min, max).
        2) Determine the final output by passing the rescaled values through a
           lookup table.

    Both stages are optional.

    ============== ==================================================================================
    **Arguments:**
    data           numpy array of int/float types. If
    levels         List [min, max]; optionally rescale data before converting through the
                   lookup table. The data is rescaled such that min->0 and max->*scale*::

                      rescaled = (clip(data, min, max) - min) * (*scale* / (max - min))

                   It is also possible to use a 2D (N,2) array of values for levels. In this case,
                   it is assumed that each pair of min,max values in the levels array should be
                   applied to a different subset of the input data (for example, the input data may
                   already have RGB values and the levels are used to independently scale each
                   channel). The use of this feature requires that levels.shape[0] == data.shape[-1].
    scale          The maximum value to which data will be rescaled before being passed through the
                   lookup table (or returned if there is no lookup table). By default this will
                   be set to the length of the lookup table, or 255 if no lookup table is provided.
    lut            Optional lookup table (array with dtype=ubyte).
                   Values in data will be converted to color by indexing directly from lut.
                   The output data shape will be input.shape + lut.shape[1:].
                   Lookup tables can be built using ColorMap or GradientWidget.
    useRGBA        If True, the data is returned in RGBA order (useful for building OpenGL textures).
                   The default is False, which returns in ARGB order for use with QImage
                   (Note that 'ARGB' is a term used by the Qt documentation; the *actual* order
                   is BGRA).
    maskNans       Enable or disable masking NaNs as transparent. Converting NaN values to ints is
                   undefined behavior per the C-standard, results may vary across platforms. Highly
                   recommend leaving this option to the default value of True.
    ============== ==================================================================================
    """
def makeQImage(imgData, alpha: Incomplete | None = None, copy: bool = True, transpose: bool = True):
    """
    Turn an ARGB array into QImage.
    By default, the data is copied; changes to the array will not
    be reflected in the image. The image will be given a 'data' attribute
    pointing to the array which shares its data to prevent python
    freeing that memory while the image is in use.

    ============== ===================================================================
    **Arguments:**
    imgData        Array of data to convert. Must have shape (height, width),
                   (height, width, 3), or (height, width, 4). If transpose is
                   True, then the first two axes are swapped. The array dtype
                   must be ubyte. For 2D arrays, the value is interpreted as
                   greyscale. For 3D arrays, the order of values in the 3rd
                   axis must be (b, g, r, a).
    alpha          If the input array is 3D and *alpha* is True, the QImage
                   returned will have format ARGB32. If False,
                   the format will be RGB32. By default, _alpha_ is True if
                   array.shape[2] == 4.
    copy           If True, the data is copied before converting to QImage.
                   If False, the new QImage points directly to the data in the array.
                   Note that the array must be contiguous for this to work
                   (see numpy.ascontiguousarray).
    transpose      If True (the default), the array x/y axes are transposed before
                   creating the image. Note that Qt expects the axes to be in
                   (height, width) order whereas pyqtgraph usually prefers the
                   opposite.
    ============== ===================================================================
    """
def imageToArray(img, copy: bool = False, transpose: bool = True):
    """
    Convert a QImage into numpy array. The image must have format RGB32, ARGB32, or ARGB32_Premultiplied.
    By default, the image is not copied; changes made to the array will appear in the QImage as well (beware: if
    the QImage is collected before the array, there may be trouble).
    The array will have shape (width, height, (b,g,r,a)).
    """
def colorToAlpha(data, color):
    """
    Given an RGBA image in *data*, convert *color* to be transparent.
    *data* must be an array (w, h, 3 or 4) of ubyte values and *color* must be
    an array (3) of ubyte values.
    This is particularly useful for use with images that have a black or white background.

    Algorithm is taken from Gimp's color-to-alpha function in plug-ins/common/colortoalpha.c
    Credit:
        /*
        * Color To Alpha plug-in v1.0 by Seth Burgess, sjburges@gimp.org 1999/05/14
        *  with algorithm by clahey
        */

    """
def gaussianFilter(data, sigma):
    """
    Drop-in replacement for scipy.ndimage.gaussian_filter.

    (note: results are only approximately equal to the output of
     gaussian_filter)
    """
def downsample(data, n, axis: int = 0, xvals: str = 'subsample'):
    """Downsample by averaging points together across axis.
    If multiple axes are specified, runs once per axis.
    If a metaArray is given, then the axis values can be either subsampled
    or downsampled to match.
    """
def arrayToQPath(x, y, connect: str = 'all', finiteCheck: bool = True):
    """
    Convert an array of x,y coordinates to QPainterPath as efficiently as
    possible. The *connect* argument may be 'all', indicating that each point
    should be connected to the next; 'pairs', indicating that each pair of
    points should be connected, or an array of int32 values (0 or 1) indicating
    connections.

    Parameters
    ----------
    x : np.ndarray
        x-values to be plotted of shape (N,)
    y : np.ndarray
        y-values to be plotted, must be same length as `x` of shape (N,)
    connect : {'all', 'pairs', 'finite', (N,) ndarray}, optional
        Argument detailing how to connect the points in the path. `all` will
        have sequential points being connected.  `pairs` generates lines
        between every other point.  `finite` only connects points that are
        finite.  If an ndarray is passed, containing int32 values of 0 or 1,
        only values with 1 will connect to the previous point.  Def
    finiteCheck : bool, default True
        When false, the check for finite values will be skipped, which can
        improve performance. If nonfinite values are present in `x` or `y`,
        an empty QPainterPath will be generated.

    Returns
    -------
    QPainterPath
        QPainterPath object to be drawn

    Raises
    ------
    ValueError
        Raised when the connect argument has an invalid value placed within.

    Notes
    -----
    A QPainterPath is generated through one of two ways.  When the connect
    parameter is 'all', a QPolygonF object is created, and
    ``QPainterPath.addPolygon()`` is called.  For other connect parameters
    a ``QDataStream`` object is created and the QDataStream >> QPainterPath
    operator is used to pass the data.  The memory format is as follows

    numVerts(i4)
    0(i4)   x(f8)   y(f8)    <-- 0 means this vertex does not connect
    1(i4)   x(f8)   y(f8)    <-- 1 means this vertex connects to the previous vertex
    ...
    cStart(i4)   fillRule(i4)

    see: https://github.com/qt/qtbase/blob/dev/src/gui/painting/qpainterpath.cpp

    All values are big endian--pack using struct.pack('>d') or struct.pack('>i')
    This binary format may change in future versions of Qt
    """
def isocurve(data, level, connected: bool = False, extendToEdge: bool = False, path: bool = False):
    """
    Generate isocurve from 2D data using marching squares algorithm.

    ============== =========================================================
    **Arguments:**
    data           2D numpy array of scalar values
    level          The level at which to generate an isosurface
    connected      If False, return a single long list of point pairs
                   If True, return multiple long lists of connected point
                   locations. (This is slower but better for drawing
                   continuous lines)
    extendToEdge   If True, extend the curves to reach the exact edges of
                   the data.
    path           if True, return a QPainterPath rather than a list of
                   vertex coordinates. This forces connected=True.
    ============== =========================================================

    This function is SLOW; plenty of room for optimization here.
    """
def traceImage(image, values, smooth: float = 0.5):
    """
    Convert an image to a set of QPainterPath curves.
    One curve will be generated for each item in *values*; each curve outlines the area
    of the image that is closer to its value than to any others.

    If image is RGB or RGBA, then the shape of values should be (nvals, 3/4)
    The parameter *smooth* is expressed in pixels.
    """
def isosurface(data, level):
    '''
    Generate isosurface from volumetric data using marching cubes algorithm.
    See Paul Bourke, "Polygonising a Scalar Field"
    (http://paulbourke.net/geometry/polygonise/)

    *data*   3D numpy array of scalar values. Must be contiguous.
    *level*  The level at which to generate an isosurface

    Returns an array of vertex coordinates (Nv, 3) and an array of
    per-face vertex indexes (Nf, 3)
    '''
def invertQTransform(tr):
    """Return a QTransform that is the inverse of *tr*.
    A pseudo-inverse is returned if tr is not invertible.

    Note that this function is preferred over QTransform.inverted() due to
    bugs in that method. (specifically, Qt has floating-point precision issues
    when determining whether a matrix is invertible)
    """
def pseudoScatter(data, spacing: Incomplete | None = None, shuffle: bool = True, bidir: bool = False, method: str = 'exact'):
    """Return an array of position values needed to make beeswarm or column scatter plots.

    Used for examining the distribution of values in an array.

    Given an array of x-values, construct an array of y-values such that an x,y scatter-plot
    will not have overlapping points (it will look similar to a histogram).
    """
def toposort(deps, nodes: Incomplete | None = None, seen: Incomplete | None = None, stack: Incomplete | None = None, depth: int = 0):
    '''Topological sort. Arguments are:
      deps    dictionary describing dependencies where a:[b,c] means "a depends on b and c"
      nodes   optional, specifies list of starting nodes (these should be the nodes
              which are not depended on by any other nodes). Other candidate starting
              nodes will be ignored.

    Example::

        # Sort the following graph:
        #
        #   B ──┬─────> C <── D
        #       │       │
        #   E <─┴─> A <─┘
        #
        deps = {\'a\': [\'b\', \'c\'], \'c\': [\'b\', \'d\'], \'e\': [\'b\']}
        toposort(deps)
         => [\'b\', \'d\', \'c\', \'a\', \'e\']
    '''
def disconnect(signal, slot):
    """Disconnect a Qt signal from a slot.

    This method augments Qt's Signal.disconnect():

      * Return bool indicating whether disconnection was successful, rather than
        raising an exception
      * Attempt to disconnect prior versions of the slot when using pg.reload
    """

class SignalBlock:
    """Class used to temporarily block a Qt signal connection::

        with SignalBlock(signal, slot):
            # do something that emits a signal; it will
            # not be delivered to slot
    """
    signal: Incomplete
    slot: Incomplete
    def __init__(self, signal, slot) -> None: ...
    reconnect: Incomplete
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...
