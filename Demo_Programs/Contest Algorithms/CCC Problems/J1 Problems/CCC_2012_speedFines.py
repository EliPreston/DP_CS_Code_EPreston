

speedLimit = int(input("Enter the speed limit:"))

recordedSpeed = int(input("Enter the recorded speed or the car:"))


difference = recordedSpeed - speedLimit

if difference <= 0:
    print("Congratulations, you are within the speed limit!")
elif 1 <= difference <= 20:
    print("You are speeding and your fine is $100")
elif 21 <= difference <= 30:
    print("You are speeding and your fine is $270")
elif difference >= 31:
    print("You are speeding and your fine is $500")
