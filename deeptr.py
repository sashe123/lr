from deep_translation import TransLate, LangDetect, LanguageList

print(TransLate("Привіт", "uk", "fr"))
print(LangDetect("Привіт"))
print(LanguageList("screen", "Привіт"))