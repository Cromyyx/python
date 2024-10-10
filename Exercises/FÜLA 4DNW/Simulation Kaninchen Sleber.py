months = 12
females = 3
females_delayed = 0
males = 1
for i in range(months):
    if i % 5 == 0:
        if females_delayed == 0:
            females_delayed = females * 3
        else:
            females = females_delayed + females
    else:
        females = females * 3
print(females)
