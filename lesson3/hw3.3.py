def split_list(lst):
    n = len(lst)

    # Випадок 1: порожній список
    if n == 0:
        return [[], []]

    # Випадок 2: непарна кількість елементів
    if n % 2 == 1:
        mid = n // 2 + 1  # перша половина більша
    else:
        # Випадок 3: парна кількість елементів
        mid = n // 2

    return [lst[:mid], lst[mid:]]



print(split_list([1, 2, 3, 4, 5, 6]))  # [[], []]
print(split_list([1,]))  # [[1], [2]]
print(split_list([1, 2, 3]))  # [[1, 2], [3]]
print(split_list([10, 20, 30, 40]))  # [[10, 20], [30, 40]]
print(split_list([5, 6, 7, 8, 9]))  # [[5, 6, 7], [8, 9]]

