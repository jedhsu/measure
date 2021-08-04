"""

    *Scaling Measure*

  A scaling measure.

"""

from abc import ABCMeta

from .._measure import Measure

__all__ = [
    "ScalingMeasure",
]


class ScalingMeasure(
    Measure,
):
    __metaclass__ = ABCMeta
