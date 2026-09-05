# Write a program that takes a year as input and determines if it is a leap year.

year=int(input("Enter your year: "))

if((year%4==0 and year%100!=0) or (year%400==0)):
    print(f"{year} is a leap year")
    
else:
    print(f"{year} this year is not leap year.")