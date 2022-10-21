def fibo(n):
    a = 0
    b = 1
    print(a)
    print(b)
    while (a+b) < n:
        t = a+b
        print(t)
        a = b
        b = t

fibo(25)