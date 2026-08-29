age = int(input("Enter your age: "))

if age < 13:
    print("You are a baby.")
elif 13 <= age <= 18:
    print("Teenager.")
else:
    print("Adult.")