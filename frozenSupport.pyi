def listdir(path):
    """Replacement for os.listdir that works in frozen environments."""
def isdir(path):
    """Replacement for os.path.isdir that works in frozen environments."""
def splitZip(path):
    """Splits a path containing a zip file into (zipfile, subpath).
    If there is no zip file, returns (path, None)"""
