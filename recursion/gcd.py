# n= int(input("n="))
def gcd(a,b):
    assert a==int(a) and b==int(b)
    if(a<0):#gcd of negative no is same as the positive
        a*=-1
    if(b<0):
        b*=-1
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

print(gcd(4,-6))