import pyqtgraph.parametertree.parameterTypes as pTypes
from _typeshed import Incomplete
from pyqtgraph.Qt import QtWidgets as QtWidgets
from pyqtgraph.parametertree import Parameter as Parameter, ParameterTree as ParameterTree

app: Incomplete

class ComplexParameter(pTypes.GroupParameter):
    a: Incomplete
    b: Incomplete
    def __init__(self, **opts) -> None: ...
    def aChanged(self) -> None: ...
    def bChanged(self) -> None: ...

class ScalableGroup(pTypes.GroupParameter):
    def __init__(self, **opts) -> None: ...
    def addNew(self, typ) -> None: ...

params: Incomplete
p: Incomplete

def change(param, changes) -> None: ...
def valueChanging(param, value) -> None: ...
def save() -> None: ...
def restore() -> None: ...

t: Incomplete
t2: Incomplete
win: Incomplete
layout: Incomplete
state: Incomplete
compareState: Incomplete
