from ..Qt import QtCore as QtCore, QtGui as QtGui, QtWidgets as QtWidgets
from ..widgets.GraphicsView import GraphicsView as GraphicsView
from ..widgets.HistogramLUTWidget import HistogramLUTWidget as HistogramLUTWidget
from ..widgets.PlotWidget import PlotWidget as PlotWidget
from _typeshed import Incomplete

class Ui_Form:
    gridLayout_3: Incomplete
    splitter: Incomplete
    layoutWidget: Incomplete
    gridLayout: Incomplete
    graphicsView: Incomplete
    histogram: HistogramLUTWidget
    roiBtn: QtWidgets.QPushButton
    menuBtn: QtWidgets.QPushButton
    roiPlot: Incomplete
    normGroup: Incomplete
    gridLayout_2: Incomplete
    normSubtractRadio: Incomplete
    normDivideRadio: Incomplete
    label_5: Incomplete
    label_3: Incomplete
    label_4: Incomplete
    normROICheck: Incomplete
    normXBlurSpin: Incomplete
    label_8: Incomplete
    label_9: Incomplete
    normYBlurSpin: Incomplete
    label_10: Incomplete
    normOffRadio: Incomplete
    normTimeRangeCheck: Incomplete
    normFrameCheck: Incomplete
    normTBlurSpin: Incomplete
    def setupUi(self, Form) -> None: ...
    def retranslateUi(self, Form) -> None: ...
