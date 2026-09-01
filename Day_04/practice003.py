# Input two lists of integers from the user. Merge them into one list and sort the
#  result.



list1 = list(map(int, input("Enter first list of integers (separated by spaces): ").split()))
list2 = list(map(int, input("Enter second list of integers (separated by spaces): ").split()))

merged_list = list1 + list2


merged_list.sort()


print("Merged and Sorted List:", merged_list)