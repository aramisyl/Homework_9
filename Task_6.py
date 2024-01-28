def reverse_number(num: int) -> int:
    if num < 10:
        return num

    last_digit = num % 10
    remaining_digits = num // 10
    reversed_remaining_digits = reverse_number(remaining_digits)

    return last_digit * (10 ** len(str(remaining_digits))) + reversed_remaining_digits

def test_1():
    result = reverse_number(1234)
    assert result == 4321

def test_2():
    result = reverse_number(7)
    assert result == 7

def test_3():
    result = reverse_number(0)
    assert result == 0