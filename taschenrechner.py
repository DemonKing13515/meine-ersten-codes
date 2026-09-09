# Einfacher Taschenrechner

print("Einfacher Taschenrechner")
print("Rechenarten: +, -, *, /")

zahl1 = float(input("Erste Zahl: "))
operation = input("Operation (+, -, *, /): ")
zahl2 = float(input("Zweite Zahl: "))

if operation == "+":
    ergebnis = zahl1 + zahl2
elif operation == "-":
    ergebnis = zahl1 - zahl2
elif operation == "*":
    ergebnis = zahl1 * zahl2
elif operation == "/":
    if zahl2 != 0:
        ergebnis = zahl1 / zahl2
    else:
        print("Fehler: Division durch Null ist nicht erlaubt.")
        exit()
else:
    print("Ungültige Operation.")
    exit()

print(f"Ergebnis: {ergebnis}")
