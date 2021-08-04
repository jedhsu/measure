"""

    *Hundredth*

  The hundredth fractional measure.

"""

from dataclasses import dataclass

from ._fractional import DenaryFractional

__all__ = ["Hundredth"]


@dataclass
class Hundredth(
    DenaryFractional,
):
    denominator = 100
    numerator: int

    def __init__(
        self,
        numerator: int,
    ):
        self.numerator = numerator
        super(Hundredth, self).__init__(
            self.denominator,
        )
