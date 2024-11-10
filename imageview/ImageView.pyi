from .. import getConfigOption as getConfigOption
from ..Qt import QtCore as QtCore, QtGui as QtGui, QtWidgets as QtWidgets
from ..SignalProxy import SignalProxy as SignalProxy
from ..graphicsItems.GradientEditorItem import (
    addGradientListToDocstring as addGradientListToDocstring,
)
from ..graphicsItems.ImageItem import ImageItem as ImageItem
from ..graphicsItems.InfiniteLine import InfiniteLine as InfiniteLine
from ..graphicsItems.LinearRegionItem import LinearRegionItem as LinearRegionItem
from ..graphicsItems.ROI import ROI as ROI
from ..graphicsItems.VTickGroup import VTickGroup as VTickGroup
from ..graphicsItems.ViewBox import ViewBox as ViewBox
from _typeshed import Incomplete
from . import ImageViewTemplate_generic as ui_template
import numpy as np
from numpy import NDArray

translate: Incomplete

class PlotROI(ROI):
    def __init__(self, size) -> None: ...

class ImageView(QtWidgets.QWidget):
    """
    Widget used for display and analysis of image data.
    Implements many features:

      * Displays 2D and 3D image data. For 3D data, a z-axis
        slider is displayed allowing the user to select which frame is displayed.
      * Displays histogram of image data with movable region defining the dark/light levels
      * Editable gradient provides a color lookup table
      * Frame slider may also be moved using left/right arrow keys as well as pgup, pgdn, home, and end.
      * Basic analysis features including:

          * ROI and embedded plot for measuring image values across frames
          * Image normalization / background subtraction

    Basic Usage::

        imv = pg.ImageView()
        imv.show()
        imv.setImage(data)

    **Keyboard interaction**

      * left/right arrows step forward/backward 1 frame when pressed,
        seek at 20fps when held.
      * up/down arrows seek at 100fps
      * pgup/pgdn seek at 1000fps
      * home/end seek immediately to the first/last frame
      * space begins playing frames. If time values (in seconds) are given
        for each frame, then playback is in realtime.
    """

    sigTimeChanged: Incomplete
    sigProcessingChanged: Incomplete
    levelMin: Incomplete
    levelMax: Incomplete
    name: Incomplete
    image: Incomplete
    axes: Incomplete
    imageDisp: Incomplete
    ui: ui_template.Ui_Form
    scene: Incomplete
    discreteTimeLine: Incomplete
    ignoreTimeLine: bool
    view: Incomplete
    menu: Incomplete
    roi: Incomplete
    normRoi: Incomplete
    roiCurves: Incomplete
    timeLine: Incomplete
    imageItem: Incomplete
    currentIndex: int
    frameTicks: Incomplete
    keysPressed: Incomplete
    playTimer: Incomplete
    playRate: int
    fps: int
    lastPlayTime: int
    normRgn: Incomplete
    normProxy: Incomplete
    noRepeatKeys: Incomplete
    def __init__(
        self,
        parent: Incomplete | None = None,
        name: str = "ImageView",
        view: Incomplete | None = None,
        imageItem: Incomplete | None = None,
        levelMode: str = "mono",
        discreteTimeLine: bool = False,
        roi: Incomplete | None = None,
        normRoi: Incomplete | None = None,
        *args,
    ) -> None:
        """
        By default, this class creates an :class:`ImageItem <pyqtgraph.ImageItem>` to display image data
        and a :class:`ViewBox <pyqtgraph.ViewBox>` to contain the ImageItem.

        Parameters
        ----------
        parent : QWidget
            Specifies the parent widget to which this ImageView will belong. If None, then the ImageView is created with
            no parent.
        name : str
            The name used to register both the internal ViewBox and the PlotItem used to display ROI data. See the
            *name* argument to :func:`ViewBox.__init__() <pyqtgraph.ViewBox.__init__>`.
        view : ViewBox or PlotItem
            If specified, this will be used as the display area that contains the displayed image. Any
            :class:`ViewBox <pyqtgraph.ViewBox>`, :class:`PlotItem <pyqtgraph.PlotItem>`, or other compatible object is
            acceptable. Note: to display axis ticks inside the ImageView, instantiate it with a PlotItem instance as its
            view::

                pg.ImageView(view=pg.PlotItem())
        imageItem : ImageItem
            If specified, this object will be used to display the image. Must be an instance of ImageItem or other
            compatible object.
        levelMode : str
            See the *levelMode* argument to :func:`HistogramLUTItem.__init__() <pyqtgraph.HistogramLUTItem.__init__>`
        discreteTimeLine : bool
            Whether to snap to xvals / frame numbers when interacting with the timeline position.
        roi : ROI
            If specified, this object is used as ROI for the plot feature. Must be an instance of ROI.
        normRoi : ROI
            If specified, this object is used as ROI for the normalization feature. Must be an instance of ROI.
        """
    tVals: Incomplete
    def setImage(
        self,
        img: np.ndarray[
            tuple[int, int] | tuple[int, int, int],
            np.dtype[np.int64 | np.float32 | np.float64 | np.uint8 | np.bool],
        ],
        autoRange: bool = True,
        autoLevels: bool = True,
        levels: tuple[float, float] | None = None,
        axes: dict[str, int] | None = None,
        xvals: NDArray[np.int64] | None = None,
        pos: tuple[float, float] | list[tuple[float]] | None = None,
        scale: tuple[float, float] | list[tuple[float]] | None = None,
        transform: QtGui.QTransform | None = None,
        autoHistogramRange: bool = True,
        levelMode: str | None = None,
    ) -> None:
        """
        Set the image to be displayed in the widget.

        Parameters
        ----------
        img : np.ndarray
            The image to be displayed. See :func:`ImageItem.setImage` and *notes* below.
        autoRange : bool
            Whether to scale/pan the view to fit the image.
        autoLevels : bool
            Whether to update the white/black levels to fit the image.
        levels : tuple
            (min, max) white and black level values to use.
        axes : dict
            Dictionary indicating the interpretation for each axis. This is only needed to override the default guess.
            Format is::

                {'t':0, 'x':1, 'y':2, 'c':3};
        xvals : np.ndarray
            1D array of values corresponding to the first axis in a 3D image. For video, this array should contain
            the time of each frame.
        pos
            Change the position of the displayed image
        scale
            Change the scale of the displayed image
        transform
            Set the transform of the displayed image. This option overrides *pos* and *scale*.
        autoHistogramRange : bool
            If True, the histogram y-range is automatically scaled to fit the image data.
        levelMode : str
            If specified, this sets the user interaction mode for setting image levels. Options are 'mono',
            which provides a single level control for all image channels, and 'rgb' or 'rgba', which provide
            individual controls for each channel.

        Notes
        -----
        For backward compatibility, image data is assumed to be in column-major order (column, row).
        However, most image data is stored in row-major order (row, column) and will need to be
        transposed before calling setImage()::

            imageview.setImage(imagedata.T)

        This requirement can be changed by the ``imageAxisOrder``
        :ref:`global configuration option <apiref_config>`.
        """
    def clear(self) -> None: ...
    def play(self, rate: Incomplete | None = None) -> None:
        """Begin automatically stepping frames forward at the given rate (in fps).
        This can also be accessed by pressing the spacebar."""
    def togglePause(self) -> None: ...
    def setHistogramLabel(self, text: Incomplete | None = None, **kwargs) -> None:
        """
        Set the label text of the histogram axis similar to
        :func:`AxisItem.setLabel() <pyqtgraph.AxisItem.setLabel>`
        """
    def nframes(self):
        """
        Returns
        -------
        int
            The number of frames in the image data.
        """
    def autoLevels(self) -> None:
        """Set the min/max intensity levels automatically to match the image data."""
    def setLevels(self, *args, **kwds) -> None:
        """Set the min/max (bright and dark) levels.

        See :func:`HistogramLUTItem.setLevels <pyqtgraph.HistogramLUTItem.setLevels>`.
        """
    def autoRange(self) -> None:
        """Auto scale and pan the view around the image such that the image fills the view."""
    def getProcessedImage(self):
        """Returns the image data after it has been processed by any normalization options in use."""
    def close(self) -> None:
        """Closes the widget nicely, making sure to clear the graphics scene and release memory."""
    def keyPressEvent(self, ev) -> None: ...
    def keyReleaseEvent(self, ev) -> None: ...
    def evalKeyState(self) -> None: ...
    def timeout(self) -> None: ...
    def setCurrentIndex(self, ind) -> None:
        """Set the currently displayed frame index."""
    def jumpFrames(self, n) -> None:
        """Move video frame ahead n frames (may be negative)"""
    def normRadioChanged(self) -> None: ...
    def updateNorm(self) -> None: ...
    def normToggled(self, b) -> None: ...
    def hasTimeAxis(self): ...
    def roiClicked(self) -> None: ...
    def roiChanged(self) -> None: ...
    def quickMinMax(self, data):
        """
        Estimate the min/max values of *data* by subsampling.
        Returns [(min, max), ...] with one item per channel
        """
    def normalize(self, image):
        """
        Process *image* using the normalization options configured in the
        control panel.

        This can be repurposed to process any data through the same filter.
        """
    def timeLineChanged(self) -> None: ...
    def updateImage(self, autoHistogramRange: bool = True) -> None: ...
    def timeIndex(self, slider):
        """
        Returns
        -------
        int
            The index of the frame closest to the timeline slider.
        float
            The time value of the slider.
        """
    def getView(self) -> ViewBox:
        """Return the ViewBox (or other compatible object) which displays the ImageItem"""
    def getImageItem(self) -> ImageItem:
        """Return the ImageItem for this ImageView."""
    def getRoiPlot(self):
        """Return the ROI PlotWidget for this ImageView"""
    def getHistogramWidget(self):
        """Return the HistogramLUTWidget for this ImageView"""
    def export(self, fileName) -> None:
        """
        Export data from the ImageView to a file, or to a stack of files if
        the data is 3D. Saving an image stack will result in index numbers
        being added to the file name. Images are saved as they would appear
        onscreen, with levels and lookup table applied.
        """
    def exportClicked(self) -> None: ...
    normAction: Incomplete
    exportAction: Incomplete
    def buildMenu(self) -> None: ...
    def menuClicked(self) -> None: ...
    def setColorMap(self, colormap) -> None:
        """Set the color map.

        Parameters
        ----------
        colormap : ColorMap
            The ColorMap to use for coloring images.
        """
    def setPredefinedGradient(self, name) -> None:
        """Set one of the gradients defined in :class:`GradientEditorItem`.
        Currently available gradients are:
        """
