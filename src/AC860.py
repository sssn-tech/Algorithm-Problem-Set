from typing import *
from collections import deque

def is_bipartite(graph: List[List[int]]) -> bool:
    n = len(graph) - 1
    colors = [0 for _ in range(n + 1)] # 0是无颜色, 1和-1是两种颜色
    
    def bfs(graph: List[List[int]], src: int):
        colors[src] = 1 
        que = deque([src])
        
        while que:
            u = que.popleft()
            for v in graph[u]:
                if colors[v] == colors[u]:
                    return False
                if colors[v] == 0:
                    colors[v] = -colors[u]
                    que.append(v)
                    
        return True
    
    for src in range(1, n + 1):
        if colors[src] == 0 and not bfs(graph, src):
            return False
    return True
        

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print('Yes' if is_bipartite(graph) else 'No')


