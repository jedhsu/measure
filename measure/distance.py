"""

    *Distance*

  A measure of distance.

"""

from abc import ABCMeta

from ._measure import Measure

__all__ = ["Distance"]


class Distance(
    Measure,
):
    __metaclass__ = ABCMeta
