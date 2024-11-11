from googletrans import Translator, LANGUAGES

translator = Translator()

def TransLate(text: str, src: str, dest: str) -> str:
    try:
        result = translator.translate(text, src=src, dest=dest)
        return result.text
    except Exception as e:
        return f"Error: {str(e)}"

def LangDetect(text: str, set: str = "all") -> str:
    try:
        result = translator.detect(text)
        if set == "lang":
            return result.lang
        elif set == "confidence":
            return result.confidence
        else:
            return f"Language: {result.lang}, Confidence: {result.confidence}"
    except Exception as e:
        return f"Error: {str(e)}"

def CodeLang(lang: str) -> str:
    lang_lower = lang.lower()
    if lang_lower in LANGUAGES.values():
        for code, name in LANGUAGES.items():
            if name == lang_lower:
                return code
    elif lang_lower in LANGUAGES:
        return LANGUAGES[lang_lower]
    return "Error: Неправильний код або назва мови"

def LanguageList(out: str = "screen", text: str = "") -> str:
    if out == "screen":
        print(f"{'N':<3} {'Language':<20} {'ISO-639 code':<10} {'Text':<30}")
        print("-" * 65)
        for i, (lang_code, lang_name) in enumerate(LANGUAGES.items(), 1):
            translated_text = TransLate(text, "auto", lang_code) if text else ""
            print(f"{i:<3} {lang_name.capitalize():<20} {lang_code:<10} {translated_text:<30}")
        return "Ok"
    
    elif out == "file":
        try:
            with open("language_list.txt", "w") as file:
                file.write(f"{'N':<3} {'Language':<20} {'ISO-639 code':<10} {'Text':<30}\n")
                file.write("-" * 65 + "\n")
                for i, (lang_code, lang_name) in enumerate(LANGUAGES.items(), 1):
                    translated_text = TransLate(text, "auto", lang_code) if text else ""
                    file.write(f"{i:<3} {lang_name.capitalize():<20} {lang_code:<10} {translated_text:<30}\n")
            return "Ok"
        except Exception as e:
            return f"Error: {str(e)}"