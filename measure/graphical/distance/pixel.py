"""

    Pixel

  The graphical pixel distance measure.

"""

from abc import ABCMeta


from wich.measure.unit import UnitDistance
from wich.literal.integer import Integer

from ._distance import GraphicalDistance

__all__ = [
    "Pixel",
]


class Pixel(
    Integer,
    GraphicalDistance,
    UnitDistance,
):
    __metaclass__ = ABCMeta

    def __init__(
        self,
        int: int,
    ):
        super(Integer, self).__init__(
            int,
        )
