"""

    *Percent*

  The percentage scaling measure.

"""


from ._measure import ScalingMeasure

__all__ = ["Percent"]


class Percent(
    float,
    ScalingMeasure,
):
    def __init__(
        self,
        flt: float,
    ):
        assert 0 <= flt <= 1, "Percent must be between 0 and 1."
        super(Percent, self).__new__(
            float,
            flt,
        )
