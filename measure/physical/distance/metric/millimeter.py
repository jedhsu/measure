"""

    Millimeter

  The metric millimeter unit distance measure.

"""

from abc import ABCMeta

from ..._unit import UnitDistance
from ._distance import MetricDistance

from wich.literal.float_ import Float

__all__ = [
    "Millimeter",
]


class Millimeter(
    Float,
    MetricDistance,
    UnitDistance,
):
    __metaclass__ = ABCMeta

    def __init__(
        self,
        float: float,
    ):
        super(Millimeter, self).__init__(
            float,
        )
