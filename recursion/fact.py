n=int(input("N:"))
assert n>=0 and n ==int(n)

def fact(n):
    if n<2:
        return 1
    else:
        return (fact(n-1)*(n))


def facc(n):
    p=1
    for i in range(1,n):
        p*=i
        return p

print(facc(n))
