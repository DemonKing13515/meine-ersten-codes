# Einmaleins-Trainer
# Uebt das kleine Einmaleins: Der Computer stellt 5 Aufgaben.
# Du tippst die Antwort. Am Ende siehst du, wie viele richtig waren.

import random  # fuer zufaellige Zahlen

print("=== Einmaleins-Trainer ===")
print("Loese 5 Aufgaben. Tippe nur die Zahl.")
print()

richtig = 0  # Zaehler fuer richtige Antworten

# 5 Aufgaben hintereinander
for nummer in range(1, 6):
    a = random.randint(1, 10)  # erste Zahl von 1 bis 10
    b = random.randint(1, 10)  # zweite Zahl von 1 bis 10
    loesung = a * b

    antwort_text = input("Aufgabe " + str(nummer) + ": Was ist " + str(a) + " x " + str(b) + "? ")

    # Pruefen, ob eine Zahl eingegeben wurde
    if not antwort_text.isdigit():
        print("Bitte eine ganze Zahl eingeben. Die Loesung war", loesung)
        continue

    antwort = int(antwort_text)
    if antwort == loesung:
        print("Richtig!")
        richtig = richtig + 1
    else:
        print("Leider nicht. Die Loesung ist", loesung)

print()
print("Fertig! Du hast", richtig, "von 5 Aufgaben richtig.")
