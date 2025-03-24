"""
本代码对原代码进行了优化，主要优化点为：
1. 显式传参记录当前用到的递增系统数量(su)和递减系统数量(sd)。
2. 在递归里，仅在已用部分（up[0:su]和dn[0:sd]）里用bisect查找插入位置，
   如果返回下标小于当前系统数量则直接更新已有系统，否则认为需要新开系统，
   从而分别调用dfs(p+1, su, sd)和dfs(p+1, su+1, sd)（dn同理）。
"""

from typing import *
import bisect
inf = int(1e9 + 10)

def dfs(p: int, su: int, sd: int) -> None:
    global ans
    # 剪枝：当前接收系统总数量已经不可能比当前最优解更优
    if su + sd >= ans:
        return
    if p >= n:
        ans = su + sd
        return 
    
    height = nums[p]
    
    # 递增系统（up）分支
    # 仅在已用部分 up[0:su] 内查找应插入位置
    u = bisect.bisect_left(up, height, 0, su)
    # 保存备份，便于回溯
    backup = up[u] if u < len(up) else inf
    up[u] = height
    if u < su:
        # 使用已有系统，不增加su
        dfs(p + 1, su, sd)
    else:
        # 新增一个递增系统
        dfs(p + 1, su + 1, sd)
    up[u] = backup  # 回溯还原

    # 递减系统（dn）分支
    # 注意dn数组中存储的是 -height，即反向表示，所以查找时使用 -height
    v = bisect.bisect_left(dn, -height, 0, sd)
    backup = dn[v] if v < len(dn) else inf
    dn[v] = -height
    if v < sd:
        dfs(p + 1, su, sd)
    else:
        dfs(p + 1, su, sd + 1)
    dn[v] = backup  # 回溯

# 主程序
n = int(input())
while n != 0:
    nums = list(map(int, input().split()))
    # up 和 dn 数组长度为 n，初始值分别为 inf（递增系统）和 inf（dn中存储的为 -height，所以初始为 inf）
    up = [inf] * n 
    dn = [inf] * n 
    ans = n  # 初始答案设置为 n, 或任何足够大的值
    dfs(0, 0, 0)
    print(ans)
    n = int(input())