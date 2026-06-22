# Введення першого числа
num1 = float(input("Введіть перше число: "))

# Введення математичної дії
operation = input("Введіть дію (+, -, *, /): ")

# Введення другого числа
num2 = float(input("Введіть друге число: "))

# Перевірка умови та обчислення результату
if operation == '+':
    result = num1 + num2
    print(f"Результат: {num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"Результат: {num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"Результат: {num1} * {num2} = {result}")
elif operation == '/':
    # Обов'язкова перевірка ділення на нуль
    if num2 == 0:
        print("Помилка! Ділити на нуль не можна.")
    else:
        result = num1 / num2
        print(f"Результат: {num1} / {num2} = {result}")
else:
    print("Некоректна дія! Будь ласка, оберіть +, -, * або /.")