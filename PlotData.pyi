from _typeshed import Incomplete

class PlotData:
    """
    Class used for managing plot data
      - allows data sharing between multiple graphics items (curve, scatter, graph..)
      - each item may define the columns it needs
      - column groupings ('pos' or x, y, z)
      - efficiently appendable 
      - log, fft transformations
      - color mode conversion (float/byte/qcolor)
      - pen/brush conversion
      - per-field cached masking
        - allows multiple masking fields (different graphics need to mask on different criteria) 
        - removal of nan/inf values
      - option for single value shared by entire column
      - cached downsampling
      - cached min / max / hasnan / isuniform
    """
    fields: Incomplete
    maxVals: Incomplete
    minVals: Incomplete
    def __init__(self) -> None: ...
    def addFields(self, **fields) -> None: ...
    def hasField(self, f): ...
    def __getitem__(self, field): ...
    def __setitem__(self, field, val) -> None: ...
    def max(self, field): ...
    def min(self, field): ...
