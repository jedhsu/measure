"""

    *Tenth*

  The tenth fractional measure.

"""

from dataclasses import dataclass

from ._fractional import DenaryFractional

__all__ = ["Tenth"]


class Tenth(
    DenaryFractional,
):
    denominator = 10
