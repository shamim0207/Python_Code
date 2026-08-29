# Write a function to return the count the number of digits in a number,n.

def num_count(number):
   
    return len(str(abs(number)))

total_number = num_count(102456325)
print(total_number)  