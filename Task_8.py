def sum_list(lst: list) -> int:
    try:
        total = 0
        for item in lst:
            if isinstance(item, list):
                total += sum_list(item)
            else:
                total += item
    except:
        total = ("Invalid argument provided. Please make sure only numbers are used in list.")
    return total

def test_1():
    result = sum_list([1, 2, [3, 4], 5, [6, [7, 8]]])
    assert result == 36

def test_2():
    result = sum_list([1, 2, [3, 'a'], 5, [6, [7, 8]]])
    assert result == "Invalid argument provided. Please make sure only numbers are used in list."