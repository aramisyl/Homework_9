def count_vowels(s: str, case_sensitive: bool = False) -> int:
    vowels = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']
    if not case_sensitive:
        s = s.lower()
    count = 0
    for char in s:
        if char in vowels:
            count += 1
            vowels.remove(char)
    return count

print(count_vowels("Hello, wOrld!", case_sensitive=True))

def test_1():
    result = count_vowels("Hello, wOrld!", case_sensitive=True)
    assert result == 3

def test_2():
    result = count_vowels("Hello, wOrld!", case_sensitive=False)
    assert result == 2