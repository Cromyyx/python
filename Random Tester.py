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


print("one:", one)
print("two", two)
print("three", three)
print("four", four)
print("five", five)
