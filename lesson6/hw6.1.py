import string


def letters_range(user_input: str):
    # Розділяємо рядок на дві літери
    start, end = user_input.split('-')

    # Беремо весь набір літер (латиниця, великі та малі)
    letters = string.ascii_letters

    # Знаходимо індекси початкової та кінцевої літери
    start_index = letters.index(start)
    end_index = letters.index(end)

    # Формуємо підрядок від start до end включно
    return letters[start_index:end_index + 1]


# Приклади використання:
print(letters_range("A-w"))  # abc d → "abcd"
print(letters_range("a-W"))  # xyz → "xyz"
print(letters_range("A-D"))  # ABCD → "ABCD"
print(letters_range("c-h"))  # cdefgh → "cdefgh"
