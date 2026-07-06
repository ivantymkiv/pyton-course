def add_one(digits: list[int]) -> list[int]:
    # Перетворюємо список цифр у число
    number = int("".join(map(str, digits)))

    # Додаємо 1
    number += 1

    # Перетворюємо назад у список цифр
    return [int(ch) for ch in str(number)]


# Unit tests
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("OK")
