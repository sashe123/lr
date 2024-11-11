import json
import os
from google_translation import TransLate, LangDetect

def count_sentences(text):
    return text.count('.') + text.count('!') + text.count('?')

with open("config.json", "r") as config_file:
    config = json.load(config_file)

text_file = config["TextFile"]
lang = config["Language"]
output = config["Output"]
min_chars = config["MinChars"]
max_chars = config["MaxChars"]
max_words = config["MaxWords"]
max_sentences = config["MaxSentences"]

if not os.path.exists(text_file):
    print(f"Error: Файл {text_file} не знайдено.")
else:
    with open(text_file, "r") as file:
        text = file.read()

    num_chars = len(text)
    num_words = len(text.split())
    num_sentences = count_sentences(text)

    print(f"Назва файлу: {text_file}")
    print(f"Розмір файлу: {num_chars} символів")
    print(f"Кількість символів: {num_chars}")
    print(f"Кількість слів: {num_words}")
    print(f"Кількість речень: {num_sentences}")

    if num_chars < min_chars:
        print(f"Текст занадто короткий. Мінімум потрібно 600 символів, а у файлі лише {num_chars}.")
    else:
        detected_language = LangDetect(text, set="lang")
        if "Error" in detected_language:
            print(f"Помилка в визначенні мови: {detected_language}")
        else:
            print(f"Мова тексту: {detected_language}")

        # Перевіряємо ліміти
        if num_chars > max_chars:
            print(f"Текст перевищує ліміт символів. Максимум дозволено {max_chars}, а у файлі {num_chars}.")
        elif num_words > max_words:
            print(f"Текст перевищує ліміт слів. Максимум дозволено {max_words}, а у файлі {num_words}.")
        elif num_sentences > max_sentences:
            print(f"Текст перевищує ліміт речень. Максимум дозволено {max_sentences}, а у файлі {num_sentences}.")
        else:
            translated_text = TransLate(text, src='auto', dest=lang)

            if output == "file":
                output_file = f"{os.path.splitext(text_file)[0]}_{lang}.txt"
                try:
                    with open(output_file, "w") as out_file:
                        out_file.write(translated_text)
                    print(f"Ok: Переклад збережено у файл {output_file}")
                except Exception as e:
                    print(f"Помилка запису у файл: {str(e)}")
            else:
                try:
                    print(f"Мова перекладу: {lang}")
                    print(f"Перекладений текст:\n{translated_text}")
                except Exception as e:
                    print(f"Помилка виведення на екран: {str(e)}")