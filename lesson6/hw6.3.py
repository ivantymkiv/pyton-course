def multiply_digits_until_single(num: int) -> int:
    # Працюємо доти, доки число більше 9
    while num > 9:
        product = 1
        for digit in str(num):
            product *= int(digit)
        num = product
    return num

# Приклад використання:
user_input = int(input("Введіть ціле число: "))
result = multiply_digits_until_single(user_input)
print("Результат:", result)
