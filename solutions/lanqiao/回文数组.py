from typing import *
from collections import *
from datetime import *
from functools import *
import heapq
import bisect
import math

n = int(input())
nums = list(map(int, input().split()))

lo, hi, ans = 0, n - 1, 0
while lo < hi:
    if nums[lo] != nums[hi]:
        gap = nums[lo] - nums[hi]
        nums[lo] -= gap 
        if lo + 1 < hi - 1:
            gap2 = nums[lo + 1] - nums[hi - 1]
            if gap * gap2 < 0: # 如果一个要升一个要降, 那没法处理, 继续
                continue
            nums[lo + 1] -= (1 if gap2 > 0 else -1) * min(abs(gap), abs(gap2))
        ans += abs(gap)
    lo += 1
    hi -= 1
print(ans)

