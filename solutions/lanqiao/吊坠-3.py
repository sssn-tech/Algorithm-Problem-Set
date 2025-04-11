from typing import *
from collections import *
from datetime import *
from functools import *
import heapq
import bisect
import math

n, m = map(int, input().split())
ss = []
for _ in range(n):
    ss.append(input())

def circ_lcs() -> int:
    ...

# build edges
edges = []
for i in range(n):
    for j in range(i + 1, n):
        w = circ_lcs(ss[i], ss[j])
        edges.append((w, i, j))

# Kruscal MaxST
fa = [i for i in range(n)]

def find(u):
    if fa[u] != u:
        fa[u] = find(fa[u])
    return fa[u]

def union(u, v):
    fu, fv = find(u), find(v)
    if fu != fv:
        fa[fu] = fv

edges.sort(reverse=True)
ans = 0
for w, u, v in edges:
    fu, fv = find(u), find(v)
    if fu != fv:
        ans += w 
        union(u, v)

print(ans)
