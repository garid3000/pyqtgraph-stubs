from ..GraphicsScene import GraphicsScene as GraphicsScene
from ..Qt import QtCore as QtCore, QtWidgets as QtWidgets
from ..widgets.FileDialog import FileDialog as FileDialog
from _typeshed import Incomplete

LastExportDirectory: Incomplete

class Exporter:
    """
    Abstract class used for exporting graphics to file / printer / whatever.
    """
    allowCopy: bool
    Exporters: Incomplete
    @classmethod
    def register(cls) -> None:
        """
        Used to register Exporter classes to appear in the export dialog.
        """
    item: Incomplete
    def __init__(self, item) -> None:
        """
        Initialize with the item to be exported.
        Can be an individual graphics item or a scene.
        """
    def parameters(self) -> None:
        """Return the parameters used to configure this exporter."""
    def export(self, fileName: Incomplete | None = None, toBytes: bool = False, copy: bool = False) -> None:
        """
        If *fileName* is None, pop-up a file dialog.
        If *toBytes* is True, return a bytes object rather than writing to file.
        If *copy* is True, export to the copy buffer rather than writing to file.
        """
    fileDialog: Incomplete
    def fileSaveDialog(self, filter: Incomplete | None = None, opts: Incomplete | None = None) -> None: ...
    def fileSaveFinished(self, fileName) -> None: ...
    def getScene(self): ...
    def getSourceRect(self): ...
    def getTargetRect(self): ...
    def setExportMode(self, export, opts: Incomplete | None = None) -> None:
        """
        Call setExportMode(export, opts) on all items that will 
        be painted during the export. This informs the item
        that it is about to be painted for export, allowing it to 
        alter its appearance temporarily
        
        
        *export*  - bool; must be True before exporting and False afterward
        *opts*    - dict; common parameters are 'antialias' and 'background'
        """
    def getPaintItems(self, root: Incomplete | None = None):
        """Return a list of all items that should be painted in the correct order."""
    def render(self, painter, targetRect, sourceRect, item: Incomplete | None = None) -> None: ...
