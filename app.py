import jamspell
import string

# Input a string from the user
userStringActual = input("Enter a string: ")
userString = userStringActual.translate(str.maketrans('', '', string.punctuation)).split(" ")

errors = []

corrector = jamspell.TSpellCorrector()
corrector.LoadLangModel('en.bin')

corrected = corrector.FixFragment(userStringActual)
print(corrected)
corrected = corrected.translate(str.maketrans('', '', string.punctuation)).split(" ")

for i in range(len(userString)):
    candidates = corrector.GetCandidates(userString, i)
    if corrected[i] in candidates and corrected[i] != userString[i]:
        errors.append({
            "position": i,
            "word": userString[i],
            "candidates": candidates,
        })

print(errors)