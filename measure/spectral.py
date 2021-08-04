"""

    *Spectral*

  A spectral measure.

"""

from abc import ABCMeta

from ._measure import Measure

__all__ = ["Spectral"]


class Spectral(
    Measure,
):
    __metaclass__ = ABCMeta
