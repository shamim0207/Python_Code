marks=[89,85,93,100,75,79,69]

print(marks)
print(len(marks))
#update value of list
marks[3]=84
print(F"updated list is {marks}")
#slicing
print(marks[2:5])
#reverse slicing
print(("reverse marks: "),marks[-4:-1])


#append=add a new value in list
marks.append(72)
print(f"after added a new value {marks}")

#insert=add a new value in list with indexing
marks.insert(4,60)
print(f"after added a new value with indexing {marks}")

#reverse the list
print(f"before reverse the list: {marks}")
marks.reverse()
print(f"after reverse the list: {marks}")

#sorting in ascending order
marks.sort()
print(f"ascending order sorting: {marks}")


#sorting in descending order
marks.sort(reverse=True)
print(f"descending order sorting: {marks}")
