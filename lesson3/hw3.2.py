def move_last_to_first(lst):
    # Якщо список порожній або має лише один елемент – повертаємо його без змін
    if len(lst) <= 1:
        return lst

    # Беремо останній елемент і додаємо його на початок
    return [lst[-1]] + lst[:-1]
print(move_last_to_first([10, 20, 30, 40 , 50]))
print(move_last_to_first([1, 2, 3, 4, 5]))


