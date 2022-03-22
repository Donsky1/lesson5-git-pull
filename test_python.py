# модуль тестирования  встроенных функций
# В модуле написать тесты для встроенных функций filter, map, sorted, а также для функций из библиотеки math: pi, sqrt, pow, hypot.
import math

def test_filter():
    assert list(filter(lambda x: x % 2 == 0, range(20)[:6])) == [0, 2, 4]
    assert list(filter(lambda x: x % 3 == 0, range(20)[:6])) == [0, 3]
    assert sum(list(filter(lambda x: x % 2 == 0, range(20)))) % 2 == 0

def test_map():
    assert list(map(lambda x: x*2, range(4))) == [0, 2, 4, 6]
    assert len(list(map(lambda x: x*2, range(4)))) == 4

def test_sorted():
    assert sorted([1, 2, 3], reverse=True) == [3, 2, 1]
    assert sorted(['3', '2', '1'], key=int) == ['1', '2', '3']

def test_math_pi():
    assert isinstance(math.pi, float)
    assert round(math.pi, 2) == 3.14

def test_math_sqrt():
    assert math.sqrt(9) == 3.0
    assert isinstance(math.sqrt(9), float)

def test_math_pow():
    assert math.pow(2, 3) == 8
    assert math.pow(2, 4) % 2 == 0
    assert math.pow(5, 0) == 1

def test_math_hypot():
    assert math.hypot(3, 4) == 5.0
    assert math.hypot(8, 6) == 10.
