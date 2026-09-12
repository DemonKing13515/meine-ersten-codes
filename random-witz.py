"""Zeigt einen zufaelligen, kindgerechten Witz."""

import random

WITZE = [
    "Warum koennen Geister so schlecht luegen? Weil man durch sie hindurchsieht.",
    "Was macht ein Pirat am Computer? Er drueckt die Enter-Taste.",
    "Warum hat der Mathematiker eine Leiter mitgenommen? Er wollte auf hoehere Potenzen steigen.",
    "Was ist gruen und steht vor der Tuer? Ein Klopfsalat.",
    "Warum nehmen Seerosen nie den Bus? Weil sie Schwimmblaetter haben.",
    "Was sagt ein groesserer Stift zum kleineren? Wachs mal wieder!",
    "Warum ging der Computer zum Arzt? Er hatte einen Virus.",
    "Was ist orange und schwimmt im Meer? Ein Saftboot.",
]

print("=== Witz des Tages ===")
print(random.choice(WITZE))
noch = input("Noch einen? (j/n) ").strip().lower()
while noch == "j":
    print(random.choice(WITZE))
    noch = input("Noch einen? (j/n) ").strip().lower()
print("Bis bald!")
