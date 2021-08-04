"""

    Typepoint

  The graphical typepoint distance measure.

"""

from abc import ABCMeta


from wich.measure.unit import UnitDistance
from wich.measure.fractional import Quarter

from ._distance import GraphicalDistance

__all__ = [
    "Typepoint",
]


class Typepoint(
    Quarter,
    GraphicalDistance,
    UnitDistance,
):
    __metaclass__ = ABCMeta

    def __init__(
        self,
        int: int,
    ):
        super(Typepoint, self).__init__(
            int,
        )
