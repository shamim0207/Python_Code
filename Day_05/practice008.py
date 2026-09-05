# Practice Problem: Create a new list from two given lists such that the new list contains odd numbers from the first list and even numbers from the second list.

list1=[11,12,18,21,23,25,32,33,36,50,55,60]
list2=[9,45,26,41,45,47,48,41,42,46,32,25,645,12,32,65,42,51,58,96,99,86,75]
new_list=[]

for val in list1:
    if(val%2!=0):
        new_list.append(val)

print(f"odd number from {list1}")

for val in list2:
    if(val%2==0):
            new_list.append(val)

print(f"new list after add odd and even number from list1 & list2: {new_list}")