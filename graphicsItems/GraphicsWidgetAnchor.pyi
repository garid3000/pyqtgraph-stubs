__all__ = ['GraphicsWidgetAnchor']

class GraphicsWidgetAnchor:
    """
    Class used to allow GraphicsWidgets to anchor to a specific position on their
    parent. The item will be automatically repositioned if the parent is resized. 
    This is used, for example, to anchor a LegendItem to a corner of its parent 
    PlotItem.

    """
    def __init__(self) -> None: ...
    def anchor(self, itemPos, parentPos, offset=(0, 0)) -> None:
        """
        Anchors the item at its local itemPos to the item's parent at parentPos.
        Both positions are expressed in values relative to the size of the item or parent;
        a value of 0 indicates left or top edge, while 1 indicates right or bottom edge.
        
        Optionally, offset may be specified to introduce an absolute offset. 
        
        Example: anchor a box such that its upper-right corner is fixed 10px left
        and 10px down from its parent's upper-right corner::
        
            box.anchor(itemPos=(1,0), parentPos=(1,0), offset=(-10,10))
        """
    def autoAnchor(self, pos, relative: bool = True) -> None:
        """
        Set the position of this item relative to its parent by automatically 
        choosing appropriate anchor settings.
        
        If relative is True, one corner of the item will be anchored to 
        the appropriate location on the parent with no offset. The anchored
        corner will be whichever is closest to the parent's boundary.
        
        If relative is False, one corner of the item will be anchored to the same
        corner of the parent, with an absolute offset to achieve the correct
        position. 
        """
