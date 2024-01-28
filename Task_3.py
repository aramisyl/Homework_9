def map_square(lst: list) -> list:
    return list(map(lambda x: x**2, lst))

def test_1():
    result = map_square([1, 2, 3])
    assert result == [1, 4, 9]

def test_2():
    result = map_square([])
    assert result == []