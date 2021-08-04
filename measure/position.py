"""

    *Position*

  A measure of position.

"""

from abc import ABCMeta

from ._measure import Measure

__all__ = ["Position"]


class Position(
    Measure,
):
    __metaclass__ = ABCMeta
