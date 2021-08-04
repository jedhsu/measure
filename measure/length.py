"""

    *Length*

  A measure of length.

"""

from abc import ABCMeta

from ._measure import Measure

__all__ = ["Length"]


class Length(
    Measure,
):
    __metaclass__ = ABCMeta
