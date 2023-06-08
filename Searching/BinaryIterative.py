arr=[1,2,3,5,6,8,9,11,13,15,17,18,21]

x=9
def BinarySearch(arr,x):
    l=0
    r=len(arr)-1
    while(l<=r):
        mid=((l+r)//2)
        if(arr[mid]==x):
            return mid
        elif(arr[mid]>x):
            r=mid-1
        elif(arr[mid]<x):
            l=mid+1
            
    return("Element not found!!")
            
print(BinarySearch(arr,x))
        
