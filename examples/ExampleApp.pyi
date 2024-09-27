from _typeshed import Incomplete
from pyqtgraph.Qt import QT_LIB as QT_LIB, QtCore as QtCore, QtGui as QtGui, QtWidgets as QtWidgets

app: Incomplete
path: Incomplete
QRegularExpression = QtCore.QRegularExpression
QFont = QtGui.QFont
QColor = QtGui.QColor
QTextCharFormat = QtGui.QTextCharFormat
QSyntaxHighlighter = QtGui.QSyntaxHighlighter

def charFormat(color, style: str = '', background: Incomplete | None = None):
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
    searchText: Incomplete
    def __init__(self, document) -> None: ...
    @property
    def styles(self): ...
    def highlightBlock(self, text) -> None:
        """Apply syntax highlighting to the given block of text.
        """
    def match_multiline(self, text, delimiter, in_state, style):
        """Do highlighting of multi-line strings. 
        
        =========== ==========================================================
        delimiter   (QRegularExpression) for triple-single-quotes or 
                    triple-double-quotes
        in_state    (int) to represent the corresponding state changes when 
                    inside those strings. Returns True if we're still inside a
                    multi-line string when this function is finished.
        style       (str) representation of the kind of style to use
        =========== ==========================================================
        """
    def applySearchHighlight(self, text) -> None: ...

def unnestedDict(exDict):
    """Converts a dict-of-dicts to a singly nested dict for non-recursive parsing"""

class ExampleLoader(QtWidgets.QMainWindow):
    bindings: Incomplete
    modules: Incomplete
    ui: Incomplete
    cw: Incomplete
    codeBtn: Incomplete
    codeLayout: Incomplete
    hl: Incomplete
    curListener: Incomplete
    itemCache: Incomplete
    oldText: Incomplete
    def __init__(self) -> None: ...
    def event(self, event: QtCore.QEvent | None): ...
    def updateCodeViewTabWidth(self, font) -> None:
        """
        Change the codeView tabStopDistance to 4 spaces based on the size of the current font
        """
    def showEvent(self, event) -> None: ...
    def onTextChange(self) -> None:
        '''
        textChanged fires when the highlighter is reassigned the same document.
        Prevent this from showing "run edited code" by checking for actual
        content change
        '''
    def filterByTitle(self, text) -> None: ...
    def filterByContent(self, text: Incomplete | None = None) -> None: ...
    def getMatchingTitles(self, text, exDict: Incomplete | None = None, acceptAll: bool = False): ...
    def showExamplesByTitle(self, titles) -> None: ...
    def simulate_black_mode(self) -> None:
        '''
        used to simulate MacOS "black mode" on other platforms
        intended for debug only, as it manage only the QPlainTextEdit
        '''
    def populateTree(self, root, examples) -> None: ...
    def currentFile(self): ...
    def loadFile(self, *, edited: bool = False) -> None: ...
    def showFile(self) -> None: ...
    def getExampleContent(self, filename): ...
    def codeEdited(self) -> None: ...
    def runEditedCode(self) -> None: ...
    def keyPressEvent(self, event) -> None: ...

def main() -> None: ...
