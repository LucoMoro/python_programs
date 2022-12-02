numbers = [5, 2, 1, 7, 3, 3, 3, 7, 5, 4, 3, 4]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)