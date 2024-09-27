from ..Qt import QtCore as QtCore, QtGui as QtGui, QtWidgets as QtWidgets
from ..functions import mkPen as mkPen
from _typeshed import Incomplete

class PenPreviewLabel(QtWidgets.QLabel):
    param: Incomplete
    pen: Incomplete
    def __init__(self, param) -> None: ...
    def onPenChanging(self, param, val) -> None: ...
    def paintEvent(self, ev) -> None: ...
