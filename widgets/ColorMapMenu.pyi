from ..Qt import QtWidgets
from _typeshed import Incomplete
from typing import NamedTuple

__all__ = ['ColorMapMenu']

class PrivateActionData(NamedTuple):
    name: Incomplete
    source: Incomplete

class ColorMapMenu(QtWidgets.QMenu):
    sigColorMapTriggered: Incomplete
    def __init__(self, *, userList: Incomplete | None = None, showGradientSubMenu: bool = False, showColorMapSubMenus: bool = False) -> None:
        '''
        Creates a new ColorMapMenu.

        Parameters
        ----------
        userList : list of ColorMapSpecifier, optional
            Supported values for ColorMapSpecifier are 
            ``str``, ``(str, str)``, :class:`~pyqtgraph.ColorMap`
            
            Example: ``["viridis", ("glasbey", "colorcet"), ("rainbow", "matplotlib")]``
        showGradientSubMenu : bool, default=False
            Adds legacy gradients in a submenu.
        showColorMapSubMenus : bool, default=False
            Adds bundled colormaps and external (colorcet, matplotlib) colormaps in submenus.
        '''
    def onTriggered(self, action) -> None: ...
    def buildGradientSubMenu(self) -> None: ...
    def buildLocalSubMenu(self) -> None: ...
    def buildCetLocalSubMenu(self) -> None: ...
    def buildCetExternalSubMenu(self) -> None: ...
    def buildMplCategorySubMenu(self) -> None: ...
    def buildMplOthersSubMenu(self) -> None: ...
    def buildColorcetSubMenu(self) -> None: ...
    def buildSubMenu(self, names, source, sort: bool = True) -> None: ...
    @staticmethod
    def actionDataToColorMap(data): ...
