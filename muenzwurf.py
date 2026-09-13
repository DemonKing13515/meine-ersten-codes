# Muenzenwurf-Simulator
# Wirf eine Muenze so oft du willst und sieh, wie oft Kopf oder Zahl kommt.

import random

print("Muenzenwurf")

while True:
    eingabe = input("Wie oft werfen? (Zahl, oder q zum Beenden): ").strip().lower()
    if eingabe in ("q", "quit", "ende"):
        print("Tschuess!")
        break
    if not eingabe.isdigit() or int(eingabe) < 1:
        print("Bitte eine positive Zahl eingeben.")
        continue

    anzahl = int(eingabe)
    if anzahl > 10000:
        print("Maximal 10000 Wuerfe auf einmal.")
        continue

    kopf = 0
    zahl = 0
    for _ in range(anzahl):
        if random.choice(["Kopf", "Zahl"]) == "Kopf":
            kopf += 1
        else:
            zahl += 1

    print(f"Kopf: {kopf}")
    print(f"Zahl: {zahl}")
    print(f"Kopf in Prozent: {kopf / anzahl * 100:.1f}%")
    print()
