import random
import names

my_list = []
for i in range(0, 100):
    my_list.append({"name": names.get_full_name(), "age": random.randint(1, 100)})
print(my_list)
