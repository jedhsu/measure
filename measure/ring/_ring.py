"""

    *Ring*

  # [TODO] think about proper placing

"""

from __future__ import annotations
from dataclasses import dataclass

from typing import TypeVar
from typing import Generic

T = TypeVar("T", float, int)

# [TODO] this is kind of like the size of an array, could need metaclass.
class RingMeta(
    Generic[T],
):
    def __prepare__(cls, modulo: T):
        dct = {}
        dct["modulo"] = modulo
        return dct


@dataclass
class Ring(
    RingMeta,
    Generic[T],
):
    value: T
    modulo: T

    def __add__(self, x: T) -> Ring[T]:
        self.value = (self.value + x) % self.modulo
        return self

    def __sub__(self, x: T) -> Ring[T]:
        self.value = (self.value - x) % self.modulo
        return self

    def __mult__(self, x: T) -> Ring[T]:
        self.value = (self.value - x) % self.modulo
        return self

    def __div__(self, x: T) -> Ring[T]:
        self.value = (self.value / x) % self.modulo
        return self
