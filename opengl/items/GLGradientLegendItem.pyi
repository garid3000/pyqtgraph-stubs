from ..GLGraphicsItem import GLGraphicsItem
from _typeshed import Incomplete

__all__ = ['GLGradientLegendItem']

class GLGradientLegendItem(GLGraphicsItem):
    """
    Displays legend colorbar on the screen.
    """
    pos: Incomplete
    size: Incomplete
    fontColor: Incomplete
    gradient: Incomplete
    labels: Incomplete
    def __init__(self, parentItem: Incomplete | None = None, **kwds) -> None:
        '''
        Arguments:
            pos: position of the colorbar on the screen, from the top left corner, in pixels
            size: size of the colorbar without the text, in pixels
            gradient: a pg.ColorMap used to color the colorbar
            labels: a dict of "text":value to display next to the colorbar.
                The value corresponds to a position in the gradient from 0 to 1.
            fontColor: sets the color of the texts. Accepts any single argument accepted by
                :func:`~pyqtgraph.mkColor`
            #Todo:
                size as percentage
                legend title
        '''
    antialias: bool
    def setData(self, **kwds) -> None: ...
    def paint(self) -> None: ...
