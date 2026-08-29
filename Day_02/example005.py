# Design a program to continuously input a number from user & print if it is
# positive or negative until the user enters “Quit”.

while True:
    number=input("enter your number: ")
    if(number=="Quit"):
        
        break
    else:
        print("your number is: ",number)
    