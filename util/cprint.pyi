from .colorama.win32 import windll as windll
from .colorama.winterm import WinColor as WinColor, WinStyle as WinStyle, WinTerm as WinTerm
from _typeshed import Incomplete

winterm: Incomplete

def winset(reset: bool = False, fore: Incomplete | None = None, back: Incomplete | None = None, style: Incomplete | None = None, stderr: bool = False) -> None: ...

ANSI: Incomplete
WIN: Incomplete
color: Incomplete
RESET: int

def cprint(stream, *args, **kwds) -> None:
    """
    Print with color. Examples::

        # colors are BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE
        cprint('stdout', RED, 'This is in red. ', RESET, 'and this is normal
')

        # Adding BR_ before the color manes it bright
        cprint('stdout', BR_GREEN, 'This is bright green.
', RESET)

        # Adding BACK_ changes background color
        cprint('stderr', BACK_BLUE, WHITE, 'This is white-on-blue.', -1)

        # Integers 0-7 for normal, 8-15 for bright, and 40-47 for background.
        # -1 to reset.
        cprint('stderr', 1, 'This is in red.', -1)

    """
def cout(*args) -> None:
    """Shorthand for cprint('stdout', ...)"""
def cerr(*args) -> None:
    """Shorthand for cprint('stderr', ...)"""
