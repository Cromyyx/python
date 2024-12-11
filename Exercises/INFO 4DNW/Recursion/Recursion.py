def recursion_count_to_10(x):
  if x < 10:
    print(x)
    return recursion_count_to_10(x+1)
  else:
    return 10


print(recursion_count_to_10(int(input("Enter a number: "))))
