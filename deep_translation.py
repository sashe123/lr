from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory
from deep_translator.constants import GOOGLE_LANGUAGES_TO_CODES

GOOGLE_CODES_TO_LANGUAGES = {code: lang for lang, code in GOOGLE_LANGUAGES_TO_CODES.items()}

DetectorFactory.seed = 0

def TransLate(text: str, src: str, dest: str) -> str:
    try:
        translator = GoogleTranslator(source=src, target=dest)
        return translator.translate(text)
    except Exception as e:
        return f"Error: {str(e)}"

def LangDetect(text: str, set: str = "all") -> str:
    try:
        lang = detect(text)
        if set == "lang":
            return lang
        elif set == "confidence":
            return "Confidence not available in langdetect"
        else:
            return f"Language: {lang}"
    except Exception as e:
        return f"Error: {str(e)}"

def CodeLang(lang: str) -> str:
    if lang in GOOGLE_LANGUAGES_TO_CODES:
        return GOOGLE_LANGUAGES_TO_CODES[lang]
    elif lang in GOOGLE_CODES_TO_LANGUAGES:
        return GOOGLE_CODES_TO_LANGUAGES[lang]
    else:
        return f"Error: Invalid language or code '{lang}'"

def LanguageList(out: str = "screen", text: str = "") -> str:
    languages = GOOGLE_LANGUAGES_TO_CODES
    
    if out == "screen":
        print(f"{'N':<3} {'Language':<20} {'ISO-639 code':<10} {'Text':<30}")
        print("-" * 65)
        for i, (lang_name, lang_code) in enumerate(languages.items(), 1):
            translated_text = TransLate(text, "auto", lang_code) if text else ""
            print(f"{i:<3} {lang_name.capitalize():<20} {lang_code:<10} {translated_text:<30}")
        return "Ok"
    
    elif out == "file":
        try:
            with open("language_list.txt", "w") as file:
                file.write(f"{'N':<3} {'Language':<20} {'ISO-639 code':<10} {'Text':<30}\n")
                file.write("-" * 65 + "\n")
                for i, (lang_name, lang_code) in enumerate(languages.items(), 1):
                    translated_text = TransLate(text, "auto", lang_code) if text else ""
                    file.write(f"{i:<3} {lang_name.capitalize():<20} {lang_code:<10} {translated_text:<30}\n")
            return "Ok"
        except Exception as e:
            return f"Error: {str(e)}"