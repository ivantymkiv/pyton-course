def prime_generator(limit):
    """
    Генератор простих чисел до заданої межі (limit).
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    for num in range(2, limit + 1):
        if is_prime(num):
            yield num
print(list(prime_generator(10)))   # [2, 3, 5, 7]
print(list(prime_generator(20)))   # [2, 3, 5, 7, 11, 13, 17, 19]
print(list(prime_generator(29)))   # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]