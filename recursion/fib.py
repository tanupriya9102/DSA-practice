n=int(input("n="))
def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)

# print("Element at index ",n,"=",fib(n))

# print fibonacci sequence till n

for i in range(n+1):
    print("at ",i,"=",fib(i))