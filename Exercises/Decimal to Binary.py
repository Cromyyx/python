def decimal_to_binary(decimal_num):
    binary_str = format(int(decimal_num, 10), 'b')
    return binary_str


list_fused = []
while True:
    list_temp = []
    decimal = input("Enter a decimal number: ")
    list_temp.append(decimal)
    if decimal == "x":
        break
    else:
        num_dez = (decimal_to_binary(decimal))
        list_temp.append(num_dez)
        print(num_dez)
        list_fused.append(list_temp)
        print(list_fused)
