from typing import *

n = int(input())
nums1 = list(input().split())
nums2 = list(input().split())

nums = [nums1, nums2]
ans, i, j = 0, 0, 0

def check(num: str) -> bool:
    return '0' in num or '2' in num or '4' in num

while j < n:
    # print(j)
    while j < n and not check(nums[i][j]):
        j += 1
    if j >= n:
        break 
    i = (i + 1) % 2
    j += 1
    ans += 1
    

print(ans)

