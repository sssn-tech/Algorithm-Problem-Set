from typing import *
from collections import *
import sys 

data = map(int, sys.stdin.read().split())

c, m, n = next(data), next(data), next(data)
drops = [] # 水滴数组, 第一个元素为位置, 第二个元素是大小, 第三, 第四个元素是prev和next
for _ in range(m):
    x, w = next(data), next(data)
    drops.append([x, w, -1, -1])

drops.sort()

mp = defaultdict() # 第pos格对应的是drops里下标i的水滴
for i in range(m):
    if i > 0:
        drops[i - 1][3] = i # 上一个的next是当前
        drops[i][2] = i - 1 # 当前的prev是上一个
    mp[drops[i][0]] = i 

def explode(id: int, drops: List[int]) -> None:
    if drops[id][1] < 5:
        return 
    # 如果这个节点爆炸了, 则要删除他, 并且左右节点+1, 再递归处理左右
    drops[id][1] = -1 # 大小改为-1, 标记已经死了
    global m
    m -= 1
    prev, post = drops[id][2], drops[id][3]
    if prev != -1:
        drops[prev][3] = drops[id][3]
        drops[prev][1] += 1
    if post != -1:
        drops[post][2] = drops[id][2]
        drops[post][1] += 1
    
    if prev != -1:
        explode(prev, drops)
    if post != -1 and drops[post][1] != -1:
        explode(post, drops)
    


for _ in range(n):
    p = next(data) # 操作了p位置
    id = mp[p] # 找到drops数组的下标
    drops[id][1] += 1 # 大小涨1
    explode(id, drops)
    print(m)

    
    
        




