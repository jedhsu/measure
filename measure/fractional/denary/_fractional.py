"""

    *Denary Fractional*

  The base 10 fractional measure.

"""

from abc import ABCMeta

from .._fractional import Fractional

__all__ = ["DenaryFractional"]


class DenaryFractional(
    Fractional,
):
    __metaclass__ = ABCMeta

    def __init__(
        self,
        denominator: int,
    ):
        super(DenaryFractional, self).__init__(
            denominator,
        )
