secret_number = 9
guess_count =0
guess_limit = 3

while guess_count < guess_limit: 
    number= int(input("Guess: "))
    guess_count +=1
    if number == secret_number:
        print("You won!")
        break
else: 
    print("Sorry you failed!")
