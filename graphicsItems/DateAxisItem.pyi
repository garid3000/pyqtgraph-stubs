from .AxisItem import AxisItem
from _typeshed import Incomplete

__all__ = ['DateAxisItem']

class TickSpec:
    """ Specifies the properties for a set of date ticks and computes ticks
    within a given utc timestamp range """
    spacing: Incomplete
    step: Incomplete
    format: Incomplete
    autoSkip: Incomplete
    def __init__(self, spacing, stepper, format, autoSkip: Incomplete | None = None) -> None:
        """
        ============= ==========================================================
        Arguments
        spacing       approximate (average) tick spacing
        stepper       a stepper function that takes a utc time stamp and a step
                      steps number n to compute the start of the next unit. You
                      can use the make_X_stepper functions to create common
                      steppers.
        format        a strftime compatible format string which will be used to
                      convert tick locations to date/time strings
        autoSkip      list of step size multipliers to be applied when the tick
                      density becomes too high. The tick spec automatically
                      applies additional powers of 10 (10, 100, ...) to the list
                      if necessary. Set to None to switch autoSkip off
        ============= ==========================================================

        """
    def makeTicks(self, minVal, maxVal, minSpc): ...
    def skipFactor(self, minSpc): ...

class ZoomLevel:
    """ Generates the ticks which appear in a specific zoom level """
    tickSpecs: Incomplete
    utcOffset: int
    exampleText: Incomplete
    def __init__(self, tickSpecs, exampleText) -> None:
        """
        ============= ==========================================================
        tickSpecs     a list of one or more TickSpec objects with decreasing
                      coarseness
        ============= ==========================================================

        """
    def tickValues(self, minVal, maxVal, minSpc): ...

class DateAxisItem(AxisItem):
    """
    **Bases:** :class:`AxisItem <pyqtgraph.AxisItem>`
    
    An AxisItem that displays dates from unix timestamps.

    The display format is adjusted automatically depending on the current time
    density (seconds/point) on the axis. For more details on changing this
    behaviour, see :func:`setZoomLevelForDensity() <pyqtgraph.DateAxisItem.setZoomLevelForDensity>`.
    
    Can be added to an existing plot e.g. via 
    :func:`setAxisItems({'bottom':axis}) <pyqtgraph.PlotItem.setAxisItems>`.

    """
    utcOffset: Incomplete
    zoomLevels: Incomplete
    autoSIPrefix: bool
    def __init__(self, orientation: str = 'bottom', utcOffset: Incomplete | None = None, **kwargs) -> None:
        """
        Create a new DateAxisItem.
        
        For `orientation` and `**kwargs`, see
        :func:`AxisItem.__init__ <pyqtgraph.AxisItem.__init__>`.
        
        """
    def tickStrings(self, values, scale, spacing): ...
    def tickValues(self, minVal, maxVal, size): ...
    zoomLevel: Incomplete
    minSpacing: Incomplete
    def setZoomLevelForDensity(self, density):
        """
        Setting `zoomLevel` and `minSpacing` based on given density of seconds per pixel
        
        The display format is adjusted automatically depending on the current time
        density (seconds/point) on the axis. You can customize the behaviour by 
        overriding this function or setting a different set of zoom levels
        than the default one. The `zoomLevels` variable is a dictionary with the
        maximal distance of ticks in seconds which are allowed for each zoom level
        before the axis switches to the next coarser level. To customize the zoom level
        selection, override this function.
        """
    def linkToView(self, view) -> None:
        """Link this axis to a ViewBox, causing its displayed range to match the visible range of the view."""
    fontMetrics: Incomplete
    def generateDrawSpecs(self, p): ...
