from _typeshed import Incomplete
from pyqtgraph.Qt import QtWidgets as QtWidgets
from pyqtgraph.dockarea.Dock import Dock as Dock
from pyqtgraph.dockarea.DockArea import DockArea as DockArea
from qtconsole import inprocess

class JupyterConsoleWidget(inprocess.QtInProcessRichJupyterWidget):
    kernel_manager: Incomplete
    kernel_client: Incomplete
    def __init__(self) -> None: ...
    def shutdown_kernel(self) -> None: ...

class MainWindow(QtWidgets.QMainWindow):
    plot_widget: Incomplete
    jupyter_console_widget: Incomplete
    def __init__(self, dark_mode: bool = True) -> None: ...
