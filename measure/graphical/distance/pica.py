"""

    Pica

  The graphical pica (12 points) distance measure.

"""


from abc import ABCMeta


from wich.measure.unit import UnitDistance
from wich.literal.integer import Integer

from ._distance import GraphicalDistance

__all__ = [
    "Pica",
]


class Pica(
    Integer,
    GraphicalDistance,
    UnitDistance,
):
    __metaclass__ = ABCMeta

    def __init__(
        self,
        int: int,
    ):
        super(Pica, self).__init__(
            int,
        )
