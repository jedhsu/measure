"""

    *Graphical Measure*

  A measure of a digital graphical system.

"""

from abc import ABCMeta

from .._measure import Measure

__all__ = ["GraphicalMeasure"]


class GraphicalMeasure(
    Measure,
):
    __metaclass__ = ABCMeta
