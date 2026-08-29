# count the number of 'i' in a string
word="artificial intelligence"
count=0

for ch in word:
    if(ch=='i'):
        count+=1
        
print("The number of i is: ",count)