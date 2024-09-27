from _typeshed import Incomplete

SI_PREFIXES: Incomplete
UNITS: Incomplete
allUnits: Incomplete

def addUnit(prefix, val) -> None: ...

v: Incomplete
pre: str

def evalUnits(unitStr) -> None:
    """
    Evaluate a unit string into ([numerators,...], [denominators,...])
    Examples:
        N m/s^2   =>  ([N, m], [s, s])
        A*s / V   =>  ([A, s], [V,])
    """
def formatUnits(units) -> None:
    """
    Format a unit specification ([numerators,...], [denominators,...])
    into a string (this is the inverse of evalUnits)
    """
def simplify(units) -> None:
    """
    Cancel units that appear in both numerator and denominator, then attempt to replace 
    groups of units with single units where possible (ie, J/s => W)
    """
