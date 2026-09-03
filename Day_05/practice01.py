# Given a list of integers, find and print both the largest and the smallest numbers.


nums = [45, 10, 20, 9, 50, 69, 75, 80, 2]


maximum = nums[0]
minimum = nums[0]

for value in nums:
    if value > maximum:
        maximum = value
    if value < minimum:
        minimum = value

print(f"maximum value is: {maximum}")
print(f"minimum value is: {minimum}")