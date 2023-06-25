# Heapq Functions
# Assuming that you know how the heap data structure works, let’s see what functions are provided by Python’s heapq model.

# heappush(heap, item) — Push the value item into the heap
# heappop(heap) — Pop and return the smallest value from the heap
# heappushpop(heap, item) — Push the value item into the heap and return the smallest value from the heap
# heapify(x) — Convert the list x into a heap
# heapreplace(heap, item) — Pop and return the smallest value from the heap then push the value item into the heap

import heapq
heap=[]
heapq.heappush(heap,10)
heapq.heappush(heap,5)
print(heap)
