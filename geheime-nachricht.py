"""Verschluesselt und entschluesselt eine Nachricht mit der Caesar-Verschiebung."""

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def verschieben(text, schritte):
    ergebnis = ""
    for zeichen in text:
        klein = zeichen.lower()
        if klein in ALPHABET:
            index = ALPHABET.index(klein)
            neu = ALPHABET[(index + schritte) % len(ALPHABET)]
            ergebnis += neu.upper() if zeichen.isupper() else neu
        else:
            ergebnis += zeichen
    return ergebnis


print("=== Geheime Nachricht ===")
print("1 = verschluesseln")
print("2 = entschluesseln")
wahl = input("Was moechtest du tun? ").strip()

text = input("Deine Nachricht: ")
try:
    schritte = int(input("Verschiebung (z. B. 3): "))
except ValueError:
    print("Bitte eine ganze Zahl eingeben.")
    raise SystemExit(1)

if wahl == "2":
    schritte = -schritte

print("Ergebnis:", verschieben(text, schritte))
