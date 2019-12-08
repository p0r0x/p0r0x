# Die ganzen leeren print Befehle dienen nur um Platz zu schaffen in der Ausgabe.
# Das kann ganz sicher optimiert werden, nur weiß ich nicht wie xD
import time # Dazu da, um den sleep Timer zu enablen
from random import randint
print("Das ist eine Testversion!")
print(" ")
print(" ")
print("Es müssen drei Zahlen erraten werden!")
print(" ")

# Zufallsgeneration einer einstelligen Zahl

z1 = randint(0,9)
z2 = randint(0,9)
z3 = randint(0,9)

# Dauerschleife für wiederholte Abfrage:

bed = True
while bed:

    print(" ")
    var1 = int(input("1. Zahl zwischen 0 - 9: "))
    var2 = int(input("2. Zahl zwischen 0 - 9: "))
    var3 = int(input("3. Zahl zwischen 0 - 9: "))
    print(" ")

# Prüfung jeder einzelnen Variable auf Größe etc.

    if var1 == z1:
        print("Zahl 1 ist richtig!")
    elif var1 > z1:
        print("Zahl 1 zu groß!")
    elif var1 < z1:
        print("Zahl 1 zu klein!")
    if var2 == z2:
        print("Zahl 2 ist richtig!")
    elif var2 > z2:
        print("Zahl 2 zu groß!")
    elif var2 < z2:
        print("Zahl 2 zu klein!")
    if var3 == z3:
        print("Zahl 3 ist richtig!")
    elif var3 > z3:
        print("Zahl 3 zu groß!")
    elif var3 < z3:
        print("Zahl 3 zu klein!")

    if var1 > 9 or var2 > 9 or var3 > 9:
        print("Zahl zu groß! Bitte immer nur eine einstellige Zahl eingeben!")
    if var1 == z1 and var2 == z2 and var3 == z3:
        bed = False

print(" ")
print("Der richtige Code war",z1,",",z2,",",z3)
print(" ")
print("Danke fürs spielen!")
time.sleep(5)
print(" ")
print("Code by Julian aka p0r0x ")
time.sleep(10)