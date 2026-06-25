import random
def create_lists():
    # 1. Створюємо список випадкової довжини від 3 до 10
    length = random.randint(3, 10)
    lst = [random.randint(1, 10) for _ in range(length)]

    # 2. Формуємо новий список із трьох елементів:
    #    - перший
    #    - третій
    #    - другий з кінця
    new_lst = [lst[0], lst[2], lst[-2]]

    return lst, new_lst


# Приклад використання:
original, final = create_lists()
print("Початковий список:", original)
print("Фінальний список:", final)
