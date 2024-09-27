from ...metaarray import MetaArray as MetaArray
from _typeshed import Incomplete

def downsample(data, n, axis: int = 0, xvals: str = 'subsample'):
    """Downsample by averaging points together across axis.
    If multiple axes are specified, runs once per axis.
    If a metaArray is given, then the axis values can be either subsampled
    or downsampled to match.
    """
def applyFilter(data, b, a, padding: int = 100, bidir: bool = True):
    """Apply a linear filter with coefficients a, b. Optionally pad the data before filtering
    and/or run the filter in both directions."""
def besselFilter(data, cutoff, order: int = 1, dt: Incomplete | None = None, btype: str = 'low', bidir: bool = True):
    """return data passed through bessel filter"""
def butterworthFilter(data, wPass, wStop: Incomplete | None = None, gPass: float = 2.0, gStop: float = 20.0, order: int = 1, dt: Incomplete | None = None, btype: str = 'low', bidir: bool = True):
    """return data passed through bessel filter"""
def rollingSum(data, n): ...
def mode(data, bins: Incomplete | None = None):
    """Returns location max value from histogram."""
def modeFilter(data, window: int = 500, step: Incomplete | None = None, bins: Incomplete | None = None):
    """Filter based on histogram-based mode function"""
def denoise(data, radius: int = 2, threshold: int = 4):
    """Very simple noise removal function. Compares a point to surrounding points,
    replaces with nearby values if the difference is too large."""
def adaptiveDetrend(data, x: Incomplete | None = None, threshold: float = 3.0):
    """Return the signal with baseline removed. Discards outliers from baseline measurement."""
def histogramDetrend(data, window: int = 500, bins: int = 50, threshold: float = 3.0, offsetOnly: bool = False):
    """Linear detrend. Works by finding the most common value at the beginning and end of a trace, excluding outliers.
    If offsetOnly is True, then only the offset from the beginning of the trace is subtracted.
    """
def concatenateColumns(data):
    """Returns a single record array with columns taken from the elements in data. 
    data should be a list of elements, which can be either record arrays or tuples (name, type, data)
    """
def suggestDType(x):
    """Return a suitable dtype for x"""
def removePeriodic(data, f0: float = 60.0, dt: Incomplete | None = None, harmonics: int = 10, samples: int = 4): ...
