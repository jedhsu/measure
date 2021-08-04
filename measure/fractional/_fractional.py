"""

    *Fractional*

  The fractional measure.

"""

from fractions import Fraction

from dataclasses import dataclass


__all__ = ["Fractional"]


@dataclass
class Fractional(
    Fraction,
):
    denominator: int

    def __init__(
        self,
        denominator: int,
    ):
        self.denominator = denominator
        super(Fractional, self).__new__(
            Fraction,
            1,
            self.denominator,
        )
