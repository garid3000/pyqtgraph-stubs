from collections.abc import Generator

__all__ = ['BusyCursor']

def BusyCursor() -> Generator[None, None, None]:
    """
    Display a busy mouse cursor during long operations.
    Usage::

        with BusyCursor():
            doLongOperation()

    May be nested. If called from a non-gui thread, then the cursor will not be affected.
    """
