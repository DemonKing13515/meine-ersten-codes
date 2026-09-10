"""Ein kleines Wissens-Quiz."""

fragen = [
    {
        "frage": "Wie viele Planeten hat unser Sonnensystem?",
        "antworten": ["7", "8", "9"],
        "richtig": "8",
    },
    {
        "frage": "Welche Farbe entsteht, wenn man Blau und Gelb mischt?",
        "antworten": ["Gruen", "Lila", "Orange"],
        "richtig": "Gruen",
    },
    {
        "frage": "Wie viele Minuten hat eine Stunde?",
        "antworten": ["30", "60", "100"],
        "richtig": "60",
    },
    {
        "frage": "Welches Tier ist ein Saeugetier?",
        "antworten": ["Hai", "Delfin", "Lachs"],
        "richtig": "Delfin",
    },
    {
        "frage": "Wie nennt man den groessten Ozean der Erde?",
        "antworten": ["Atlantik", "Indischer Ozean", "Pazifik"],
        "richtig": "Pazifik",
    },
]

print("=== Kleines Quiz ===")
print("Tippe die richtige Antwort ein.\n")

punkte = 0

for nummer, eintrag in enumerate(fragen, start=1):
    print(f"Frage {nummer}: {eintrag['frage']}")
    print("Moeglichkeiten:", ", ".join(eintrag["antworten"]))
    antwort = input("Deine Antwort: ").strip()

    if antwort.lower() == eintrag["richtig"].lower():
        print("Richtig!\n")
        punkte += 1
    else:
        print(f"Leider falsch. Richtig waere: {eintrag['richtig']}\n")

print(f"Fertig! Du hast {punkte} von {len(fragen)} Punkten.")
