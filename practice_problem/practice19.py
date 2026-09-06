# Practice Problem: Print a downward number pattern where each row starts with a decreasing value.
n = int(input("Enter your number: "))

for i in range(n, 0, -1):
   
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()  