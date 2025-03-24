
from typing import *

n = int(input())
nums = list(map(int, input().split()))

mid = n // 2
ans = 0
for i in range(mid):
    if nums[i] != nums[-(i + 1)]:
        gap1 = nums[i] - nums[-(i + 1)]
        gap2 = 0
        if i < mid - 1 and nums[i + 1] != nums[-(i + 2)]:
            gap2 = nums[i + 1] - nums[-(i + 2)]
        ans += abs(gap1)
        nums[i] -= gap1
        if gap2 != 0 and gap1 * gap2 > 0: 
            nums[i + 1] -= (1 if gap2 > 0 else -1) * min(abs(gap1), abs(gap2))

print(ans)
