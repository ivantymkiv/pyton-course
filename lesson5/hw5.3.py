import string


def make_hashtag(text: str) -> str:
    # 1. Видаляємо пунктуацію та пробіли
    clean_text = ''.join(ch if ch not in string.punctuation else ' ' for ch in text)

    # 2. Розділяємо на слова (після заміни пунктуації на пробіли)
    words = clean_text.split()

    # 3. Формуємо хештег: кожне слово з великої літери
    hashtag = '#' + ''.join(word.capitalize() for word in words)

    # 4. Якщо довжина > 140, обрізаємо
    if len(hashtag) > 140:
        hashtag = hashtag[:140]

    return hashtag



print(make_hashtag("hello world!"))
print(make_hashtag("це дуже довгий рядок який може перевищити 140 символів, тому його потрібно обрізатиmmlmlnmnmnjknjnjknkjn.ooooooooooooooooooooooooooooooooooooooooooooooooooooookkkkkkkkkkkkkkkkkkkkkkkkkkkkkka.."))

