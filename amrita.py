# a=open("amrita.txt","r")
# b=a.read()
# c=0
# count=0
# for i in b:
#     if i=="A" or i=="a":
#         c+=1
#     elif i=="M" or i=="m":
#         count+=1
# print("A or a",c)
# print("M or m",count)
# print(b)
# a.close()



a=open("amrita.txt","r")
b=a.read()
c=0
count=0
i=0
while i<len(b):
    if b[i]=="A" or b[i]=="a":
        c+=1
    elif b[i]=="M" or b[i]=="m":
        count+=1
    i=i+1
print("A or a",c)
print("M or m",count)
print(b)
a.close()