import statistics
list_numbers_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def binary_search(list_numbers, value):
    low = 0
    high = len(list_numbers) - 1

    while low <= high:
        mid = (low + high) // 2
        if list_numbers[mid] == value:
            return mid
        elif list_numbers[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Value not found

index_binary = binary_search(list_numbers_, 7)
if index_binary != -1:
    print(f'Binary: Value found at index {index_binary}')
else:
    print('Binary: Value not found')


def linear_search(list_numbers, value):
    for k in range(len(list_numbers)-1):
        if list_numbers[k] == value:
            return k
        else:
            pass


index_linear = linear_search(list_numbers_, 7)
print(f'Linear: Value found at index {index_linear}')

x = statistics.mean([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(x)
