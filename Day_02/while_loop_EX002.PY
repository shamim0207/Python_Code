#PRINT multiplication table for any number

n = int(input("enter your number: "))
i = 1

while i <= 10:
    multiplication = n * i
    print(n, "*", i, "=", multiplication)
    i += 1