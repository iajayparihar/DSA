def fibo(num):
    # base condition 
    if num<=1:
        return num
    # function call for n-1
    a=fibo(num-1)
    #function call for n-2
    b=fibo(num-2)
    return a+b

print(fibo(3))