import time

print("Countdown")
sekunden_text = input("Von welcher Zahl soll runtergezaehlt werden? (1-20): ").strip()

if not sekunden_text.isdigit():
    print("Bitte eine Zahl eingeben.")
else:
    sekunden = int(sekunden_text)
    if sekunden < 1 or sekunden > 20:
        print("Bitte eine Zahl zwischen 1 und 20 waehlen.")
    else:
        for i in range(sekunden, 0, -1):
            print(i)
            time.sleep(1)
        print("Fertig!")
