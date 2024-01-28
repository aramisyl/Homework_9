def modify_list(lst: list, *funcs: callable) -> None:
    for i in range(len(lst)):
        for func in funcs:
            lst[i] = func(lst[i])

def test_1():
    a = [1, 2, 3]
    modify_list(a, lambda x: x**2 if x % 2 == 0 else x, lambda x: x + 1 if x % 2 != 0 else x)
    assert a == [2, 4, 4]