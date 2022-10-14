a=open("python.txt","r")
b=a.read()
c=b.split()
min=c[0]
i=0
while i<len(c):
    if len(c[i])<len(min):
        min=c[i]
    i=i+1
print(min)
a.close()







file=open("software.txt")
f=file.read()
words=f.split()
print(words)
max=words[0]
i=0
while i<len(words):
    if len(words[i])>len(max):
        max=words[i]
    i=i+1
print("this is longest words=",max)