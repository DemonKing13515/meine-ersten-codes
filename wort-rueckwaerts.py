# Wort rueckwaerts
# Dieses Programm nimmt ein Wort und schreibt es von hinten nach vorne.
# So lernst du, wie man mit Text (Strings) in Python arbeitet.

print("Wort rueckwaerts")
print("Schreibe ein Wort. Ich drehe es um!")
print()

# Wort vom Nutzer einlesen und Leerzeichen am Rand entfernen
wort = input("Dein Wort: ").strip()

# Pruefen, ob wirklich etwas eingegeben wurde
if wort == "":
    print("Du hast nichts eingegeben. Versuche es noch einmal!")
else:
    # [::-1] kehrt den Text um: erstes Zeichen wird letztes
    umgedreht = wort[::-1]
    print()
    print("Vorwaerts: ", wort)
    print("Rueckwaerts:", umgedreht)

    # Extra: Palindrom-Check (Wort ist vorwaerts und rueckwaerts gleich)
    if wort.lower() == umgedreht.lower():
        print("Toll! Das Wort liest sich vorwaerts und rueckwaerts gleich.")
