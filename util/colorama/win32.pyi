from _typeshed import Incomplete
from ctypes import Structure, c_short as c_short, c_uint32 as c_uint32, c_ushort as c_ushort

STDOUT: int
STDERR: int
SetConsoleTextAttribute: Incomplete

class CONSOLE_SCREEN_BUFFER_INFO(Structure):
    """struct in wincon.h."""

handles: Incomplete

def GetConsoleScreenBufferInfo(stream_id=...): ...
def SetConsoleCursorPosition(stream_id, position): ...
def FillConsoleOutputCharacter(stream_id, char, length, start): ...
def FillConsoleOutputAttribute(stream_id, attr, length, start):
    """ FillConsoleOutputAttribute( hConsole, csbi.wAttributes, dwConSize, coordScreen, &cCharsWritten )"""
