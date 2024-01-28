def power(x: int, y: int) -> int:
    if y == 0:
        return 1
    else:
        return x * power(x, y - 1)

def test_1():
    result = power(12, 0)
    assert result == 1

def test_2():
    result = power(2, 3)
    assert result == 8

def test_3():
    result = power(0, 3)
    assert result == 0