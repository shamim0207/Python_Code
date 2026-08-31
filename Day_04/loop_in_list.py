numbers=[10,14,5,71,25,35,11,13,45]
for val in numbers:
    print(val)


# index printing
x=25
index=0
for val in numbers:
    if(val==x):
        print(f"{x} finding in index {index}")
        break
    index+=1    