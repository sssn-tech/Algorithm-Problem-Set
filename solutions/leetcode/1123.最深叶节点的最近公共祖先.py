#
# @lc app=leetcode.cn id=1123 lang=python3
#
# [1123] 最深叶节点的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        g_max_depth, ans = 0, 0
        def dfs(curr, curr_depth):
            nonlocal g_max_depth, ans
            if not curr:
                g_max_depth = max(g_max_depth, curr_depth)
                return curr_depth
            le_max_depth = dfs(curr.left, curr_depth + 1)
            ri_max_depth = dfs(curr.right, curr_depth + 1)
            if le_max_depth == ri_max_depth and le_max_depth == g_max_depth:
                ans = curr 
            return max(le_max_depth, ri_max_depth)
        dfs(root, 0)
        return ans

        
# @lc code=end

