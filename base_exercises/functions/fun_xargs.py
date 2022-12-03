def multiply(*numbers): #passing a variable number of arguments
    total = 1
    for number in numbers:
        total *= number
    return total


print("Start")
result = multiply(2, 3, 4, 5)
print(result)