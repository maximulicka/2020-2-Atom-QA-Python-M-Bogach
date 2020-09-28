import pytest
from pytest import raises

parametrs = [
    'x, y, result', [(6, 3, 2.0),
    (6, 0, ZeroDivisionError),
    (0, 6, 0.0)]

]

class TestInt:

    def test_sum(self):
        x = 5
        y = 3
        assert x + y == 8

    def test_multiplication(self):
        x = 5
        y = 3
        assert x * y == 15

    def test_power(self):
        x = 5
        y = 3
        assert x ** y == 125

    def test_difference(self):
        x = 5
        y = 3
        assert 5 - 3 == 2

    @pytest.mark.parametrize(*parametrs)
    def test_division(self, x, y, result):
        if y == 0:
            with pytest.raises(ZeroDivisionError):
                assert x / y == result
        else:
            assert x / y == result