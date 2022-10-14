a=open("RAM.txt","r")
b=a.read()
c=b.split()
i=0
while i<len(c):
    if i==3:
        print(c[i])
    i=i+1
a.close()