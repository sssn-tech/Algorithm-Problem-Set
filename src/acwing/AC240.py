from typing import *

n, k = map(int, input().split())

parent = [i for i in range(n + 1)]
weight = [0 for _ in range(n + 1)]  # 节点与父节点的关系，0同类，1吃父节点，2被父节点吃

def find(u: int, parent: List[int], weight: List[int]) -> Tuple[int, int]:
    if parent[u] != u:
        orig_parent = parent[u]
        parent[u], w = find(parent[u], parent, weight)
        weight[u] = (weight[u] + w) % 3
    return parent[u], weight[u]

def union(u: int, v: int, relation: int, parent: List[int], weight: List[int]):
    fu, du = find(u, parent, weight)
    fv, dv = find(v, parent, weight)
    if fu != fv:
        parent[fu] = fv
        weight[fu] = (relation + dv - du) % 3

ans = 0
for _ in range(k):
    statement, u, v = map(int, input().split())
    statement -= 1  # 转换为0同类，1吃
    if u <= 0 or v <= 0 or u > n or v > n:
        ans += 1
        continue
    fu, du = find(u, parent, weight)
    fv, dv = find(v, parent, weight)
    if fu != fv:
        union(u, v, statement, parent, weight)
    else:
        current_relation = (du - dv) % 3
        if current_relation != statement:
            ans += 1

print(ans)