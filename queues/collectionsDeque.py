# methods for deque FIFO
# deque()
# append()
# popleft()
# clear() 
from collections import deque

customQueue=deque(maxlen=3)
customQueue.append(1)
customQueue.append(2)
customQueue.append(3)
# customQueue.append(4) 
print(customQueue.popleft()) #to remove 1st element
print(customQueue.clear())


print(customQueue)