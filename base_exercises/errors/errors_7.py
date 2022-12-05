def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10 / age

try:
    print(calculate_xfactor(-1))
except ValueError as error:
    print(error) #the message error is the message defined by us in the function