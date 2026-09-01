# Ask the user for a string and check whether it is a palindrome or not.
word=input("Enter your word:")

if(word==word[::-1]):
    print("yes")
else:
    print("not")