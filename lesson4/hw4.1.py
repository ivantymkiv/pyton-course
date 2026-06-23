
def move_zeros_to_end(lst):
    # Створюємо новий список із ненульових елементів
    non_zero = [x for x in lst if x != 0]
    # Рахуємо кількість нулів
    zero_count = lst.count(0)
    # Додаємо потрібну кількість нулів у кінець
    return non_zero + [0] * zero_count

# Приклади використання:
print(move_zeros_to_end([9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]))                 # []
print(move_zeros_to_end([1, 0, 13, 0, 0, 0, 5]))          # [0, 0, 0]
print(move_zeros_to_end([0, 1, 0, 12, 3]))    # [1, 2, 3, 0, 0]
print(move_zeros_to_end([0])) # [4, 5, 6, 7, 0, 0]


