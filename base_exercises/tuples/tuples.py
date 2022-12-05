numbers = (1, 2, 3)
#numbers[0] = 10 #tuples can't be changed
#print(numbers[0])

point1 = 1, #whitout , the class of point would be int
point2 = ()
print(type(point1))
print(type(point2))

result1 = (1, 2) + (3, 4)
print(result1)
x, y, z, v = result1

result2 = (1, 2) * 3
print(result2)
print(result2[0:3])

tuple_conversion = tuple([1, 2])
print(tuple_conversion)