def MaxSumSubarray(arr,k):
  s,i,j=0,0,0
  msum=0
  while j<len(arr):
    s+=arr[j]
    if(j-i+1<k):
      j+=1
    elif(j-i+1==k):
      msum=max(msum,s)
      s-=arr[i]
      i+=1
      j+=1
return msum
