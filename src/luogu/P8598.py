from typing import *


n = int(input())
nums = []
for i in range(n):
    temp = list(map(int, input().split()))
    nums.extend(temp)
nums.sort()

dup, brk = 0, 0
for i in range(len(nums) - 1):
    if nums[i] == nums[i + 1]:
        dup = nums[i]
    if nums[i] + 2 == nums[i + 1]:
        brk = nums[i] + 1

print(f'{brk} {dup}')
