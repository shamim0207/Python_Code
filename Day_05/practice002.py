#  Write a script that takes a list containing duplicate items and returns a new list with only unique elements.


data=[1,3,10,1,2,30,5,6,7,2,7,8,9,8]
unique_list=list(set(data))
print(f"unique list is:{unique_list}")