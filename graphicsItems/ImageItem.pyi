from .GraphicsObject import GraphicsObject
from _typeshed import Incomplete

__all__ = ['ImageItem']

class ImageItem(GraphicsObject):
    """
    **Bases:** :class:`GraphicsObject <pyqtgraph.GraphicsObject>`
    """
    sigImageChanged: Incomplete
    sigRemoveRequested: Incomplete
    menu: Incomplete
    image: Incomplete
    qimage: Incomplete
    paintMode: Incomplete
    levels: Incomplete
    lut: Incomplete
    autoDownsample: bool
    axisOrder: Incomplete
    drawKernel: Incomplete
    border: Incomplete
    removable: bool
    def __init__(self, image: Incomplete | None = None, **kargs) -> None:
        """
        See :func:`~pyqtgraph.ImageItem.setOpts` for further keyword arguments and 
        and :func:`~pyqtgraph.ImageItem.setImage` for information on supported formats.

        Parameters
        ----------
            image: np.ndarray, optional
                Image data
        """
    def setCompositionMode(self, mode) -> None:
        """
        Change the composition mode of the item. This is useful when overlaying
        multiple items.
        
        Parameters
        ----------
        mode : ``QtGui.QPainter.CompositionMode``
            Composition of the item, often used when overlaying items.  Common
            options include:

            ``QPainter.CompositionMode.CompositionMode_SourceOver`` (Default)
            Image replaces the background if it is opaque. Otherwise, it uses
            the alpha channel to blend the image with the background.

            ``QPainter.CompositionMode.CompositionMode_Overlay`` Image color is
            mixed with the background color to reflect the lightness or
            darkness of the background

            ``QPainter.CompositionMode.CompositionMode_Plus`` Both the alpha
            and color of the image and background pixels are added together.

            ``QPainter.CompositionMode.CompositionMode_Plus`` The output is the
            image color multiplied by the background.

            See ``QPainter::CompositionMode`` in the Qt Documentation for more
            options and details
        """
    def setBorder(self, b) -> None:
        """
        Defines the border drawn around the image. Accepts all arguments supported by 
        :func:`~pyqtgraph.mkPen`.
        """
    def width(self): ...
    def height(self): ...
    def channels(self): ...
    def boundingRect(self): ...
    def setLevels(self, levels, update: bool = True) -> None:
        """
        Sets image scaling levels. 
        See :func:`makeARGB <pyqtgraph.makeARGB>` for more details on how levels are applied.
        
        Parameters
        ----------
            levels: array_like
                - ``[blackLevel, whiteLevel]`` 
                  sets black and white levels for monochrome data and can be used with a lookup table.
                - ``[[minR, maxR], [minG, maxG], [minB, maxB]]``
                  sets individual scaling for RGB values. Not compatible with lookup tables.
            update: bool, optional
                Controls if image immediately updates to reflect the new levels.
        """
    def getLevels(self):
        """
        Returns the list representing the current level settings. See :func:`~setLevels`.
        When ``autoLevels`` is active, the format is ``[blackLevel, whiteLevel]``.
        """
    def setColorMap(self, colorMap) -> None:
        """
        Sets a color map for false color display of a monochrome image.

        Parameters
        ----------
        colorMap : :class:`~pyqtgraph.ColorMap` or `str`
            A string argument will be passed to :func:`colormap.get() <pyqtgraph.colormap.get>`
        """
    def getColorMap(self):
        """
        Returns the assigned :class:`pyqtgraph.ColorMap`, or `None` if not available
        """
    def setLookupTable(self, lut, update: bool = True) -> None:
        """
        Sets lookup table ``lut`` to use for false color display of a monochrome image. See :func:`makeARGB <pyqtgraph.makeARGB>` for more 
        information on how this is used. Optionally, `lut` can be a callable that accepts the current image as an
        argument and returns the lookup table to use.

        Ordinarily, this table is supplied by a :class:`~pyqtgraph.HistogramLUTItem`,
        :class:`~pyqtgraph.GradientEditorItem` or :class:`~pyqtgraph.ColorBarItem`.
        
        Setting ``update = False`` avoids an immediate image update.
        """
    def setAutoDownsample(self, active: bool = True) -> None:
        """
        Controls automatic downsampling for this ImageItem.

        If `active` is `True`, the image is automatically downsampled to match the
        screen resolution. This improves performance for large images and
        reduces aliasing. If `autoDownsample` is not specified, then ImageItem will
        choose whether to downsample the image based on its size.
        
        `False` disables automatic downsampling.
        """
    def setOpts(self, update: bool = True, **kargs) -> None:
        """
        Sets display and processing options for this ImageItem. :func:`~pyqtgraph.ImageItem.__init__` and 
        :func:`~pyqtgraph.ImageItem.setImage` support all keyword arguments listed here.

        Parameters
        ----------
            autoDownsample: bool
                See :func:`~pyqtgraph.ImageItem.setAutoDownsample`.
            axisOrder: str
                | `'col-major'`: The shape of the array represents (width, height) of the image. This is the default.
                | `'row-major'`: The shape of the array represents (height, width).
            border: bool
                Sets a pen to draw to draw an image border. See :func:`~pyqtgraph.ImageItem.setBorder`.
            compositionMode:
                See :func:`~pyqtgraph.ImageItem.setCompositionMode`
            colorMap: :class:`~pyqtgraph.ColorMap` or `str`
                Sets a color map. A string will be passed to :func:`colormap.get() <pyqtgraph.colormap.get()>`
            lut: array_like
                Sets a color lookup table to use when displaying the image.
                See :func:`~pyqtgraph.ImageItem.setLookupTable`.
            levels: array_like
                Shape of (min, max). Sets minimum and maximum values to use when
                rescaling the image data. By default, these will be set to the
                estimated minimum and maximum values in the image. If the image array
                has dtype uint8, no rescaling is necessary. See
                :func:`~pyqtgraph.ImageItem.setLevels`.
            opacity: float
                Overall opacity for an RGB image. Between 0.0-1.0.
            rect: :class:`QRectF`, :class:`QRect` or array_like
                Displays the current image within the specified rectangle in plot
                coordinates. If ``array_like``, should be of the of ``floats 
                (`x`,`y`,`w`,`h`)`` . See :func:`~pyqtgraph.ImageItem.setRect`.
            update : bool, optional
                Controls if image immediately updates to reflect the new options.
        """
    def setRect(self, *args) -> None:
        """
        setRect(rect) or setRect(x,y,w,h)
        
        Sets translation and scaling of this ImageItem to display the current image within the rectangle given
        as ``rect`` (:class:`QtCore.QRect` or :class:`QtCore.QRectF`), or described by parameters `x, y, w, h`, 
        defining starting position, width and height.

        This method cannot be used before an image is assigned.
        See the :ref:`examples <ImageItem_examples>` for how to manually set transformations.
        """
    def clear(self) -> None:
        """
        Clears the assigned image.
        """
    def setImage(self, image: Incomplete | None = None, autoLevels: Incomplete | None = None, **kargs) -> None:
        """
        Updates the image displayed by this ImageItem. For more information on how the image
        is processed before displaying, see :func:`~pyqtgraph.makeARGB`.
        
        For backward compatibility, image data is assumed to be in column-major order (column, row) by default.
        However, most data is stored in row-major order (row, column). It can either be transposed before assignment::

            imageitem.setImage(imagedata.T)
        
        or the interpretation of the data can be changed locally through the ``axisOrder`` keyword or by changing the 
        `imageAxisOrder` :ref:`global configuration option <apiref_config>`
        
        All keywords supported by :func:`~pyqtgraph.ImageItem.setOpts` are also allowed here.

        Parameters
        ----------
        image: np.ndarray, optional
            Image data given as NumPy array with an integer or floating
            point dtype of any bit depth. A 2-dimensional array describes single-valued (monochromatic) data.
            A 3-dimensional array is used to give individual color components. The third dimension must
            be of length 3 (RGB) or 4 (RGBA).
        rect: QRectF or QRect or array_like, optional
            If given, sets translation and scaling to display the image within the
            specified rectangle. If ``array_like`` should be the form of floats
            ``[x, y, w, h]`` See :func:`~pyqtgraph.ImageItem.setRect`
        autoLevels: bool, optional
            If `True`, ImageItem will automatically select levels based on the maximum and minimum values encountered 
            in the data. For performance reasons, this search subsamples the images and may miss individual bright or
            or dark points in the data set.
            
            If `False`, the search will be omitted.

            The default is `False` if a ``levels`` keyword argument is given, and `True` otherwise.
        levelSamples: int, default 65536
            When determining minimum and maximum values, ImageItem
            only inspects a subset of pixels no larger than this number.
            Setting this larger than the total number of pixels considers all values.
        """
    def dataTransform(self):
        """
        Returns the transform that maps from this image's input array to its
        local coordinate system.

        This transform corrects for the transposition that occurs when image data
        is interpreted in row-major order.
        
        :meta private:
        """
    def inverseDataTransform(self):
        """Return the transform that maps from this image's local coordinate
        system to its input array.

        See dataTransform() for more information.

        :meta private:
        """
    def mapToData(self, obj): ...
    def mapFromData(self, obj): ...
    def quickMinMax(self, targetSize: float = 1000000.0):
        """
        Estimates the min/max values of the image data by subsampling.
        Subsampling is performed at regular strides chosen to evaluate a number of samples
        equal to or less than `targetSize`.
        
        Returns (`min`, `max`).
        """
    def updateImage(self, *args, **kargs): ...
    def render(self) -> None: ...
    def paint(self, p, *args) -> None: ...
    def save(self, fileName, *args) -> None:
        """
        Saves this image to file. Note that this saves the visible image (after scale/color changes), not the 
        original data.
        """
    def getHistogram(self, bins: str = 'auto', step: str = 'auto', perChannel: bool = False, targetImageSize: int = 200, targetHistogramSize: int = 500, **kwds):
        """
        Returns `x` and `y` arrays containing the histogram values for the current image.
        For an explanation of the return format, see :func:`numpy.histogram()`.

        The `step` argument causes pixels to be skipped when computing the histogram to save time.
        If `step` is 'auto', then a step is chosen such that the analyzed data has
        dimensions approximating `targetImageSize` for each axis.

        The `bins` argument and any extra keyword arguments are passed to
        :func:`numpy.histogram()`. If `bins` is `auto`, a bin number is automatically
        chosen based on the image characteristics:

          * Integer images will have approximately `targetHistogramSize` bins,
            with each bin having an integer width.
          * All other types will have `targetHistogramSize` bins.

        If `perChannel` is `True`, then a histogram is computed for each channel, 
        and the output is a list of the results.
        """
    def setPxMode(self, b) -> None:
        """
        Sets whether the item ignores transformations and draws directly to screen pixels.
        If `True`, the item will not inherit any scale or rotation transformations from its
        parent items, but its position will be transformed as usual.
        (see ``GraphicsItem::ItemIgnoresTransformations`` in the Qt documentation)
        """
    def setScaledMode(self) -> None: ...
    def getPixmap(self): ...
    def pixelSize(self):
        """
        Returns the scene-size of a single pixel in the image
        """
    def viewTransformChanged(self) -> None: ...
    def mouseDragEvent(self, ev) -> None: ...
    def mouseClickEvent(self, ev) -> None: ...
    def raiseContextMenu(self, ev): ...
    def getMenu(self): ...
    def hoverEvent(self, ev) -> None: ...
    def tabletEvent(self, ev) -> None: ...
    def drawAt(self, pos, ev: Incomplete | None = None) -> None: ...
    drawKernelCenter: Incomplete
    drawMode: Incomplete
    drawMask: Incomplete
    def setDrawKernel(self, kernel: Incomplete | None = None, mask: Incomplete | None = None, center=(0, 0), mode: str = 'set') -> None: ...
    removeTimer: Incomplete
    def removeClicked(self) -> None: ...
    def emitRemoveRequested(self) -> None: ...
