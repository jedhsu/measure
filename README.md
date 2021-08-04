## Measure

`measure`{:.python} is a library for unit-of-measure types.

1. models unit-of-measure types such that there is form equivalence.

Consider temperature, which is measured in units of Kelvin, Celsius, or Fahrenheit.

Theoretically, ...

We have

```python

temp = Temperature.from_fahrenheit(80.9)
equivalence = temp.as_celsius() == approx(temp.as_fahrenheit()) == approx(temp.as_kelvin())
assert equivalence

```

Another example, for the complex numbers:

This is useful, because it enables abstraction from the unit to the underlying measure.

Consider these additional examples:
* Rotation - over angle or radians
* Graphical distance - over px, pt, em, etc...

2. unit validation via symbolic expressions (time permitted)






It implements the `Measure`{:.python} type




