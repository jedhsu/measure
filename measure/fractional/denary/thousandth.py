"""

    *Thousandth*

  The thousandth fractional measure.

"""

from dataclasses import dataclass

from ._fractional import DenaryFractional

__all__ = ["Thousandth"]


@dataclass
class Thousandth(
    DenaryFractional,
):
    denominator = 1000
