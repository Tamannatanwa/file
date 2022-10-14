# a=open("people2.txt","r")
# for i in a:
#     if "delhi" in i:
#         f=open("delhi2.txt","a")
#         f.write(i)
#         f.close()
#     elif "shimla" in i:
#         f=open("shimla2.txt","a")
#         f.write(i)
#         f.close()
#     else:
#         f=open("other","a")
#         f.write(i)
#         f.close()
# print("successfully!!!!")




a=open("people2.txt","r")
for i in a:
    if "delhi" in i:
        f=open("delhi2.txt","a")
        f.write(i)
        f.close()
    elif "shimla" in i:
        f=open("shimla2.txt","a")
        f.write(i)
        f.close()
    else:
        f=open("other2","a")
        f.write(i)
        f.close()
print("successfully!!!!")

    

6