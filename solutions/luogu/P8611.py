from typing import *

n = int(input())
nums = list(map(int, input().split()))

ans = 1
if nums[0] > 0: # 如果零号病人往右走, 则他会传染给所有出发点在他右边, 并往左走的
    last = -1
    for i in range(1, n): 
        if nums[i] < 0 and abs(nums[i]) > nums[0]:
            ans += 1
            last = max(last, abs(nums[i])) # last是母体最后一个传染的往左走的病人
    if last != -1:
        for i in range(1, n): # 统计last的感染情况
            if nums[i] > 0 and nums[i] < last:
                ans += 1
else: # 零号病人往左走
    last = 1e5
    for i in range(1, n):
        if nums[i] > 0 and nums[i] < abs(nums[0]):
            ans += 1
            last = min(last, nums[i])
    if last != -1:
        for i in range(1, n):
            if nums[i] < 0 and abs(nums[i]) > last:
                ans += 1
print(ans)
        