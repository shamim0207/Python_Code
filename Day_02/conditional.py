color = input("Enter your color: ").lower().strip()

if color == "red":
    print("Stop your car.")
elif color == "yellow":
    print("Waiting.....")
elif color == "green":
    print("You can go now..")
else:
    print("You entered a wrong color.")