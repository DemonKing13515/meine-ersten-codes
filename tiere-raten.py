# Tiere raten
# Der Computer denkt sich ein Tier aus. Du darfst Fragen stellen, indem du Buchstaben raten kannst.

import random

TIERE = [
    "hund",
    "katze",
    "pferd",
    "fuchs",
    "loewe",
    "panda",
    "fisch",
    "vogel",
    "hase",
    "zebra",
]

geheim = random.choice(TIERE)
geraten = ["_"] * len(geheim)
versuche = 8
schon = set()

print("Tiere raten")
print("Ich denke an ein Tier. Rate Buchstaben!")
print("Laenge:", len(geheim), "Buchstaben")

while versuche > 0 and "_" in geraten:
    print()
    print("Wort:", " ".join(geraten))
    print("Versuche uebrig:", versuche)
    buchstabe = input("Buchstabe: ").strip().lower()

    if len(buchstabe) != 1 or not buchstabe.isalpha():
        print("Bitte genau einen Buchstaben eingeben.")
        continue
    if buchstabe in schon:
        print("Den Buchstaben hattest du schon.")
        continue

    schon.add(buchstabe)
    if buchstabe in geheim:
        for i, z in enumerate(geheim):
            if z == buchstabe:
                geraten[i] = buchstabe
        print("Treffer!")
    else:
        versuche -= 1
        print("Leider nicht.")

print()
if "_" not in geraten:
    print("Super! Das Tier war:", geheim)
else:
    print("Schade. Das Tier war:", geheim)
