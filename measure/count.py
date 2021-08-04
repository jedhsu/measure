"""

    *Count*

  The counting measure.

"""

from ._measure import Measure

__all__ = ["Count"]


class Count(
    int,
    Measure,
):
    def __init__(
        self,
        integer: int,
    ):
        super(Count, self).__new__(
            int,
            integer,
        )
