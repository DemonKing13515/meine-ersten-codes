import random
import string

print("Einfacher Passwort-Generator")

laenge_text = input("Wie lang soll das Passwort sein? (z.B. 8): ").strip()

if not laenge_text.isdigit():
    print("Bitte eine Zahl eingeben.")
else:
    laenge = int(laenge_text)
    if laenge < 4 or laenge > 20:
        print("Bitte eine Laenge zwischen 4 und 20 waehlen.")
    else:
        zeichen = string.ascii_letters + string.digits
        passwort = "".join(random.choice(zeichen) for _ in range(laenge))
        print("Dein Passwort:", passwort)
