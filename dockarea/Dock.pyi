from ..Qt import QtCore as QtCore, QtGui as QtGui, QtWidgets as QtWidgets
from ..widgets.VerticalLabel import VerticalLabel as VerticalLabel
from .DockDrop import DockDrop as DockDrop
from _typeshed import Incomplete

class Dock(QtWidgets.QWidget):
    sigStretchChanged: Incomplete
    sigClosed: Incomplete
    dockdrop: Incomplete
    area: Incomplete
    label: Incomplete
    labelHidden: bool
    moveLabel: bool
    autoOrient: Incomplete
    orientation: str
    topLayout: Incomplete
    widgetArea: Incomplete
    layout: Incomplete
    widgets: Incomplete
    currentRow: int
    hStyle: str
    vStyle: str
    nStyle: str
    dragStyle: str
    def __init__(self, name, area: Incomplete | None = None, size=(10, 10), widget: Incomplete | None = None, hideTitle: bool = False, autoOrientation: bool = True, label: Incomplete | None = None, **kargs) -> None: ...
    def implements(self, name: Incomplete | None = None): ...
    def setStretch(self, x: Incomplete | None = None, y: Incomplete | None = None) -> None:
        """
        Set the 'target' size for this Dock.
        The actual size will be determined by comparing this Dock's
        stretch value to the rest of the docks it shares space with.
        """
    def stretch(self): ...
    def hideTitleBar(self) -> None:
        """
        Hide the title bar for this Dock.
        This will prevent the Dock being moved by the user.
        """
    def showTitleBar(self) -> None:
        """
        Show the title bar for this Dock.
        """
    def title(self):
        """
        Gets the text displayed in the title bar for this dock.
        """
    def setTitle(self, text) -> None:
        """
        Sets the text displayed in title bar for this Dock.
        """
    def setOrientation(self, o: str = 'auto', force: bool = False) -> None:
        """
        Sets the orientation of the title bar for this Dock.
        Must be one of 'auto', 'horizontal', or 'vertical'.
        By default ('auto'), the orientation is determined
        based on the aspect ratio of the Dock.
        """
    def updateStyle(self) -> None: ...
    def resizeEvent(self, ev) -> None: ...
    def name(self): ...
    def addWidget(self, widget, row: Incomplete | None = None, col: int = 0, rowspan: int = 1, colspan: int = 1) -> None:
        """
        Add a new widget to the interior of this Dock.
        Each Dock uses a QGridLayout to arrange widgets within.
        """
    drag: Incomplete
    def startDrag(self) -> None: ...
    def float(self) -> None: ...
    def container(self): ...
    def containerChanged(self, c) -> None: ...
    def raiseDock(self) -> None:
        """If this Dock is stacked underneath others, raise it to the top."""
    def close(self) -> None:
        """Remove this dock from the DockArea it lives inside."""
    def dragEnterEvent(self, *args) -> None: ...
    def dragMoveEvent(self, *args) -> None: ...
    def dragLeaveEvent(self, *args) -> None: ...
    def dropEvent(self, *args) -> None: ...

class DockLabel(VerticalLabel):
    sigClicked: Incomplete
    sigCloseClicked: Incomplete
    dim: bool
    fixedWidth: bool
    fontSize: Incomplete
    dock: Incomplete
    mouseMoved: bool
    closeButton: Incomplete
    def __init__(self, text, closable: bool = False, fontSize: str = '12px') -> None: ...
    vStyle: Incomplete
    hStyle: Incomplete
    def updateStyle(self) -> None: ...
    def setDim(self, d) -> None: ...
    def setOrientation(self, o) -> None: ...
    def isClosable(self): ...
    pressPos: Incomplete
    def mousePressEvent(self, ev) -> None: ...
    def mouseMoveEvent(self, ev) -> None: ...
    def mouseReleaseEvent(self, ev) -> None: ...
    def mouseDoubleClickEvent(self, ev) -> None: ...
    def resizeEvent(self, ev) -> None: ...
