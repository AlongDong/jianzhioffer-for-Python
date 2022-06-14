
def Fibonacci_1(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return Fibonacci_1(n-1)+Fibonacci_1(n-2)

def Fibonacci_2(n):
    result=[0,1]
    if n<2:
        return result[n]
    fibzero=0
    fibone=1
    fibN=0
    for i in range(2,n+1):
        fibN=fibzero+fibone
        fibzero=fibone
        fibone=fibN
    return fibN

a=Fibonacci_2(10)
print(a)