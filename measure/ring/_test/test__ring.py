from .._ring import Ring


class TestInteger:
    def test_init(self):
        x = Ring(100, 360)
        assert isinstance(x, Ring)
        assert isinstance(x, int)

    def test_add(self):
        x = Ring(100, 360)
        x = x + 300
        assert x == Ring(400, 360)

    def test_subtract(self):
        x = Ring(100, 360)
        x = x - 300
        assert x == Ring(-200, 360)

    def test_multiply(self):
        pass

    def test_divide(self):
        pass


class TestFloat:
    pass
