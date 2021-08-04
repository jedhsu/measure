"""

    *Physical Distance*

  A measure of physical distance.

"""

from abc import ABCMeta

from strism._measure import Distance

from .._measure import PhysicalMeasure

__all__ = ["PhysicalDistance"]


class PhysicalDistance(
    PhysicalMeasure,
    Distance,
):
    __metaclass__ = ABCMeta
