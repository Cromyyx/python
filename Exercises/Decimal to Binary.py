def decimal_to_binary(decimal_num):
    binary_str = format(int(decimal_num), 'b')
    return binary_str


while True:
    decimal = input("Enter a decimal number: ")
    if decimal != "x":
        print(decimal_to_binary(decimal))
    else:
        break
