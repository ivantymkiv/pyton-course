def calculator():
    while True:
        try:
            # Запитуємо вираз у користувача
            expr = input("Введіть вираз (наприклад 2+3*4): ")
            result = eval(expr)
            print("Результат:", result)
        except Exception as e:
            print("Помилка:", e)

        # Запитуємо, чи продовжувати
        cont = input("Продовжити? (y/yes для продовження): ").strip().lower()
        if cont not in ("y", "yes"):
            print("Роботу завершено.")
            break


# Запуск калькулятора
calculator()

