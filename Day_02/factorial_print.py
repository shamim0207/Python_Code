def cal_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i;
    return fact
        
factorial=cal_fact(5)
print("factorial value is: ",factorial)