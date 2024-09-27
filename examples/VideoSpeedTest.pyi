import cupy as cp
import numpy as np
from _typeshed import Incomplete
from pyqtgraph.Qt import QtCore as QtCore, QtGui as QtGui, QtWidgets as QtWidgets
from pyqtgraph.widgets.RawImageWidget import RawImageGLWidget as RawImageGLWidget

parser: Incomplete
args: Incomplete
iterations_counter: Incomplete
sfmt: Incomplete
app: Incomplete
win: Incomplete
ui: Incomplete
levelSpins: Incomplete
xp = cp
xp = np
vb: Incomplete
img: Incomplete
LUT: Incomplete

def updateLUT() -> None: ...
def updateScale() -> None: ...

cache: Incomplete

def mkData() -> None: ...
def updateSize() -> None: ...
def noticeCudaCheck() -> None: ...
def noticeNumbaCheck() -> None: ...

ptr: int

def update() -> None: ...

timer: Incomplete
framecnt: Incomplete
