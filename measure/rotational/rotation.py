"""

    Rotation

  A counting measure of rotation.

"""

from ..count import Count
from ._rotational import RotationalMeasure

__all__ = [
    "Rotation",
]


class Rotation(
    Count,
    RotationalMeasure,
):
    def __init__(
        self,
        count: int,
    ):
        super(Rotation, self).__init__(
            count,
        )
