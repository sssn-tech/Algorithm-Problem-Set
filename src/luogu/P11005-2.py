# 一张无向带权图, 定义一条路径的cost为路径包含边权的最大值
# 求图中两点间存在合法路径点点对计数和, 合法指[l, r]
# 把边分为3类, w < l, l <= w <= r, l > r
# 一条合法的路径必不包含第三种, 并包含至少一条第二种


from typing import *

class UnionFind:
    def __init__(self, n: int):
        self.parent = [_ for _ in range(n + 1)]
        self.size = [1 for _ in range(n + 1)]
    
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> None:
        fx, fy = self.find(x), self.find(y)
        if fx == fy: # 如果已经在一个集合, 就不操作了
            return 
        if self.size[fx] > self.size[fy]: # 让fx是小树, fy是大树
            fx, fy = fy, fx 
        self.parent[fx] = fy # 小树合并进大树
        self.size[fy] += self.size[fx]

n, m, l, r = map(int, input().split())
edges = []
uf = UnionFind(n)

for _ in range(m):
    u, v, w = map(int, input().split())
    if w <= r:
        edges.append((u, v, w))

edges.sort(key=lambda edge: edge[-1])

ans = 0
for u, v, w in edges:
    fu, fv = uf.find(u), uf.find(v)
    if fu == fv:
        continue
    if w >= l: # 如果一条合法w联通了两个块, 这两个块的点可以互通
        ans += uf.size[fu] * uf.size[fv]
    uf.union(fu, fv)

print(ans)

