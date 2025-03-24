# 观察条件得到, 要不一条路走到黑, 要不回头一次, 不可能多次回头

from typing import *

zero = False
n, m = map(int, input().split()) # n个矿藏位置, 体力限制为m
nums = list(map(int, input().split())) # 有矿的位置
if 0 in nums: # 为了方便计算收益, 直接假设0位置有矿, 没有也填一个
    zero = True
else:
    nums.append(0)
nums.sort() 

def find0(nums: List[int]) -> int:
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r + 1) // 2
        if nums[mid] > 0:
            r = mid - 1
        else:
            l = mid 
    return l
p0 = find0(nums)
income = []
for i, num in enumerate(nums):
    income.append(abs(i - p0) + 1)

# nums = [-11, -3, -2, -1, 0, 1, 2, 5, 9, 15]
# incm = [6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6]
ans = 0
for i, num in enumerate(nums):
    if abs(num) < m: # 至少要能走到
        ans = max(ans, income[i])
    rst = m - 2 * abs(num)
    if rst > 0: # 如果有余力折返回来
        # 找到可以reach到的反方向最远距离
        if num <= 0: # 这时候往正方向找
            l, r = 0, n - 1
            while l < r: # 找最后一个小于等于rst的数的下标
                mid = (l + r + 1) // 2
                if nums[mid] > rst:
                    r = mid - 1
                else:
                    l = mid
            if l != p0:
                ans = max(ans, income[i] + income[l] - 1) # 0算了两次
        else: # 这时候往反方向找
            l, r = 0, n - 1
            while l < r: # 找第一个大于等于-rst的数的下标
                mid = (l + r) // 2
                if nums[mid] < -rst:
                    l = mid + 1
                else:
                    r = mid 
            if l != p0:
                ans = max(ans, income[i] + income[l] - 1)

print(ans + (0 if zero else -1)) # 补上最开始假设的0


