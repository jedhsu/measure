"""

    *Unit Distance*

  A unit measure of distance.

"""

from abc import ABCMeta

from ._measure import UnitMeasure

__all__ = [
    "UnitDistance",
]


class UnitDistance(
    UnitMeasure,
):
    __metaclass__ = ABCMeta
