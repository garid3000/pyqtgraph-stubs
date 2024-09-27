from .. import parametertree as ptree
from _typeshed import Incomplete

__all__ = ['ColorMapWidget', 'ColorMapParameter']

class ColorMapWidget(ptree.ParameterTree):
    """
    This class provides a widget allowing the user to customize color mapping
    for multi-column data. Given a list of field names, the user may specify
    multiple criteria for assigning colors to each record in a numpy record array.
    Multiple criteria are evaluated and combined into a single color for each
    record by user-defined compositing methods.
    
    For simpler color mapping using a single gradient editor, see 
    :class:`GradientWidget <pyqtgraph.GradientWidget>`
    """
    sigColorMapChanged: Incomplete
    params: Incomplete
    setFields: Incomplete
    map: Incomplete
    def __init__(self, parent: Incomplete | None = None) -> None: ...
    def mapChanged(self) -> None: ...
    def widgetGroupInterface(self): ...
    def saveState(self): ...
    def restoreState(self, state) -> None: ...
    def addColorMap(self, name):
        """Add a new color mapping and return the created parameter.
        """

class ColorMapParameter(ptree.types.GroupParameter):
    sigColorMapChanged: Incomplete
    fields: Incomplete
    def __init__(self) -> None: ...
    def mapChanged(self) -> None: ...
    def addNew(self, name): ...
    def fieldNames(self): ...
    def setFields(self, fields) -> None:
        """
        Set the list of fields to be used by the mapper. 
        
        The format of *fields* is::
        
            [ (fieldName, {options}), ... ]
        
        ============== ============================================================
        Field Options:
        mode           Either 'range' or 'enum' (default is range). For 'range', 
                       The user may specify a gradient of colors to be applied 
                       linearly across a specific range of values. For 'enum', 
                       the user specifies a single color for each unique value
                       (see *values* option).
        units          String indicating the units of the data for this field.
        values         List of unique values for which the user may assign a 
                       color when mode=='enum'. Optionally may specify a dict 
                       instead {value: name}.
        defaults       Dict of default values to apply to color map items when
                       they are created. Valid keys are 'colormap' to provide
                       a default color map, or otherwise they a string or tuple
                       indicating the parameter to be set, such as 'Operation' or
                       ('Channels..', 'Red').
        ============== ============================================================
        """
    def map(self, data, mode: str = 'byte'):
        """
        Return an array of colors corresponding to *data*. 
        
        ==============  =================================================================
        **Arguments:**
        data            A numpy record array where the fields in data.dtype match those
                        defined by a prior call to setFields().
        mode            Either 'byte' or 'float'. For 'byte', the method returns an array
                        of dtype ubyte with values scaled 0-255. For 'float', colors are
                        returned as 0.0-1.0 float values.
        ==============  =================================================================
        """
    def saveState(self): ...
    def restoreState(self, state) -> None: ...

class RangeColorMapItem(ptree.types.ColorMapParameter):
    mapType: str
    fieldName: Incomplete
    def __init__(self, name, opts) -> None: ...
    def map(self, data): ...

class EnumColorMapItem(ptree.types.GroupParameter):
    mapType: str
    fieldName: Incomplete
    def __init__(self, name, opts) -> None: ...
    def map(self, data): ...
