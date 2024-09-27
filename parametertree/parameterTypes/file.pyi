from ...Qt import QtCore as QtCore, QtGui as QtGui, QtWidgets as QtWidgets
from ..Parameter import Parameter as Parameter
from .str import StrParameterItem as StrParameterItem
from _typeshed import Incomplete

def popupFilePicker(parent: Incomplete | None = None, windowTitle: str = '', nameFilter: str = '', directory: Incomplete | None = None, selectFile: Incomplete | None = None, relativeTo: Incomplete | None = None, **kwargs):
    """
    Thin wrapper around Qt file picker dialog. Used internally so all options are consistent
    among all requests for external file information

    ============== ========================================================
    **Arguments:**
    parent         Dialog parent
    windowTitle    Title of dialog window
    nameFilter     File filter as required by the Qt dialog
    directory      Where in the file system to open this dialog
    selectFile     File to preselect
    relativeTo     Parent directory that, if provided, will be removed from the prefix of all returned paths. So,
                   if '/my/text/file.txt' was selected, and `relativeTo='/my/text/'`, the return value would be
                   'file.txt'. This uses os.path.relpath under the hood, so expect that behavior.
    kwargs         Any enum value accepted by a QFileDialog and its value. Values can be a string or list of strings,
                   i.e. fileMode='AnyFile', options=['ShowDirsOnly', 'DontResolveSymlinks'], acceptMode='AcceptSave'
    ============== ========================================================

    """

class FileParameterItem(StrParameterItem):
    def __init__(self, param, depth) -> None: ...
    def makeWidget(self): ...
    def setValue(self, value) -> None: ...
    def value(self): ...
    def updateDefaultBtn(self) -> None: ...
    def updateDisplayLabel(self, value: Incomplete | None = None): ...

class FileParameter(Parameter):
    """
    Interfaces with the myriad of file options available from a QFileDialog.

    Note that the output can either be a single file string or list of files, depending on whether
    `fileMode='ExistingFiles'` is specified.

    Note that in all cases, absolute file paths are returned unless `relativeTo` is specified as
    elaborated below.

    ============== ========================================================
    **Options:**
    parent         Dialog parent
    winTitle       Title of dialog window
    nameFilter     File filter as required by the Qt dialog
    directory      Where in the file system to open this dialog
    selectFile     File to preselect
    relativeTo     Parent directory that, if provided, will be removed from the prefix of all returned paths. So,
                   if '/my/text/file.txt' was selected, and `relativeTo='my/text/'`, the return value would be
                   'file.txt'. This uses os.path.relpath under the hood, so expect that behavior.
    kwargs         Any enum value accepted by a QFileDialog and its value. Values can be a string or list of strings,
                   i.e. fileMode='AnyFile', options=['ShowDirsOnly', 'DontResolveSymlinks']
    ============== ========================================================
    """
    itemClass = FileParameterItem
    def __init__(self, **opts) -> None: ...
