def sum_even_indices_times_last(lst):
    # Якщо список порожній → результат 0
    if not lst:
        return 0

    # Знаходимо суму елементів із парними індексами
    sum_even = sum(lst[i] for i in range(0, len(lst), 2))

    # Множимо на останній елемент
    return sum_even * lst[-1]

print(sum_even_indices_times_last([0, 1, 7, 2, 4, 8]))
print(sum_even_indices_times_last([6]))
print(sum_even_indices_times_last([1, 3, 5]))