"""

    *Unit Angle*

  A unit measure of angle.

"""

from abc import ABCMeta

from ._measure import UnitMeasure

__all__ = [
    "UnitAngle",
]


class UnitAngle(
    UnitMeasure,
):
    __metaclass__ = ABCMeta
