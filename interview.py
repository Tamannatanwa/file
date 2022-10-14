from asyncore import read


# a=open("mom.py")
# n=a.read(2)
# print(n)
# a.close()


a=open("mom.txt","w+")
n=a.write("tamanna")
c=a.read()
print(c)
a.close()