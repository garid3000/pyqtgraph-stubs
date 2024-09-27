from .colormap import *
from .functions import *
from .graphicsItems.ArrowItem import *
from .graphicsItems.AxisItem import *
from .graphicsItems.BarGraphItem import *
from .graphicsItems.ButtonItem import *
from .graphicsItems.ColorBarItem import *
from .graphicsItems.CurvePoint import *
from .graphicsItems.DateAxisItem import *
from .graphicsItems.ErrorBarItem import *
from .graphicsItems.FillBetweenItem import *
from .graphicsItems.GradientEditorItem import *
from .graphicsItems.GradientLegend import *
from .graphicsItems.GraphicsItem import *
from .graphicsItems.GraphicsLayout import *
from .graphicsItems.GraphicsObject import *
from .graphicsItems.GraphicsWidget import *
from .graphicsItems.GraphicsWidgetAnchor import *
from .graphicsItems.GraphItem import *
from .graphicsItems.GridItem import *
from .graphicsItems.HistogramLUTItem import *
from .graphicsItems.ImageItem import *
from .graphicsItems.InfiniteLine import *
from .graphicsItems.IsocurveItem import *
from .graphicsItems.ItemGroup import *
from .graphicsItems.LabelItem import *
from .graphicsItems.LegendItem import *
from .graphicsItems.LinearRegionItem import *
from .graphicsItems.MultiPlotItem import *
from .graphicsItems.PColorMeshItem import *
from .graphicsItems.PlotCurveItem import *
from .graphicsItems.PlotDataItem import *
from .graphicsItems.PlotItem import *
from .graphicsItems.ROI import *
from .graphicsItems.ScaleBar import *
from .graphicsItems.ScatterPlotItem import *
from .graphicsItems.TargetItem import *
from .graphicsItems.TextItem import *
from .graphicsItems.UIGraphicsItem import *
from .graphicsItems.ViewBox import *
from .graphicsItems.VTickGroup import *
from .imageview import *
from .SignalProxy import *
from .ThreadsafeTimer import *
from .WidgetGroup import *
from .widgets.BusyCursor import *
from .widgets.CheckTable import *
from .widgets.ColorButton import *
from .widgets.ColorMapWidget import *
from .widgets.ComboBox import *
from .widgets.DataFilterWidget import *
from .widgets.DataTreeWidget import *
from .widgets.DiffTreeWidget import *
from .widgets.FeedbackButton import *
from .widgets.FileDialog import *
from .widgets.GradientWidget import *
from .widgets.GraphicsLayoutWidget import *
from .widgets.GraphicsView import *
from .widgets.HistogramLUTWidget import *
from .widgets.JoystickButton import *
from .widgets.LayoutWidget import *
from .widgets.MultiPlotWidget import *
from .widgets.PathButton import *
from .widgets.PlotWidget import *
from .widgets.ProgressDialog import *
from .widgets.RawImageWidget import *
from .widgets.ScatterPlotWidget import *
from .widgets.SpinBox import *
from .widgets.TableWidget import *
from .widgets.TreeWidget import *
from .widgets.ValueLabel import *
from .widgets.VerticalLabel import *
from .GraphicsScene import GraphicsScene as GraphicsScene
from .Point import Point as Point
from .Qt import QtCore as QtCore, isQObjectAlive as isQObjectAlive
from .SRTTransform import SRTTransform as SRTTransform
from .SRTTransform3D import SRTTransform3D as SRTTransform3D
from .Transform3D import Transform3D as Transform3D
from .Vector import Vector as Vector
from .metaarray import MetaArray as MetaArray
from .util.cupy_helper import getCupy as getCupy
from .widgets.ColorMapMenu import ColorMapMenu as ColorMapMenu
from .widgets.GroupBox import GroupBox as GroupBox
from .widgets.RemoteGraphicsView import RemoteGraphicsView as RemoteGraphicsView
from _typeshed import Incomplete

__version__: str
useOpenGL: bool
CONFIG_OPTIONS: Incomplete

def setConfigOption(opt: str, value: str|bool|int|None) -> None: ...
def setConfigOptions(**opts: str|bool|int|None) -> None:
    """Set global configuration options.

    Each keyword argument sets one global option.
    """
def getConfigOption(opt):
    """Return the value of a single global configuration option.
    """
def systemInfo() -> None: ...
def renamePyc(startDir) -> None: ...

path: Incomplete

def cleanup() -> None: ...
def exit() -> None:
    """
    Causes python to exit without garbage-collecting any objects, and thus avoids
    calling object destructor methods. This is a sledgehammer workaround for
    a variety of bugs in PyQt and Pyside that cause crashes on exit.

    This function does the following in an attempt to 'safely' terminate
    the process:

      * Invoke atexit callbacks
      * Close all open file handles
      * os._exit()

    Note: there is some potential for causing damage with this function if you
    are using objects that _require_ their destructors to be called (for example,
    to properly terminate log files, disconnect from devices, etc). Situations
    like this are probably quite rare, but use at your own risk.
    """

plots: Incomplete
images: Incomplete
QAPP: Incomplete

def plot(*args, **kargs):
    """
    Create and return a :class:`PlotWidget <pyqtgraph.PlotWidget>`
    Accepts a *title* argument to set the title of the window.
    All other arguments are used to plot data. (see :func:`PlotItem.plot() <pyqtgraph.PlotItem.plot>`)
    """
def image(*args, **kargs):
    """
    Create and return an :class:`ImageView <pyqtgraph.ImageView>`
    Will show 2D or 3D image data.
    Accepts a *title* argument to set the title of the window.
    All other arguments are used to show data. (see :func:`ImageView.setImage() <pyqtgraph.ImageView.setImage>`)
    """
show = image

def dbg(*args, **kwds):
    """
    Create a console window and begin watching for exceptions.

    All arguments are passed to :func:`ConsoleWidget.__init__() <pyqtgraph.console.ConsoleWidget.__init__>`.
    """
def stack(*args, **kwds):
    """
    Create a console window and show the current stack trace.

    All arguments are passed to :func:`ConsoleWidget.__init__() <pyqtgraph.console.ConsoleWidget.__init__>`.
    """
def setPalette(app, style) -> None: ...
