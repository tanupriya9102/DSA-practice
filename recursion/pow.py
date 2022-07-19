# using inbuilt function: print(pow(4,3))
# using recursion
def pon(x,n):
    assert n>=0 and n==int(n)
    if n==1:
        return x
    if n==0:
        return 1
    else:
        return x*pon(x,n-1)

print(pon(3,1))