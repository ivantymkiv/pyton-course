def second_index(text: str, search: str):
    # Знаходимо перше входження
    first = text.find(search)
    if first == -1:
        return None

    # Шукаємо друге входження, починаючи після першого
    second = text.find(search, first + len(search))
    if second == -1:
        return None

    return second


# Перевірка:
print(second_index("sims", "s"))
print(second_index("find the river", "e", ))
print(second_index("abcabc", "abc"))  # 3
print(second_index("Hello, hello","lo"))  # 3

