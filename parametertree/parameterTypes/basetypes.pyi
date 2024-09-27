from ... import icons as icons
from ...Qt import QtCore as QtCore, QtWidgets as QtWidgets
from ..Parameter import Parameter as Parameter
from ..ParameterItem import ParameterItem as ParameterItem
from _typeshed import Incomplete

class WidgetParameterItem(ParameterItem):
    """
    ParameterTree item with:

      * label in second column for displaying value
      * simple widget for editing value (displayed instead of label when item is selected)
      * button that resets value to default

    This class can be subclassed by overriding makeWidget() to provide a custom widget.
    """
    asSubItem: bool
    hideWidget: bool
    widget: Incomplete
    eventProxy: Incomplete
    subItem: Incomplete
    defaultBtn: Incomplete
    displayLabel: Incomplete
    layoutWidget: Incomplete
    def __init__(self, param, depth) -> None: ...
    def makeWidget(self) -> None:
        """
        Return a single widget whose position in the tree is determined by the
        value of self.asSubItem. If True, it will be placed in the second tree
        column, and if False, the first tree column of a child item.

        The widget must be given three attributes:

        ==========  ============================================================
        sigChanged  a signal that is emitted when the widget's value is changed
        value       a function that returns the value
        setValue    a function that sets the value
        ==========  ============================================================

        This function must be overridden by a subclass.
        """
    def widgetEventFilter(self, obj, ev): ...
    def makeDefaultButton(self): ...
    def setFocus(self) -> None: ...
    def isFocusable(self): ...
    def valueChanged(self, param, val, force: bool = False) -> None: ...
    def updateDefaultBtn(self) -> None: ...
    def updateDisplayLabel(self, value: Incomplete | None = None) -> None:
        """Update the display label to reflect the value of the parameter."""
    def widgetValueChanged(self) -> None: ...
    def widgetValueChanging(self, *args) -> None:
        """
        Called when the widget's value is changing, but not finalized.
        For example: editing text before pressing enter or changing focus.
        """
    def selected(self, sel) -> None:
        """Called when this item has been selected (sel=True) OR deselected (sel=False)"""
    def showEditor(self) -> None: ...
    def hideEditor(self) -> None: ...
    def limitsChanged(self, param, limits) -> None:
        """Called when the parameter's limits have changed"""
    def defaultChanged(self, param, value) -> None: ...
    def treeWidgetChanged(self) -> None:
        """Called when this item is added or removed from a tree."""
    def defaultClicked(self) -> None: ...
    def optsChanged(self, param, opts) -> None:
        """Called when any options are changed that are not
        name, value, default, or limits"""

class EventProxy(QtCore.QObject):
    callback: Incomplete
    def __init__(self, qobj, callback) -> None: ...
    def eventFilter(self, obj, ev): ...

class SimpleParameter(Parameter):
    """
    Parameter representing a single value.

    This parameter is backed by :class:`~pyqtgraph.parametertree.parameterTypes.basetypes.WidgetParameterItem`
     to represent the following parameter names through various subclasses:

      - 'int'
      - 'float'
      - 'bool'
      - 'str'
      - 'color'
      - 'colormap'
    """
    @property
    def itemClass(self): ...

class GroupParameterItem(ParameterItem):
    """
    Group parameters are used mainly as a generic parent item that holds (and groups!) a set
    of child parameters. It also provides a simple mechanism for displaying a button or combo
    that can be used to add new parameters to the group.
    """
    addItem: Incomplete
    addWidget: Incomplete
    addWidgetBox: Incomplete
    def __init__(self, param, depth) -> None: ...
    def pointSize(self): ...
    def updateDepth(self, depth) -> None:
        """
        Change set the item font to bold and increase the font size on outermost groups.
        """
    def addClicked(self) -> None:
        '''Called when "add new" button is clicked
        The parameter MUST have an \'addNew\' method defined.
        '''
    def addChanged(self) -> None:
        '''Called when "add new" combo is changed
        The parameter MUST have an \'addNew\' method defined.
        '''
    def treeWidgetChanged(self) -> None: ...
    def addChild(self, child) -> None: ...
    def optsChanged(self, param, opts) -> None: ...
    def updateAddList(self) -> None: ...

class GroupParameter(Parameter):
    """
    Group parameters are used mainly as a generic parent item that holds (and groups!) a set
    of child parameters.

    It also provides a simple mechanism for displaying a button or combo
    that can be used to add new parameters to the group. To enable this, the group
    must be initialized with the 'addText' option (the text will be displayed on
    a button which, when clicked, will cause addNew() to be called). If the 'addList'
    option is specified as well, then a dropdown-list of addable items will be displayed
    instead of a button.
    """
    itemClass = GroupParameterItem
    sigAddNew: Incomplete
    def addNew(self, typ: Incomplete | None = None) -> None:
        """
        This method is called when the user has requested to add a new item to the group.
        By default, it emits ``sigAddNew(self, typ)``.
        """
    def setAddList(self, vals) -> None:
        """Change the list of options available for the user to add to the group."""

class Emitter(QtCore.QObject):
    """
    WidgetParameterItem is not a QObject, so create a QObject wrapper that items can use for emitting
    """
    sigChanging: Incomplete
    sigChanged: Incomplete
