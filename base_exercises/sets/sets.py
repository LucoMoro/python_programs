numbers = [1, 1, 2, 3, 4]
first = set(numbers)
first.add(5)
second = {1, 6}

print(first | second)
print(first & second)
print(first - second)
print(first ^ second) #in first or second but not in both
#first[0] can't be used

print(first)