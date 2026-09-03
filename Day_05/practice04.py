# Iterate through a given list of numbers and print only those numbers which are divisible by 5.


num=[10,12,30,45,25,31,33,17,8,10,65,89,69,90]
print(f"given list is:{num}")
for val in num:
    if(val%5==0):
        print(val)