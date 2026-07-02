def correct_sentence(text: str) -> str:
    # Перша літера завжди велика
    corrected = text[0].upper() + text[1:]

    # Якщо немає крапки в кінці — додаємо
    if not corrected.endswith('.'):
        corrected += '.'

    return corrected



print(correct_sentence("hello ivan"))