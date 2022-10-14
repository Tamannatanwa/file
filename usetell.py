# a=open("usetell.txt","w+")
# print(a.tell())
# print(a.readable())
# print(a.tell())
# print(a.writable())
# a.close()



a=open("usetell.txt","r")
print(a.tell())
print(a.readable())
print(a.tell())
print(a.readable())
print(a.seek(1))
a.close()