n=int(input("N:"))
assert n>=0 and n ==int(n)
def PowOfTwo(n):
    if n==0:
        return 1
    else:
        power=PowOfTwo(n-1)
        return power*2


print(PowOfTwo(n))