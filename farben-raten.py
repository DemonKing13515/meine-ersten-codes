# Farben raten
# Der Computer denkt sich eine Farbe aus. Du rätst, bis du sie findest.
# Du lernst: Listen, Zufall und eine while-Schleife.

import random

# Eine kleine Liste mit freundlichen Farben
farben = ["rot", "blau", "gruen", "gelb", "lila", "orange"]

geheim = random.choice(farben)
versuche = 0

print("Ich denke an eine Farbe.")
print("Moeglichkeiten:", ", ".join(farben))

while True:
    tipp = input("Deine Farbe: ").strip().lower()
    versuche += 1

    if tipp == geheim:
        print("Richtig! Es war", geheim + ".")
        print("Du hast", versuche, "Versuch(e) gebraucht.")
        break
    elif tipp not in farben:
        print("Diese Farbe steht nicht auf der Liste. Versuch es nochmal.")
    else:
        print("Leider nicht. Rate weiter!")
