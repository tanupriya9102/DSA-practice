def cout(n):
    if(n==1):
        print(n)
        return
    else:
        # print(n)#for n to1 
        cout(n-1)
        print(n)#for 1 to n

cout(4)
