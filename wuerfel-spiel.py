# Würfelspiel
# Ein einfaches Programm für Anfänger:
# Du würfelst eine Zahl von 1 bis 6. Der Computer würfelt auch.
# Wer die höhere Zahl hat, gewinnt die Runde.

import random  # Zufallszahlen für den Würfel

print("Willkommen beim Würfelspiel!")
print("Beide würfeln. Die höhere Zahl gewinnt.")
print()

# Punkte zählen
deine_punkte = 0
computer_punkte = 0

# Drei Runden spielen
for runde in range(1, 4):
    print("--- Runde", runde, "---")
    input("Drücke Enter, um zu würfeln...")

    dein_wurf = random.randint(1, 6)
    computer_wurf = random.randint(1, 6)

    print("Du hast eine", dein_wurf, "gewürfelt.")
    print("Der Computer hat eine", computer_wurf, "gewürfelt.")

    if dein_wurf > computer_wurf:
        print("Du gewinnst diese Runde!")
        deine_punkte = deine_punkte + 1
    elif computer_wurf > dein_wurf:
        print("Der Computer gewinnt diese Runde.")
        computer_punkte = computer_punkte + 1
    else:
        print("Unentschieden!")

    print()

print("=== Endergebnis ===")
print("Deine Punkte:", deine_punkte)
print("Computer-Punkte:", computer_punkte)

if deine_punkte > computer_punkte:
    print("Super, du hast das Spiel gewonnen!")
elif computer_punkte > deine_punkte:
    print("Der Computer hat gewonnen. Nächstes Mal klappt es!")
else:
    print("Es ist unentschieden. Gutes Spiel!")
