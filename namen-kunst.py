# Namenskunst
# Gibt deinen Namen gross in Sternchen aus.

print("Namenskunst")
name = input("Dein Name: ").strip()

if not name:
    name = "Freund"

name = name.upper()

print()
print("*" * (len(name) + 4))
print("* " + name + " *")
print("*" * (len(name) + 4))
print()
print("Buchstabe fuer Buchstabe:")
for buchstabe in name:
    print(buchstabe)
