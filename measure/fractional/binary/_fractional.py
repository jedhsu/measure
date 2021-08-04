"""

    *Binary Fractional*

  The base 2 fractional measure.

"""

from abc import ABCMeta

from .._fractional import Fractional


class BinaryFractional(
    Fractional,
):
    __metaclass__ = ABCMeta
