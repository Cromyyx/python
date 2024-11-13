string = str(input("Enter a string: "))
string_rev = string[::-1]
if string == string_rev:
    print("String is palindrom")
else:
    print("String is not palindrom")
