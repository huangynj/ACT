"""
This module contains classes for displaying data.
:func:`act.plotting.Display` is the
base class on which all other Display classes are inherited from. If you are making
a new Display object, please make it inherited from this class.

| :func:`act.plotting.ContourDisplay` handles the plotting of contour plots.
| :func:`act.plotting.GeographicPlotDisplay` handles the plotting of lat-lon plots.
| :func:`act.plotting.HistogramDisplay` handles the plotting of histogram plots.
| :func:`act.plotting.SkewTDisplay` handles the plotting of Skew-T diagrams.
| :func:`act.plotting.TimeSeriesDisplay` handles the plotting of timeseries.
| :func:`act.plotting.WindRoseDisplay` handles the plotting of wind rose plots.
| :func:`act.plotting.XSectionDisplay` handles the plotting of cross sections.

"""

from . import act_cmap, common
from .contourdisplay import ContourDisplay
from .geodisplay import GeographicPlotDisplay
from .histogramdisplay import HistogramDisplay
from .plot import Display
from .skewtdisplay import SkewTDisplay
from .timeseriesdisplay import TimeSeriesDisplay
from .windrosedisplay import WindRoseDisplay
from .xsectiondisplay import XSectionDisplay
