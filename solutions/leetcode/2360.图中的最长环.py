#
# @lc app=leetcode.cn id=2360 lang=python3
#
# [2360] 图中的最长环
#

# @lc code=start
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        ind = [0] * n

        for v in edges:
            if v != -1:
                ind[v] += 1
        que = deque([u for u in range(n) if ind[u] == 0])

        while que:
            u = que.pop()
            v = edges[u]
            if v != -1:
                ind[v] -= 1
                if ind[v] == 0:
                    que.append(v)
        
        # nodes是环上的节点
        nodes = set([u for u in range(n) if ind[u] != 0])
        ans = -1

        while nodes:
            start = nodes.pop()
            u = edges[start]
            len_circle = 1
            while u != start:
                u = edges[u]
                nodes.discard(u)
                len_circle += 1
            ans = max(ans, len_circle)

        return ans


# @lc code=end

