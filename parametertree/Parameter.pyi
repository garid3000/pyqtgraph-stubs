from ..Qt import QtCore as QtCore
from .ParameterItem import ParameterItem as ParameterItem
from _typeshed import Incomplete

PARAM_TYPES: Incomplete
PARAM_NAMES: Incomplete

def registerParameterItemType(name, itemCls, parameterCls: Incomplete | None = None, override: bool = False) -> None:
    """
    Similar to :func:`registerParameterType`, but works on ParameterItems. This is useful for Parameters where the
    `itemClass` does all the heavy lifting, and a redundant Parameter class must be defined just to house `itemClass`.
    Instead, use `registerParameterItemType`. If this should belong to a subclass of `Parameter`, specify which one
    in `parameterCls`.
    """
def registerParameterType(name, cls, override: bool = False) -> None:
    """Register a parameter type in the parametertree system.

    This enables construction of custom Parameter classes by name in
    :meth:`~pyqtgraph.parametertree.Parameter.create`.
    """
def __reload__(old) -> None: ...

class Parameter(QtCore.QObject):
    """
    A Parameter is the basic unit of data in a parameter tree. Each parameter has
    a name, a type, a value, and several other properties that modify the behavior of the 
    Parameter. Parameters may have parent / child / sibling relationships to construct
    organized hierarchies. Parameters generally do not have any inherent GUI or visual
    interpretation; instead they manage ParameterItem instances which take care of
    display and user interaction.
    
    Note: It is fairly uncommon to use the Parameter class directly; mostly you 
    will use subclasses which provide specialized type and data handling. The static
    method Parameter.create(...) is an easy way to generate instances of these subclasses.
       
    For more Parameter types, see ParameterTree.parameterTypes module.
    
    ===================================  =========================================================
    **Signals:**
    sigStateChanged(self, change, info)  Emitted when anything changes about this parameter at 
                                         all.
                                         The second argument is a string indicating what changed 
                                         ('value', 'childAdded', etc..)
                                         The third argument can be any extra information about 
                                         the change
    sigTreeStateChanged(self, changes)   Emitted when any child in the tree changes state
                                         (but only if monitorChildren() is called)
                                         the format of *changes* is [(param, change, info), ...]
    sigValueChanged(self, value)         Emitted when value is finished changing
    sigValueChanging(self, value)        Emitted immediately for all value changes, 
                                         including during editing.
    sigChildAdded(self, child, index)    Emitted when a child is added
    sigChildRemoved(self, child)         Emitted when a child is removed
    sigRemoved(self)                     Emitted when this parameter is removed
    sigParentChanged(self, parent)       Emitted when this parameter's parent has changed
    sigLimitsChanged(self, limits)       Emitted when this parameter's limits have changed
    sigDefaultChanged(self, default)     Emitted when this parameter's default value has changed
    sigNameChanged(self, name)           Emitted when this parameter's name has changed
    sigOptionsChanged(self, opts)        Emitted when any of this parameter's options have changed
    sigContextMenu(self, name)           Emitted when a context menu was clicked
    ===================================  =========================================================
    """
    sigValueChanged: Incomplete
    sigValueChanging: Incomplete
    sigChildAdded: Incomplete
    sigChildRemoved: Incomplete
    sigRemoved: Incomplete
    sigParentChanged: Incomplete
    sigLimitsChanged: Incomplete
    sigDefaultChanged: Incomplete
    sigNameChanged: Incomplete
    sigOptionsChanged: Incomplete
    sigStateChanged: Incomplete
    sigTreeStateChanged: Incomplete
    sigContextMenu: Incomplete
    @staticmethod
    def create(**opts):
        """
        Static method that creates a new Parameter (or subclass) instance using 
        opts['type'] to select the appropriate class.
        
        All options are passed directly to the new Parameter's __init__ method.
        Use registerParameterType() to add new class types.
        """
    opts: Incomplete
    childs: Incomplete
    names: Incomplete
    items: Incomplete
    treeStateChanges: Incomplete
    blockTreeChangeEmit: int
    def __init__(self, **opts) -> None:
        """
        Initialize a Parameter object. Although it is rare to directly create a
        Parameter instance, the options available to this method are also allowed
        by most Parameter subclasses.
        
        =======================      =========================================================
        **Keyword Arguments:**
        name                         The name to give this Parameter. This is the name that
                                     will appear in the left-most column of a ParameterTree
                                     for this Parameter.
        value                        The value to initially assign to this Parameter.
        default                      The default value for this Parameter (most Parameters
                                     provide an option to 'reset to default').
        children                     A list of children for this Parameter. Children
                                     may be given either as a Parameter instance or as a
                                     dictionary to pass to Parameter.create(). In this way,
                                     it is possible to specify complex hierarchies of
                                     Parameters from a single nested data structure.
        readonly                     If True, the user will not be allowed to edit this
                                     Parameter. (default=False)
        enabled                      If False, any widget(s) for this parameter will appear
                                     disabled. (default=True)
        visible                      If False, the Parameter will not appear when displayed
                                     in a ParameterTree. (default=True)
        renamable                    If True, the user may rename this Parameter.
                                     (default=False)
        removable                    If True, the user may remove this Parameter.
                                     (default=False)
        expanded                     If True, the Parameter will initially be expanded in
                                     ParameterTrees: Its children will be visible.
                                     (default=True)
        syncExpanded                 If True, the `expanded` state of this Parameter is
                                     synchronized with all ParameterTrees it is displayed in.
                                     (default=False)
        title                        (str or None) If specified, then the parameter will be 
                                     displayed to the user using this string as its name. 
                                     However, the parameter will still be referred to 
                                     internally using the *name* specified above. Note that
                                     this option is not compatible with renamable=True.
                                     (default=None; added in version 0.9.9)
        =======================      =========================================================
        """
    @property
    def itemClass(self):
        """
        The class of ParameterItem to use when displaying this parameter in a ParameterTree.
        """
    def name(self):
        """Return the name of this Parameter."""
    def title(self):
        """Return the title of this Parameter.
        
        By default, the title is the same as the name unless it has been explicitly specified
        otherwise."""
    def contextMenu(self, name) -> None:
        '''"A context menu entry was clicked'''
    def setName(self, name):
        """Attempt to change the name of this parameter; return the actual name. 
        (The parameter may reject the name change or automatically pick a different name)"""
    def type(self):
        """Return the type string for this Parameter."""
    def isType(self, typ):
        """
        Return True if this parameter type matches the name *typ*.
        This can occur either of two ways:
        
          - If self.type() == *typ*
          - If this parameter's class is registered with the name *typ*
        """
    def childPath(self, child):
        """
        Return the path of parameter names from self to child.
        If child is not a (grand)child of self, return None.
        """
    def setValue(self, value, blockSignal: Incomplete | None = None):
        """
        Set the value of this Parameter; return the actual value that was set.
        (this may be different from the value that was requested)
        """
    def hasValue(self):
        """Return True if this Parameter has a value set."""
    def value(self):
        """
        Return the value of this Parameter. Raises ValueError if no value has been set.
        """
    def getValues(self):
        """
        Return a tree of all values that are children of this parameter. Raises ValueError if any child has no value.
        """
    def saveState(self, filter: Incomplete | None = None):
        """
        Return a structure representing the entire state of the parameter tree.
        The tree state may be restored from this structure using restoreState().

        If *filter* is set to 'user', then only user-settable data will be included in the
        returned state.
        """
    def restoreState(self, state, recursive: bool = True, addChildren: bool = True, removeChildren: bool = True, blockSignals: bool = True) -> None:
        """
        Restore the state of this parameter and its children from a structure generated using saveState()
        If recursive is True, then attempt to restore the state of child parameters as well.
        If addChildren is True, then any children which are referenced in the state object will be
        created if they do not already exist.
        If removeChildren is True, then any children which are not referenced in the state object will 
        be removed.
        If blockSignals is True, no signals will be emitted until the tree has been completely restored. 
        This prevents signal handlers from responding to a partially-rebuilt network.
        """
    def valueModifiedSinceResetToDefault(self):
        """Return True if this parameter's value has been changed since the last time
        it was reset to its default value."""
    def defaultValue(self):
        """Return the default value for this parameter. Raises ValueError if no default."""
    def setDefault(self, val, updatePristineValues: bool = False) -> None:
        """Set the default value for this parameter. If updatePristineValues is True, then
        any values that haven't been modified since the last time they were reset to default
        will be updated to the new default value (default: False)."""
    def setToDefault(self) -> None:
        """Set this parameter's value to the default. Raises ValueError if no default is set."""
    def hasDefault(self):
        """Returns True if this parameter has a default value."""
    def valueIsDefault(self):
        """Returns True if this parameter's value is equal to the default value."""
    def setLimits(self, limits):
        """Set limits on the acceptable values for this parameter. 
        The format of limits depends on the type of the parameter and
        some parameters do not make use of limits at all."""
    def writable(self):
        """
        Returns True if this parameter's value can be changed by the user.
        Note that the value of the parameter can *always* be changed by
        calling setValue().
        """
    def setWritable(self, writable: bool = True) -> None:
        """Set whether this Parameter should be editable by the user. (This is 
        exactly the opposite of setReadonly)."""
    def readonly(self):
        """
        Return True if this parameter is read-only. (this is the opposite of writable())
        """
    def setReadonly(self, readonly: bool = True) -> None:
        """Set whether this Parameter's value may be edited by the user
        (this is the opposite of setWritable())."""
    def setOpts(self, **opts) -> None:
        """
        Set any arbitrary options on this parameter.
        The exact behavior of this function will depend on the parameter type, but
        most parameters will accept a common set of options: value, name, limits,
        default, readonly, removable, renamable, visible, enabled, expanded and
        syncExpanded.
        
        See :func:`Parameter.__init__ <pyqtgraph.parametertree.Parameter.__init__>`
        for more information on default options.
        """
    def emitStateChanged(self, changeDesc, data) -> None: ...
    def makeTreeItem(self, depth):
        """
        Return a TreeWidgetItem suitable for displaying/controlling the content of 
        this parameter. This is called automatically when a ParameterTree attempts
        to display this Parameter.
        Most subclasses will want to override this function.
        """
    def addChild(self, child, autoIncrementName: Incomplete | None = None, existOk: bool = False):
        """
        Add another parameter to the end of this parameter's child list.
        
        See insertChild() for a description of the *autoIncrementName* and *existOk*
        arguments.
        """
    def addChildren(self, children) -> None:
        """
        Add a list or dict of children to this parameter. This method calls
        addChild once for each value in *children*.
        """
    def insertChild(self, pos, child, autoIncrementName: Incomplete | None = None, existOk: bool = False):
        """
        Insert a new child at pos.
        If pos is a Parameter, then insert at the position of that Parameter.
        If child is a dict, then a parameter is constructed using
        :func:`Parameter.create <pyqtgraph.parametertree.Parameter.create>`.
        
        By default, the child's 'autoIncrementName' option determines whether
        the name will be adjusted to avoid prior name collisions. This 
        behavior may be overridden by specifying the *autoIncrementName* 
        argument. This argument was added in version 0.9.9.

        If 'autoIncrementName' is *False*, an error is raised when the inserted child already exists. However, if
        'existOk' is *True*, the existing child will be returned instead, and this child will *not* be inserted.
        """
    def removeChild(self, child) -> None:
        """Remove a child parameter."""
    def clearChildren(self) -> None:
        """Remove all child parameters."""
    def children(self):
        """Return a list of this parameter's children.
        Warning: this overrides QObject.children
        """
    def hasChildren(self):
        """Return True if this Parameter has children."""
    def parentChanged(self, parent) -> None:
        """This method is called when the parameter's parent has changed.
        It may be useful to extend this method in subclasses."""
    def parent(self):
        """Return the parent of this parameter."""
    def remove(self) -> None:
        """Remove this parameter from its parent's child list"""
    def incrementName(self, name): ...
    def __iter__(self): ...
    def __getitem__(self, names):
        """Get the value of a child parameter. The name may also be a tuple giving
        the path to a sub-parameter::
        
            value = param[('child', 'grandchild')]

        Raises ValueError if the child value is not set.
        """
    def __setitem__(self, names, value) -> None:
        """Set the value of a child parameter. The name may also be a tuple giving
        the path to a sub-parameter::
        
            param[('child', 'grandchild')] = value
        """
    def keys(self): ...
    def child(self, *names):
        """Return a child parameter. 
        Accepts the name of the child or a tuple (path, to, child)

        Added in version 0.9.9. Earlier versions used the 'param' method, which is still
        implemented for backward compatibility.
        """
    def param(self, *names): ...
    def registerItem(self, item) -> None: ...
    def hide(self) -> None:
        """Hide this parameter. It and its children will no longer be visible in any ParameterTree
        widgets it is connected to."""
    def show(self, s: bool = True) -> None:
        """Show this parameter. """
    def treeChangeBlocker(self):
        """
        Return an object that can be used to temporarily block and accumulate
        sigTreeStateChanged signals. This is meant to be used when numerous changes are 
        about to be made to the tree and only one change signal should be
        emitted at the end.
        
        Example::

            with param.treeChangeBlocker():
                param.addChild(...)
                param.removeChild(...)
                param.setValue(...)
        """
    def blockTreeChangeSignal(self) -> None:
        """
        Used to temporarily block and accumulate tree change signals.
        *You must remember to unblock*, so it is advisable to use treeChangeBlocker() instead.
        """
    def unblockTreeChangeSignal(self) -> None:
        """Unblocks enission of sigTreeStateChanged and flushes the changes out through a single signal."""
    def treeStateChanged(self, param, changes) -> None:
        """
        Called when the state of any sub-parameter has changed. 
        
        ==============  ================================================================
        **Arguments:**
        param           The immediate child whose tree state has changed.
                        note that the change may have originated from a grandchild.
        changes         List of tuples describing all changes that have been made
                        in this event: (param, changeDescr, data)
        ==============  ================================================================
                     
        This function can be extended to react to tree state changes.
        """
    def emitTreeChanges(self) -> None: ...

class SignalBlocker:
    enterFn: Incomplete
    exitFn: Incomplete
    def __init__(self, enterFn, exitFn) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, tb: types.TracebackType | None) -> None: ...
