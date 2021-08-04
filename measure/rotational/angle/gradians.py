"""

    Gradians

  The gradians unit angle measure.

"""

from abc import ABCMeta


from wich.literal.float_ import Float
from wich.measure.unit import UnitAngle

from ._angle import Angle


__all__ = [
    "Gradians",
]


class Gradians(
    Float,
    Angle,
    UnitAngle,
):
    __metaclass__ = ABCMeta

    def __init__(
        self,
        float: float,
    ):
        super(Gradians, self).__init__(
            float,
        )
