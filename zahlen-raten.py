# Zahlenraten
# Der Computer denkt sich eine Zahl zwischen 1 und 20 aus.
# Du versuchst, sie zu erraten. Nach jedem Tipp sagt das Programm,
# ob deine Zahl zu klein oder zu groß war.

import random

geheimzahl = random.randint(1, 20)
versuche = 0

print("Ich habe mir eine Zahl zwischen 1 und 20 ausgedacht.")
print("Kannst du sie erraten?")

while True:
    tipp_text = input("Dein Tipp: ")

    # Pruefen, ob wirklich eine Zahl eingegeben wurde
    if not tipp_text.isdigit():
        print("Bitte gib eine ganze Zahl ein.")
        continue

    tipp = int(tipp_text)
    versuche += 1

    if tipp < geheimzahl:
        print("Zu klein!")
    elif tipp > geheimzahl:
        print("Zu groß!")
    else:
        print(f"Richtig! Die Zahl war {geheimzahl}.")
        print(f"Du hast {versuche} Versuch(e) gebraucht.")
        break
