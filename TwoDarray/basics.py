
# for 2d arrays
# insertion in 2d array
import numpy as np
tdarray=np.array([[1,2,3,4],[5,6,7,8],[9,0,0,0],[1,1,1,1]])
print(tdarray)
# to add column on 2nd position 
nd2=np.insert(tdarray,2,[[1,2,3,4]],axis=1)
print(nd2)

# to add row on 2nd position 
nd2=np.insert(tdarray,2,[[1,2,3,4]],axis=0)
print(nd2)

# to add row/column at the end
nd3=np.append(tdarray,[[4,4,4,4]],axis=0)
print(nd3)

# accessing elements:
import numpy as np

arr = np.array([[1,2,3,4],[6,7,8,9],[10,11,12,13],[11,11,11,11]])
def AccessElement(arr,rindex,cindex):
    if rindex>=len(arr) and cindex>=len(arr[0]):
        print("Out of limit!")
    else:
        print(arr[rindex][cindex])

print(arr)
AccessElement(arr,2,3)
