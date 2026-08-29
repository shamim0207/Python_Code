def hello():
    for i in range(0,16,3):
        print(i)

hello()

def add_numbers(a, b):
    summation = a + b
    return summation


result = add_numbers(20, 30)
print("sum value:", result)