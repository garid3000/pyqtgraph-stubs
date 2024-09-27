from . import functions as functions
from ... import Point as Point, PolyLineROI as PolyLineROI
from .common import CtrlNode as CtrlNode, PlottingCtrlNode as PlottingCtrlNode, metaArrayWrapper as metaArrayWrapper
from _typeshed import Incomplete

class Downsample(CtrlNode):
    """Downsample by averaging samples together."""
    nodeName: str
    uiTemplate: Incomplete
    def processData(self, data): ...

class Subsample(CtrlNode):
    """Downsample by selecting every Nth sample."""
    nodeName: str
    uiTemplate: Incomplete
    def processData(self, data): ...

class Bessel(CtrlNode):
    """Bessel filter. Input data must have time values."""
    nodeName: str
    uiTemplate: Incomplete
    def processData(self, data): ...

class Butterworth(CtrlNode):
    """Butterworth filter"""
    nodeName: str
    uiTemplate: Incomplete
    def processData(self, data): ...

class ButterworthNotch(CtrlNode):
    """Butterworth notch filter"""
    nodeName: str
    uiTemplate: Incomplete
    def processData(self, data): ...

class Mean(CtrlNode):
    """Filters data by taking the mean of a sliding window"""
    nodeName: str
    uiTemplate: Incomplete
    def processData(self, data): ...

class Median(CtrlNode):
    """Filters data by taking the median of a sliding window"""
    nodeName: str
    uiTemplate: Incomplete
    def processData(self, data): ...

class Mode(CtrlNode):
    """Filters data by taking the mode (histogram-based) of a sliding window"""
    nodeName: str
    uiTemplate: Incomplete
    def processData(self, data): ...

class Denoise(CtrlNode):
    """Removes anomalous spikes from data, replacing with nearby values"""
    nodeName: str
    uiTemplate: Incomplete
    def processData(self, data): ...

class Gaussian(CtrlNode):
    """Gaussian smoothing filter."""
    nodeName: str
    uiTemplate: Incomplete
    def processData(self, data): ...

class Derivative(CtrlNode):
    """Returns the pointwise derivative of the input"""
    nodeName: str
    def processData(self, data): ...

class Integral(CtrlNode):
    """Returns the pointwise integral of the input"""
    nodeName: str
    def processData(self, data): ...

class Detrend(CtrlNode):
    """Removes linear trend from the data"""
    nodeName: str
    def processData(self, data): ...

class RemoveBaseline(PlottingCtrlNode):
    """Remove an arbitrary, graphically defined baseline from the data."""
    nodeName: str
    line: Incomplete
    def __init__(self, name) -> None: ...
    def connectToPlot(self, node) -> None:
        """Define what happens when the node is connected to a plot"""
    def disconnectFromPlot(self, plot) -> None:
        """Define what happens when the node is disconnected from a plot"""
    def processData(self, data): ...
    def adjustXPositions(self, pts, data):
        """Return a list of Point() where the x position is set to the nearest x value in *data* for each point in *pts*."""

class AdaptiveDetrend(CtrlNode):
    """Removes baseline from data, ignoring anomalous events"""
    nodeName: str
    uiTemplate: Incomplete
    def processData(self, data): ...

class HistogramDetrend(CtrlNode):
    """Removes baseline from data by computing mode (from histogram) of beginning and end of data."""
    nodeName: str
    uiTemplate: Incomplete
    def processData(self, data): ...

class RemovePeriodic(CtrlNode):
    nodeName: str
    uiTemplate: Incomplete
    def processData(self, data): ...
