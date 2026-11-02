squares=[]

for i in range(6):
    squares.append(i*i)
    
print(squares)


sq=[i*i for i in range(6)]
print(sq)


sq=[i*i for i in range(10) if i%2!=0]
print(sq)


nums = [-1, -2, -3, -4, 2, 4, 5, 6, 7, -5, 9, 10, 15, -5]

list=[0 if val<0 else val for val in nums]
print(list)