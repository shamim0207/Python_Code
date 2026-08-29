# print vowel count of a fiven string 

syntax=input("enter your sentence: ")
vowel=0
for ch in syntax:
    if(ch=='a' or ch=='e'or ch=='i'or ch=='o' or ch=='u'):
        vowel+=1
        

print("total number of vowel: ",vowel)        