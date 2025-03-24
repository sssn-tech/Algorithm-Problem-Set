# 最长公共子序列问题(LCS)可以转移成最长上升子序列问题
# 用哈希表记录nums2的每个元素出现的位置
# 初始化一个列表ls, 遍历nums1, 如果没出现过抛弃, 如果出现过, 则append这个数在nums2中出现的下标
# 则我们得到了公共子序列下标列表ls
# 对ls求最长上升子序列即可

from typing import *
inf = int(1e9 + 10)

def lcs(nums1: List[int], nums2: List[int], n: int) -> int:
    # 返回最长公共子序列的长度
    idx = {nums2[i]: i for i in range(n)}
    ls = []
    for num1 in nums1:
        if num1 in idx:
            ls.append(idx[num1])
    return lis(ls, len(ls))

def lis(nums: List[int], n) -> int:
    # 返回最长严格上升子序列的长度
    dp = [inf] * (n + 1) # dp[i]表示长度为i的最长严格上升子序列的末尾数字(0-based)
    res = 1
    for num in nums:
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) >> 1
            if dp[mid] < num: # 因为是严格上升, 所以不能取等
                l = mid + 1
            else:
                r = mid 
        if dp[l] == inf:
            res = max(res, l + 1) 
        dp[l] = num 
    return res


n = int(input())
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

print(lcs(nums1, nums2, n))

