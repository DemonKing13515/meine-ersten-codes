# Tic-Tac-Toe fuer zwei Spieler am gleichen Computer

FELD = [" "] * 9


def zeigen():
    print()
    print(f" {FELD[0]} | {FELD[1]} | {FELD[2]} ")
    print("---+---+---")
    print(f" {FELD[3]} | {FELD[4]} | {FELD[5]} ")
    print("---+---+---")
    print(f" {FELD[6]} | {FELD[7]} | {FELD[8]} ")
    print()


def gewonnen(zeichen):
    wege = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6),
    ]
    return any(FELD[a] == FELD[b] == FELD[c] == zeichen for a, b, c in wege)


print("Tic-Tac-Toe")
print("Felder sind 1 bis 9, so angeordnet:")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 ")

spieler = "X"

for zug in range(9):
    zeigen()
    while True:
        wahl = input(f"Spieler {spieler}, Feld 1-9: ").strip()
        if not wahl.isdigit():
            print("Bitte eine Zahl eingeben.")
            continue
        nummer = int(wahl)
        if nummer < 1 or nummer > 9:
            print("Nur 1 bis 9.")
            continue
        if FELD[nummer - 1] != " ":
            print("Feld schon belegt.")
            continue
        FELD[nummer - 1] = spieler
        break

    if gewonnen(spieler):
        zeigen()
        print(f"Spieler {spieler} gewinnt!")
        break

    spieler = "O" if spieler == "X" else "X"
else:
    zeigen()
    print("Unentschieden!")
