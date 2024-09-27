from . import FlowchartGraphicsView as FlowchartGraphicsView
from .. import DataTreeWidget as DataTreeWidget, FileDialog as FileDialog, dockarea as dockarea
from ..Qt import QtCore as QtCore, QtWidgets as QtWidgets
from ..debug import printExc as printExc
from ..graphicsItems.GraphicsObject import GraphicsObject as GraphicsObject
from .Node import Node as Node
from .Terminal import Terminal as Terminal
from .library import LIBRARY as LIBRARY
from _typeshed import Incomplete

__init__: Incomplete

def strDict(d): ...

class Flowchart(Node):
    sigFileLoaded: Incomplete
    sigFileSaved: Incomplete
    sigChartLoaded: Incomplete
    sigStateChanged: Incomplete
    sigChartChanged: Incomplete
    library: Incomplete
    filePath: Incomplete
    inputWasSet: bool
    nextZVal: int
    processing: bool
    inputNode: Incomplete
    outputNode: Incomplete
    def __init__(self, terminals: Incomplete | None = None, name: Incomplete | None = None, filePath: Incomplete | None = None, library: Incomplete | None = None) -> None: ...
    def setLibrary(self, lib) -> None: ...
    def setInput(self, **args) -> None:
        """Set the input values of the flowchart. This will automatically propagate
        the new values throughout the flowchart, (possibly) causing the output to change.
        """
    def outputChanged(self) -> None: ...
    def output(self):
        """Return a dict of the values on the Flowchart's output terminals.
        """
    def nodes(self): ...
    def addTerminal(self, name, **opts): ...
    def removeTerminal(self, name) -> None: ...
    def internalTerminalRenamed(self, term, oldName) -> None: ...
    def internalTerminalAdded(self, node, term) -> None: ...
    def internalTerminalRemoved(self, node, term) -> None: ...
    def terminalRenamed(self, term, oldName) -> None: ...
    def createNode(self, nodeType, name: Incomplete | None = None, pos: Incomplete | None = None):
        """Create a new Node and add it to this flowchart.
        """
    def addNode(self, node, name, pos: Incomplete | None = None) -> None:
        """Add an existing Node to this flowchart.
        
        See also: createNode()
        """
    def removeNode(self, node) -> None:
        """Remove a Node from this flowchart.
        """
    def nodeClosed(self, node) -> None: ...
    def nodeRenamed(self, node, oldName) -> None: ...
    def arrangeNodes(self) -> None: ...
    def internalTerminal(self, term):
        """If the terminal belongs to the external Node, return the corresponding internal terminal"""
    def connectTerminals(self, term1, term2) -> None:
        """Connect two terminals together within this flowchart."""
    def process(self, **args):
        """
        Process data through the flowchart, returning the output.
        
        Keyword arguments must be the names of input terminals. 
        The return value is a dict with one key per output terminal.
        
        """
    def processOrder(self):
        """Return the order of operations required to process this chart.
        The order returned should look like [('p', node1), ('p', node2), ('d', terminal1), ...] 
        where each tuple specifies either (p)rocess this node or (d)elete the result from this terminal
        """
    def nodeOutputChanged(self, startNode) -> None:
        """Triggered when a node's output values have changed. (NOT called during process())
        Propagates new data forward through network."""
    def chartGraphicsItem(self):
        """Return the graphicsItem that displays the internal nodes and
        connections of this flowchart.
        
        Note that the similar method `graphicsItem()` is inherited from Node
        and returns the *external* graphical representation of this flowchart."""
    scene: Incomplete
    viewBox: Incomplete
    def widget(self):
        """Return the control widget for this flowchart.
        
        This widget provides GUI access to the parameters for each node and a
        graphical representation of the flowchart.
        """
    def listConnections(self): ...
    def saveState(self):
        """Return a serializable data structure representing the current state of this flowchart. 
        """
    def restoreState(self, state, clear: bool = False):
        """Restore the state of this flowchart from a previous call to `saveState()`.
        """
    fileDialog: Incomplete
    def loadFile(self, fileName: Incomplete | None = None, startDir: Incomplete | None = None) -> None:
        """Load a flowchart (``*.fc``) file.
        """
    def saveFile(self, fileName: Incomplete | None = None, startDir: Incomplete | None = None, suggestedFileName: str = 'flowchart.fc') -> None:
        """Save this flowchart to a .fc file
        """
    def clear(self) -> None:
        """Remove all nodes from this flowchart except the original input/output nodes.
        """
    def clearTerminals(self) -> None: ...

class FlowchartGraphicsItem(GraphicsObject):
    chart: Incomplete
    def __init__(self, chart) -> None: ...
    terminals: Incomplete
    def updateTerminals(self) -> None: ...
    def boundingRect(self): ...
    def paint(self, p, *args) -> None: ...

class FlowchartCtrlWidget(QtWidgets.QWidget):
    """The widget that contains the list of all the nodes in a flowchart and their controls, as well as buttons for loading/saving flowcharts."""
    items: Incomplete
    currentFileName: Incomplete
    chart: Incomplete
    ui: Incomplete
    cwWin: Incomplete
    def __init__(self, chart) -> None: ...
    def chartToggled(self, b) -> None: ...
    def reloadClicked(self) -> None: ...
    def loadClicked(self) -> None: ...
    def fileSaved(self, fileName) -> None: ...
    def saveClicked(self) -> None: ...
    def saveAsClicked(self) -> None: ...
    def setCurrentFile(self, fileName) -> None: ...
    def itemChanged(self, *args) -> None: ...
    def scene(self): ...
    def viewBox(self): ...
    def nodeRenamed(self, node, oldName) -> None: ...
    def addNode(self, node) -> None: ...
    def removeNode(self, node) -> None: ...
    def bypassClicked(self) -> None: ...
    def chartWidget(self): ...
    def outputChanged(self, data) -> None: ...
    def clear(self) -> None: ...
    def select(self, node) -> None: ...
    def clearSelection(self) -> None: ...

class FlowchartWidget(dockarea.DockArea):
    """Includes the actual graphical flowchart and debugging interface"""
    chart: Incomplete
    ctrl: Incomplete
    hoverItem: Incomplete
    view: Incomplete
    viewDock: Incomplete
    hoverText: Incomplete
    hoverDock: Incomplete
    selInfo: Incomplete
    selInfoLayout: Incomplete
    selDescLabel: Incomplete
    selNameLabel: Incomplete
    selectedTree: Incomplete
    selDock: Incomplete
    def __init__(self, chart, ctrl) -> None: ...
    nodeMenu: Incomplete
    subMenus: Incomplete
    def reloadLibrary(self) -> None: ...
    def buildMenu(self, pos: Incomplete | None = None): ...
    menuPos: Incomplete
    def menuPosChanged(self, pos) -> None: ...
    def showViewMenu(self, ev) -> None: ...
    def scene(self): ...
    def viewBox(self): ...
    def nodeMenuTriggered(self, action) -> None: ...
    def selectionChanged(self) -> None: ...
    def hoverOver(self, items) -> None: ...
    def clear(self) -> None: ...

class FlowchartNode(Node): ...
