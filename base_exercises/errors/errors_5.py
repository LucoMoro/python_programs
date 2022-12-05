try:
    #with can be used only for classes with __exit__  & __enter__ functions
    with open("app.py") as file: #with calls automatically the __exit__ method
        print("File opened")

    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age")
else:
    print("No exceptions were thrown")

