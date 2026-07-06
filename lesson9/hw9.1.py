def difference(*args):
    if not args:  # якщо аргументів немає
        return 0
    max_val = max(args)
    min_val = min(args)
    result = max_val - min_val
    return round(result, 2)  # округлення до 2 знаків після коми

print(difference(1, 2, 3))
print(difference(5, -5))
print(difference(10.2, -2.2, 0, 1.1, 0.5))
print(difference())
print('OK')

