from _typeshed import Incomplete

class SystemSolver:
    '''
    This abstract class is used to formalize and manage user interaction with a 
    complex system of equations (related to "constraint satisfaction problems").
    It is often the case that devices must be controlled
    through a large number of free variables, and interactions between these 
    variables make the system difficult to manage and conceptualize as a user
    interface. This class does _not_ attempt to numerically solve the system
    of equations. Rather, it provides a framework for subdividing the system
    into manageable pieces and specifying closed-form solutions to these small 
    pieces.
    
    For an example, see the simple Camera class below.
    
    Theory of operation: Conceptualize the system as 1) a set of variables
    whose values may be either user-specified or automatically generated, and 
    2) a set of functions that define *how* each variable should be generated. 
    When a variable is accessed (as an instance attribute), the solver first
    checks to see if it already has a value (either user-supplied, or cached
    from a previous calculation). If it does not, then the solver calls a 
    method on itself (the method must be named `_variableName`) that will
    either return the calculated value (which usually involves acccessing
    other variables in the system), or raise RuntimeError if it is unable to
    calculate the value (usually because the user has not provided sufficient
    input to fully constrain the system). 
    
    Each method that calculates a variable value may include multiple 
    try/except blocks, so that if one method generates a RuntimeError, it may 
    fall back on others. 
    In this way, the system may be solved by recursively searching the tree of 
    possible relationships between variables. This allows the user flexibility
    in deciding which variables are the most important to specify, while 
    avoiding the apparent combinatorial explosion of calculation pathways
    that must be considered by the developer.
    
    Solved values are cached for efficiency, and automatically cleared when 
    a state change invalidates the cache. The rules for this are simple: any
    time a value is set, it invalidates the cache *unless* the previous value
    was None (which indicates that no other variable has yet requested that 
    value). More complex cache management may be defined in subclasses.
    
    
    Subclasses must define:
    
    1) The *defaultState* class attribute: This is a dict containing a 
       description of the variables in the system--their default values,
       data types, and the ways they can be constrained. The format is::

           { name: [value, type, constraint, allowed_constraints], ...}

       Where:
         * *value* is the default value. May be None if it has not been specified
           yet.
         * *type* may be float, int, bool, np.ndarray, ...
         * *constraint* may be None, single value, or (min, max)
              * None indicates that the value is not constrained--it may be
                automatically generated if the value is requested.
         * *allowed_constraints* is a string composed of (n)one, (f)ixed, and (r)ange.
       
       Note: do not put mutable objects inside defaultState!
       
    2) For each variable that may be automatically determined, a method must 
       be defined with the name `_variableName`. This method may either return
       the 
    '''
    defaultState: Incomplete
    def __init__(self) -> None: ...
    def copy(self): ...
    def reset(self) -> None:
        """
        Reset all variables in the solver to their default state.
        """
    def __getattr__(self, name): ...
    def __setattr__(self, name, value) -> None:
        """
        Set the value of a state variable. 
        If None is given for the value, then the constraint will also be set to None.
        If a tuple is given for a scalar variable, then the tuple is used as a range constraint instead of a value.
        Otherwise, the constraint is set to 'fixed'.
        
        """
    def get(self, name):
        """
        Return the value for parameter *name*. 
        
        If the value has not been specified, then attempt to compute it from
        other interacting parameters.
        
        If no value can be determined, then raise RuntimeError.
        """
    def set(self, name, value: Incomplete | None = None, constraint: bool = True):
        """
        Set a variable *name* to *value*. The actual set value is returned (in
        some cases, the value may be cast into another type).
        
        If *value* is None, then the value is left to be determined in the 
        future. At any time, the value may be re-assigned arbitrarily unless
        a constraint is given.
        
        If *constraint* is True (the default), then supplying a value that 
        violates a previously specified constraint will raise an exception.
        
        If *constraint* is 'fixed', then the value is set (if provided) and
        the variable will not be updated automatically in the future.

        If *constraint* is a tuple, then the value is constrained to be within the 
        given (min, max). Either constraint may be None to disable 
        it. In some cases, a constraint cannot be satisfied automatically,
        and the user will be forced to resolve the constraint manually.
        
        If *constraint* is None, then any constraints are removed for the variable.
        """
    def check_constraint(self, name, value): ...
    def saveState(self):
        """
        Return a serializable description of the solver's current state.
        """
    def restoreState(self, state) -> None:
        """
        Restore the state of all values and constraints in the solver.
        """
    def resetUnfixed(self) -> None:
        """
        For any variable that does not have a fixed value, reset
        its value to None.
        """
    def solve(self) -> None: ...
    def checkOverconstraint(self):
        """Check whether the system is overconstrained. If so, return the name of
        the first overconstrained parameter.

        Overconstraints occur when any fixed parameter can be successfully computed by the system.
        (Ideally, all parameters are either fixed by the user or constrained by the
        system, but never both).
        """
