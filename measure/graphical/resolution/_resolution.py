"""

    *Resolution*

  A measure of resolution.

  Measures density.

  Graphical / Physical 

"""

from abc import ABCMeta

from .._graphical import GraphicalMeasure

__all__ = ["Resolution"]


class Resolution(
    GraphicalMeasure,
):
    __metaclass__ = ABCMeta
