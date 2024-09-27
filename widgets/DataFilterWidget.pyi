from .. import parametertree as ptree
from _typeshed import Incomplete

__all__ = ['DataFilterWidget']

class DataFilterWidget(ptree.ParameterTree):
    """
    This class allows the user to filter multi-column data sets by specifying
    multiple criteria
    
    Wraps methods from DataFilterParameter: setFields, generateMask,
    filterData, and describe.
    """
    sigFilterChanged: Incomplete
    params: Incomplete
    setFields: Incomplete
    generateMask: Incomplete
    filterData: Incomplete
    describe: Incomplete
    def __init__(self) -> None: ...
    def parameters(self): ...
    def addFilter(self, name):
        """Add a new filter and return the created parameter item.
        """

class DataFilterParameter(ptree.types.GroupParameter):
    """A parameter group that specifies a set of filters to apply to tabular data.
    """
    sigFilterChanged: Incomplete
    fields: Incomplete
    def __init__(self) -> None: ...
    def filterChanged(self) -> None: ...
    def addNew(self, name): ...
    def fieldNames(self): ...
    def setFields(self, fields) -> None:
        """Set the list of fields that are available to be filtered.

        *fields* must be a dict or list of tuples that maps field names
        to a specification describing the field. Each specification is
        itself a dict with either ``'mode':'range'`` or ``'mode':'enum'``::

            filter.setFields([
                ('field1', {'mode': 'range'}),
                ('field2', {'mode': 'enum', 'values': ['val1', 'val2', 'val3']}),
                ('field3', {'mode': 'enum', 'values': {'val1':True, 'val2':False, 'val3':True}}),
            ])
        """
    def filterData(self, data): ...
    def generateMask(self, data):
        """Return a boolean mask indicating whether each item in *data* passes
        the filter critera.
        """
    def describe(self):
        """Return a list of strings describing the currently enabled filters."""

class RangeFilterItem(ptree.types.SimpleParameter):
    fieldName: Incomplete
    units: Incomplete
    def __init__(self, name, opts) -> None: ...
    def generateMask(self, data, mask): ...
    def describe(self): ...
    def updateFilter(self, opts) -> None: ...

class EnumFilterItem(ptree.types.SimpleParameter):
    fieldName: Incomplete
    def __init__(self, name, opts) -> None: ...
    def generateMask(self, data, startMask): ...
    def describe(self): ...
    def updateFilter(self, opts) -> None: ...
    def setEnumVals(self, opts) -> None: ...
