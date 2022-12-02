started = False

while True:
    command = input(">").lower()
    if command== 'help':
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif command == 'start':
        if started:
            print("Car is alredy started!")
        else:
            started = True
            print("Car started... Ready to go!")
    elif command == 'stop':
        if not started:
            print("Car is alredy stopped!")
        else:
            print("Car stopped")
            started = False
    elif command == 'quit':
        break
    else:
        print("Sorry, I don't understand that...")