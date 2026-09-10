"""Zaehlt Woerter und Buchstaben in einem Satz."""

print("=== Wort- und Buchstabenzaehler ===")
text = input("Schreib einen Satz: ").strip()

woerter = [wort for wort in text.split() if wort]
buchstaben = [zeichen for zeichen in text if zeichen.isalpha()]

print(f"Woerter: {len(woerter)}")
print(f"Buchstaben: {len(buchstaben)}")
print(f"Zeichen insgesamt: {len(text)}")
