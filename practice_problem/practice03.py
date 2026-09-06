# Write a function to return True if the first and last number of a given list is the same. If the numbers are different, return False.

def check_first_and_last(list_num):
    print(f"The given list is:{list_num}")
    first_number= list_num[0]
    last_number= list_num[-1]
    
    for  val in list_num:
        if(first_number==last_number):
            return True
        else:
            return False
    
numbers=check_first_and_last([10, 20, 30, 40, 10])
print(numbers)
