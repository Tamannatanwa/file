a=open("aniket.txt","r")
b=a.read()
i=0
c=0
count=0
vowel=0
consonant=0
while i<len(b):
    if b[i].isupper()==True:
        c+=1
    if b[i].islower()==True:
        count+=1
    if b[i] in "aeiouAEIOU":
        vowel+=1
    if b[i] in "bcdfghjklmnpqrstvwxtyzBCDFGHJKLMNPQRSTVWXYZ":
        consonant+=1
    i=i+1
print(c)
print(count)
print(vowel)
print(consonant)
a.close()