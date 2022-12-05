numbers = [1, 2, 3, 4, 4, 4, 5]
#first, second, third = numbers #list unpacking
first, second, *other = numbers
print(first)
print(other)
#first, *other, last = numbers
