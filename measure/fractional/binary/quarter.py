"""

    *Quarter*

  The quarter fractional measure.

"""

from ._fractional import BinaryFractional

__all__ = ["Quarter"]


class Quarter(
    BinaryFractional,
):
    denominator = 4
