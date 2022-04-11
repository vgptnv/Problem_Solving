# Q. 11286
import heapq
import sys

heap = []
        
n = int(sys.stdin.readline())
for _ in range(n):
    i = int(sys.stdin.readline())
    if i != 0:
        heapq.heappush(heap, (abs(i), i))
    else:
        if len(heap) > 0:
            print(heapq.heappop(heap)[1])
        else:
            print(0)