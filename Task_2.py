def sort_by_length(lst: list) -> list:
    return sorted(lst, key=lambda x: len(x))

def test_1():
    result = sort_by_length(["apple", "banana", "cherry", "date"])
    assert result ==  ["date", "apple", "banana", "cherry"]

