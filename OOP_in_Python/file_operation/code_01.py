data =True
line=1
with open("sample.txt","r") as f :
    while data:
     data = f.readline()
     if("python" in data):
         print(f"word found in line {line}...")
         break
     print(data)
     line+=1