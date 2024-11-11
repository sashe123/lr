import re

def read_first_sentence(filename):
    """Зчитує перше речення з файлу та повертає його."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            sentences = re.split(r'[.!?]', text)
            first_sentence = sentences[0].strip()
            return first_sentence
    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
        return None
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return None

def sort_words(text):
    """Сортує слова в алфавітному порядку та повертає окремо українські та англійські слова."""
    words = re.findall(r'\b\w+\b', text.lower())  # Знаходимо всі слова, ігноруючи пунктуацію
    ukrainian_words = sorted([word for word in words if re.match(r'[а-яА-ЯїЇєЄіІґҐ]', word)])
    english_words = sorted([word for word in words if re.match(r'[a-zA-Z]', word)])
    return ukrainian_words, english_words

def main():
    filename = 'text.txt'
    first_sentence = read_first_sentence(filename)
    
    if first_sentence:
        print("Перше речення:", first_sentence)
        
        ukrainian_words, english_words = sort_words(first_sentence)
        all_sorted_words = ukrainian_words + english_words
        
        print("\nСлова відсортовані по алфавіту (спочатку українські, потім англійські):")
        print(all_sorted_words)
        
        print("\nЗагальна кількість слів:", len(all_sorted_words))

if __name__ == "__main__":
    main()
