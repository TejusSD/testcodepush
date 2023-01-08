
def fib(n):
    a=1
    b=1
    l=[]
    for i in range(n):
        l.append(a)
        a,b=b,a+b
    return l

print(fib(5))