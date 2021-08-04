"""

    Angle

  A measure of angle. 

"""

from abc import ABCMeta

from ..._measure import Measure

__all__ = [
    "Angle",
]


class Angle(
    Measure,
):
    __metaclass__ = ABCMeta
