from ..Qt import QtCore, QtWidgets
from ..graphicsItems.GraphicsObject import GraphicsObject
from _typeshed import Incomplete

__all__ = ['Node', 'NodeGraphicsItem']

class Node(QtCore.QObject):
    """
    Node represents the basic processing unit of a flowchart. 
    A Node subclass implements at least:
    
    1) A list of input / output terminals and their properties
    2) a process() function which takes the names of input terminals as keyword arguments and returns a dict with the names of output terminals as keys.

    A flowchart thus consists of multiple instances of Node subclasses, each of which is connected
    to other by wires between their terminals. A flowchart is, itself, also a special subclass of Node.
    This allows Nodes within the flowchart to connect to the input/output nodes of the flowchart itself.

    Optionally, a node class can implement the ctrlWidget() method, which must return a QWidget (usually containing other widgets) that will be displayed in the flowchart control panel. Some nodes implement fairly complex control widgets, but most nodes follow a simple form-like pattern: a list of parameter names and a single value (represented as spin box, check box, etc..) for each parameter. To make this easier, the CtrlNode subclass allows you to instead define a simple data structure that CtrlNode will use to automatically generate the control widget.     """
    sigOutputChanged: Incomplete
    sigClosed: Incomplete
    sigRenamed: Incomplete
    sigTerminalRenamed: Incomplete
    sigTerminalAdded: Incomplete
    sigTerminalRemoved: Incomplete
    bypassButton: Incomplete
    terminals: Incomplete
    exception: Incomplete
    def __init__(self, name, terminals: Incomplete | None = None, allowAddInput: bool = False, allowAddOutput: bool = False, allowRemove: bool = True) -> None:
        """
        ==============  ============================================================
        **Arguments:**
        name            The name of this specific node instance. It can be any 
                        string, but must be unique within a flowchart. Usually,
                        we simply let the flowchart decide on a name when calling
                        Flowchart.addNode(...)
        terminals       Dict-of-dicts specifying the terminals present on this Node.
                        Terminal specifications look like::
                        
                            'inputTerminalName': {'io': 'in'}
                            'outputTerminalName': {'io': 'out'} 
                            
                        There are a number of optional parameters for terminals:
                        multi, pos, renamable, removable, multiable, bypass. See
                        the Terminal class for more information.
        allowAddInput   bool; whether the user is allowed to add inputs by the
                        context menu.
        allowAddOutput  bool; whether the user is allowed to add outputs by the
                        context menu.
        allowRemove     bool; whether the user is allowed to remove this node by the
                        context menu.
        ==============  ============================================================  
        
        """
    def nextTerminalName(self, name):
        """Return an unused terminal name"""
    def addInput(self, name: str = 'Input', **args):
        """Add a new input terminal to this Node with the given name. Extra
        keyword arguments are passed to Terminal.__init__.
        
        This is a convenience function that just calls addTerminal(io='in', ...)"""
    def addOutput(self, name: str = 'Output', **args):
        """Add a new output terminal to this Node with the given name. Extra
        keyword arguments are passed to Terminal.__init__.
        
        This is a convenience function that just calls addTerminal(io='out', ...)"""
    def removeTerminal(self, term) -> None:
        """Remove the specified terminal from this Node. May specify either the 
        terminal's name or the terminal itself.
        
        Causes sigTerminalRemoved to be emitted."""
    def terminalRenamed(self, term, oldName) -> None:
        """Called after a terminal has been renamed        
        
        Causes sigTerminalRenamed to be emitted."""
    def addTerminal(self, name, **opts):
        """Add a new terminal to this Node with the given name. Extra
        keyword arguments are passed to Terminal.__init__.
                
        Causes sigTerminalAdded to be emitted."""
    def inputs(self):
        """Return dict of all input terminals.
        Warning: do not modify."""
    def outputs(self):
        """Return dict of all output terminals.
        Warning: do not modify."""
    def process(self, **kargs):
        """Process data through this node. This method is called any time the flowchart 
        wants the node to process data. It will be called with one keyword argument
        corresponding to each input terminal, and must return a dict mapping the name
        of each output terminal to its new value.
        
        This method is also called with a 'display' keyword argument, which indicates
        whether the node should update its display (if it implements any) while processing
        this data. This is primarily used to disable expensive display operations
        during batch processing.
        """
    def graphicsItem(self):
        """Return the GraphicsItem for this node. Subclasses may re-implement
        this method to customize their appearance in the flowchart."""
    def __getitem__(self, item):
        """Return the terminal with the given name"""
    def name(self):
        """Return the name of this node."""
    def rename(self, name) -> None:
        """Rename this node. This will cause sigRenamed to be emitted."""
    def dependentNodes(self):
        """Return the list of nodes which provide direct input to this node"""
    def ctrlWidget(self) -> None:
        """Return this Node's control widget. 
        
        By default, Nodes have no control widget. Subclasses may reimplement this 
        method to provide a custom widget. This method is called by Flowcharts
        when they are constructing their Node list."""
    def bypass(self, byp) -> None:
        """Set whether this node should be bypassed.
        
        When bypassed, a Node's process() method is never called. In some cases,
        data is automatically copied directly from specific input nodes to 
        output nodes instead (see the bypass argument to Terminal.__init__). 
        This is usually called when the user disables a node from the flowchart 
        control panel.
        """
    def isBypassed(self):
        """Return True if this Node is currently bypassed."""
    def setInput(self, **args) -> None:
        """Set the values on input terminals. For most nodes, this will happen automatically through Terminal.inputChanged.
        This is normally only used for nodes with no connected inputs."""
    def inputValues(self):
        """Return a dict of all input values currently assigned to this node."""
    def outputValues(self):
        """Return a dict of all output values currently generated by this node."""
    def connected(self, localTerm, remoteTerm) -> None:
        """Called whenever one of this node's terminals is connected elsewhere."""
    def disconnected(self, localTerm, remoteTerm) -> None:
        """Called whenever one of this node's terminals is disconnected from another."""
    def update(self, signal: bool = True) -> None:
        """Collect all input values, attempt to process new output values, and propagate downstream.
        Subclasses should call update() whenever thir internal state has changed
        (such as when the user interacts with the Node's control widget). Update
        is automatically called when the inputs to the node are changed.
        """
    def processBypassed(self, args):
        """Called when the flowchart would normally call Node.process, but this node is currently bypassed.
        The default implementation looks for output terminals with a bypass connection and returns the
        corresponding values. Most Node subclasses will _not_ need to reimplement this method."""
    def setOutput(self, **vals) -> None: ...
    def setOutputNoSignal(self, **vals) -> None: ...
    def setException(self, exc) -> None: ...
    def clearException(self) -> None: ...
    def recolor(self) -> None: ...
    def saveState(self):
        """Return a dictionary representing the current state of this node
        (excluding input / output values). This is used for saving/reloading
        flowcharts. The default implementation returns this Node's position,
        bypass state, and information about each of its terminals. 
        
        Subclasses may want to extend this method, adding extra keys to the returned
        dict."""
    def restoreState(self, state) -> None:
        """Restore the state of this node from a structure previously generated
        by saveState(). """
    def saveTerminals(self): ...
    def restoreTerminals(self, state) -> None: ...
    def clearTerminals(self) -> None: ...
    def close(self) -> None:
        """Cleans up after the node--removes terminals, graphicsItem, widget"""
    def disconnectAll(self) -> None: ...

class TextItem(QtWidgets.QGraphicsTextItem):
    on_update: Incomplete
    def __init__(self, text, parent, on_update) -> None: ...
    def focusOutEvent(self, ev) -> None: ...
    def keyPressEvent(self, ev) -> None: ...
    def mousePressEvent(self, ev) -> None: ...

class NodeGraphicsItem(GraphicsObject):
    pen: Incomplete
    selectPen: Incomplete
    brush: Incomplete
    hoverBrush: Incomplete
    selectBrush: Incomplete
    hovered: bool
    node: Incomplete
    bounds: Incomplete
    nameItem: Incomplete
    menu: Incomplete
    def __init__(self, node) -> None: ...
    def setTitleOffset(self, new_offset) -> None:
        """
        This method sets the rendering offset introduced after the title of the node.
        This method automatically updates the terminal labels. The default for this value is 25px.

        :param new_offset: The new offset to use in pixels at 100% scale.
        """
    def titleOffset(self):
        """
        This method returns the current title offset in use.

        :returns: The offset in px.
        """
    def setTerminalOffset(self, new_offset) -> None:
        """
        This method sets the rendering offset introduced after every terminal of the node.
        This method automatically updates the terminal labels. The default for this value is 12px.

        :param new_offset: The new offset to use in pixels at 100% scale.
        """
    def terminalOffset(self):
        """
        This method returns the current terminal offset in use.

        :returns: The offset in px.
        """
    def labelChanged(self) -> None: ...
    def setPen(self, *args, **kwargs) -> None: ...
    def setBrush(self, brush) -> None: ...
    terminals: Incomplete
    def updateTerminals(self) -> None: ...
    def boundingRect(self): ...
    def paint(self, p, *args) -> None: ...
    def mousePressEvent(self, ev) -> None: ...
    def mouseClickEvent(self, ev) -> None: ...
    def mouseDragEvent(self, ev) -> None: ...
    def hoverEvent(self, ev) -> None: ...
    def keyPressEvent(self, ev) -> None: ...
    def itemChange(self, change, val): ...
    def getMenu(self): ...
    def raiseContextMenu(self, ev) -> None: ...
    def buildMenu(self) -> None: ...
    def addInputFromMenu(self) -> None: ...
    def addOutputFromMenu(self) -> None: ...
