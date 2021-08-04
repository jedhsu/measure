"""

    Rotational Measure

  A measure of a rotational system.

"""

from abc import ABCMeta


from .._measure import Measure

__all__ = [
    "RotationalMeasure",
]


class RotationalMeasure(
    Measure,
):
    __metaclass__ = ABCMeta
