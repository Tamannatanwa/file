a=open("mom.txt","r")
b=a.read()
x=b.split()
co=0
count=0
for i in x:
    if i=="me":
        count+=1
    elif i=="my":
        co+=1
print("me",co)
print("my",count)
a.close()