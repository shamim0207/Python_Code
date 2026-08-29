# . Letʼs create a “NumberGuessingGame”. Given a secret number (already
# decided by you), write a program that asks the user to guess it and prints:

secretNumber=69


while True:
    guessing_number=int(input("enter your number: "))
    
    if(guessing_number == secretNumber):
        print("Correct Guess")
        
    elif(guessing_number<secretNumber):
        print("Too low..")
        
    else:
        print("too high.")

