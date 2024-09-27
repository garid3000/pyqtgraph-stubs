from ..Qt import QtWidgets
from _typeshed import Incomplete

__all__ = ['FeedbackButton']

class FeedbackButton(QtWidgets.QPushButton):
    """
    QPushButton which flashes success/failure indication for slow or asynchronous procedures.
    """
    sigCallSuccess: Incomplete
    sigCallFailure: Incomplete
    sigCallProcess: Incomplete
    sigReset: Incomplete
    origStyle: Incomplete
    origText: Incomplete
    origTip: Incomplete
    limitedTime: bool
    def __init__(self, *args) -> None: ...
    def feedback(self, success, message: Incomplete | None = None, tip: str = '', limitedTime: bool = True) -> None:
        """Calls success() or failure(). If you want the message to be displayed until the user takes an action, set limitedTime to False. Then call self.reset() after the desired action.Threadsafe."""
    def success(self, message: Incomplete | None = None, tip: str = '', limitedTime: bool = True) -> None:
        """Displays specified message on button and flashes button green to let user know action was successful. If you want the success to be displayed until the user takes an action, set limitedTime to False. Then call self.reset() after the desired action. Threadsafe."""
    def failure(self, message: Incomplete | None = None, tip: str = '', limitedTime: bool = True) -> None:
        """Displays specified message on button and flashes button red to let user know there was an error. If you want the error to be displayed until the user takes an action, set limitedTime to False. Then call self.reset() after the desired action. Threadsafe. """
    def processing(self, message: str = 'Processing..', tip: str = '', processEvents: bool = True) -> None:
        """Displays specified message on button to let user know the action is in progress. Threadsafe. """
    def reset(self) -> None:
        """Resets the button to its original text and style. Threadsafe."""
    count: int
    indStyle: Incomplete
    def startBlink(self, color, message: Incomplete | None = None, tip: str = '', limitedTime: bool = True) -> None: ...
    def borderOn(self) -> None: ...
    def borderOff(self) -> None: ...
    def setText(self, text: Incomplete | None = None, temporary: bool = False) -> None: ...
    def setToolTip(self, text: Incomplete | None = None, temporary: bool = False) -> None: ...
    def setStyleSheet(self, style: Incomplete | None = None, temporary: bool = False) -> None: ...
