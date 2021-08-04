"""

    *Centimeter*

  The metric centimeter unit distance measure.

"""

from abc import ABCMeta

from strism._measure.unit import UnitDistance

from ._distance import MetricDistance

__all__ = ["Centimeter"]


class Centimeter(
    float,
    MetricDistance,
    UnitDistance,
):
    __metaclass__ = ABCMeta

    def __init__(
        self,
        flt: float,
    ):
        super(Centimeter, self).__new__(
            float,
            flt,
        )
