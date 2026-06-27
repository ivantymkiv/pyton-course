def format_time(seconds: int) -> str:
    # Перевірка діапазону
    if seconds < 0 or seconds >= 8640000:
        return "Число поза допустимим діапазоном!"

    # Визначаємо кількість днів, годин, хвилин і секунд
    days, remainder = divmod(seconds, 24 * 60 * 60)
    hours, remainder = divmod(remainder, 60 * 60)
    minutes, secs = divmod(remainder, 60)

    # Правильна форма слова "день"
    if days == 1:
        day_word = "день"
    elif 2 <= days <= 4:
        day_word = "дні"
    else:
        day_word = "днів"

    # Формуємо рядок з ведучими нулями для годин, хвилин і секунд
    time_str = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(secs).zfill(2)}"

    return f"{days} {day_word}, {time_str}"


# Приклади використання:
print(format_time(250000))
print(format_time(90000))
print(format_time(835661))
print(format_time(272))
