import statistics

numbers = [3, 3, 1, 2, 2, 4, 5, 2, 2, 4, 6, 4, 5, 3, 1, 5, 1, 4, 6, 1, 4, 3, 6,
           5, 2, 2, 6, 6, 3, 2, 2, 5, 3, 5, 2, 3, 5, 6, 2, 3, 6, 3, 4, 1, 6, 2, 6, 2, 4, 2]

varianz = statistics.variance(numbers)
print(varianz)

stdev = statistics.stdev(numbers)
print(stdev)
