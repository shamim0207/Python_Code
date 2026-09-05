# Practice Problem: Print a downward half-pyramid pattern using stars (*).

for i in range(5,0,-1):
    for j in range(0,i):
        print("*",end=("\t"))

    print("\n")