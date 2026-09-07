list_a = [10, 10, 15, 21, 12, 65, 45, 78, 95, 74, 12]


first_val = list_a[0]
min_val = first_val
max_val = first_val

for i in list_a:
    if i < min_val:
        min_val = i
    if i > max_val:
        max_val = i

print(f"minimum value is: {min_val}")
print(f"maximum value is: {max_val}")