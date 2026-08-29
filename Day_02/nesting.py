username=input("Enter your username:")
password=input("Enter your password:")

if (username=="admin" and password=="1234"):
    print("Log in sucessfull")

else:
    if(username!="admin"):
        print("wrong username")
        
    elif(password!="1234"):
        print("wrong password")  
