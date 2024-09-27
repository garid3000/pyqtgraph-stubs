from . import Parameter as Parameter
from .parameterTypes import ActionGroupParameter as ActionGroupParameter
from _typeshed import Incomplete
from collections.abc import Generator

class PARAM_UNSET:
    """Sentinel value for detecting parameters with unset values"""

class RunOptions:
    ON_ACTION: str
    ON_CHANGED: str
    ON_CHANGING: str

class InteractiveFunction:
    """
    ``interact`` can be used with regular functions. However, when they are connected to
    changed or changing signals, there is no way to access these connections later to
    i.e. disconnect them temporarily. This utility class wraps a normal function but
    can provide an external scope for accessing the hooked up parameter signals.
    """
    __qualname__: str
    parameters: Incomplete
    extra: Incomplete
    function: Incomplete
    closures: Incomplete
    parametersNeedRunKwargs: bool
    parameterCache: Incomplete
    def __init__(self, function, *, closures: Incomplete | None = None, **extra) -> None:
        """
        Wraps a callable function in a way that forwards Parameter arguments as keywords

        Parameters
        ----------
        function: callable
            Function to wrap
        closures: dict[str, callable]
            Arguments that shouldn't be constant, but can't be represented as a parameter.
            See the rst docs for more information.
        extra: dict
            extra keyword arguments to pass to ``function`` when this wrapper is called
        """
    def __call__(self, **kwargs):
        """
        Calls ``self.function``. Extra, closures, and parameter keywords as defined on
        init and through :func:`InteractiveFunction.setParams` are forwarded during the
        call.
        """
    def updateCachedParameterValues(self, param, value) -> None:
        """
        This function is connected to ``sigChanged`` of every parameter associated with
        it. This way, those parameters don't have to be queried for their value every
        time InteractiveFunction is __call__'ed
        """
    def hookupParameters(self, params: Incomplete | None = None, clearOld: bool = True) -> None:
        """
        Binds a new set of parameters to this function. If ``clearOld`` is *True* (
        default), previously bound parameters are disconnected.

        Parameters
        ----------
        params: Sequence[Parameter]
            New parameters to listen for updates and optionally propagate keywords
            passed to :meth:`__call__`
        clearOld: bool
            If ``True``, previously hooked up parameters will be removed first
        """
    def removeParameters(self, clearCache: bool = True) -> None:
        """
        Disconnects from all signals of parameters in ``self.parameters``. Also,
        optionally clears the old cache of param values
        """
    def runFromChangedOrChanging(self, param, value): ...
    def runFromAction(self, **kwargs): ...
    def disconnect(self):
        """
        Simulates disconnecting the runnable by turning ``runFrom*`` functions into no-ops
        """
    def setDisconnected(self, disconnected):
        """
        Sets the disconnected state of the runnable, see :meth:`disconnect` and
        :meth:`reconnect` for more information
        """
    def reconnect(self):
        """Simulates reconnecting the runnable by re-enabling ``runFrom*`` functions"""

class Interactor:
    runOptions: Incomplete
    parent: Incomplete
    titleFormat: Incomplete
    nest: bool
    existOk: bool
    runActionTemplate: Incomplete
    def __init__(self, **kwargs) -> None:
        """
        Initializes an Interactor with initial keyword arguments which can be anything
        accepted by :meth:`setOpts`
        """
    def setOpts(self, **opts):
        """
        Overrides the default options for this interactor.

        Note! This method should only be used if you spawn your own Interactor; do not
        call it on ``defaultInteractor``. Instead, use ``defaultInteractor.optsContext``,
        which is guaranteed to revert to the default options when the context expires.

        Parameters
        ----------
        opts
            Keyword arguments to override the default options

        Returns
        -------
            dict of previous options that were overridden. This is useful for resetting
            the options afterward.
        """
    def optsContext(self, **opts) -> Generator[None, None, None]:
        """
        Creates a new context for ``opts``, where each is reset to the old value
        when the context expires

        Parameters
        ----------
        opts:
            Options to set, must be one of the keys in :attr:`_optNames`
        """
    def interact(self, function, *, ignores: Incomplete | None = None, runOptions=..., parent=..., titleFormat=..., nest=..., runActionTemplate=..., existOk=..., **overrides):
        '''
        Interacts with a function by making Parameters for each argument.

        There are several potential use cases and argument handling possibilities
        depending on which values are passed to this function, so a more detailed
        explanation of several use cases is provided in the "Interactive Parameters" doc.

        if any non-defaults exist, a value must be provided for them in ``overrides``. If
        this value should *not* be made into a parameter, include its name in ``ignores``.

        Parameters
        ----------
        function: Callable
            function with which to interact. Can also be a :class:`InteractiveFunction`,
            if a reference to the bound signals is required.
        runOptions: ``GroupParameter.<RUN_ACTION, CHANGED, or CHANGING>`` value
            How the function should be run, i.e. when pressing an action, on
            sigValueChanged, and/or on sigValueChanging
        ignores: Sequence
            Names of function arguments which shouldn\'t have parameters created
        parent: GroupParameter
            Parent in which to add argument Parameters. If *None*, a new group
            parameter is created.
        titleFormat: str or Callable
            title of the group sub-parameter if one must be created (see ``nest``
            behavior). If a function is supplied, it must be of the form (str) -> str
            and will be passed the function name as an input
        nest: bool
            If *True*, the interacted function is given its own GroupParameter,
            and arguments to that function are \'nested\' inside as its children.
            If *False*, function arguments are directly added to this parameter
            instead of being placed inside a child GroupParameter
        runActionTemplate: dict
            Template for the action parameter which runs the function, used
            if ``runOptions`` is set to ``GroupParameter.RUN_ACTION``. Note that
            if keys like "name" or "type" are not included, they are inferred
            from the previous / default ``runActionTemplate``. This allows
            items that should only be set per-function to exist here, like
            a ``shortcut`` or ``icon``.
        existOk: bool
            Whether it is OK for existing parameter names to bind to this function.
            See behavior during \'Parameter.insertChild\'
        overrides:
            Override descriptions to provide additional parameter options for each
            argument. Moreover, extra parameters can be defined here if the original
            function uses ``**`` to consume additional keyword arguments. Each
            override can be a value (e.g. 5) or a dict specification of a
            parameter (e.g. dict(type=\'list\', limits=[0, 10, 20]))
        '''
    def __call__(self, function, **kwargs): ...
    def decorate(self, **kwargs):
        """
        Calls :meth:`interact` and returns the :class:`InteractiveFunction`.

        Parameters
        ----------
        kwargs
            Keyword arguments to pass to :meth:`interact`
        """
    def resolveAndHookupParameterChild(self, functionGroup, childOpts, interactiveFunction): ...
    def functionToParameterDict(self, function, **overrides):
        """
        Converts a function into a list of child parameter dicts
        """
    def createFunctionParameter(self, name, signatureParameter, overridesInfo):
        '''
        Constructs a dict ready for insertion into a group parameter based on the
        provided information in the ``inspect.signature`` parameter, user-specified
        overrides, and true parameter name. Parameter signature information is
        considered the most "overridable", followed by documentation specifications.
        User overrides should be given the highest priority, i.e. not usurped by
        parameter default information.

        Parameters
        ----------
        name : str
            Name of the parameter, comes from function signature
        signatureParameter : inspect.Parameter
            Information from the function signature, parsed by ``inspect``
        overridesInfo : dict
            User-specified overrides for this parameter. Can be a dict of options
            accepted by :class:`~pyqtgraph.parametertree.Parameter` or a value
        '''
    def getOpts(self): ...

interact: Incomplete
