"""Rechnet Temperaturen zwischen Celsius und Fahrenheit um."""

print("=== Temperatur-Umrechner ===")
print("1 = Celsius nach Fahrenheit")
print("2 = Fahrenheit nach Celsius")

wahl = input("Bitte 1 oder 2 waehlen: ").strip()

try:
    wert = float(input("Temperatur eingeben: ").replace(",", "."))
except ValueError:
    print("Das war keine Zahl.")
    raise SystemExit(1)

if wahl == "1":
    fahrenheit = wert * 9 / 5 + 32
    print(f"{wert} Grad Celsius sind {fahrenheit:.1f} Grad Fahrenheit.")
elif wahl == "2":
    celsius = (wert - 32) * 5 / 9
    print(f"{wert} Grad Fahrenheit sind {celsius:.1f} Grad Celsius.")
else:
    print("Unbekannte Auswahl.")
