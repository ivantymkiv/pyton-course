import string
import keyword


def is_valid_variable(name: str) -> bool:
    # 1. Не може бути порожнім
    if not name:
        return False

    # 2. Не може починатися з цифри
    if name[0].isdigit():
        return False

    # 3. Не може містити великі літери
    if any(ch.isupper() for ch in name):
        return False

    # 4. Не може містити пробіли та пунктуацію, окрім "_"
    for ch in name:
        if ch in string.punctuation and ch != "_":
            return False
        if ch.isspace():
            return False

    # 5. Не може містити "__" підряд
    if "__" in name:
        return False

    # 6. Не може бути зареєстрованим словом
    if name in keyword.kwlist:
        return False

    return True
print(is_valid_variable("some_super_puper_value"))





