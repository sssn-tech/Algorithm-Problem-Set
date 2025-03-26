#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# type: ignore
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(root, ans):
            if not root:
                return
            dfs(root.left, ans)
            ans.append(root.val)
            dfs(root.right, ans)
        dfs(root, ans)
        return ans

        
        
# @lc code=end

