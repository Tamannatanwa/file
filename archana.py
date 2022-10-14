# a=input("enter the elenment..")
# b=open("arech.txt","a")
# d=b.write("neha-delhi")
# print(d)
# b.close()


# file=open("archana.txt")
# c=0
# for i in file:
#     c=c+len(i)
#     # c=c+1
# print(c)



file=open("archana.txt","r")
data=file.read()
number=data.split()
c=0
i=0
while i<len(number):
    if number[i] in number:
        c=c+1
    i=i+1
print(c)
file.close()

