# Write a function to return the count the number of digits in a number,N.

def sum_of_num(number):
    sum=0
    for ch in str((number)):
        sum+=int(ch)
    return sum


digit_of_sum=sum_of_num(145785632)
print(digit_of_sum)