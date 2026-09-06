# Calculate income tax for a given income based on these rules:

# First $10,000: 0% tax
# Next $10,000: 10% tax
# # Remaining income: 20% tax


salary=int(input("Enter your salary: "))
if(salary>20000):
    first_tax=10000*0
    salary=salary-10000
    next_tax=10000*0.1
    salary=salary-10000
    remaining_salary_tax=salary*0.2
    Total_tax=first_tax+next_tax+remaining_salary_tax
    print(f"Your total tax is:{Total_tax}")
    
elif(10000<salary<=20000):
    first_tax=10000*0
    salary=salary-10000
    next_tax=10000*0.1
    Total_tax=first_tax+next_tax
    print(f"Your total tax is:{Total_tax}")
    
else:
    Total_tax=0
    print(f"Your total tax is:{Total_tax}")
