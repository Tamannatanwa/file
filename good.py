a=open("good.txt","r")
b=a.read()
i=0
count=0
while i<len(b):
    # if b[i]=="i" or b[i]=="n" or b[i]=="g":
    if "ing" in b:
        count+=1
    i=i+1
print(count)
print(b)
a.close()
        