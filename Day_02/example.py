salary = float(input("Enter your salary: "))

if salary < 30000:
    tax = salary* 0.05
    print("Tax amount is:", tax)
elif (30000<=salary<=70000 ):
    tax = salary* 0.15
    print("Tax amount is:", tax)
    
else:
    tax = salary* 0.25
    print("Tax amount is:", tax)