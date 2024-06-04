import random
import matplotlib.pyplot as plt

x = random.randint(1, 6)
amount = int(input("Number of times: "))

sum_dice = []
for k in range(amount):
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    sum_dice.append(dice_1 + dice_2)


def count_numbers(lst):
    # Initialize a dictionary to store the count of each number
    count_dict = {i: 0 for i in range(2, 13)}

    # Iterate over each number in the list
    for number in lst:
        # If the number is between 1 and 12, increment its count
        if 2 <= number <= 12:
            count_dict[number] += 1

    return count_dict


dict_count_numbers = count_numbers(sum_dice)
print(dict_count_numbers)

plt.bar(*zip(*sorted(dict_count_numbers.items())))
plt.xticks(range(2, 13))
plt.show()
