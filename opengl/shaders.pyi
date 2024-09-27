from OpenGL.GL import *
from _typeshed import Incomplete

def initShaders() -> None: ...

CompiledShaderPrograms: Incomplete

def getShaderProgram(name): ...

class Shader:
    shaderType: Incomplete
    code: Incomplete
    compiled: Incomplete
    def __init__(self, shaderType, code) -> None: ...
    def shader(self): ...

class VertexShader(Shader):
    def __init__(self, code) -> None: ...

class FragmentShader(Shader):
    def __init__(self, code) -> None: ...

class ShaderProgram:
    names: Incomplete
    name: Incomplete
    shaders: Incomplete
    prog: Incomplete
    blockData: Incomplete
    uniformData: Incomplete
    def __init__(self, name, shaders, uniforms: Incomplete | None = None) -> None: ...
    def setBlockData(self, blockName, data) -> None: ...
    def setUniformData(self, uniformName, data) -> None: ...
    def __setitem__(self, item, val) -> None: ...
    def __delitem__(self, item) -> None: ...
    def program(self): ...
    def __enter__(self) -> None: ...
    def __exit__(self, *args) -> None: ...
    def uniform(self, name):
        """Return the location integer for a uniform variable in this program"""

class HeightColorShader(ShaderProgram):
    def __enter__(self) -> None: ...
