a=open("priya.txt","r")
b=a.readlines()
i=0
while i<len(b):
    if i==2:
        pass
    else:
        print(b[i])
    i=i+1
a.close()