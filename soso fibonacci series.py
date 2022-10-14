def fibo(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
for n in range(1,11):
    # print(n,":",fibo(n))
    print(fibo(n))

   
