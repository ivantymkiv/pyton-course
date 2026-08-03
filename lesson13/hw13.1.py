import re

def clean_html_file(input_file, output_file="cleaned.txt"):
    """
    Читає HTML-файл, видаляє всі теги <...> і записує очищений текст у новий файл.
    За замовчуванням результат зберігається у cleaned.txt.
    """
    # 1. Читаємо вхідний файл
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    # 2. Видаляємо всі HTML-теги
    cleaned_text = re.sub(r"<.*?>", "", content)

    # 3. Прибираємо порожні рядки (додаткове завдання)
    cleaned_lines = [line.strip() for line in cleaned_text.splitlines() if line.strip()]
    cleaned_text = "\n".join(cleaned_lines)

    # 4. Записуємо результат у вихідний файл
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(cleaned_text)

# Виклик функції
clean_html_file("draft.html", "cleaned.txt")
