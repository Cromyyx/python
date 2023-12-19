import random


amount = int(input("Amount of Cycles "))
one = 0
two = 0
three = 0
four = 0
five = 0


for i in range(amount):
    number = random.randint(1, 5)
    if number == 1:
        one = one + 1
    elif number == 2:
        two = two + 1
    elif number == 3:
        three = three + 1
    elif number == 4:
        four = four + 1
    else:
        five = five + 1

medialwert = amount / 5
percentage_one = abs(one - medialwert)
percentage_two = abs(two - medialwert)
percentage_three = abs(three - medialwert)
percentage_four = abs(four - medialwert)
percentage_five = abs(five - medialwert)

percentage = percentage_one + percentage_two + percentage_three + percentage_four + percentage_five
answer = percentage / 5
print("one:", one)
print("two", two)
print("three", three)
print("four", four)
print("five", five)

answer_ver = answer / amount
print("Standart abweichung", answer)
print("Standart Abweichung im Verhältnis", answer_ver)
