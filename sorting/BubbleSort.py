#bubble sort
def BubbleSort(a:[int]):
    for j in range(len(a)-1):
        for i in range(len(a)-1):
            if(a[i]>a[i+1]):
                a[i],a[i+1]=a[i+1],a[i]
            else:
                continue
    return a
        
    
    
a=[2,5,1,4,2,8,4,9,0,5,3,5,1,2]
print(BubbleSort(a))
