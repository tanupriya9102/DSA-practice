arr=[1,2,3,5,6,8,9,11,13,15,17,18,21]

x=9
l=0
r=len(arr)-1
def BinarySearch(arr,l,r,x):
    mid=(l+r)//2
    if(arr[mid]==x):
        mid=((l+r)//2)
        return mid
    elif(arr[mid]>x):
        r=mid-1
        return BinarySearch(arr,l,r,x)
    elif(arr[mid]<x):
        l=mid+1
        return BinarySearch(arr,l,r,x)
            
    return("Element not found!!")
            
print(BinarySearch(arr,l,r,x))
        
