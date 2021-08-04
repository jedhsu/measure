"""

    *Dot*

  The graphical dot unit distance measure.

"""


from abc import ABCMeta

from strism._measure.unit import UnitDistance

from ._distance import GraphicalDistance

__all__ = ["Dot"]


class Dot(
    int,
    GraphicalDistance,
    UnitDistance,
):
    __metaclass__ = ABCMeta

    def __init__(
        self,
        n: int,
    ):
        super(Dot, self).__new__(
            int,
            n,
        )
