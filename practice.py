import os


# import os
# a=open("practice.txt")
# b=os.remove("practice.txt")


a=open("practice.txt","w+")
c=a.write("\nshe loves our  family more")
b=a.readline()
print(b)
print(c)
a.close()
