"""

    *Half*

  The half fractional measure.

"""

from ._fractional import BinaryFractional

__all__ = ["Half"]


class Half(
    BinaryFractional,
):
    denominator = 2
