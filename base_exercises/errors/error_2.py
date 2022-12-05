try: 
    numbers = [1, 2]
    print(numbers[3])
except IndexError as ex:
    print("The list is smaller, select a lower index")
    print(ex)
    print(type(ex))
else:
    #code if we haven't got exceptions
    print("No exceptions were thrown")
print("Execution continues") 
