numbers = [1, 2, 3]
print(numbers)
print(*numbers)

#values=list(range(5)) 
values = [*range(5), *"Hello"]
print(values)
print(*range(5))

first = [1, 2]
second = [3]
combined = [*first, *second]

