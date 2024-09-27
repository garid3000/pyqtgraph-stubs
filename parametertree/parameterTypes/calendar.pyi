from ...Qt import QtCore as QtCore, QtWidgets as QtWidgets
from ..Parameter import Parameter as Parameter
from .basetypes import WidgetParameterItem as WidgetParameterItem
from _typeshed import Incomplete

class CalendarParameterItem(WidgetParameterItem):
    asSubItem: bool
    hideWidget: bool
    def makeWidget(self): ...

class CalendarParameter(Parameter):
    """
    Displays a Qt calendar whose date is specified by a 'format' option.

    ============== ========================================================
    **Options:**
    format         Format for displaying the date and converting from a string. Can be any value accepted by
                   `QDate.toString` and `fromString`, or a stringified version of a QDateFormat enum, i.e. 'ISODate',
                   'TextDate' (default), etc.
    ============== ========================================================
    """
    itemClass = CalendarParameterItem
    def __init__(self, **opts) -> None: ...
    def saveState(self, filter: Incomplete | None = None): ...
