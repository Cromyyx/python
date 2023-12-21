#Calculates the sum of an amount of dice with an abount of sides.
import random


def dice(amount, sides):
    summ = 0
    for i in range(amount):
        number = random.randint(1, sides)
        print("Würfel nr." + str(i + 1), number)
        summ = summ + number
    return summ


summ = dice(int(input("Anzahl der Würfel ")), int(input("Anzahl der Würfelseiten ")))
print("Summe Zahlen:", summ)
