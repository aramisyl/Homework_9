def sum_list(lst: list) -> int:
    total = 0
    for item in lst:
        if isinstance(item, list):
            total += sum_list(item)
        else:
            total += item
    return total

def test_1():
    result = sum_list([1, 2, [3, 4], 5, [6, [7, 8]]])
    assert result == 36

def test_2():
    result = sum_list([1, 2, 3])
    assert result == 6

def test_3():
    result = sum_list([])
    assert result == 0