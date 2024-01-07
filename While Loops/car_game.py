command = ""
car_started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if car_started:
            print("The car already started!")
        else:
            car_started = True
            print("Car Started....")
    elif command == "stop":
        if not car_started:
            print("The car is already stopped!")
        else:
            car_started = False
            print("The car stopped...")
    elif command == "help":
        print("""
start - To start the car
stop - To stop the car
quit - To exit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that....")

