successful = False

for number in range(3):
    print("Attempt", number + 1)
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")