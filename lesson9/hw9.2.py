def popular_words(text, words):
    # Переводимо текст у нижній регістр і розбиваємо на слова
    text_words = text.lower().split()

    # Формуємо словник з кількістю входжень кожного слова
    result = {word: text_words.count(word) for word in words}

    return result
print(popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']))
print('OK')
