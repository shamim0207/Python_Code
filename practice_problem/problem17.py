# Practice Problem: Start with a list of 10 numbers. Iterate through them and sort them into two separate lists: one for even numbers and one for odd numbers.

numbers = [12, 7, 34, 21, 5, 10, 8, 3, 19, 2]
even_list=[]
odd_list=[]
for val in numbers:
    if(val%2==0):
        even_list.append(val)
        
    else:
        odd_list.append(val)
        
print(f"even list is: {even_list}")
print(f"odd list is: {odd_list}")