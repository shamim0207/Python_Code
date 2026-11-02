try:
    input=int(input(f"Enter your input: "))
    Ans=10/input
    
except ZeroDivisionError:
    print(f"Devide by 0 is not allowed.")
    
except ValueError:
    print(f"Inavlid input.")
    
    
else:
    print(f"Final ans is: {Ans}")