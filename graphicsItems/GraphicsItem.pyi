from _typeshed import Incomplete
from collections import OrderedDict
from xml.etree.ElementTree import Element

__all__ = ['GraphicsItem']

class LRU(OrderedDict):
    """Limit size, evicting the least recently looked-up key when full"""
    maxsize: Incomplete
    def __init__(self, maxsize: int = 128, *args, **kwds) -> None: ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value) -> None: ...

class GraphicsItem:
    """
    **Bases:** :class:`object`

    Abstract class providing useful methods to GraphicsObject and GraphicsWidget.
    (This is required because we cannot have multiple inheritance with QObject subclasses.)

    A note about Qt's GraphicsView framework:

    The GraphicsView system places a lot of emphasis on the notion that the graphics within the scene should be device independent--you should be able to take the same graphics and display them on screens of different resolutions, printers, export to SVG, etc. This is nice in principle, but causes me a lot of headache in practice. It means that I have to circumvent all the device-independent expectations any time I want to operate in pixel coordinates rather than arbitrary scene coordinates. A lot of the code in GraphicsItem is devoted to this task--keeping track of view widgets and device transforms, computing the size and shape of a pixel in local item coordinates, etc. Note that in item coordinates, a pixel does not have to be square or even rectangular, so just asking how to increase a bounding rect by 2px can be a rather complex task.
    """
    def __init__(self) -> None: ...
    def getViewWidget(self):
        """
        Return the view widget for this item. 
        
        If the scene has multiple views, only the first view is returned.
        The return value is cached; clear the cached value with forgetViewWidget().
        If the view has been deleted by Qt, return None.
        """
    def forgetViewWidget(self) -> None: ...
    def getViewBox(self):
        """
        Return the first ViewBox or GraphicsView which bounds this item's visible space.
        If this item is not contained within a ViewBox, then the GraphicsView is returned.
        If the item is contained inside nested ViewBoxes, then the inner-most ViewBox is returned.
        The result is cached; clear the cache with forgetViewBox()
        """
    def forgetViewBox(self) -> None: ...
    def deviceTransform(self, viewportTransform: Incomplete | None = None):
        """
        Return the transform that converts local item coordinates to device coordinates (usually pixels).
        Extends deviceTransform to automatically determine the viewportTransform.
        """
    def viewTransform(self):
        """Return the transform that maps from local coordinates to the item's ViewBox coordinates
        If there is no ViewBox, return the scene transform.
        Returns None if the item does not have a view."""
    def getBoundingParents(self):
        """Return a list of parents to this item that have child clipping enabled."""
    def viewRect(self):
        """Return the visible bounds of this item's ViewBox or GraphicsWidget,
        in the local coordinate system of the item."""
    def pixelVectors(self, direction: Incomplete | None = None):
        """Return vectors in local coordinates representing the width and height of a view pixel.
        If direction is specified, then return vectors parallel and orthogonal to it.
        
        Return (None, None) if pixel size is not yet defined (usually because the item has not yet been displayed)
        or if pixel size is below floating-point precision limit.
        """
    def pixelLength(self, direction, ortho: bool = False):
        """Return the length of one pixel in the direction indicated (in local coordinates)
        If ortho=True, then return the length of one pixel orthogonal to the direction indicated.
        
        Return None if pixel size is not yet defined (usually because the item has not yet been displayed).
        """
    def pixelSize(self): ...
    def pixelWidth(self): ...
    def pixelHeight(self): ...
    def mapToDevice(self, obj):
        """
        Return *obj* mapped from local coordinates to device coordinates (pixels).
        If there is no device mapping available, return None.
        """
    def mapFromDevice(self, obj):
        """
        Return *obj* mapped from device coordinates (pixels) to local coordinates.
        If there is no device mapping available, return None.
        """
    def mapRectToDevice(self, rect):
        """
        Return *rect* mapped from local coordinates to device coordinates (pixels).
        If there is no device mapping available, return None.
        """
    def mapRectFromDevice(self, rect):
        """
        Return *rect* mapped from device coordinates (pixels) to local coordinates.
        If there is no device mapping available, return None.
        """
    def mapToView(self, obj): ...
    def mapRectToView(self, obj): ...
    def mapFromView(self, obj): ...
    def mapRectFromView(self, obj): ...
    def pos(self): ...
    def viewPos(self): ...
    def parentItem(self): ...
    def setParentItem(self, parent): ...
    def childItems(self): ...
    def sceneTransform(self): ...
    def transformAngle(self, relativeItem: Incomplete | None = None):
        """Return the rotation produced by this item's transform (this assumes there is no shear in the transform)
        If relativeItem is given, then the angle is determined relative to that item.
        """
    def changeParent(self) -> None:
        """Called when the item's parent has changed. 
        This method handles connecting / disconnecting from ViewBox signals
        to make sure viewRangeChanged works properly. It should generally be 
        extended, not overridden."""
    def parentChanged(self) -> None: ...
    def viewChanged(self, view, oldView) -> None:
        """Called when this item's view has changed
        (ie, the item has been added to or removed from a ViewBox)"""
    def viewRangeChanged(self) -> None:
        """
        Called whenever the view coordinates of the ViewBox containing this item have changed.
        """
    def viewTransformChanged(self) -> None:
        """
        Called whenever the transformation matrix of the view has changed.
        (eg, the view range has changed or the view was resized)
        Invalidates the viewRect cache.
        """
    def informViewBoundsChanged(self) -> None:
        """
        Inform this item's container ViewBox that the bounds of this item have changed.
        This is used by ViewBox to react if auto-range is enabled.
        """
    def childrenShape(self):
        """Return the union of the shapes of all descendants of this item in local coordinates."""
    def allChildItems(self, root: Incomplete | None = None):
        """Return list of the entire item tree descending from this item."""
    def setExportMode(self, export, opts: Incomplete | None = None) -> None:
        """
        This method is called by exporters to inform items that they are being drawn for export
        with a specific set of options. Items access these via self._exportOptions.
        When exporting is complete, _exportOptions is set to False.
        """
    def getContextMenus(self, event): ...
    def generateSvg(self, nodes: dict[str, Element]) -> tuple[Element, list[Element]] | None:
        """Method to override to manually specify the SVG writer mechanism.

        Parameters
        ----------
        nodes
            Dictionary keyed by the name of graphics items and the XML
            representation of the the item that can be written as valid
            SVG.
        
        Returns
        -------
        tuple
            First element is the top level group for this item. The
            second element is a list of xml Elements corresponding to the
            child nodes of the item.
        None
            Return None if no XML is needed for rendering

        Raises
        ------
        NotImplementedError
            override method to implement in subclasses of GraphicsItem

        See Also
        --------
        pyqtgraph.exporters.SVGExporter._generateItemSvg
            The generic and default implementation

        """
