from .Exporter import Exporter
from _typeshed import Incomplete

__all__ = ['PrintExporter']

class PrintExporter(Exporter):
    Name: str
    params: Incomplete
    def __init__(self, item) -> None: ...
    def widthChanged(self) -> None: ...
    def heightChanged(self) -> None: ...
    def parameters(self): ...
    def export(self, fileName: Incomplete | None = None) -> None: ...
