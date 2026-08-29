# Iterate through the first 10 numbers (0–9). In each iteration, print the current number, the previous number, and their sum.

current_number=0
previous_number=0
sum=0

for i in range(0,10):
    sum=current_number+previous_number
    print("current number: ",current_number,"previous number: ",previous_number,"sum: ",sum)
    previous_number=current_number
    current_number+=1