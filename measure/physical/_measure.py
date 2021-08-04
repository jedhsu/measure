"""

    *Physical Measure*

  A measure of a physical system.

"""

from abc import ABCMeta

from .._measure import Measure

__all__ = ["PhysicalMeasure"]


class PhysicalMeasure(
    Measure,
):
    __metaclass__ = ABCMeta
