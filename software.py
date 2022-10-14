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
print("this is longest words:",max)





