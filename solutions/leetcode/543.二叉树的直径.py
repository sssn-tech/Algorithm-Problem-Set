#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(root):
            if not root:
                return 0
            le_h = dfs(root.left)
            ri_h = dfs(root.right)
            nonlocal ans
            ans = max(ans, le_h + ri_h)
            curr_h = max(le_h, ri_h) + 1
            return curr_h

        _ = dfs(root)
        return ans 

        
# @lc code=end

