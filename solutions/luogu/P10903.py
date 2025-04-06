# https://www.lanqiao.cn/problems/19716/learning/?page=1&first_category_id=1&second_category_id=3&name=%E5%95%86%E5%93%81%E5%BA%93%E5%AD%98%E7%AE%A1%E7%90%86
# 十五届python 研究生组D题 商品库存管理

from typing import *

n, m = map(int, input().split())
diff = [0] * n 
opts = []
for opt in range(m):
    l, r = map(int, input().split())
    l -= 1 # to 0 base
    r -= 1
    opts.append([l, r])
    diff[l] += 1
    if r < n - 1:
        diff[r + 1] -= 1
# 从差分数组还原出原数组nums[]的同时, 记录0, 1的计数前缀和sum0[], sum1[]
# 这样当询问不执行[l, r]时, nums中0元素的个数就是这个整个数组中0的个数加这个区间内1的个数
nums, sum1 = [], []
curr_sum, curr_0, curr_1 = 0, 0, 0
for i in range(n):
    curr_sum += diff[i]
    nums.append(curr_sum)
    if nums[-1] == 1:
        curr_1 += 1
    sum1.append(curr_1)

# 现在回答m个操作对应的问题
for i in range(m):
    l, r = opts[i]
    cnt1 = sum1[r] - (sum1[l - 1] if l > 0 else 0)
    print(curr_0 + cnt1)




