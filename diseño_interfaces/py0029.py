def fibo(num):
    a = 0
    b = 1
    fibonazi=[]
    for p in range(num):
        fibonazi.append(a)
        b=a+b
        a=b-a
    return fibonazi
print(fibo(8))