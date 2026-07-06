import string


def is_palindrome(text: str) -> bool:
    # Переводимо рядок у нижній регістр
    text = text.lower()

    # Видаляємо всі знаки пунктуації та пробіли
    cleaned = "".join(ch for ch in text if ch.isalnum())

    # Перевіряємо, чи рядок однаковий зліва направо і справа наліво
    return cleaned == cleaned[::-1]


# Приклади перевірки:
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")