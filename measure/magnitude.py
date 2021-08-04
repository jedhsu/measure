"""

    *Magnitude*

  A measure of magnitude.

"""

from abc import ABCMeta

from ._measure import Measure

__all__ = ["Magnitude"]


class Magnitude(
    Measure,
):
    __metaclass__ = ABCMeta
