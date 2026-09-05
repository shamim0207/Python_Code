# Write a program to print the first 15 terms of the Fibonacci series. The sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding 

pre_num = 0
cur_num = 1


print(pre_num)
print(cur_num)


for i in range(13):
    next_num = pre_num + cur_num
    print(next_num)
    pre_num, cur_num = cur_num, next_num