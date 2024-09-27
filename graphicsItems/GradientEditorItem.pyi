from ..Qt import QtWidgets
from .GraphicsWidget import GraphicsWidget
from _typeshed import Incomplete

__all__ = ['TickSliderItem', 'GradientEditorItem', 'addGradientListToDocstring']

def addGradientListToDocstring():
    """Decorator to add list of current pre-defined gradients to the end of a function docstring."""

class TickSliderItem(GraphicsWidget):
    """**Bases:** :class:`GraphicsWidget <pyqtgraph.GraphicsWidget>`
    
    A rectangular item with tick marks along its length that can (optionally) be moved by the user."""
    sigTicksChanged: Incomplete
    sigTicksChangeFinished: Incomplete
    orientation: Incomplete
    length: int
    tickSize: int
    ticks: Incomplete
    maxDim: int
    allowAdd: Incomplete
    allowRemove: Incomplete
    tickPen: Incomplete
    orientations: Incomplete
    def __init__(self, orientation: str = 'bottom', allowAdd: bool = True, allowRemove: bool = True, **kargs) -> None:
        """
        ==============  =================================================================================
        **Arguments:**
        orientation     Set the orientation of the gradient. Options are: 'left', 'right'
                        'top', and 'bottom'.
        allowAdd        Specifies whether the user can add ticks.
        allowRemove     Specifies whether the user can remove new ticks.
        tickPen         Default is white. Specifies the color of the outline of the ticks.
                        Can be any of the valid arguments for :func:`mkPen <pyqtgraph.mkPen>`
        ==============  =================================================================================
        """
    def paint(self, p, opt, widget) -> None: ...
    def keyPressEvent(self, ev) -> None: ...
    def setMaxDim(self, mx: Incomplete | None = None) -> None: ...
    def setOrientation(self, orientation) -> None:
        """Set the orientation of the TickSliderItem.
        
        ==============  ===================================================================
        **Arguments:**
        orientation     Options are: 'left', 'right', 'top', 'bottom'
                        The orientation option specifies which side of the slider the
                        ticks are on, as well as whether the slider is vertical ('right'
                        and 'left') or horizontal ('top' and 'bottom').
        ==============  ===================================================================
        """
    def addTick(self, x, color: Incomplete | None = None, movable: bool = True, finish: bool = True):
        """
        Add a tick to the item.
        
        ==============  ==================================================================
        **Arguments:**
        x               Position where tick should be added.
        color           Color of added tick. If color is not specified, the color will be
                        white.
        movable         Specifies whether the tick is movable with the mouse.
        ==============  ==================================================================
        """
    def removeTick(self, tick, finish: bool = True) -> None:
        """
        Removes the specified tick.
        """
    def tickMoved(self, tick, pos) -> None: ...
    def tickMoveFinished(self, tick) -> None: ...
    def tickClicked(self, tick, ev) -> None: ...
    def widgetLength(self): ...
    def resizeEvent(self, ev) -> None: ...
    def setLength(self, newLen) -> None: ...
    def mouseClickEvent(self, ev) -> None: ...
    def hoverEvent(self, ev) -> None: ...
    def showMenu(self, ev) -> None: ...
    def setTickColor(self, tick, color) -> None:
        """Set the color of the specified tick.
        
        ==============  ==================================================================
        **Arguments:**
        tick            Can be either an integer corresponding to the index of the tick
                        or a Tick object. Ex: if you had a slider with 3 ticks and you
                        wanted to change the middle tick, the index would be 1.
        color           The color to make the tick. Can be any argument that is valid for
                        :func:`mkBrush <pyqtgraph.mkBrush>`
        ==============  ==================================================================
        """
    def setTickValue(self, tick, val) -> None:
        """
        Set the position (along the slider) of the tick.
        
        ==============   ==================================================================
        **Arguments:**
        tick             Can be either an integer corresponding to the index of the tick
                         or a Tick object. Ex: if you had a slider with 3 ticks and you
                         wanted to change the middle tick, the index would be 1.
        val              The desired position of the tick. If val is < 0, position will be
                         set to 0. If val is > 1, position will be set to 1.
        ==============   ==================================================================
        """
    def tickValue(self, tick):
        """Return the value (from 0.0 to 1.0) of the specified tick.
        
        ==============  ==================================================================
        **Arguments:**
        tick            Can be either an integer corresponding to the index of the tick
                        or a Tick object. Ex: if you had a slider with 3 ticks and you
                        wanted the value of the middle tick, the index would be 1.
        ==============  ==================================================================
        """
    def getTick(self, tick):
        """Return the Tick object at the specified index.
        
        ==============  ==================================================================
        **Arguments:**
        tick            An integer corresponding to the index of the desired tick. If the
                        argument is not an integer it will be returned unchanged.
        ==============  ==================================================================
        """
    def listTicks(self):
        """Return a sorted list of all the Tick objects on the slider."""

class GradientEditorItem(TickSliderItem):
    """
    **Bases:** :class:`TickSliderItem <pyqtgraph.TickSliderItem>`
    
    An item that can be used to define a color gradient. Implements common pre-defined gradients that are 
    customizable by the user. :class: `GradientWidget <pyqtgraph.GradientWidget>` provides a widget
    with a GradientEditorItem that can be added to a GUI. 
    
    ================================ ===========================================================
    **Signals:**
    sigGradientChanged(self)         Signal is emitted anytime the gradient changes. The signal 
                                     is emitted in real time while ticks are being dragged or 
                                     colors are being changed.
    sigGradientChangeFinished(self)  Signal is emitted when the gradient is finished changing.
    ================================ ===========================================================    
 
    """
    sigGradientChanged: Incomplete
    sigGradientChangeFinished: Incomplete
    currentTick: Incomplete
    currentTickColor: Incomplete
    rectSize: int
    gradRect: Incomplete
    backgroundRect: Incomplete
    colorMode: str
    colorDialog: Incomplete
    rgbAction: Incomplete
    hsvAction: Incomplete
    menu: Incomplete
    linkedGradients: Incomplete
    def __init__(self, *args, **kargs) -> None:
        """
        Create a new GradientEditorItem. 
        All arguments are passed to :func:`TickSliderItem.__init__ <pyqtgraph.TickSliderItem.__init__>`
        
        ===============  =================================================================================
        **Arguments:**
        orientation      Set the orientation of the gradient. Options are: 'left', 'right'
                         'top', and 'bottom'.
        allowAdd         Default is True. Specifies whether ticks can be added to the item.
        tickPen          Default is white. Specifies the color of the outline of the ticks.
                         Can be any of the valid arguments for :func:`mkPen <pyqtgraph.mkPen>`
        ===============  =================================================================================
        """
    allowAdd: Incomplete
    def showTicks(self, show: bool = True) -> None: ...
    def setOrientation(self, orientation) -> None:
        """
        Set the orientation of the GradientEditorItem. 
        
        ==============  ===================================================================
        **Arguments:**
        orientation     Options are: 'left', 'right', 'top', 'bottom'
                        The orientation option specifies which side of the gradient the
                        ticks are on, as well as whether the gradient is vertical ('right'
                        and 'left') or horizontal ('top' and 'bottom').
        ==============  ===================================================================
        """
    def showMenu(self, ev) -> None: ...
    def colorMapMenuClicked(self, cmap) -> None: ...
    def loadPreset(self, name) -> None:
        """
        Load a predefined gradient. Currently defined gradients are: 
        """
    def setColorMode(self, cm) -> None:
        """
        Set the color mode for the gradient. Options are: 'hsv', 'rgb'
        
        """
    def colorMap(self):
        """Return a ColorMap object representing the current state of the editor."""
    gradient: Incomplete
    def updateGradient(self) -> None: ...
    def setLength(self, newLen) -> None: ...
    def currentColorChanged(self, color) -> None: ...
    def currentColorRejected(self) -> None: ...
    def currentColorAccepted(self) -> None: ...
    def tickClicked(self, tick, ev) -> None: ...
    def raiseColorDialog(self, tick) -> None: ...
    tickMenu: Incomplete
    def raiseTickContextMenu(self, tick, ev) -> None: ...
    def tickMoveFinished(self, tick) -> None: ...
    def getGradient(self):
        """Return a QLinearGradient object."""
    def getColor(self, x, toQColor: bool = True):
        """
        Return a color for a given value.
        
        ==============  ==================================================================
        **Arguments:**
        x               Value (position on gradient) of requested color.
        toQColor        If true, returns a QColor object, else returns a (r,g,b,a) tuple.
        ==============  ==================================================================
        """
    def getLookupTable(self, nPts, alpha: Incomplete | None = None):
        """
        Return an RGB(A) lookup table (ndarray). 
        
        ==============  ============================================================================
        **Arguments:**
        nPts            The number of points in the returned lookup table.
        alpha           True, False, or None - Specifies whether or not alpha values are included
                        in the table.If alpha is None, alpha will be automatically determined.
        ==============  ============================================================================
        """
    def usesAlpha(self):
        """Return True if any ticks have an alpha < 255"""
    def isLookupTrivial(self):
        """Return True if the gradient has exactly two stops in it: black at 0.0 and white at 1.0"""
    def addTick(self, x, color: Incomplete | None = None, movable: bool = True, finish: bool = True):
        """
        Add a tick to the gradient. Return the tick.
        
        ==============  ==================================================================
        **Arguments:**
        x               Position where tick should be added.
        color           Color of added tick. If color is not specified, the color will be
                        the color of the gradient at the specified position.
        movable         Specifies whether the tick is movable with the mouse.
        ==============  ==================================================================
        """
    def saveState(self):
        """
        Return a dictionary with parameters for rebuilding the gradient. Keys will include:
        
           - 'mode': hsv or rgb
           - 'ticks': a list of tuples (pos, (r,g,b,a))
        """
    def restoreState(self, state) -> None:
        """
        Restore the gradient specified in state.
        
        ==============  ====================================================================
        **Arguments:**
        state           A dictionary with same structure as those returned by
                        :func:`saveState <pyqtgraph.GradientEditorItem.saveState>`
                      
                        Keys must include:
                      
                            - 'mode': hsv or rgb
                            - 'ticks': a list of tuples (pos, (r,g,b,a))
        ==============  ====================================================================
        """
    def setColorMap(self, cm) -> None: ...
    def linkGradient(self, slaveGradient, connect: bool = True): ...

class Tick(QtWidgets.QGraphicsWidget):
    sigMoving: Incomplete
    sigMoved: Incomplete
    sigClicked: Incomplete
    movable: Incomplete
    moving: bool
    scale: Incomplete
    color: Incomplete
    pen: Incomplete
    hoverPen: Incomplete
    currentPen: Incomplete
    removeAllowed: Incomplete
    pg: Incomplete
    def __init__(self, pos, color, movable: bool = True, scale: int = 10, pen: str = 'w', removeAllowed: bool = True) -> None: ...
    def boundingRect(self): ...
    def shape(self): ...
    def paint(self, p, *args) -> None: ...
    cursorOffset: Incomplete
    startPosition: Incomplete
    def mouseDragEvent(self, ev) -> None: ...
    def mouseClickEvent(self, ev) -> None: ...
    def hoverEvent(self, ev) -> None: ...

class TickMenu(QtWidgets.QMenu):
    tick: Incomplete
    sliderItem: Incomplete
    removeAct: Incomplete
    fracPosSpin: Incomplete
    def __init__(self, tick, sliderItem) -> None: ...
    def fractionalValueChanged(self, x) -> None: ...
