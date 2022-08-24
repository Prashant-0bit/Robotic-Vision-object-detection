numbers = [3, 10, 87, 25, 14, 64]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)


#list method


numbers = [3, 2, 5, 8, 2, 6, 5, 2, 3]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

