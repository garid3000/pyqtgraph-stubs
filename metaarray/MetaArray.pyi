from _typeshed import Incomplete

USE_HDF5: bool
HAVE_HDF5: bool

def axis(name: Incomplete | None = None, cols: Incomplete | None = None, values: Incomplete | None = None, units: Incomplete | None = None):
    """Convenience function for generating axis descriptions when defining MetaArrays"""

class sliceGenerator:
    """Just a compact way to generate tuples of slice objects."""
    def __getitem__(self, arg): ...
    def __getslice__(self, arg): ...

SLICER: Incomplete

class MetaArray:
    """N-dimensional array with meta data such as axis titles, units, and column names.
  
    May be initialized with a file name, a tuple representing the dimensions of the array,
    or any arguments that could be passed on to numpy.array()
  
    The info argument sets the metadata for the entire array. It is composed of a list
    of axis descriptions where each axis may have a name, title, units, and a list of column 
    descriptions. An additional dict at the end of the axis list may specify parameters
    that apply to values in the entire array.
  
    For example:
        A 2D array of altitude values for a topographical map might look like
            info=[
        {'name': 'lat', 'title': 'Lattitude'}, 
        {'name': 'lon', 'title': 'Longitude'}, 
        {'title': 'Altitude', 'units': 'm'}
      ]
        In this case, every value in the array represents the altitude in feet at the lat, lon
        position represented by the array index. All of the following return the 
        value at lat=10, lon=5:
            array[10, 5]
            array['lon':5, 'lat':10]
            array['lat':10][5]
        Now suppose we want to combine this data with another array of equal dimensions that
        represents the average rainfall for each location. We could easily store these as two 
        separate arrays or combine them into a 3D array with this description:
            info=[
        {'name': 'vals', 'cols': [
          {'name': 'altitude', 'units': 'm'}, 
          {'name': 'rainfall', 'units': 'cm/year'}
        ]},
        {'name': 'lat', 'title': 'Lattitude'}, 
        {'name': 'lon', 'title': 'Longitude'}
      ]
        We can now access the altitude values with array[0] or array['altitude'], and the
        rainfall values with array[1] or array['rainfall']. All of the following return
        the rainfall value at lat=10, lon=5:
            array[1, 10, 5]
            array['lon':5, 'lat':10, 'val': 'rainfall']
            array['rainfall', 'lon':5, 'lat':10]
        Notice that in the second example, there is no need for an extra (4th) axis description
        since the actual values are described (name and units) in the column info for the first axis.
    """
    version: str
    defaultCompression: Incomplete
    nameTypes: Incomplete
    @staticmethod
    def isNameType(var): ...
    wrapMethods: Incomplete
    def __init__(self, data: Incomplete | None = None, info: Incomplete | None = None, dtype: Incomplete | None = None, file: Incomplete | None = None, copy: bool = False, **kwargs) -> None: ...
    def checkInfo(self) -> None: ...
    def implements(self, name: Incomplete | None = None): ...
    def __getitem__(self, ind): ...
    @property
    def ndim(self): ...
    @property
    def shape(self): ...
    @property
    def dtype(self): ...
    def __len__(self) -> int: ...
    def __getslice__(self, *args): ...
    def __setitem__(self, ind, val) -> None: ...
    def __getattr__(self, attr): ...
    def __eq__(self, b): ...
    def __ne__(self, b): ...
    def __sub__(self, b): ...
    def __add__(self, b): ...
    def __mul__(self, b): ...
    def __div__(self, b): ...
    def __truediv__(self, b): ...
    def asarray(self): ...
    def __array__(self, dtype: Incomplete | None = None): ...
    def axisValues(self, axis):
        """Return the list of values for an axis"""
    def xvals(self, axis):
        """Synonym for axisValues()"""
    def axisHasValues(self, axis): ...
    def axisHasColumns(self, axis): ...
    def axisUnits(self, axis):
        """Return the units for axis"""
    def hasColumn(self, axis, col): ...
    def listColumns(self, axis: Incomplete | None = None):
        """Return a list of column names for axis. If axis is not specified, then return a dict of {axisName: (column names), ...}."""
    def columnName(self, axis, col): ...
    def axisName(self, n): ...
    def columnUnits(self, axis, column):
        """Return the units for column in axis"""
    def rowsort(self, axis, key: int = 0):
        """Return this object with all records sorted along axis using key as the index to the values to compare. Does not yet modify meta info."""
    def append(self, val, axis):
        """Return this object with val appended along axis. Does not yet combine meta info."""
    def extend(self, val, axis):
        """Return the concatenation along axis of this object and val. Does not yet combine meta info."""
    def infoCopy(self, axis: Incomplete | None = None):
        """Return a deep copy of the axis meta info for this object"""
    def copy(self): ...
    def prettyInfo(self): ...
    def axisCollapsingFn(self, fn, axis: Incomplete | None = None, *args, **kargs): ...
    def mean(self, axis: Incomplete | None = None, *args, **kargs): ...
    def min(self, axis: Incomplete | None = None, *args, **kargs): ...
    def max(self, axis: Incomplete | None = None, *args, **kargs): ...
    def transpose(self, *args): ...
    def readFile(self, filename, **kwargs) -> None:
        """Load the data and meta info stored in *filename*
        Different arguments are allowed depending on the type of file.
        For HDF5 files:
        
            *writable* (bool) if True, then any modifications to data in the array will be stored to disk.
            *readAllData* (bool) if True, then all data in the array is immediately read from disk
                          and the file is closed (this is the default for files < 500MB). Otherwise, the file will
                          be left open and data will be read only as requested (this is 
                          the default for files >= 500MB).
        
        
        """
    @staticmethod
    def mapHDF5Array(data, writable: bool = False): ...
    @staticmethod
    def readHDF5Meta(root, mmap: bool = False): ...
    def write(self, fileName, **opts):
        '''Write this object to a file. The object can be restored by calling MetaArray(file=fileName)
        opts:
            appendAxis: the name (or index) of the appendable axis. Allows the array to grow.
            appendKeys: a list of keys (other than "values") for metadata to append to on the appendable axis.
            compression: None, \'gzip\' (good compression), \'lzf\' (fast compression), etc.
            chunks: bool or tuple specifying chunk shape
        '''
    def writeMeta(self, fileName) -> None:
        """Used to re-write meta info to the given file.
        This feature is only available for HDF5 files."""
    def writeHDF5(self, fileName, **opts) -> None: ...
    def writeHDF5Meta(self, root, name, data, **dsOpts) -> None: ...
    def writeMa(self, fileName, appendAxis: Incomplete | None = None, newFile: bool = False) -> None:
        """Write an old-style .ma file"""
    def writeCsv(self, fileName: Incomplete | None = None):
        """Write 2D array to CSV file or return the string if no filename is given"""
