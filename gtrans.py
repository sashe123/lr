from google_translation import TransLate, LangDetect, LanguageList

print(TransLate("Привіт", "uk", "fr"))
print(LangDetect("Привіт"))
print(LanguageList("file", "Привіт"))