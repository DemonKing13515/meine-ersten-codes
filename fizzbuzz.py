"""Klassisches FizzBuzz: Vielfache von 3 und 5."""

print("=== FizzBuzz ===")
try:
    ende = int(input("Bis welche Zahl? (z. B. 30) "))
except ValueError:
    print("Bitte eine ganze Zahl eingeben.")
    raise SystemExit(1)

if ende < 1:
    print("Bitte eine Zahl groesser als 0 eingeben.")
    raise SystemExit(1)

for zahl in range(1, ende + 1):
    if zahl % 15 == 0:
        print("FizzBuzz")
    elif zahl % 3 == 0:
        print("Fizz")
    elif zahl % 5 == 0:
        print("Buzz")
    else:
        print(zahl)
