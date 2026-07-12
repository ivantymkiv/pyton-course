def sequence_generator(func, first, n):
    """
    func  : функція, яка задає закон послідовності
    first : перший член послідовності
    n     : кількість членів, які потрібно згенерувати
    """
    current = first
    for _ in range(n):
        yield current
        current = func(current)


def pow(x):
    return x ** 2

gen = sequence_generator(pow, 2, 4)
print(list(gen))
print('OK')
