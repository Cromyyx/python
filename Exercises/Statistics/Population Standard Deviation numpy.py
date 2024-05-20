import numpy as np
import random


def random_list_generator_100():
    random_numbers = []
    for i in range(0, 10):  # 10 times
        random_numbers.append(random.randint(1, 100))
    return random_numbers


def p_std_average(amount_of_times):
    list_of_std = []
    for k in range(0, amount_of_times):
        list_of_std.append(np.std(random_list_generator_100(), ddof=0))
    return np.mean(list_of_std)


# calculate population standard deviation with numpy
population_standard_deviation_average = p_std_average(100)
# 0 = no freedom = population
print("population_standard_deviation_average of 1-100 for 100 times",
      population_standard_deviation_average)
