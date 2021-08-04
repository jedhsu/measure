"""

    *Imperial Distance*

  A distance measure of the imperial system.

"""

from abc import ABCMeta

from .._distance import PhysicalDistance

__all__ = ["ImperialDistance"]


class ImperialDistance(
    PhysicalDistance,
):
    __metaclass__ = ABCMeta
