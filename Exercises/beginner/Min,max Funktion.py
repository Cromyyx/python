import random

rand_list = []
n = 3
for i in range(n):
	rand_list.append(random.randint(3, 9))
print(rand_list)


def maxi(max_list):
	temp_high = max_list[0]
	for k in range(len(max_list)):
		if max_list[k] > temp_high:
			temp_high = max_list[k]
		else:
			pass
	return "max:", temp_high


def mini(min_list):
	temp_low = min_list[0]
	for k in range(len(min_list)):
		if min_list[k] < temp_low:
			temp_low = min_list[k]
		else:
			pass
	return "min:", temp_low


print(maxi(rand_list))
print(mini(rand_list))
