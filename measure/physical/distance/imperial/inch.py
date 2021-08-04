"""

    Inch

  The imperial inch distance measure.

"""

from abc import ABCMeta


from wich.literal.float_ import Float
from wich.measure.unit import UnitDistance

from ._distance import ImperialDistance


__all__ = [
    "Inch",
]


class Inch(
    Float,
    ImperialDistance,
    UnitDistance,
):
    __metaclass__ = ABCMeta

    def __init__(
        self,
        float: float,
    ):
        super(Inch, self).__init__(
            float,
        )
