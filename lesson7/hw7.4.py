def common_elements():
    # Генеруємо числа від 0 до 99
    multiples_of_3 = [x for x in range(100) if x % 3 == 0]
    multiples_of_5 = [x for x in range(100) if x % 5 == 0]

    # Перетворюємо списки на множини
    set_3 = set(multiples_of_3)
    set_5 = set(multiples_of_5)

    # Знаходимо перетин множин
    intersection = set_3 & set_5

    return intersection


# Перевірка роботи:
print(common_elements())
# {0, 15, 30, 45, 60, 75, 90}

