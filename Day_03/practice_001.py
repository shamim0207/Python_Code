# Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.

def calculate_product_or_sum(num1, num2):
    product_of_numbers = num1 * num2
    sum_of_numbers=(num1+num2)
    if(product_of_numbers<=1000):
     return product_of_numbers
    else:
        return sum_of_numbers
        
    
    
result=calculate_product_or_sum(40,30)
print(result)
