# f=open("RAM.txt","r")
f=open("delhi2.txt","r")
f.seek(5)
print(f.tell())
print(f.readlines())
f.close()



# f=open("RAM.txt","r")
# a=f.read()
# print(f.tell())