def sod(n):
    assert n>=0
    if n==0:
        return 0
    else:
        return(int(n%10)+sod(int(n/10)))

print(sod(223))