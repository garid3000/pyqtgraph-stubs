__all__ = ['getGraphIcon', 'getGraphPixmap']

class GraphIcon:
    '''An icon place holder for lazy loading of QIcons

    The icon must reside in the icons folder and the path refers to the full
    name including suffix of the icon file, e.g.:

        tiny = GraphIcon("tiny.png")

    Icons can be later retrieved via the function `getGraphIcon` and providing
    the name:

        tiny = getGraphIcon("tiny")
    '''
    def __init__(self, path) -> None: ...
    @property
    def qicon(self): ...

def getGraphIcon(name):
    """Return a `PyQtGraph` icon from the registry by `name`"""
def getGraphPixmap(name, size=(20, 20)):
    """Return a `QPixmap` from the registry by `name`"""
