a=open("vowel","w+")
b=a.write("i love mummydaddy")
count=0
c=0
for i in "i love mummydaddy":
    if i in "aioue":
        count+=1
    else:
        c+=1
print(count,c)
a.close()
