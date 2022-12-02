weight = float(input('Weight: '))
type = input('(L)bs or (K)g: ')
if type.upper() =='L':
    weight = weight * 0.45
    print(f"Your weight is: {weight} kilos")
elif type.upper() =='K':
    weight = weight / 0.45
    print(f"Your weight is: {weight} lbs")

