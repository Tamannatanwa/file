count=0
c=0
my_file=open("people1.txt")
for i in my_file:
    count+=1
    c=c+len(i)
print(count)
print(c)
my_file.close()