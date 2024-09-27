from _typeshed import Incomplete

__all__ = ['MouseDragEvent', 'MouseClickEvent', 'HoverEvent']

class MouseDragEvent:
    """
    Instances of this class are delivered to items in a :class:`GraphicsScene <pyqtgraph.GraphicsScene>` via their mouseDragEvent() method when the item is being mouse-dragged. 
    
    """
    start: Incomplete
    finish: Incomplete
    accepted: bool
    currentItem: Incomplete
    acceptedItem: Incomplete
    def __init__(self, moveEvent, pressEvent, lastEvent, start: bool = False, finish: bool = False) -> None: ...
    def accept(self) -> None:
        """An item should call this method if it can handle the event. This will prevent the event being delivered to any other items."""
    def ignore(self) -> None:
        """An item should call this method if it cannot handle the event. This will allow the event to be delivered to other items."""
    def isAccepted(self): ...
    def scenePos(self):
        """Return the current scene position of the mouse."""
    def screenPos(self):
        """Return the current screen position (pixels relative to widget) of the mouse."""
    def buttonDownScenePos(self, btn: Incomplete | None = None):
        """
        Return the scene position of the mouse at the time *btn* was pressed.
        If *btn* is omitted, then the button that initiated the drag is assumed.
        """
    def buttonDownScreenPos(self, btn: Incomplete | None = None):
        """
        Return the screen position (pixels relative to widget) of the mouse at the time *btn* was pressed.
        If *btn* is omitted, then the button that initiated the drag is assumed.
        """
    def lastScenePos(self):
        """
        Return the scene position of the mouse immediately prior to this event.
        """
    def lastScreenPos(self):
        """
        Return the screen position of the mouse immediately prior to this event.
        """
    def buttons(self):
        """
        Return the buttons currently pressed on the mouse.
        (see QGraphicsSceneMouseEvent::buttons in the Qt documentation)
        """
    def button(self):
        """Return the button that initiated the drag (may be different from the buttons currently pressed)
        (see QGraphicsSceneMouseEvent::button in the Qt documentation)
        
        """
    def pos(self):
        """
        Return the current position of the mouse in the coordinate system of the item
        that the event was delivered to.
        """
    def lastPos(self):
        """
        Return the previous position of the mouse in the coordinate system of the item
        that the event was delivered to.
        """
    def buttonDownPos(self, btn: Incomplete | None = None):
        """
        Return the position of the mouse at the time the drag was initiated
        in the coordinate system of the item that the event was delivered to.
        """
    def isStart(self):
        """Returns True if this event is the first since a drag was initiated."""
    def isFinish(self):
        """Returns False if this is the last event in a drag. Note that this
        event will have the same position as the previous one."""
    def modifiers(self):
        """Return any keyboard modifiers currently pressed.
        (see QGraphicsSceneMouseEvent::modifiers in the Qt documentation)
        
        """

class MouseClickEvent:
    """
    Instances of this class are delivered to items in a :class:`GraphicsScene <pyqtgraph.GraphicsScene>` via their mouseClickEvent() method when the item is clicked. 
    
    
    """
    accepted: bool
    currentItem: Incomplete
    acceptedItem: Incomplete
    def __init__(self, pressEvent, double: bool = False) -> None: ...
    def accept(self) -> None:
        """An item should call this method if it can handle the event. This will prevent the event being delivered to any other items."""
    def ignore(self) -> None:
        """An item should call this method if it cannot handle the event. This will allow the event to be delivered to other items."""
    def isAccepted(self): ...
    def scenePos(self):
        """Return the current scene position of the mouse."""
    def screenPos(self):
        """Return the current screen position (pixels relative to widget) of the mouse."""
    def buttons(self):
        """
        Return the buttons currently pressed on the mouse.
        (see QGraphicsSceneMouseEvent::buttons in the Qt documentation)
        """
    def button(self):
        """Return the mouse button that generated the click event.
        (see QGraphicsSceneMouseEvent::button in the Qt documentation)
        """
    def double(self):
        """Return True if this is a double-click."""
    def pos(self):
        """
        Return the current position of the mouse in the coordinate system of the item
        that the event was delivered to.
        """
    def lastPos(self):
        """
        Return the previous position of the mouse in the coordinate system of the item
        that the event was delivered to.
        """
    def modifiers(self):
        """Return any keyboard modifiers currently pressed.
        (see QGraphicsSceneMouseEvent::modifiers in the Qt documentation)        
        """
    def time(self): ...

class HoverEvent:
    """
    Instances of this class are delivered to items in a :class:`GraphicsScene <pyqtgraph.GraphicsScene>` via their hoverEvent() method when the mouse is hovering over the item.
    This event class both informs items that the mouse cursor is nearby and allows items to 
    communicate with one another about whether each item will accept *potential* mouse events. 
    
    It is common for multiple overlapping items to receive hover events and respond by changing 
    their appearance. This can be misleading to the user since, in general, only one item will
    respond to mouse events. To avoid this, items make calls to event.acceptClicks(button) 
    and/or acceptDrags(button).
    
    Each item may make multiple calls to acceptClicks/Drags, each time for a different button. 
    If the method returns True, then the item is guaranteed to be
    the recipient of the claimed event IF the user presses the specified mouse button before
    moving. If claimEvent returns False, then this item is guaranteed NOT to get the specified
    event (because another has already claimed it) and the item should change its appearance 
    accordingly.
    
    event.isEnter() returns True if the mouse has just entered the item's shape;
    event.isExit() returns True if the mouse has just left.
    """
    enter: bool
    acceptable: Incomplete
    exit: bool
    currentItem: Incomplete
    def __init__(self, moveEvent, acceptable) -> None: ...
    def isEnter(self):
        """Returns True if the mouse has just entered the item's shape"""
    def isExit(self):
        """Returns True if the mouse has just exited the item's shape"""
    def acceptClicks(self, button):
        """Inform the scene that the item (that the event was delivered to)
        would accept a mouse click event if the user were to click before
        moving the mouse again.
        
        Returns True if the request is successful, otherwise returns False (indicating
        that some other item would receive an incoming click).
        """
    def acceptDrags(self, button):
        """Inform the scene that the item (that the event was delivered to)
        would accept a mouse drag event if the user were to drag before
        the next hover event.
        
        Returns True if the request is successful, otherwise returns False (indicating
        that some other item would receive an incoming drag event).
        """
    def scenePos(self):
        """Return the current scene position of the mouse."""
    def screenPos(self):
        """Return the current screen position of the mouse."""
    def lastScenePos(self):
        """Return the previous scene position of the mouse."""
    def lastScreenPos(self):
        """Return the previous screen position of the mouse."""
    def buttons(self):
        """
        Return the buttons currently pressed on the mouse.
        (see QGraphicsSceneMouseEvent::buttons in the Qt documentation)
        """
    def pos(self):
        """
        Return the current position of the mouse in the coordinate system of the item
        that the event was delivered to.
        """
    def lastPos(self):
        """
        Return the previous position of the mouse in the coordinate system of the item
        that the event was delivered to.
        """
    def modifiers(self):
        """Return any keyboard modifiers currently pressed.
        (see QGraphicsSceneMouseEvent::modifiers in the Qt documentation)        
        """
    def clickItems(self): ...
    def dragItems(self): ...
