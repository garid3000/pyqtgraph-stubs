from .GraphicsObject import GraphicsObject
from _typeshed import Incomplete

__all__ = ['BarGraphItem']

class BarGraphItem(GraphicsObject):
    opts: Incomplete
    picture: Incomplete
    def __init__(self, **opts) -> None:
        """
        Valid keyword options are:
        x, x0, x1, y, y0, y1, width, height, pen, brush
        
        x specifies the x-position of the center of the bar.
        x0, x1 specify left and right edges of the bar, respectively.
        width specifies distance from x0 to x1.
        You may specify any combination:
            
            x, width
            x0, width
            x1, width
            x0, x1
            
        Likewise y, y0, y1, and height. 
        If only height is specified, then y0 will be set to 0
        
        Example uses:
        
            BarGraphItem(x=range(5), height=[1,5,2,4,3], width=0.5)
            
        
        """
    def setOpts(self, **opts) -> None: ...
    def drawPicture(self) -> None: ...
    def paint(self, p, *args) -> None: ...
    def shape(self): ...
    def implements(self, interface: Incomplete | None = None): ...
    def name(self): ...
    def getData(self): ...
    def dataBounds(self, ax, frac: float = 1.0, orthoRange: Incomplete | None = None): ...
    def pixelPadding(self): ...
    def boundingRect(self): ...
