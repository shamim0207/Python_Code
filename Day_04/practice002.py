# Given a list of integers compute the average of all numbers in the list.
nums=[10,5,7,9,15,41,43,45]
nums_len=len(nums)
sum=0
for val in nums:
    sum+=val
    
print(f"average={sum/nums_len}")