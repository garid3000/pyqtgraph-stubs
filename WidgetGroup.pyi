from .Qt import QtCore
from _typeshed import Incomplete

__all__ = ['WidgetGroup']

class WidgetGroup(QtCore.QObject):
    """State manager for groups of widgets.

    WidgetGroup handles common problems that arise when dealing with groups of widgets like a control
    panel:
    - Provide a single place for saving / restoring the state of all widgets in the group
    - Provide a single signal for detecting when any of the widgets have changed
    """
    classes: Incomplete
    sigChanged: Incomplete
    widgetList: Incomplete
    scales: Incomplete
    cache: Incomplete
    uncachedWidgets: Incomplete
    def __init__(self, widgetList: Incomplete | None = None) -> None:
        """Initialize WidgetGroup, adding specified widgets into this group.
        widgetList can be: 
         - a list of widget specifications (widget, [name], [scale])
         - a dict of name: widget pairs
         - any QObject, and all compatible child widgets will be added recursively.
        
        The 'scale' parameter for each widget allows QSpinBox to display a different value than the value recorded
        in the group state (for example, the program may set a spin box value to 100e-6 and have it displayed as 100 to the user)
        """
    def addWidget(self, w, name: Incomplete | None = None, scale: Incomplete | None = None) -> None: ...
    def findWidget(self, name): ...
    def interface(self, obj): ...
    def checkForChildren(self, obj):
        """Return true if we should automatically search the children of this object for more."""
    def autoAdd(self, obj) -> None: ...
    def acceptsType(self, obj): ...
    def setScale(self, widget, scale) -> None: ...
    def widgetChanged(self, *args) -> None: ...
    def state(self): ...
    def setState(self, s) -> None: ...
    def readWidget(self, w): ...
    def setWidget(self, w, v) -> None: ...
