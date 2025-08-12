# ------ Exercise 1
# True
# True
# False
# False
# True
# False
# x is True
# y is False
# a: 5
# b: 10

# ------ Exercise 2
phrase_plus_longue = ""  

while True:
    phrase = input("Entrez la phrase la plus longue sans la lettre 'A' : ")
    if "a" in phrase.lower():
        print("La phrase contient la lettre 'A', réessayez.")
        continue

    if len(phrase) > len(phrase_plus_longue):
        phrase_plus_longue = phrase
        print(f"Vous avez saisi la phrase la plus longue jusqu'à présent ({len(phrase)} caractères).")
    else:
        print("cette phrase n'est pas plus longue que la précédente.")
