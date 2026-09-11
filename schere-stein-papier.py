import random

print("Schere, Stein, Papier!")
print("Waehle: schere, stein oder papier")

moeglichkeiten = ["schere", "stein", "papier"]
spieler = input("Deine Wahl: ").strip().lower()

if spieler not in moeglichkeiten:
    print("Das kenne ich nicht. Bitte schere, stein oder papier eingeben.")
else:
    computer = random.choice(moeglichkeiten)
    print("Computer waehlt:", computer)

    if spieler == computer:
        print("Unentschieden!")
    elif (
        (spieler == "stein" and computer == "schere")
        or (spieler == "schere" and computer == "papier")
        or (spieler == "papier" and computer == "stein")
    ):
        print("Du gewinnst!")
    else:
        print("Der Computer gewinnt!")
