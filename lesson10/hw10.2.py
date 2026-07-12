
def first_word(text: str) -> str:
    # Прибираємо зайві пробіли на початку та кінці
    text = text.strip(" .,")
    # Розбиваємо рядок на слова, враховуючи пробіли та розділові знаки
    import re
    words = re.split(r"[ ,.]+", text)
    # Повертаємо перше слово
    return words[0]
print(first_word("Hello world"))
print(first_word("greetings, friends"))
print(first_word("don't touch it"))
print(first_word(".., and so on ..."))
print(first_word("hi"))
print(first_word("Hello.World"))
print('OK')