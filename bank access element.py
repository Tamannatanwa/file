a=open("banks.txt")
b=a.read()
i=0
while i<len(b):
    print(b[i],end="")
    i=i+1
a.close()
