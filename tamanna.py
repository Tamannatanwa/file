# f=open("tamana.txt","r")
# print(f.read())
# print(f,end="")
# f.close



# f=open("tamana.txt","r")
# print(f.readline(2))
# print(f)
# f.close



# f=open("tamana.txt","r")
# data=f.readlines()
# for i in data:
#     print(i,end="")
# f.close()




a=open("tamana.txt",mode="w")
f=["mummy\n","papa\n","dadi\n","bhai\n","bahne\n","me\n"]
a.writelines(f)
a.close()
print("success")
