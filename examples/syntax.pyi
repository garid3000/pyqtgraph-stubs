from _typeshed import Incomplete
from pyqtgraph.Qt import QtCore as QtCore, QtGui as QtGui, QtWidgets as QtWidgets

QRegExp: Incomplete
QFont = QtGui.QFont
QColor = QtGui.QColor
QTextCharFormat = QtGui.QTextCharFormat
QSyntaxHighlighter = QtGui.QSyntaxHighlighter

def format(color, style: str = ''):
    """
    Return a QTextCharFormat with the given attributes.
    """

class LightThemeColors:
    Red: str
    Pink: str
    Purple: str
    DeepPurple: str
    Indigo: str
    Blue: str
    LightBlue: str
    Cyan: str
    Teal: str
    Green: str
    LightGreen: str
    Lime: str
    Yellow: str
    Amber: str
    Orange: str
    DeepOrange: str
    Brown: str
    Grey: str
    BlueGrey: str

class DarkThemeColors:
    Red: str
    Pink: str
    Purple: str
    DeepPurple: str
    Indigo: str
    Blue: str
    LightBlue: str
    Cyan: str
    Teal: str
    Green: str
    LightGreen: str
    Lime: str
    Yellow: str
    Amber: str
    Orange: str
    DeepOrange: str
    Brown: str
    Grey: str
    BlueGrey: str

LIGHT_STYLES: Incomplete
DARK_STYLES: Incomplete

class PythonHighlighter(QSyntaxHighlighter):
    """Syntax highlighter for the Python language.
    """
    keywords: Incomplete
    operators: Incomplete
    braces: Incomplete
    tri_single: Incomplete
    tri_double: Incomplete
    rules: Incomplete
    def __init__(self, document) -> None: ...
    @property
    def styles(self): ...
    def highlightBlock(self, text) -> None:
        """Apply syntax highlighting to the given block of text.
        """
    def match_multiline(self, text, delimiter, in_state, style):
        """Do highlighting of multi-line strings. ``delimiter`` should be a
        ``QRegExp`` for triple-single-quotes or triple-double-quotes, and
        ``in_state`` should be a unique integer to represent the corresponding
        state changes when inside those strings. Returns True if we're still
        inside a multi-line string when this function is finished.
        """
