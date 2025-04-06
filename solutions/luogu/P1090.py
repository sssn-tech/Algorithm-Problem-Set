from typing import *
import heapq

n = int(input())
nums = list(map(int, input().split()))

pq = []
for num in nums:
    heapq.heappush(pq, num)

ans = 0
while len(pq) > 1:
    u = heapq.heappop(pq)
    v = heapq.heappop(pq)
    ans += u + v 
    heapq.heappush(pq, u + v)

print(ans)
