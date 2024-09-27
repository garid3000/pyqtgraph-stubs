from .GraphicsWidget import GraphicsWidget
from _typeshed import Incomplete
from .ViewBox import ViewBox

__all__ = ['AxisItem']

class AxisItem(GraphicsWidget):
    """
    GraphicsItem showing a single plot axis with ticks, values, and label.
    Can be configured to fit on any side of a plot,
    Can automatically synchronize its displayed scale with ViewBox items.
    Ticks can be extended to draw a grid.
    If maxTickLength is negative, ticks point into the plot.
    """
    label: Incomplete
    picture: Incomplete
    orientation: Incomplete
    style: Incomplete
    textWidth: int
    textHeight: int
    fixedWidth: Incomplete
    fixedHeight: Incomplete
    labelText: Incomplete
    labelUnits: Incomplete
    labelUnitPrefix: Incomplete
    labelStyle: Incomplete
    logMode: bool
    scale: float
    autoSIPrefix: bool
    autoSIPrefixScale: float
    grid: bool
    def __init__(self, orientation, pen: Incomplete | None = None, textPen: Incomplete | None = None, tickPen: Incomplete | None = None, linkView: Incomplete | None = None, parent: Incomplete | None = None, maxTickLength: int = -5, showValues: bool = True, text: str = '', units: str = '', unitPrefix: str = '', **args) -> None:
        """
        =============== ===============================================================
        **Arguments:**
        orientation     one of 'left', 'right', 'top', or 'bottom'
        maxTickLength   (px) maximum length of ticks to draw. Negative values draw
                        into the plot, positive values draw outward.
        linkView        (ViewBox) causes the range of values displayed in the axis
                        to be linked to the visible range of a ViewBox.
        showValues      (bool) Whether to display values adjacent to ticks
        pen             (QPen) Pen used when drawing axis and (by default) ticks
        textPen         (QPen) Pen used when drawing tick labels.
        tickPen         (QPen) Pen used when drawing ticks.
        text            The text (excluding units) to display on the label for this
                        axis.
        units           The units for this axis. Units should generally be given
                        without any scaling prefix (eg, 'V' instead of 'mV'). The
                        scaling prefix will be automatically prepended based on the
                        range of data displayed.
        args            All extra keyword arguments become CSS style options for
                        the <span> tag which will surround the axis label and units.
        =============== ===============================================================
        """
    def setStyle(self, **kwds) -> None:
        """
        Set various style options.

        ===================== =======================================================
        Keyword Arguments:
        tickLength            (int) The maximum length of ticks in pixels.
                              Positive values point toward the text; negative
                              values point away.
        tickTextOffset        (int) reserved spacing between text and axis in px
        tickTextWidth         (int) Horizontal space reserved for tick text in px
        tickTextHeight        (int) Vertical space reserved for tick text in px
        autoExpandTextSpace   (bool) Automatically expand text space if the tick
                              strings become too long.
        autoReduceTextSpace   (bool) Automatically shrink the axis if necessary
        hideOverlappingLabels (bool or int)

                              * *True*  (default for horizontal axis): Hide tick labels which extend beyond the AxisItem's geometry rectangle.
                              * *False* (default for vertical axis): Labels may be drawn extending beyond the extent of the axis.
                              * *(int)* sets the tolerance limit for how many pixels a label is allowed to extend beyond the axis. Defaults to 15 for `hideOverlappingLabels = False`.

        tickFont              (QFont or None) Determines the font used for tick
                              values. Use None for the default font.
        stopAxisAtTick        (tuple: (bool min, bool max)) If True, the axis
                              line is drawn only as far as the last tick.
                              Otherwise, the line is drawn to the edge of the
                              AxisItem boundary.
        textFillLimits        (list of (tick #, % fill) tuples). This structure
                              determines how the AxisItem decides how many ticks
                              should have text appear next to them. Each tuple in
                              the list specifies what fraction of the axis length
                              may be occupied by text, given the number of ticks
                              that already have text displayed. For example::

                                  [(0, 0.8), # Never fill more than 80% of the axis
                                   (2, 0.6), # If we already have 2 ticks with text,
                                             # fill no more than 60% of the axis
                                   (4, 0.4), # If we already have 4 ticks with text,
                                             # fill no more than 40% of the axis
                                   (6, 0.2)] # If we already have 6 ticks with text,
                                             # fill no more than 20% of the axis

        showValues            (bool) indicates whether text is displayed adjacent
                              to ticks.
        tickAlpha             (float or int or None) If None, pyqtgraph will draw the
                              ticks with the alpha it deems appropriate.  Otherwise,
                              the alpha will be fixed at the value passed.  With int,
                              accepted values are [0..255].  With value of type
                              float, accepted values are from [0..1].
        ===================== =======================================================

        Added in version 0.9.9
        """
    def close(self) -> None: ...
    def setGrid(self, grid) -> None:
        """Set the alpha value (0-255) for the grid, or False to disable.

        When grid lines are enabled, the axis tick lines are extended to cover
        the extent of the linked ViewBox, if any.
        """
    def setLogMode(self, *args, **kwargs) -> None:
        """
        Set log scaling for x and/or y axes.

        If two positional arguments are provided, the first will set log scaling
        for the x axis and the second for the y axis. If a single positional
        argument is provided, it will set the log scaling along the direction of
        the AxisItem. Alternatively, x and y can be passed as keyword arguments.

        If an axis is set to log scale, ticks are displayed on a logarithmic scale
        and values are adjusted accordingly. (This is usually accessed by changing
        the log mode of a :func:`PlotItem <pyqtgraph.PlotItem.setLogMode>`.) The
        linked ViewBox will be informed of the change.
        """
    def setTickFont(self, font) -> None:
        """
        (QFont or None) Determines the font used for tick values.
        Use None for the default font.
        """
    def resizeEvent(self, ev: Incomplete | None = None) -> None: ...
    def showLabel(self, show: bool = True) -> None:
        """Show/hide the label text for this axis."""
    def setLabel(self, text: str | None = None, units: str | None = None, unitPrefix: str | None = None, **args : str) -> None:
        '''Set the text displayed adjacent to the axis.

        ==============  =============================================================
        **Arguments:**
        text            The text (excluding units) to display on the label for this
                        axis.
        units           The units for this axis. Units should generally be given
                        without any scaling prefix (eg, \'V\' instead of \'mV\'). The
                        scaling prefix will be automatically prepended based on the
                        range of data displayed.
        args            All extra keyword arguments become CSS style options for
                        the <span> tag which will surround the axis label and units.
        ==============  =============================================================

        The final text generated for the label will look like::

            <span style="...options...">{text} (prefix{units})</span>

        Each extra keyword argument will become a CSS option in the above template.
        For example, you can set the font size and color of the label::

            labelStyle = {\'color\': \'#FFF\', \'font-size\': \'14pt\'}
            axis.setLabel(\'label text\', units=\'V\', **labelStyle)

        '''
    def labelString(self): ...
    def setHeight(self, h: Incomplete | None = None) -> None:
        """Set the height of this axis reserved for ticks and tick labels.
        The height of the axis label is automatically added.

        If *height* is None, then the value will be determined automatically
        based on the size of the tick text."""
    def setWidth(self, w: Incomplete | None = None) -> None:
        """Set the width of this axis reserved for ticks and tick labels.
        The width of the axis label is automatically added.

        If *width* is None, then the value will be determined automatically
        based on the size of the tick text."""
    def pen(self): ...
    def setPen(self, *args, **kwargs) -> None:
        """
        Set the pen used for drawing text, axes, ticks, and grid lines.
        If no arguments are given, the default foreground color will be used
        (see :func:`setConfigOption <pyqtgraph.setConfigOption>`).
        """
    def textPen(self): ...
    def setTextPen(self, *args, **kwargs) -> None:
        """
        Set the pen used for drawing text.
        If no arguments are given, the default foreground color will be used.
        """
    def tickPen(self): ...
    def setTickPen(self, *args, **kwargs) -> None:
        """
        Set the pen used for drawing tick marks.
        If no arguments are given, the default pen will be used.
        """
    def setScale(self, scale: Incomplete | None = None) -> None:
        """
        Set the value scaling for this axis.

        Setting this value causes the axis to draw ticks and tick labels as if
        the view coordinate system were scaled. By default, the axis scaling is
        1.0.
        """
    def enableAutoSIPrefix(self, enable: bool = True) -> None:
        """
        Enable (or disable) automatic SI prefix scaling on this axis.

        When enabled, this feature automatically determines the best SI prefix
        to prepend to the label units, while ensuring that axis values are scaled
        accordingly.

        For example, if the axis spans values from -0.1 to 0.1 and has units set
        to 'V' then the axis would display values -100 to 100
        and the units would appear as 'mV'

        This feature is enabled by default, and is only available when a suffix
        (unit string) is provided to display on the label.
        """
    def updateAutoSIPrefix(self) -> None: ...
    range: Incomplete
    def setRange(self, mn, mx) -> None:
        """Set the range of values displayed by the axis.
        Usually this is handled automatically by linking the axis to a ViewBox with :func:`linkToView <pyqtgraph.AxisItem.linkToView>`"""
    def linkedView(self):
        """Return the ViewBox this axis is linked to."""
    def linkToView(self, view: ViewBox) -> None:
        """Link this axis to a ViewBox, causing its displayed range to match the visible range of the view."""
    def unlinkFromView(self) -> None:
        """Unlink this axis from a ViewBox."""
    def linkedViewChanged(self, view, newRange: Incomplete | None = None) -> None: ...
    def boundingRect(self): ...
    def paint(self, p, opt, widget) -> None: ...
    def setTickDensity(self, density: float = 1.0) -> None:
        """
        The default behavior is to show at least two major ticks for axes of up to 300 pixels in length,
        then add additional major ticks, spacing them out further as the available room increases.
        (Internally, the targeted number of major ticks grows with the square root of the axes length.)

        Setting a tick density different from the default value of `density = 1.0` scales the number of
        major ticks that is targeted for display. This only affects the automatic generation of ticks.
        """
    def setTicks(self, ticks) -> None:
        """Explicitly determine which ticks to display.
        This overrides the behavior specified by tickSpacing(), tickValues(), and tickStrings()
        The format for *ticks* looks like::

            [
                [ (majorTickValue1, majorTickString1), (majorTickValue2, majorTickString2), ... ],
                [ (minorTickValue1, minorTickString1), (minorTickValue2, minorTickString2), ... ],
                ...
            ]

        The two levels of major and minor ticks are expected. A third tier of additional ticks is optional.
        If *ticks* is None, then the default tick system will be used instead.
        """
    def setTickSpacing(self, major: Incomplete | None = None, minor: Incomplete | None = None, levels: Incomplete | None = None) -> None:
        """
        Explicitly determine the spacing of major and minor ticks. This
        overrides the default behavior of the tickSpacing method, and disables
        the effect of setTicks(). Arguments may be either *major* and *minor*,
        or *levels* which is a list of (spacing, offset) tuples for each
        tick level desired.

        If no arguments are given, then the default behavior of tickSpacing
        is enabled.

        Examples::

            # two levels, all offsets = 0
            axis.setTickSpacing(5, 1)
            # three levels, all offsets = 0
            axis.setTickSpacing(levels=[(3, 0), (1, 0), (0.25, 0)])
            # reset to default
            axis.setTickSpacing()
        """
    def tickSpacing(self, minVal, maxVal, size):
        """Return values describing the desired spacing and offset of ticks.

        This method is called whenever the axis needs to be redrawn and is a
        good method to override in subclasses that require control over tick locations.

        The return value must be a list of tuples, one for each set of ticks::

            [
                (major tick spacing, offset),
                (minor tick spacing, offset),
                (sub-minor tick spacing, offset),
                ...
            ]
        """
    def tickValues(self, minVal, maxVal, size):
        """
        Return the values and spacing of ticks to draw::

            [
                (spacing, [major ticks]),
                (spacing, [minor ticks]),
                ...
            ]

        By default, this method calls tickSpacing to determine the correct tick locations.
        This is a good method to override in subclasses.
        """
    def logTickValues(self, minVal, maxVal, size, stdTicks): ...
    def tickStrings(self, values, scale, spacing):
        """Return the strings that should be placed next to ticks. This method is called
        when redrawing the axis and is a good method to override in subclasses.
        The method is called with a list of tick values, a scaling factor (see below), and the
        spacing between ticks (this is required since, in some instances, there may be only
        one tick and thus no other way to determine the tick spacing)

        The scale argument is used when the axis label is displaying units which may have an SI scaling prefix.
        When determining the text to display, use value*scale to correctly account for this prefix.
        For example, if the axis label's units are set to 'V', then a tick value of 0.001 might
        be accompanied by a scale value of 1000. This indicates that the label is displaying 'mV', and
        thus the tick should display 0.001 * 1000 = 1.
        """
    def logTickStrings(self, values, scale, spacing): ...
    def generateDrawSpecs(self, p):
        """
        Calls tickValues() and tickStrings() to determine where and how ticks should
        be drawn, then generates from this a set of drawing commands to be
        interpreted by drawPicture().
        """
    def drawPicture(self, p, axisSpec, tickSpecs, textSpecs) -> None: ...
    def show(self) -> None: ...
    def hide(self) -> None: ...
    def wheelEvent(self, event) -> None: ...
    def mouseDragEvent(self, event): ...
    def mouseClickEvent(self, event): ...
