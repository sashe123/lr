from googletrans import Translator, LANGUAGES

translator = Translator()

def TransLate(text, lang):
    try:
        translation = translator.translate(text, dest=CodeLang(lang))
        return translation.text
    except Exception as e:
        return f"Помилка при перекладі тексту: {str(e)}"

def LangDetect(text):
    try:
        detection = translator.detect(text)
        return {
            "language": LangName(detection.lang),
            "confidence": detection.confidence
        }
    except Exception as e:
        return f"Помилка в назві або коді мови: {str(e)}"

def CodeLang(lang):
    lang = lang.lower()
    if lang in LANGUAGES:
        return lang
    else:
        for code, name in LANGUAGES.items():
            if name.lower() == lang:
                return code
        return f"Мені невідома ця мова: {lang}"

def LangName(code):
    return LANGUAGES.get(code, f"Мені не видомий код цієї мови: {code}")

def main():
    text = input("Для того, щоб я міг перекласти текст, спочатку напишіть те що Вам потрібно перевести: ")
    
    detected_lang = LangDetect(text)
    print(f"Мова, яка використовувалась: {detected_lang['language']} (впевненість: {detected_lang['confidence']})")
    
    target_lang = input("Введіть мову, на яку потрібно перекласти текст (назва або код мови): ")
    
    translated_text = TransLate(text, target_lang)
    print(f"Переклад: {translated_text}")
    
    lang_info = LangName(CodeLang(target_lang))
    print(f"Інформація про мову: {lang_info}")

if __name__ == "__main__":
    main()