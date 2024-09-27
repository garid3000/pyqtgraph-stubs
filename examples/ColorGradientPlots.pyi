import pyqtgraph as pg
from _typeshed import Incomplete
from pyqtgraph.Qt import QtCore as QtCore, mkQApp as mkQApp

class DataSource:
    """ source of buffered demonstration data """
    rate: Incomplete
    period: Incomplete
    neg_period: Incomplete
    start_time: float
    sample_idx: int
    def __init__(self, sample_rate: float = 200.0, signal_period: float = 0.55, negative_period: Incomplete | None = None, max_length: int = 300) -> None:
        """ prepare, but don't start yet """
    def start(self, timestamp) -> None:
        """ start acquiring simulated data """
    def get_data(self, timestamp, max_length: int = 6000):
        """ return all data acquired since last get_data call """

class MainWindow(pg.GraphicsLayoutWidget):
    """ example application main window """
    top_plot: Incomplete
    traces: Incomplete
    timer: Incomplete
    last_update: Incomplete
    mean_dt: Incomplete
    def __init__(self) -> None: ...
    def update(self) -> None:
        """ called by timer at 30 Hz """

main_window: Incomplete
