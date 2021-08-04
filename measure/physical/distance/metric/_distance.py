"""

    *Metric Distance*

  A distance measure of the metric system.

"""

from abc import ABCMeta

from .._distance import PhysicalDistance

__all__ = ["MetricDistance"]


class MetricDistance(
    PhysicalDistance,
):
    __metaclass__ = ABCMeta
