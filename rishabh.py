

a=[1.5,2.8,3.3]
file=open("rishabh.dat","wb")
for i in a:
    s=i
    bt=s.encode()
    file.write(bt)
