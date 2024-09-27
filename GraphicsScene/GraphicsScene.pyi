from ..Qt import QtWidgets
from _typeshed import Incomplete

__all__ = ['GraphicsScene']

class GraphicsScene(QtWidgets.QGraphicsScene):
    """
    Extension of QGraphicsScene that implements a complete, parallel mouse event system.
    (It would have been preferred to just alter the way QGraphicsScene creates and delivers 
    events, but this turned out to be impossible because the constructor for QGraphicsMouseEvent
    is private)
    
      *  Generates MouseClicked events in addition to the usual press/move/release events.
         (This works around a problem where it is impossible to have one item respond to a
         drag if another is watching for a click.)
      *  Adjustable radius around click that will catch objects so you don't have to click *exactly* over small/thin objects
      *  Global context menu--if an item implements a context menu, then its parent(s) may also add items to the menu.
      *  Allows items to decide _before_ a mouse click which item will be the recipient of mouse events.
         This lets us indicate unambiguously to the user which item they are about to click/drag on
      *  Eats mouseMove events that occur too soon after a mouse press.
      *  Reimplements items() and itemAt() to circumvent PyQt bug

    ====================== ====================================================================
    **Signals**
    sigMouseClicked(event) Emitted when the mouse is clicked over the scene. Use ev.pos() to
                           get the click position relative to the item that was clicked on,
                           or ev.scenePos() to get the click position in scene coordinates.
                           See :class:`pyqtgraph.GraphicsScene.mouseEvents.MouseClickEvent`.                        
    sigMouseMoved(pos)     Emitted when the mouse cursor moves over the scene. The position
                           is given in scene coordinates.
    sigMouseHover(items)   Emitted when the mouse is moved over the scene. Items is a list
                           of items under the cursor.
    sigItemAdded(item)     Emitted when an item is added via addItem(). The item is given.
    sigItemRemoved(item)   Emitted when an item is removed via removeItem(). The item is given.
    ====================== ====================================================================
    
    Mouse interaction is as follows:
    
    1) Every time the mouse moves, the scene delivers both the standard hoverEnter/Move/LeaveEvents 
       as well as custom HoverEvents. 
    2) Items are sent HoverEvents in Z-order and each item may optionally call event.acceptClicks(button), 
       acceptDrags(button) or both. If this method call returns True, this informs the item that _if_ 
       the user clicks/drags the specified mouse button, the item is guaranteed to be the 
       recipient of click/drag events (the item may wish to change its appearance to indicate this).
       If the call to acceptClicks/Drags returns False, then the item is guaranteed to *not* receive
       the requested event (because another item has already accepted it). 
    3) If the mouse is clicked, a mousePressEvent is generated as usual. If any items accept this press event, then
       No click/drag events will be generated and mouse interaction proceeds as defined by Qt. This allows
       items to function properly if they are expecting the usual press/move/release sequence of events.
       (It is recommended that items do NOT accept press events, and instead use click/drag events)
       Note: The default implementation of QGraphicsItem.mousePressEvent will *accept* the event if the 
       item is has its Selectable or Movable flags enabled. You may need to override this behavior.
    4) If no item accepts the mousePressEvent, then the scene will begin delivering mouseDrag and/or mouseClick events.
       If the mouse is moved a sufficient distance (or moved slowly enough) before the button is released, 
       then a mouseDragEvent is generated.
       If no drag events are generated before the button is released, then a mouseClickEvent is generated. 
    5) Click/drag events are delivered to the item that called acceptClicks/acceptDrags on the HoverEvent
       in step 1. If no such items exist, then the scene attempts to deliver the events to items near the event. 
       ClickEvents may be delivered in this way even if no
       item originally claimed it could accept the click. DragEvents may only be delivered this way if it is the initial
       move in a drag.
    """
    sigMouseHover: Incomplete
    sigMouseMoved: Incomplete
    sigMouseClicked: Incomplete
    sigPrepareForPaint: Incomplete
    sigItemAdded: Incomplete
    sigItemRemoved: Incomplete
    ExportDirectory: Incomplete
    exportDirectory: Incomplete
    clickEvents: Incomplete
    dragButtons: Incomplete
    mouseGrabber: Incomplete
    dragItem: Incomplete
    lastDrag: Incomplete
    hoverItems: Incomplete
    lastHoverEvent: Incomplete
    minDragTime: float
    contextMenu: Incomplete
    exportDialog: Incomplete
    def __init__(self, clickRadius: int = 2, moveDistance: int = 5, parent: Incomplete | None = None) -> None: ...
    def render(self, *args): ...
    def prepareForPaint(self) -> None:
        """Called before every render. This method will inform items that the scene is about to
        be rendered by emitting sigPrepareForPaint.
        
        This allows items to delay expensive processing until they know a paint will be required."""
    def setClickRadius(self, r: int):
        """
        Set the distance away from mouse clicks to search for interacting items.
        When clicking, the scene searches first for items that directly intersect the click position
        followed by any other items that are within a rectangle that extends r pixels away from the 
        click position. 
        """
    def setMoveDistance(self, d) -> None:
        """
        Set the distance the mouse must move after a press before mouseMoveEvents will be delivered.
        This ensures that clicks with a small amount of movement are recognized as clicks instead of
        drags.
        """
    def mousePressEvent(self, ev) -> None: ...
    def mouseMoveEvent(self, ev) -> None: ...
    def leaveEvent(self, ev) -> None: ...
    def mouseReleaseEvent(self, ev) -> None: ...
    def mouseDoubleClickEvent(self, ev) -> None: ...
    def sendHoverEvents(self, ev, exitOnly: bool = False) -> None: ...
    def sendDragEvent(self, ev, init: bool = False, final: bool = False): ...
    def sendClickEvent(self, ev): ...
    def addItem(self, item): ...
    def removeItem(self, item): ...
    def itemsNearEvent(self, event, selMode=..., sortOrder=..., hoverable: bool = False):
        """
        Return an iterator that iterates first through the items that directly intersect point (in Z order)
        followed by any other items that are within the scene's click radius.
        """
    def getViewWidget(self): ...
    def addParentContextMenus(self, item, menu, event):
        """
        Can be called by any item in the scene to expand its context menu to include parent context menus.
        Parents may implement getContextMenus to add new menus / actions to the existing menu.
        getContextMenus must accept 1 argument (the event that generated the original menu) and
        return a single QMenu or a list of QMenus.
        
        The final menu will look like:
        
            |    Original Item 1
            |    Original Item 2
            |    ...
            |    Original Item N
            |    ------------------
            |    Parent Item 1
            |    Parent Item 2
            |    ...
            |    Grandparent Item 1
            |    ...
            
        
        ==============  ==================================================
        **Arguments:**
        item            The item that initially created the context menu 
                        (This is probably the item making the call to this function)
        menu            The context menu being shown by the item
        event           The original event that triggered the menu to appear.
        ==============  ==================================================
        """
    contextMenuItem: Incomplete
    def getContextMenus(self, event): ...
    def showExportDialog(self) -> None: ...
