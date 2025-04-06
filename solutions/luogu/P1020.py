from typing import *
import bisect


# 给定一个数组, 求最长下降子序列长度(不严格), 和最长上升序列长度(严格)

def LIS(nums: List[int], strict: bool) -> int:
    # 返回数组的最长上升子序列长度, 严格表示能否接受相同元素
    inf = int(1e9 + 10)
    n = len(nums)
    dp = [inf] * (n + 1) # dp[i]表示长度为i的最长上升不序列末尾的值
    for num in nums:
        if strict:
            p = bisect.bisect_left(dp, num)
        else:
            p = bisect.bisect_right(dp, num) 
        dp[p] = num 
    return bisect.bisect_left(dp, inf)

nums = list(map(int, input().split()))
ans2 = LIS(nums, True)
nums.reverse()
ans1 = LIS(nums, False)
print(f'{ans1}\n{ans2}\n')





