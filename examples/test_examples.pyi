from . import utils as utils
from _typeshed import Incomplete
from pyqtgraph import Qt as Qt
from typing import NamedTuple

parent_dir: Incomplete

def buildFileList(examples, files: Incomplete | None = None): ...

path: Incomplete
files: Incomplete
frontends: Incomplete
installedFrontends: Incomplete
darwin_opengl_broken: Incomplete
darwin_opengl_reason: str

class exceptionCondition(NamedTuple):
    condition: Incomplete
    reason: Incomplete

conditionalExamples: Incomplete
openglExamples: Incomplete

def testExamples(frontend, f) -> None: ...
