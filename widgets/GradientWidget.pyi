from .GraphicsView import GraphicsView
from _typeshed import Incomplete

__all__ = ['GradientWidget']

class GradientWidget(GraphicsView):
    """
    Widget displaying an editable color gradient. The user may add, move, recolor,
    or remove colors from the gradient. Additionally, a context menu allows the 
    user to select from pre-defined gradients.
    """
    sigGradientChanged: Incomplete
    sigGradientChangeFinished: Incomplete
    maxDim: int
    item: Incomplete
    def __init__(self, parent: Incomplete | None = None, orientation: str = 'bottom', *args, **kargs) -> None:
        """
        The *orientation* argument may be 'bottom', 'top', 'left', or 'right' 
        indicating whether the gradient is displayed horizontally (top, bottom)
        or vertically (left, right) and on what side of the gradient the editable 
        ticks will appear.
        
        All other arguments are passed to 
        :func:`GradientEditorItem.__init__ <pyqtgraph.GradientEditorItem.__init__>`.
        
        Note: For convenience, this class wraps methods from 
        :class:`GradientEditorItem <pyqtgraph.GradientEditorItem>`.
        """
    orientation: Incomplete
    def setOrientation(self, ort) -> None:
        """Set the orientation of the widget. May be one of 'bottom', 'top', 
        'left', or 'right'."""
    def setMaxDim(self, mx: Incomplete | None = None) -> None: ...
    def __getattr__(self, attr): ...
    def widgetGroupInterface(self): ...
